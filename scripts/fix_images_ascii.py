#!/usr/bin/env python3
"""
Obsidian Missing Image Fixer - ASCII only
"""

from pathlib import Path
import json
import shutil
import urllib.parse

OBSIDIAN = Path(r"D:/PROJECT/Markdown/Obsidian")
REPORT = Path(r"public/blogs/obsidian-image-missing-report.json")

def main():
    print("="*80)
    print("Obsidian Missing Image Fixer")
    print("="*80)

    if not REPORT.exists():
        print("Error: Report not found")
        return

    report_data = json.loads(REPORT.read_text(encoding='utf-8'))
    missing_items = report_data.get("missing", [])

    if not missing_items:
        print("No missing images to process")
        return

    print(f"Found {len(missing_items)} missing references")
    print()

    print("Step 1: Searching for attachment directories...")
    attachment_dirs = []
    for path in OBSIDIAN.rglob("attachments"):
        if path.is_dir():
            attachment_dirs.append(path)
            print(f"  Found: {path.relative_to(OBSIDIAN)}")

    if not attachment_dirs:
        print("Warning: No attachment directories found")
        return

    print()
    print(f"Found {len(attachment_dirs)} attachment directories")
    print()

    found_count = 0
    copied_count = 0

    print("Step 2: Processing images...")
    for idx, item in enumerate(missing_items, 1):
        print()
        print(f"[{idx}/{len(missing_items)}]")
        slug = item.get("slug", "unknown")
        source_file = item.get("source", "")
        ref = item.get("ref", "")
        ref_type = item.get("type", "")

        print(f"  Article: {slug}")
        print(f"  Source: {source_file}")
        print(f"  Type: {ref_type}")
        print(f"  Reference: {ref}")

        if ref_type == "wiki" and ("#^" in ref or "人工智能期末复习笔记" in ref):
            print("  [SKIP] Unsupported special reference")
            continue

        filename = None
        if "/" in ref:
            filename = ref.split("/")[-1]
        else:
            filename = ref

        if "%" in filename:
            filename = urllib.parse.unquote(filename)

        if filename and "|" in filename:
            filename = filename.split("|")[0].strip()

        if not filename:
            print("  [Warning] Failed to extract filename")
            continue

        print(f"  Looking for: {filename}")

        found_file = None
        for att_dir in attachment_dirs:
            candidate = att_dir / filename
            if candidate.exists():
                found_file = candidate
                break

        if found_file:
            found_count += 1
            print(f"  [FOUND] {found_file.relative_to(OBSIDIAN)}")

            target_dir = Path(r"public/blogs") / slug
            if not target_dir.exists():
                print(f"  [ERROR] Target directory not found: {target_dir}")
                continue

            try:
                shutil.copy2(found_file, target_dir / filename)
                copied_count += 1
                print(f"  [SUCCESS] Copied to public/blogs/{slug}/{filename}")
            except Exception as e:
                print(f"  [ERROR] Copy failed: {e}")
        else:
            print("  [FAIL] File not found in Obsidian")

    print()
    print("="*80)
    print("Summary:")
    print(f"  Total: {len(missing_items)}")
    print(f"  Found: {found_count}")
    print(f"  Copied: {copied_count}")
    print("="*80)

    if copied_count > 0:
        print()
        print("Next steps for GitHub:")
        print("1. git status")
        print("2. git add public/blogs/*")
        print("3. git commit -m 'fix: add missing images'")
        print("4. git push")

if __name__ == "__main__":
    main()
