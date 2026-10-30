#!/usr/bin/env python3
"""Fail if any page's front matter does not parse.

Written after /research/ went 404 on a live deploy. An unquoted YAML scalar
cannot contain ": ", and a description had one, so the front matter failed to
parse and Jekyll skipped the page. The build still reported success, so nothing
caught it until a URL was checked by hand.

    python3 bin/check_frontmatter.py            # every collection and page
    python3 bin/check_frontmatter.py FILE ...   # just these
"""
import pathlib
import sys

import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
DIRS = ["_pages", "_posts", "_study", "_papers", "_aiblog", "_news"]


def check(path):
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return None
    end = text.find("\n---", 3)
    if end < 0:
        return "no closing --- for the front matter"
    try:
        yaml.safe_load(text[3:end])
    except yaml.YAMLError as exc:
        first = str(exc).splitlines()[0]
        # The common case is worth naming, because the message does not.
        hint = ""
        for line in text[3:end].splitlines():
            if ": " in line.split(": ", 1)[-1] and not line.lstrip().startswith("#"):
                key = line.split(":", 1)[0].strip()
                if not line.split(":", 1)[1].strip().startswith(('"', "'", "|", ">")):
                    hint = f' (an unquoted value for "{key}" contains ": "; quote it)'
                    break
        return first + hint
    return None


def main(argv):
    targets = [pathlib.Path(a) for a in argv] or [
        p for d in DIRS if (ROOT / d).exists() for p in sorted((ROOT / d).glob("*.md"))
    ]
    bad = 0
    for path in targets:
        problem = check(path)
        if problem:
            print(f"{path}: {problem}")
            bad += 1
    print(f"{len(targets)} files checked, {bad} with unparseable front matter")
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
