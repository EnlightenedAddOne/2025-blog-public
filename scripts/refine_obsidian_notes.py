from __future__ import annotations

import json
import re
import shutil
from pathlib import Path


REPO = Path(r"D:/PROJECT/Markdown/blog/2025-blog-public")
BLOGS = REPO / "public" / "blogs"
INDEX = BLOGS / "index.json"
CATEGORIES = BLOGS / "categories.json"
REPORT = BLOGS / "obsidian-refine-report.json"


def parse_source_rel(markdown_text: str) -> str:
    for line in markdown_text.splitlines()[:10]:
        line = line.strip()
        if line.startswith("> 来源：Obsidian/"):
            return line.replace("> 来源：Obsidian/", "", 1).strip()
    return ""


def should_remove(
    slug: str, title: str, markdown_text: str, source_rel: str
) -> tuple[bool, str]:
    slug_l = slug.lower()
    title_l = title.lower()
    source_l = source_rel.lower()

    if source_l.endswith("/agents.md") or source_l == "agents.md":
        return True, "移除系统说明文档"
    if source_l.endswith("/home.md") or source_l == "home.md":
        return True, "移除首页欢迎页"

    if any(
        k in slug_l
        for k in [
            "zhou-ji-mu-ban",
            "ri-ji-mu-ban",
            "jin-ri-xin-qing-xuan-ze",
            "ren-sheng-jin-du-tiao",
            "bi-ji-shu-ju-zong-lan",
        ]
    ):
        return True, "移除模板/总览类文件"

    if "moodtracker" in title_l or "note-50ac30" in slug_l:
        return True, "移除模板工具文件"

    if "switch to excalidraw view" in markdown_text.lower():
        return True, "移除 Excalidraw 原始导出文件"

    if "欢迎来到我的 obsidian 知识库" in markdown_text:
        return True, "移除欢迎占位页"

    return False, ""


def fine_category(source_rel: str, title: str, fallback: str) -> str:
    src = source_rel
    t = title

    if src.startswith("10-学业与考试/考研/院校详档"):
        return "学业与考试/考研择校"
    if src.startswith("10-学业与考试/考研/高数") or re.search(
        r"高数|函数|极限|微分|导数", t
    ):
        return "学业与考试/考研数学"
    if (
        "wangdao-data-structure-main" in src
        or src.startswith("10-学业与考试/考研/数据结构")
        or re.search(r"数据结构|排序|查找|二叉树|线性表|队列|栈|图|串", t)
    ):
        return "学业与考试/考研数据结构"

    if "10-学业与考试/期末复习资料/人工智能" in src or re.search(
        r"人工智能|深度学习|机器学习|神经网络|\bAI\b", t, re.IGNORECASE
    ):
        return "学业与考试/期末复习-人工智能"
    if "10-学业与考试/期末复习资料/嵌入式" in src or re.search(r"嵌入式|物联网|ARM", t):
        return "学业与考试/期末复习-嵌入式"
    if "10-学业与考试/期末复习资料/java" in src.lower() or re.search(
        r"java", t, re.IGNORECASE
    ):
        if re.search(r"期末|考试|试卷|试题|复习", t):
            return "学业与考试/期末复习-Java"

    if src.startswith("日志/日记"):
        return "日志/日记"
    if src.startswith("日志/周复盘"):
        return "日志/周复盘"

    if src.startswith("20-技术知识库/树莓派"):
        return "技术知识库/树莓派"
    if src.startswith("20-技术知识库/环境配置"):
        return "技术知识库/环境配置"
    if src.startswith("20-技术知识库/AI提示词"):
        return "技术知识库/AI提示词"
    if "20-技术知识库/服务器" in src or re.search(
        r"docker|部署|服务器|wordpress|clawcloud|fastapi", t, re.IGNORECASE
    ):
        return "技术知识库/服务器部署"
    if src.startswith("20-技术知识库"):
        return "技术知识库/通用"

    if src.startswith("30-项目与实践/项目说明"):
        return "项目与实践/项目文档"
    if src.startswith("30-项目与实践/程序流程图"):
        return "项目与实践/流程图"

    if src.startswith("90-System"):
        return "系统/模板工具"

    if fallback and fallback.strip():
        return fallback
    return "技术知识库/通用"


