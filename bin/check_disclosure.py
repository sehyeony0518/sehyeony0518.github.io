#!/usr/bin/env python3
"""Flag passages that describe the unpublished submission's method.

The site is public and the ICLR submission is not. A previous pass found a note
that had written out the estimator itself — a frozen classifier's score, paired
marked and unmarked versions of the same case, the per-case difference, and a
patient-level summary of uncertainty — presented as though it were a textbook
illustration. That checker lived in a scratch directory and was lost, so it lives
here now.

The method is recognisable as a *combination*. Any one element is ordinary; the
elements together in one passage are the contribution. This flags paragraphs
where several co-occur, for a human to judge. It is a prompt to look, not a
verdict.

Usage:  python3 bin/check_disclosure.py [files...]     (default: _study, _papers)
"""
import re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

SIGNALS = {
    # Written against the passage that actually leaked (recovered from b7214d8e0),
    # then loosened so a paraphrase still trips them. Each alone is ordinary.
    "held-fixed-model": r"\b(frozen|fixed|pre-?trained|held[- ]fixed)\b[^.\n]{0,40}\b(classifier|model|network|scorer?)\b"
                        r"|\bwithout retraining\b|\bs_?f\b",
    "paired-inputs": r"\b(with and without|marked and unmarked|annotated and unannotated|present and absent)\b"
                     r"|\b(paired|matched|identical)\b[^.\n]{0,60}\b(version|variant|export|render|input|image)s?\b"
                     r"|\bx_?i?\s*\(\s*1\s*\)|\(1\)\s*and\s*.{0,12}\(0\)",
    "annotation-artefact": r"\b(annotation layer|burned-?in|caliper|overlay|marker|measurement mark|text label)\b",
    "paired-effect": r"\b(paired|per-?case|per-?image|per-?patient)\b[^.\n]{0,40}\b(effect|difference|delta|contrast|change)\b"
                     r"|\\Delta_?i\b|\bdifference in (the )?(score|logit|probability|prediction)\b",
    "patient-level-uncertainty": r"\bpatient-?level\b[^.\n]{0,60}\b(uncertaint|interval|variance|bootstrap|cluster)\w*"
                                 r"|\b(cluster(ed)?|bootstrap\w*)\b[^.\n]{0,40}\bby patient\b",
    "reliance-estimand": r"\b(utilisation|utilization|reliance|dependence|dependency)\b[^.\n]{0,50}\b(estimat|quantif|measur|identif)\w*"
                         r"|\blearned dependency\b",
}
THRESHOLD = 3   # distinct signals in one paragraph


def paragraphs(text):
    body = text.split("---", 2)[2] if text.startswith("---") else text
    out, buf, start = [], [], 0
    for i, line in enumerate(body.split("\n")):
        if line.strip():
            if not buf:
                start = i
            buf.append(line)
        elif buf:
            out.append((start, "\n".join(buf))); buf = []
    if buf:
        out.append((start, "\n".join(buf)))
    return out


def main(argv):
    targets = [pathlib.Path(a) for a in argv] or \
              sorted(list((ROOT / "_study").glob("*.md")) + list((ROOT / "_papers").glob("*.md")))
    flagged = 0
    for p in targets:
        if not p.exists():
            print(f"  missing: {p}"); continue
        text = p.read_text(encoding="utf-8")
        for lineno, para in paragraphs(text):
            hits = [k for k, rx in SIGNALS.items() if re.search(rx, para, re.I | re.S)]
            if len(hits) >= THRESHOLD:
                flagged += 1
                try: shown = p.relative_to(ROOT)
                except ValueError: shown = p
                print(f"\n{shown}:{lineno + 1}  [{', '.join(hits)}]")
                print("   " + re.sub(r"\s+", " ", para)[:320])
    print(f"\n{len(targets)} files scanned, {flagged} passage(s) to review"
          f" (>= {THRESHOLD} co-occurring signals).")
    return 1 if flagged else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
