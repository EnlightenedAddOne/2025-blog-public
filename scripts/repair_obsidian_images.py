from __future__ import annotations

import hashlib
import json
import re
import shutil
from pathlib import Path
from urllib.parse import unquote


REPO = Path(r"D:/PROJECT/Markdown/blog/2025-blog-public")
OBSIDIAN = Path(r"D:/PROJECT/Markdown/Obsidian")
BLOGS = REPO / "public" / "blogs"
REPORT = REPO / "public" / "blogs" / "obsidian-image-missing-report.json"

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif"}

MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
WIKI_IMAGE_RE = re.compile(r"!\[\[([^\]]+)\]\]")


def parse_source_rel(markdown_text: str) -> str | None:
    for line in markdown_text.splitlines()[:8]:
        line = line.strip()
        if line.startswith("> 来源：Obsidian/"):
            return line.replace("> 来源：Obsidian/", "", 1).strip()
    return None


def extract_md_target(raw_inner: str) -> str:
    inner = raw_inner.strip()
    if not inner:
        return ""
    if inner.startswith("<") and ">" in inner:
        return inner[1 : inner.index(">")].strip()
    return inner.split()[0].strip()


def normalize_wiki_target(raw: str) -> str:
    # ![[path|600]] / ![[path#anchor|alias]]
    base = raw.split("|", 1)[0].strip()
    base = base.split("#", 1)[0].strip()
    return base


def looks_external(target: str) -> bool:
    lower = target.lower()
    return (
        lower.startswith("http://")
        or lower.startswith("https://")
        or lower.startswith("data:")
    )


def is_image_path(target: str) -> bool:
    return Path(target).suffix.lower() in IMAGE_EXTS


def resolve_source_asset(src_md_rel: str, target: str) -> Path | None:
    decoded = unquote(target.strip())
    if not decoded:
        return None

    src_md_abs = OBSIDIAN / src_md_rel
    parent = src_md_abs.parent

    candidates = [
        parent / decoded,
        OBSIDIAN / decoded,
    ]

    for c in candidates:
        if c.exists() and c.is_file() and c.suffix.lower() in IMAGE_EXTS:
            return c
    return None


def ensure_copy(
    slug_dir: Path, src_file: Path, copied_map: dict[str, str], used_names: set[str]
) -> str:
    key = str(src_file).lower()
    if key in copied_map:
        return copied_map[key]

    base_name = src_file.name
    name = base_name
    if name.lower() in used_names:
        h = hashlib.md5(str(src_file).encode("utf-8")).hexdigest()[:6]
        stem = src_file.stem
        suffix = src_file.suffix
        name = f"{stem}-{h}{suffix}"

    used_names.add(name.lower())
    dst = slug_dir / name
    shutil.copy2(src_file, dst)
    copied_map[key] = name
    return name


def main() -> None:
    missing: list[dict[str, str]] = []
    total_refs = 0
    fixed_refs = 0

    for md_file in sorted(BLOGS.glob("obsn-*/index.md")):
        slug = md_file.parent.name
        text = md_file.read_text(encoding="utf-8", errors="replace")
        source_rel = parse_source_rel(text)
        if not source_rel:
            continue

        copied_map: dict[str, str] = {}
        used_names = {p.name.lower() for p in md_file.parent.iterdir() if p.is_file()}

        def replace_md(m: re.Match[str]) -> str:
            nonlocal total_refs, fixed_refs
            raw_inner = m.group(1)
            target = extract_md_target(raw_inner)
            total_refs += 1

            if not target or looks_external(target) or target.startswith("/blogs/"):
                return m.group(0)
            if not is_image_path(target):
                # 非图片链接不处理
                return m.group(0)

            src_asset = resolve_source_asset(source_rel, target)
            if not src_asset:
                missing.append(
                    {"slug": slug, "source": source_rel, "ref": target, "type": "md"}
                )
                return m.group(0)

            new_name = ensure_copy(md_file.parent, src_asset, copied_map, used_names)
            fixed_refs += 1
            prefix = m.group(0).split("(", 1)[0]
            return f"{prefix}(/blogs/{slug}/{new_name})"

        text = MD_IMAGE_RE.sub(replace_md, text)

        def replace_wiki(m: re.Match[str]) -> str:
            nonlocal total_refs, fixed_refs
            raw = m.group(1)
            target = normalize_wiki_target(raw)
            total_refs += 1

            if not target or looks_external(target) or not is_image_path(target):
                missing.append(
                    {"slug": slug, "source": source_rel, "ref": raw, "type": "wiki"}
                )
                return m.group(0)

            src_asset = resolve_source_asset(source_rel, target)
            if not src_asset:
                missing.append(
                    {"slug": slug, "source": source_rel, "ref": raw, "type": "wiki"}
                )
                return m.group(0)

            new_name = ensure_copy(md_file.parent, src_asset, copied_map, used_names)
            fixed_refs += 1
            alt = Path(target).stem
            return f"![{alt}](/blogs/{slug}/{new_name})"

        text = WIKI_IMAGE_RE.sub(replace_wiki, text)
        md_file.write_text(text, encoding="utf-8")

    report = {
        "total_refs": total_refs,
        "fixed_refs": fixed_refs,
        "missing_refs": len(missing),
        "missing": missing,
    }
    REPORT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        json.dumps(
            {k: report[k] for k in ("total_refs", "fixed_refs", "missing_refs")},
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
