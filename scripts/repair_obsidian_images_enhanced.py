#!/usr/bin/env python3
"""
增强版 Obsidian 图片修复脚本
支持：
1. attachments/ 目录查找（相对和绝对路径）
2. Wiki 图像语法 ![[image.png|width]]
3. 块引用 ![[note#^block]]
4. 内链引用 [[note]]
"""

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
REPORT = BLOGS / "obsidian-image-missing-report.json"

IMAGE_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg", ".avif", ".bmp", ".tiff"}

MD_IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")
WIKI_IMAGE_RE = re.compile(r"!\[\[([^\]]+)\]\]")
WIKI_LINK_RE = re.compile(r"(?<!\!)\[\[([^\]]+)\]\]")  # 不匹配 ![[
BLOCK_REF_RE = re.compile(r"!\[\[[^#]*#\^([^\]]+)\]\]")


def parse_source_rel(markdown_text: str) -> str | None:
    """从 Markdown 文本中提取来源信息"""
    for line in markdown_text.splitlines()[:8]:
        line = line.strip()
        if line.startswith("> 来源：Obsidian/"):
            return line.replace("> 来源：Obsidian/", "", 1).strip()
    return None


def extract_attachment_filename(wiki_ref: str) -> str:
    """
    从 Obsidian wiki 引用中提取文件名
    支持格式:
    - image.png
    - image.png|600 (带宽度)
    - note#^block-id (块引用)
    - note#heading (标题链接)
    """
    # 先移除宽度参数
    base = wiki_ref.split("|", 1)[0].strip()
    # 移除锚点和标题
    base = base.split("#", 1)[0].strip()
    return base


def find_attachment_file(source_md_path: Path, target_filename: str) -> Path | None:
    """
    查找附件文件，支持多种 Obsidian 存储策略
    """
    if not target_filename:
        return None

    source_dir = source_md_path.parent

    # 查找策略 (按优先级):
    search_paths = [
        # 1. 同一目录下的附件文件夹
        source_dir / "attachments" / target_filename,
        # 2. 父目录的附件文件夹
        source_dir.parent / "attachments" / target_filename,
        # 3. Obsidian 全局 attachments 文件夹
        OBSIDIAN / "attachments" / target_filename,
        # 4. 当前目录
        source_dir / target_filename,
        # 5. 相对路径
        OBSIDIAN / target_filename,
    ]

    for path in search_paths:
        if path.exists() and path.is_file():
            return path

    return None


def should_process_target(target: str) -> bool:
    """判断是否需要处理这个目标"""
    if not target:
        return False

    lower = target.lower()

    # 排除外部链接
    if lower.startswith("http://") or lower.startswith("https://") or lower.startswith("data:"):
        return False

    # 排除已修复的路径
    if target.startswith("/blogs/"):
        return False

    return True


def is_image_file(filename: str) -> bool:
    """检查文件扩展名是否为图片"""
    return Path(filename).suffix.lower() in IMAGE_EXTS


def copy_image_to_blog(slug_dir: Path, source_image: Path, used_names: set[str]) -> str:
    """将图片复制到博客目录"""
    key = str(source_image).lower()

    # 生成目标文件名
    base_name = source_image.name
    name = base_name

    # 避免文件名冲突
    if name.lower() in used_names:
        h = hashlib.md5(str(source_image).encode("utf-8")).hexdigest()[:6]
        stem = source_image.stem
        suffix = source_image.suffix
        name = f"{stem}-{h}{suffix}"

    # 复制文件
    dst = slug_dir / name
    shutil.copy2(source_image, dst)
    used_names.add(name.lower())

    return name


def should_convert_to_markdown_link(raw_wiki_ref: str) -> bool:
    """
    判断 wiki 引用是否应该转换为 Markdown 链接
    返回 True: 转换为 [text](note.md)
    返回 False: 保持原样或删除
    """
    # 块引用 - 需要转换
    if "#^" in raw_wiki_ref:
        return True

    # 标题引用 - 需要转换
    if "#" in raw_wiki_ref:
        return True

    # 纯文件名 - 如果是笔记则转为链接，如果是图片则转为图片
    # 在 repair 函数中判断
    return True


