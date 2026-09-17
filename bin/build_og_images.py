#!/usr/bin/env python3
"""Render the share-preview cards: one per note, review and insight, plus the
standing pages.

A link to this site used to preview with the profile photo and a small Twitter
card, which told a reader nothing about the page behind it. Each page now gets a
1200x630 card that reproduces its own top: the breadcrumb line, the title and
the description, on the site's dark ground. The home page gets a different card,
because its top is a name and a photo rather than a heading.

The cards are generated here and committed, so the CI build needs neither
Pillow nor the fonts. Regenerate after editing a title or description:

    python3 bin/build_og_images.py            # only pages whose text changed
    python3 bin/build_og_images.py --all      # every page

Fonts are vendored under bin/fonts; see the README there for their licences.
"""
import hashlib
import json
import pathlib
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

# Standing pages worth a card of their own. Everything else keeps the site
# default. "home" selects the portrait card below.
PAGES = {
    "about.md": "home",
    "study.md": "page",
    "aiblog.md": "page",
    "papers.md": "page",
    "research.md": "page",
    "publications.md": "page",
    "projects.md": "page",
    "mission.md": "page",
    "ministry.md": "page",
}

HOME = {
    "name": "Se-Hyeon Hwang",
    "name_ko": "황세현",
    "tagline": "Medical XAI Researcher",
    "blurb": "Whether a diagnostic model's accuracy comes from clinically valid "
             "evidence or from shortcuts, and how to make that reliance measurable.",
    "foot": "M.S. student  /  Ajou University  /  Embedded & Software Lab",
    "photo": "assets/img/prof_pic.jpg",
}


def font(name, size):
    return ImageFont.truetype(str(FONTS / name), size)


def is_hangul(ch):
    o = ord(ch)
    return 0xAC00 <= o <= 0xD7A3 or 0x1100 <= o <= 0x11FF or 0x3130 <= o <= 0x318F


def runs(text):
    """Split into consecutive same-script runs so each is drawn with a font
    that actually has the glyphs. Inter carries no Hangul."""
    out = []
    for ch in text:
        k = "ko" if is_hangul(ch) else "en"
        if out and out[-1][0] == k:
            out[-1][1] += ch
        else:
            out.append([k, ch])
    return out


class Text:
    """Draws mixed Latin/Hangul with a paired font."""

    def __init__(self, draw, latin, hangul):
        self.d, self.latin, self.hangul = draw, latin, hangul

    def _f(self, kind):
        return self.hangul if kind == "ko" else self.latin

    def width(self, text):
        return sum(self.d.textlength(s, font=self._f(k)) for k, s in runs(text))

    def draw(self, xy, text, fill):
        x, y = xy
        for k, s in runs(text):
            f = self._f(k)
            self.d.text((x, y), s, font=f, fill=fill)
            x += self.d.textlength(s, font=f)
        return x


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


def wrap(t, text, width, max_lines):
    """Greedy wrap, with an ellipsis if the text does not fit in max_lines."""
    words, lines, cur = text.split(), [], ""
    for word in words:
        trial = f"{cur} {word}".strip()
        if t.width(trial) <= width or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = word
            if len(lines) == max_lines:
                break
    if cur and len(lines) < max_lines:
        lines.append(cur)
    if len(lines) == max_lines and len(" ".join(lines).split()) < len(words):
        last = lines[-1]
        while last and t.width(last + "...") > width:
            last = last.rsplit(" ", 1)[0] if " " in last else last[:-1]
        lines[-1] = last + "..."
    return lines


def kicker_for(kind, fm):
    """The line the page itself shows above its title."""
    if kind == "study":
        parts = [fm.get("tab_title"), fm.get("category_title")]
    elif kind == "aiblog":
        parts = ["Insights", fm.get("tag")]
    elif kind == "papers":
        parts = ["Paper Review", fm.get("venue")]
    else:
        parts = ["Se-Hyeon Hwang"]
    return "  /  ".join(str(p) for p in parts if p)


def base_card():
    img = Image.new("RGB", (W, H), BG)
    d = ImageDraw.Draw(img)
    # The accent edge stands in for the page's own coloured rule.
    d.rectangle([0, 0, 10, H], fill=ACCENT)
    return img, d


def footer(d, x, name_bold=True):
    ry = H - PAD - 62
    d.line([(x, ry), (W - PAD, ry)], fill=RULE, width=1)
    f_name = font("Inter-SemiBold.ttf", 24)
    f_site = font("Inter-Regular.ttf", 24)
    t = Text(d, f_name, font("NanumBarunGothic-Bold-subset.ttf", 24))
    end = t.draw((x, ry + 24), "Se-Hyeon Hwang", INK)
    d.text((end, ry + 24), "   sehyeony0518.github.io", font=f_site, fill=MUTED)


