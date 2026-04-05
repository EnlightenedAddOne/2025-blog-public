from __future__ import annotations

import hashlib
import json
import re
import shutil
from datetime import datetime
from pathlib import Path

from pypinyin import lazy_pinyin


REPO = Path(r"D:/PROJECT/Markdown/blog/2025-blog-public")
OBSIDIAN = Path(r"D:/PROJECT/Markdown/Obsidian")
BLOGS_DIR = REPO / "public" / "blogs"
INDEX_PATH = BLOGS_DIR / "index.json"

EXCLUDE_TOP = {".obsidian", ".claude", ".opencode", ".git", "node_modules"}

HEADING_RE = re.compile(r"^#\s+(.+?)\s*$")
MD_SYMBOL_RE = re.compile(r"[`*_>#\[\]\(\)!-]+")

CATEGORY_MAP = {
    "10-学业与考试": "学业与考试",
    "20-技术知识库": "技术知识库",
    "30-项目与实践": "项目与实践",
    "90-System": "系统模板",
    "日志": "日志复盘",
}


def strip_frontmatter(text: str) -> str:
    lines = text.splitlines()
    if len(lines) >= 3 and lines[0].strip() == "---":
        for i in range(1, min(len(lines), 80)):
            if lines[i].strip() == "---":
                return "\n".join(lines[i + 1 :]).lstrip("\n")
    return text


def get_title_and_summary(text: str, fallback: str) -> tuple[str, str]:
    title = fallback
    summary = ""

    for line in text.splitlines():
        s = line.strip()
        if not s:
            continue

        m = HEADING_RE.match(s)
        if m:
            title = m.group(1).strip()
            continue

        if s.startswith("```dataview") or s.startswith("```dataviewjs"):
            continue

        plain = MD_SYMBOL_RE.sub(" ", s)
        plain = re.sub(r"\s+", " ", plain).strip()
        if plain:
            summary = plain[:120]
            break

    return title[:120], summary


def to_pinyin_slug(text: str) -> str:
    parts = lazy_pinyin(text, errors="ignore")
    pinyin = "-".join(part.strip().lower() for part in parts if part.strip())
    ascii_only = re.sub(r"[^a-z0-9\-\s_]+", " ", pinyin)
    ascii_only = re.sub(r"[\s_]+", "-", ascii_only)
    ascii_only = re.sub(r"-{2,}", "-", ascii_only).strip("-")
    if not ascii_only:
        ascii_only = "note"
    return ascii_only[:80]


def pick_category(rel: Path) -> str:
    if not rel.parts:
        return "Obsidian笔记"
    return CATEGORY_MAP.get(rel.parts[0], f"Obsidian/{rel.parts[0]}")


def main() -> None:
    # 清理上次错误导入目录
    bad_dir = BLOGS_DIR / "obsidian-notes"
    if bad_dir.exists():
        shutil.rmtree(bad_dir)

    bad_index = BLOGS_DIR / "obsidian-notes-index.json"
    if bad_index.exists():
        bad_index.unlink()

    # 读取旧 index
    if INDEX_PATH.exists():
        try:
            existing = json.loads(INDEX_PATH.read_text(encoding="utf-8"))
            if not isinstance(existing, list):
                existing = []
        except Exception:
            existing = []
    else:
        existing = []

    # 保留非 Obsidian 导入条目
    kept: list[dict] = []
    for item in existing:
        slug = str(item.get("slug", ""))
        category = str(item.get("category", ""))
        if slug.startswith("obsidian-notes/"):
            continue
        if slug.startswith("obs-"):
            continue
        if slug.startswith("obsn-"):
            continue
        if category == "Obsidian笔记":
            continue
        kept.append(item)

    # 删除历史 obs-* 目录，避免残留
    for p in BLOGS_DIR.iterdir():
        if p.is_dir() and p.name.startswith("obs-"):
            shutil.rmtree(p)

    for p in BLOGS_DIR.iterdir():
        if p.is_dir() and p.name.startswith("obsn-"):
            shutil.rmtree(p)

    # 收集 Obsidian 笔记
    md_files: list[Path] = []
    for p in OBSIDIAN.rglob("*.md"):
        rel = p.relative_to(OBSIDIAN)
        parts = rel.parts
        if any(part in EXCLUDE_TOP for part in parts):
            continue
        if any(part.startswith(".") for part in parts):
            continue
        md_files.append(p)

    used_slugs = {str(i.get("slug", "")) for i in kept}
    new_items: list[dict] = []

    for p in sorted(md_files):
        rel = p.relative_to(OBSIDIAN)
        rel_posix = rel.as_posix()

        base = to_pinyin_slug(p.stem)
        slug = f"obsn-{base}"
        if slug in used_slugs:
            short = hashlib.md5(rel_posix.encode("utf-8")).hexdigest()[:6]
            slug = f"{slug}-{short}"
            if slug in used_slugs:
                k = 2
                while f"{slug}-{k}" in used_slugs:
                    k += 1
                slug = f"{slug}-{k}"
        used_slugs.add(slug)

        raw = p.read_text(encoding="utf-8", errors="replace")
        body = strip_frontmatter(raw)

        title, summary = get_title_and_summary(body, p.stem)
        source_line = f"> 来源：Obsidian/{rel_posix}"

        has_h1 = any(HEADING_RE.match(line.strip()) for line in body.splitlines())
        if has_h1:
            final_md = f"{source_line}\n\n{body}".lstrip("\n").rstrip() + "\n"
        else:
            final_md = f"# {title}\n\n{source_line}\n\n{body}".rstrip() + "\n"

        post_dir = BLOGS_DIR / slug
        post_dir.mkdir(parents=True, exist_ok=True)
        (post_dir / "index.md").write_text(final_md, encoding="utf-8")

        mtime = datetime.fromtimestamp(p.stat().st_mtime)
        date_str = mtime.strftime("%Y-%m-%dT%H:%M")
        category = pick_category(rel)

        config = {
            "title": title,
            "tags": ["obsidian"],
            "date": date_str,
            "summary": summary,
            "hidden": False,
            "category": category,
        }
        (post_dir / "config.json").write_text(
            json.dumps(config, ensure_ascii=False, indent=2), encoding="utf-8"
        )

        new_items.append(
            {
                "slug": slug,
                "title": title,
                "tags": ["obsidian"],
                "date": date_str,
                "summary": summary,
                "hidden": False,
                "category": category,
            }
        )

    merged = kept + new_items
    merged.sort(key=lambda x: str(x.get("date", "")), reverse=True)
    INDEX_PATH.write_text(
        json.dumps(merged, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"kept={len(kept)} imported={len(new_items)} total={len(merged)}")


if __name__ == "__main__":
    main()
