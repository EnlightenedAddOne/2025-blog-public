#!/usr/bin/env python3
"""
Obsidian 缺失图片修复工具
专为 GitHub 提交优化
功能: 找出缺失的图片，从 Obsidian 复制到博客项目
"""

from pathlib import Path
import json
import shutil

def fix_obsidian_images():
    # 配置路径
    OBSIDIAN = Path(r"D:/PROJECT/Markdown/Obsidian")
    REPORT = Path(r"public/blogs/obsidian-image-missing-report.json")

    print("='='*80")
    print("[Obsidian 图片修复工具]")
    print("='='*80")

    # 读取缺失图片报告
    if not REPORT.exists():
        print(f"[错误] 未找到报告文件: {REPORT}")
        return

    report_data = json.loads(REPORT.read_text(encoding='utf-8'))
    missing_items = report_data.get("missing", [])

    if not missing_items:
        print("[信息] 没有缺失的图片需要处理")
        return

    print(f"[信息] 发现 {len(missing_items)} 个缺失引用\n")

    found_count = 0
    copied_count = 0

    # 查找所有 attachments 目录
    print("[步骤1] 搜索 Obsidian 中的 attachments 目录...")
    attachment_dirs = []
    for path in OBSIDIAN.rglob("attachments"):
        if path.is_dir():
            attachment_dirs.append(path)
            relative = path.relative_to(OBSIDIAN)
            print(f"   [找到] {relative}")

    if not attachment_dirs:
        print("[警告] 未发现 attachments 目录")
        return

    print(f"\n[信息] 发现 {len(attachment_dirs)} 个 attachments 目录\n")

    # 处理每个缺失项目
    print("[步骤2] 开始处理缺失图片...")

    for idx, item in enumerate(missing_items, 1):
        slug = item.get("slug", "unknown")
        source_file = item.get("source", "")
        ref = item.get("ref", "")
        ref_type = item.get("type", "")

        print(f"\n[{idx}/{len(missing_items)}]")
        print(f"   文章: {slug}")
        print(f"   源文件: {source_file}")
        print(f"   引用类型: {ref_type}")
        print(f"   引用路径: {ref}")

        # 跳过外部链接和块引用
        if ref_type == "wiki" and ("#^" in ref or "人工智能期末复习笔记" in ref):
            print(f"   [跳过] 不支持的特殊引用: {ref}")
            continue

        # 提取文件名
        filename = None
        if "/" in ref:
            filename = ref.split("/")[-1]
        elif "\\" in ref:
            filename = ref.split("\\")[-1]
        else:
            # 简单文件名
            filename = ref

        # 去除 URL 编码
        if "%" in filename:
            import urllib.parse
            filename = urllib.parse.unquote(filename)

        # 去除宽度参数 (处理 Obsidian 语法 like.jpg|600)
        if filename and "|" in filename:
            filename = filename.split("|")[0].strip()

        if not filename:
            print(f"   [警告] 无法提取文件名")
            continue

        print(f"   [查找] 文件: {filename}")

        # 在 Obsidian 中搜索该文件
        found_file = None
        for att_dir in attachment_dirs:
            candidate = att_dir / filename
            if candidate.exists() and candidate.is_file():
                found_file = candidate
                break

        if found_file:
            found_count += 1
            print(f"   [找到] 文件位置: {found_file.relative_to(OBSIDIAN)}")

            # 确定目标路径
            target_dir = Path(r"public/blogs") / slug
            if not target_dir.exists():
                print(f"   [错误] 目标目录不存在: {target_dir}")
                continue

            # 复制图片
            try:
                shutil.copy2(found_file, target_dir / filename)
                copied_count += 1
                print(f"   [成功] 已复制到: public/blogs/{slug}/{filename}")
            except Exception as e:
                print(f"   [错误] 复制失败: {e}")
        else:
            print(f"   [失败] 在 Obsidian 中未找到文件")

    # 总结
    print("\n" + "[总结]")
    print(f"   总计处理: {len(missing_items)}")
    print(f"   找到文件: {found_count}")
    print(f"   复制成功: {copied_count}")
    print()

    if found_count > 0:
        print("\n[下一步] 请运行以下命令查看更改并提交到GitHub:")
        print("1. git status  # 查看更改的文件")
        print("2. git add public/blogs/*/attachments*  # 添加图片")
        print("3. git commit -m 'add: 补充缺失的Obsidian图片引用'  # 提交更改")
        print("4. git push  # 推送到GitHub")
        print("=" * 80)

if __name__ == "__main__":
    fix_obsidian_images()
