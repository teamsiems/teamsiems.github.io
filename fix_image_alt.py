"""
For any image with empty alt text but a title, promote the title to alt text.

Before: ![](url "My Title")
After:  ![My Title](url "My Title")

Also handles linked images:
Before: [![](url "My Title")](link)
After:  [![My Title](url "My Title")](link)
"""
import re
import glob

CONTENT_DIR = "content"

# Match ![](anything "title" anything) — capture groups:
# 1: everything before the quote  2: title text  3: everything after closing quote
PATTERN = re.compile(r'!\[\]\(([^"]*)"([^"]+)"([^)]*)\)')


def fix_alts(text):
    return PATTERN.sub(lambda m: f'![{m.group(2)}]({m.group(1)}"{m.group(2)}"{m.group(3)})', text)


def main():
    files = sorted(glob.glob(f"{CONTENT_DIR}/*.md"))
    changed = 0
    total_replacements = 0

    for filepath in files:
        with open(filepath, encoding="utf-8") as f:
            original = f.read()

        updated = fix_alts(original)

        if updated != original:
            count = len(PATTERN.findall(original))
            total_replacements += count
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(updated)
            print(f"  {filepath} ({count} fixed)")
            changed += 1

    print(f"\nDone. {total_replacements} images fixed across {changed} files.")


if __name__ == "__main__":
    main()