def cleanup_markdown(text: str) -> tuple[str, int]:
    changed = 0
    # remove waypoint blocks
    next_text = text.replace("%% Begin Waypoint %%", "").replace(
        "%% End Waypoint %%", ""
    )
    if next_text != text:
        changed += 1
    text = next_text

    # remove obvious invalid wiki embeds / anchors
    patterns = [
        r"!\[\[#\^[^\]]+\]\]",
        r"!\[\[图片名[^\]]*\]\]",
        r"!\[\[[^\]]*\.excalidraw[^\]]*\]\]",
    ]
    for p in patterns:
        next_text = re.sub(p, "", text)
        if next_text != text:
            changed += 1
        text = next_text

    # normalize source line spacing
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    lines = [ln.rstrip() for ln in text.split("\n")]
    text = "\n".join(lines)
    next_text = re.sub(r"\n{3,}", "\n\n", text)
    if next_text != text:
        changed += 1
    text = next_text.strip() + "\n"
    return text, changed


def main() -> None:
    data = json.loads(INDEX.read_text(encoding="utf-8"))
    if not isinstance(data, list):
        raise ValueError("index.json is not an array")

    removed: list[dict[str, str]] = []
    updated_count = 0
    format_fixed = 0

    kept_items: list[dict] = []

    for item in data:
        slug = str(item.get("slug", "")).strip()
        if not slug.startswith("obsn-"):
            kept_items.append(item)
            continue

        dir_path = BLOGS / slug
        md_path = dir_path / "index.md"
        cfg_path = dir_path / "config.json"

        if not md_path.exists():
            removed.append({"slug": slug, "reason": "目录缺少 index.md"})
            if dir_path.exists():
                shutil.rmtree(dir_path)
            continue

        md_text = md_path.read_text(encoding="utf-8", errors="replace")
        source_rel = parse_source_rel(md_text)
        title = str(item.get("title", ""))

        drop, reason = should_remove(slug, title, md_text, source_rel)
        if drop:
            removed.append({"slug": slug, "reason": reason})
            if dir_path.exists():
                shutil.rmtree(dir_path)
            continue

        new_category = fine_category(source_rel, title, str(item.get("category", "")))
        if item.get("category") != new_category:
            item["category"] = new_category
            updated_count += 1

        clean_text, changed = cleanup_markdown(md_text)
        if changed > 0 and clean_text != md_text:
            md_path.write_text(clean_text, encoding="utf-8")
            format_fixed += 1

        if cfg_path.exists():
            try:
                cfg = json.loads(cfg_path.read_text(encoding="utf-8"))
            except Exception:
                cfg = {}
            cfg["category"] = new_category
            cfg_path.write_text(
                json.dumps(cfg, ensure_ascii=False, indent=2), encoding="utf-8"
            )

        kept_items.append(item)

    # sort by date desc (string format already sortable)
    kept_items.sort(key=lambda x: str(x.get("date", "")), reverse=True)
    INDEX.write_text(
        json.dumps(kept_items, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    # rebuild categories list from actual items
    cats = sorted(
        {
            str(i.get("category", "")).strip()
            for i in kept_items
            if str(i.get("category", "")).strip()
        }
    )
    CATEGORIES.write_text(
        json.dumps({"categories": cats}, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    report = {
        "total_after": len(kept_items),
        "removed_count": len(removed),
        "removed": removed,
        "category_updated_count": updated_count,
        "format_fixed_count": format_fixed,
        "categories": cats,
    }
    REPORT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(
        json.dumps(
            {
                "total_after": len(kept_items),
                "removed_count": len(removed),
                "category_updated_count": updated_count,
                "format_fixed_count": format_fixed,
                "category_count": len(cats),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
