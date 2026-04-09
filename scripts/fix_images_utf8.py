#!/usr/bin/env python3
"""
Obsidian Missing Image Fixer - Debug mode output to log file
"""

from pathlib import Path
import json
import shutil
import urllib.parse
import sys

# Change stdout encoding to UTF-8
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

OBSIDIAN = Path(r"D:/PROJECT/Markdown/Obsidian")
REPORT = Path(r"public/blogs/obsidian-image-missing-report.json")
LOG = Path(r"obsidian-image-fix-log.txt")

def log(msg):
    """Log to both console (ASCII) and file (UTF-8)"""
    ascii_msg = msg.encode('ascii', errors='replace').decode('ascii')
    print(ascii_msg)
    LOG.write_text(LOG.read_text(encoding='utf-8') + msg + "\n", encoding='utf-8') if LOG.exists() else LOG.write_text(msg + "\n", encoding='utf-8')

def main():
    log("="*80)
    log("Obsidian Missing Image Fixer - Log file: obsidian-image-fix-log.txt")
    log("="*80)

    if not REPORT.exists():
        log("ERROR: Report not found")
        return

    report_data = json.loads(REPORT.read_text(encoding='utf-8'))
    missing_items = report_data.get("missing", [])

    if not missing_items:
        log("No missing images to process")
        return

    log(f"Found {len(missing_items)} missing references")
    log("")

    log("Step 1: Searching for attachment directories...")
    attachment_dirs = []
    for path in OBSIDIAN.rglob("attachments"):
        if path.is_dir():
            attachment_dirs.append(path)
            log(f"  Found: {path.relative_to(OBSIDIAN)}")

    if not attachment_dirs:
        log("Warning: No attachment directories found")
        return

    log("")
    log(f"Found {len(attachment_dirs)} attachment directories")
    log("")

    found_count = 0
    copied_count = 0

    log("Step 2: Processing images...")
    for idx, item in enumerate(missing_items, 1):
        log("")
        log(f"[{idx}/{len(missing_items)}]")
        slug = item.get("slug", "unknown")
        # Escape Unicode characters for console
        source_file_safe = item.get("source", "[PATH_CONTAINS_UNICODE]")
        ref_safe = item.get("ref", "[PATH_CONTAINS_UNICODE]")
        ref_type = item.get("type", "")

        log(f"  Article: {slug}")
        log(f"  Source: {source_file_safe}")
        log(f"  Type: {ref_type}")
        log(f"  Reference: {ref_safe}")

        # Skip special cases
        if ref_type == "wiki" and ("#^" in ref_safe or "人工智能期末复习笔记" in ref_safe):
            log("  SKIPPED: Unsupported wiki reference")
            continue

        filename = None
        if "/" in ref_safe:
            filename = ref_safe.split("/")[-1]
        else:
            filename = ref_safe

        if filename and "%" in filename:
            filename = urllib.parse.unquote(filename)

        if filename and "|" in filename:
            filename = filename.split("|")[0].strip()

        if not filename:
            log("  Warning: failed to extract filename")
            continue

        log(f"  Looking for: {filename}")

        found_file = None
        for att_dir in attachment_dirs:
            candidate = att_dir / filename
            if candidate.exists():
                found_file = candidate
                break

        if found_file:
            found_count += 1
            log(f"  OK: Found {found_file.relative_to(OBSIDIAN)}")

            target_dir = Path(r"public/blogs") / slug
            if not target_dir.exists():
                log(f"  ERROR: Target dir missing: {slug}")
                continue

            try:
                shutil.copy2(found_file, target_dir / filename)
                copied_count += 1
                log(f"  SUCCESS: Copied to public/blogs/{slug}/{filename}")
            except Exception as e:
                log(f"  ERROR: Copy failed: {e}")
        else:
            log(f"  FAILED: Not found: {filename}")

    log("")
    log("="*80)
    log(f"Summary: Total={len(missing_items)}, Found={found_count}, Copied={copied_count}")
    log("="*80)

    if copied_count > 0:
        log("")
        log("Next steps for GitHub:")
        log("1. git status")
        log("2. git add public/blogs/*")
        log("3. git commit -m 'fix: add missing images'")
        log("4. git push")

    log("")
    log(f"Detailed log saved to: {LOG}")

if __name__ == "__main__":
    main()