def render_entry(stem, kind, fm):
    """A note, review, insight or standing page: kicker, title, description."""
    img, d = base_card()
    t_kick = Text(d, font("Inter-SemiBold.ttf", 25), font("NanumBarunGothic-Bold-subset.ttf", 25))
    t_title = Text(d, font("Inter-Bold.ttf", 60), font("NanumBarunGothic-Bold-subset.ttf", 56))
    t_desc = Text(d, font("Inter-Regular.ttf", 27), font("NanumBarunGothic-Regular-subset.ttf", 26))

    x = PAD + 10
    inner = W - x - PAD
    y = PAD

    kicker = kicker_for(kind, fm)
    if kicker:
        t_kick.draw((x, y), kicker.upper(), ACCENT)
        y += 54

    for line in wrap(t_title, str(fm.get("title") or stem), inner, 4):
        t_title.draw((x, y), line, INK)
        y += 76

    desc = str(fm.get("description") or "").strip()
    if desc:
        y += 18
        room = (H - PAD - 96) - y
        for line in wrap(t_desc, desc, inner, max(0, min(3, room // 42))):
            t_desc.draw((x, y), line, MUTED)
            y += 42

    footer(d, x)
    OUT.mkdir(parents=True, exist_ok=True)
    img.save(OUT / f"{stem}.png", optimize=True)


def render_home(stem):
    """The home page's top is a name beside a photograph, not a heading."""
    img, d = base_card()
    x = PAD + 10

    photo_size = 300
    photo_x = W - PAD - photo_size
    photo_y = (H - photo_size) // 2 - 16
    src = ROOT / HOME["photo"]
    if src.exists():
        p = Image.open(src).convert("RGB")
        # Square crop from the centre, then a rounded mask.
        side = min(p.size)
        left, top = (p.width - side) // 2, (p.height - side) // 2
        p = p.crop((left, top, left + side, top + side)).resize(
            (photo_size, photo_size), Image.LANCZOS
        )
        mask = Image.new("L", (photo_size, photo_size), 0)
        ImageDraw.Draw(mask).rounded_rectangle(
            [0, 0, photo_size - 1, photo_size - 1], radius=24, fill=255
        )
        img.paste(p, (photo_x, photo_y), mask)

    inner = photo_x - x - 56
    f_name = font("Inter-Bold.ttf", 64)
    t_name = Text(d, f_name, font("NanumBarunGothic-Bold-subset.ttf", 46))
    t_line = Text(d, font("Inter-Regular.ttf", 26), font("NanumBarunGothic-Regular-subset.ttf", 25))

    y = PAD + 46
    end = t_name.draw((x, y), HOME["name"], INK)
    d.text(
        (end + 16, y + 20),
        HOME["name_ko"],
        font=font("NanumBarunGothic-Bold-subset.ttf", 40),
        fill=MUTED,
    )
    y += 88

    d.text((x, y), HOME["tagline"], font=font("Inter-SemiBold.ttf", 31), fill=ACCENT)
    y += 62

    for line in wrap(t_line, HOME["blurb"], inner, 3):
        t_line.draw((x, y), line, MUTED)
        y += 40

    d.text((x, H - PAD - 96), HOME["foot"], font=font("Inter-Regular.ttf", 23), fill=MUTED)
    footer(d, x)
    OUT.mkdir(parents=True, exist_ok=True)
    img.save(OUT / f"{stem}.png", optimize=True)


def main(argv):
    rebuild_all = "--all" in argv
    stamps = {}
    if STAMP.exists() and not rebuild_all:
        stamps = json.loads(STAMP.read_text(encoding="utf-8"))

    jobs = []
    for folder, kind in COLLECTIONS:
        d = ROOT / folder
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            fm = front_matter(path.read_text(encoding="utf-8"))
            if fm.get("written") is False:
                continue
            jobs.append((path.stem, kind, fm))
    for name, kind in PAGES.items():
        path = ROOT / "_pages" / name
        if not path.exists():
            continue
        fm = front_matter(path.read_text(encoding="utf-8"))
        jobs.append((f"page-{path.stem}", kind, fm))

    fresh, made = {}, 0
    for stem, kind, fm in jobs:
        if kind == "home":
            key = json.dumps(["home", HOME], ensure_ascii=False, sort_keys=True)
        else:
            key = json.dumps(
                [kind, fm.get("title"), fm.get("description"), kicker_for(kind, fm)],
                ensure_ascii=False,
            )
        digest = hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]
        fresh[stem] = digest
        if stamps.get(stem) == digest and (OUT / f"{stem}.png").exists():
            continue
        if kind == "home":
            render_home(stem)
        else:
            render_entry(stem, kind, fm)
        made += 1

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
