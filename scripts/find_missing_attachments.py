#!/usr/bin/env python3
"""
查找 Obsidian 中缺失的附件图片
"""

import json
import sys
from pathlib import Path

# 配置路径
OBSIDIAN = Path(r"D:/PROJECT/Markdown/Obsidian")
REPORT = Path(r"D:/PROJECT/Markdown/blog/2025-blog-public/public/blogs/obsidian-image-missing-report.json")

def search_attachment_paths():
    """搜索可能的附件目录"""
    print("正在搜索 Obsidian 中的 attachments 目录...")
    possible_paths = []

    for p in OBSIDIAN.rglob("attachments"):
        if p.is_dir():
            relative = p.relative_to(OBSIDIAN)
            print(f"  找到: {relative}")
            possible_paths.append(p)

    if not possible_paths:
        print("[WARNING] 未找到任何 attachments 目录")
        return None

    return possible_paths

def find_missing_images():
    """查找报告中缺失的图片"""
    if not REPORT.exists():
        print(f"报告文件不存在: {REPORT}")
        return

    data = json.loads(REPORT.read_text(encoding="utf-8"))
    missing = data.get("missing", [])

    if not missing:
        print("✅ 没有缺失的图片引用")
        return

    # 首先搜索所有 attachments 目录
    attachment_dirs = search_attachment_paths()

    print(f"\n发现 {len(missing)} 个缺失的引用:")
    print("=" * 80)

    found_count = 0
    for item in missing:
        ref = item.get("ref", "")
        source = item.get("source", "")
        img_type = item.get("type", "")

        print(f"\n[NOTE] 来源: {source}")
        print(f"   引用: {ref}")
        print(f"   类型: {img_type}")

        # 尝试查找文件
        if img_type in ["md", "wiki"]:
            # 从引用中提取文件名
            filename = ref.split("/")[-1] if "/" in ref else ref
            filename = filename.split("|")[-1] if "." in filename else filename

            if filename and filename != ref:
                print(f"   文件名: {filename}")

                # 搜索文件
                found = False
                for att_dir in attachment_dirs or []:
                    possible_file = att_dir / filename
                    if possible_file.exists():
                        print(f"   ✅ 找到: {possible_file.relative_to(OBSIDIAN)}")
                        found = True
                        found_count += 1
                        break

                if not found:
                    print(f"   ❌ 未找到文件")
            else:
                print(f"   ⚠️  无法从引用提取文件名")

        elif img_type == "wiki":
            # 特殊 wiki 链接处理
            if ref.startswith("#") and ref.startswith("#^"):
                print(f"   [INFO] 这是指向其他笔记块的内链: {ref}")
            elif "人工智能期末复习笔记" in ref:
                print(f"   [INFO] 这是指向其他笔记的链接: {ref}")
            else:
                print(f"   [UNKNOWN] 未知类型的 wiki 链接")

    print("\n" + "=" * 80)
    print(f"统计: 找到 {found_count}/{len(missing)} 个文件")

    if found_count > 0:
        print("\n[提示] 建议: 运行 repair_obsidian_images.py 时，检查附件目录的路径匹配逻辑")

if __name__ == "__main__":
    find_missing_images()
