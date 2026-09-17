#!/usr/bin/env python3
"""Render one share-preview image per note, review and insight.

A link to this site used to preview with the profile photo and a small Twitter
card, which told a reader nothing about the page behind the link. Each page now
gets a 1200x630 card that reproduces its own top: the breadcrumb line, the
title, and the description, on the site's dark ground.

The cards are generated here and committed, so the CI build needs neither
Pillow nor the fonts. Regenerate after editing a title or description:

    python3 bin/build_og_images.py            # only pages whose text changed
    python3 bin/build_og_images.py --all      # every page

Inter is vendored under bin/fonts (SIL Open Font License, see the LICENSE there).
"""
import hashlib
import json
import pathlib
import re
import sys

import yaml
from PIL import Image, ImageDraw, ImageFont

ROOT = pathlib.Path(__file__).resolve().parent.parent
FONTS = ROOT / "bin/fonts"
OUT = ROOT / "assets/img/og"
STAMP = OUT / ".sources.json"

W, H = 1200, 630
PAD = 72
# The site opens in dark, and these are its own tokens.
BG = "#1c1c1d"
INK = "#e8e8e8"
MUTED = "#8e8e90"
ACCENT = "#c9737d"
RULE = "#33343a"

COLLECTIONS = [("_study", "study"), ("_papers", "papers"), ("_aiblog", "aiblog")]


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def front_matter(text):
    if not text.startswith("---"):
        return {}
    end = text.find("\n---", 3)
    if end < 0:
        return {}
    try:
        return yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        return {}


def wrap(draw, text, fnt, width, max_lines):
    """Greedy wrap, with an ellipsis if the text does not fit in max_lines."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if draw.textlength(trial, font=fnt) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
            if len(lines) == max_lines:
                break
    if cur and len(lines) < max_lines:
        lines.append(cur)
    if len(lines) == max_lines and (len(" ".join(lines).split()) < len(words)):
        last = lines[-1]
        while last and draw.textlength(last + "...", font=fnt) > width:
            last = last.rsplit(" ", 1)[0] if " " in last else last[:-1]
        lines[-1] = last + "..."
    return lines


def kicker_for(kind, fm):
    """The line the page itself shows above its title."""
    if kind == "study":
        parts = [fm.get("tab_title"), fm.get("category_title")]
    elif kind == "aiblog":
        parts = ["Insights", fm.get("tag")]
    else:
        parts = ["Paper Review", fm.get("venue")]
    return "  /  ".join(str(p) for p in parts if p)


def render(path, kind, fm):
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)

    # The accent edge stands in for the page's own coloured rule.
    d.rectangle([0, 0, 10, H], fill=ACCENT)

    f_kick = font("Inter-SemiBold.ttf", 25)
    f_title = font("Inter-Bold.ttf", 60)
    f_desc = font("Inter-Regular.ttf", 27)
    f_name = font("Inter-SemiBold.ttf", 24)
    f_site = font("Inter-Regular.ttf", 24)

    x = PAD + 10
    inner = W - x - PAD
    y = PAD

    kicker = kicker_for(kind, fm)
    if kicker:
        d.text((x, y), kicker.upper(), font=f_kick, fill=ACCENT)
        y += 54

    title = str(fm.get("title") or path.stem)
    lines = wrap(d, title, f_title, inner, 4)
    for line in lines:
        d.text((x, y), line, font=f_title, fill=INK)
        y += 76

    desc = str(fm.get("description") or "").strip()
    if desc:
        y += 18
        # Leave room for the footer rule and the identity line.
        room = (H - PAD - 96) - y
        for line in wrap(d, desc, f_desc, inner, max(0, min(3, room // 42))):
            d.text((x, y), line, font=f_desc, fill=MUTED)
            y += 42

    ry = H - PAD - 62
    d.line([(x, ry), (W - PAD, ry)], fill=RULE, width=1)
    d.text((x, ry + 24), "Se-Hyeon Hwang", font=f_name, fill=INK)
    off = d.textlength("Se-Hyeon Hwang", font=f_name)
    d.text((x + off, ry + 24), "   sehyeony0518.github.io", font=f_site, fill=MUTED)

    OUT.mkdir(parents=True, exist_ok=True)
    img.save(OUT / f"{path.stem}.png", optimize=True)


def main(argv):
    rebuild_all = "--all" in argv
    stamps = {}
    if STAMP.exists() and not rebuild_all:
        stamps = json.loads(STAMP.read_text(encoding="utf-8"))

    fresh, made = {}, 0
    for folder, kind in COLLECTIONS:
        d = ROOT / folder
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            fm = front_matter(path.read_text(encoding="utf-8"))
            if fm.get("written") is False:
                continue
            key = json.dumps(
                [kind, fm.get("title"), fm.get("description"), kicker_for(kind, fm)],
                ensure_ascii=False,
            )
            digest = hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]
            fresh[path.stem] = digest
            if stamps.get(path.stem) == digest and (OUT / f"{path.stem}.png").exists():
                continue
            render(path, kind, fm)
            made += 1

    # Drop cards whose page is gone.
    removed = 0
    for png in OUT.glob("*.png"):
        if png.stem not in fresh:
            png.unlink()
            removed += 1

    STAMP.write_text(json.dumps(fresh, indent=0, sort_keys=True), encoding="utf-8")
    total = len(list(OUT.glob("*.png")))
    print(f"og images: {made} written, {removed} removed, {total} total in {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main(sys.argv[1:])