def main():
    total_refs = 0
    processed_refs = 0
    missing_refs = []
    copied_files = 0

    # 获取所有 Obsidian 导入的博客文章
    obsidian_blogs = sorted(BLOGS.glob("obsn-*/index.md"))
    print(f"开始处理 {len(obsidian_blogs)} 篇 Obsidian 笔记...")

    for md_file in obsidian_blogs:
        slug = md_file.parent.name
        text = md_file.read_text(encoding="utf-8", errors="replace")
        source_rel = parse_source_rel(text)

        if not source_rel:
            print(f"  [跳过] {slug}: 无法解析来源信息")
            continue

        # 源 Markdown 文件路径（用于查找附件）
        source_md = OBSIDIAN / source_rel

        print(f"\n处理: {slug}")
        print(f"  源文件: {source_rel}")

        used_names = {p.name.lower() for p in md_file.parent.iterdir() if p.is_file()}
        has_changes = False
        new_text = text

        # 1. 修复 Markdown 图片链接 ![]()
        def replace_md_image(match):
            nonlocal total_refs, processed_refs, has_changes, copied_files
            total_refs += 1

            raw_target = match.group(1)
            if not should_process_target(raw_target):
                return match.group(0)

            # 解码 URL
            target = unquote(raw_target.strip())

            # 查找图片文件
            source_file = find_attachment_file(source_md, target)
            if source_file:
                filename = copy_image_to_blog(md_file.parent, source_file, used_names)
                processed_refs += 1
                has_changes = True
                copied_files += 1
                prefix = match.group(0).split("(", 1)[0]
                return f"{prefix}(/blogs/{slug}/{filename})"

            # 无法找到
            missing_refs.append({
                "slug": slug,
                "source": source_rel,
                "ref": raw_target,
                "type": "md",
                "reason": "在本地找不到文件"
            })
            return match.group(0)

        # 2. 修复 Wiki 图片语法 ![[image.png]]
        def replace_wiki_image(match):
            nonlocal total_refs, processed_refs, has_changes, copied_files
            total_refs += 1

            raw_target = match.group(1)

            if not should_process_target(raw_target):
                return match.group(0)

            # 如果包含 #^ 块引用，跳过（不是图片）
            if "#^" in raw_target:
                missing_refs.append({
                    "slug": slug,
                    "source": source_rel,
                    "ref": raw_target,
                    "type": "wiki",
                    "reason": "块引用暂不支持"
                })
                return match.group(0)

            # 提取文件名
            filename = extract_attachment_filename(raw_target)

            if not filename:
                missing_refs.append({
                    "slug": slug,
                    "source": source_rel,
                    "ref": raw_target,
                    "type": "wiki",
                    "reason": "无法解析文件名"
                })
                return match.group(0)

            # 查找文件
            source_file = find_attachment_file(source_md, filename)

            if source_file and is_image_file(filename):
                new_filename = copy_image_to_blog(md_file.parent, source_file, used_names)
                processed_refs += 1
                has_changes = True
                copied_files += 1

                # 添加 alt 文本
                alt = Path(filename).stem
                return f"![{alt}](/blogs/{slug}/{new_filename})"

            missing_refs.append({
                "slug": slug,
                "source": source_rel,
                "ref": raw_target,
                "type": "wiki",
                "reason": "图片文件不存在"
            })
            return match.group(0)

        # 3. 转换 Wiki 链接 [[note]] 到 Markdown 链接
        def replace_wiki_link(match):
            nonlocal total_refs, processed_refs, has_changes
            total_refs += 1

            raw_target = match.group(1)

            # 提取基础文件名
            target = extract_attachment_filename(raw_target)

            if not target:
                return match.group(0)

            # 查找文件
            source_file = find_attachment_file(source_md, target)

            if source_file and source_file.suffix.lower() == ".md":
                processed_refs += 1
                has_changes = True

                # 转为 Markdown 链接
                note_title = Path(target).stem
                # 文件路径可能也需要访问
                link_text = raw_target.split("#", 1)[0].strip()
                if "|" in raw_target:
                    link_text = raw_target.split("|", 1)[-1]

                return f"[{link_text}]({target})"

            # 找不到的笔记，直接显示文本
            link_text = raw_target.split("#", 1)[0].strip().split("|")[0].strip()
            print(f"    [WARN] 找不到笔记: {target}")
            return link_text

        # 应用正则替换
        new_text = MD_IMAGE_RE.sub(replace_md_image, new_text)
        new_text = WIKI_IMAGE_RE.sub(replace_wiki_image, new_text)
        new_text = WIKI_LINK_RE.sub(replace_wiki_link, new_text)

        # 保存修改
        if has_changes:
            md_file.write_text(new_text, encoding="utf-8")

    # 生成报告
    report = {
        "total_refs": total_refs,
        "processed_refs": processed_refs,
        "missing_refs": len(missing_refs),
        "missing": missing_refs,
        "copied_files": copied_files
    }

    REPORT.write_text(
        json.dumps(report, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print("\n" + "=" * 80)
    print(f"处理完成:")
    print(f"  总引用数: {total_refs}")
    print(f"  已修复: {processed_refs}")
    print(f"  缺失: {len(missing_refs)}")
    print(f"  复制文件: {copied_files}")
    print("=" * 80)

    if missing_refs:
        print(f"\n详细信息见: {REPORT}")


if __name__ == "__main__":
    main()
