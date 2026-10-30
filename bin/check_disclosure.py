#!/usr/bin/env python3
"""Flag passages that describe the unpublished submission's method.

The site is public and the submission is not. What must not appear here is a
particular *combination* of ordinary ingredients: any one of them is textbook,
and the combination is the contribution. This file therefore does not spell the
combination out. It scores co-occurring signals and prints the passage for a
human to judge.

It is a prompt to look, not a clearance. Four separate faults have let real
passages through: word order, plain-language phrasing, a missing pattern for
"the same case", and -- the worst -- display math. A formula on its own line is
its own paragraph, and a bare formula carries no prose signals, so the most
precise statement of a method was structurally invisible to the paragraph
scorer. Blocks are now joined to the prose that introduces them and scored in a
sliding window, and the notation itself trips a report on its own.

The deploy workflow runs this. It cannot gate on "nothing flagged", because
several passages are ordinary statistics that happen to score: a bootstrap that
resamples patients, a Lipschitz bound on a score, a summary of a published
counterfactual study. Those are recorded in bin/disclosure_baseline.json, by
hash, after being read. The gate is therefore "nothing flagged that was not
already read", which is the question a reviewer can actually answer. Editing a
baselined passage changes its hash and brings it back for review, which is the
behaviour wanted: the text is what was judged, not the file it sits in.

Usage:
    python3 bin/check_disclosure.py [files...]       report, and fail on anything new
    python3 bin/check_disclosure.py --all            report every hit, baseline included
    python3 bin/check_disclosure.py --write-baseline accept the current hits
"""
import hashlib, json, re, sys, pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent
BASELINE = ROOT / "bin/disclosure_baseline.json"

SIGNALS = {
    # Both orders, and the input pipeline as well as the model: four real
    # passages were missed because the adjective modified the image, or because
    # the noun came before "remain fixed" rather than after it.
    "held-fixed-model": r"\b(frozen|fixed|unchanged|pre-?trained|held[- ]fixed)\b[^.\n]{0,40}"
                        r"\b(classifier|model|network|scorer?|predictor|image|input|export|pipeline|preprocessing)\b"
                        r"|\b(classifier|model|network|scorer?|predictor|image|input|export|pipeline|preprocessing)\b[^.\n]{0,40}"
                        r"\b(remains?|held|kept|stays?)\b[^.\n]{0,20}\b(fixed|frozen|unchanged|constant)\b"
                        r"|\bwithout retraining\b",
    "paired-inputs": r"\b(with and without|marked and unmarked|unmarked and marked|annotated and unannotated|present and absent)\b"
                     r"|\b(paired|matched|identical)\b[^.\n]{0,60}\b(version|variant|export|render|input|image|acquisition)s?\b"
                     r"|\b(same|identical)\b[^.\n]{0,40}\b(case|patient|image|frame|study|export)s?\b",
    "annotation-artefact": r"\b(annotation layer|burned-?in|caliper|overlay|marker|measurement mark|text label)\b",
    "paired-effect": r"\b(paired|per-?case|per-?image|per-?patient)\b[^.\n]{0,40}\b(effect|difference|delta|contrast|change|response)\b"
                     r"|\bdifference in (the )?(score|logit|probability|prediction)\b",
    "patient-level-uncertainty": r"\bpatient-?level\b[^.\n]{0,60}\b(uncertaint|interval|variance|bootstrap|cluster)\w*"
                                 r"|\b(cluster(ed)?|resampl\w*|bootstrap\w*)\b[^.\n]{0,40}\b(by|per) patient"
                                 r"|\bresample patients\b",
    # The estimand gets written in plain words too, not only as a noun phrase.
    "reliance-estimand": r"\b(utilisation|utilization|reliance|dependence|dependency)\b[^.\n]{0,50}\b(estimat|quantif|measur|identif)\w*"
                         r"|\blearned dependency\b"
                         r"|\b(marker|overlay|annotation|caliper)[- ]?(edit )?sensitivity\b"
                         r"|\bsensitivity to\b[^.\n]{0,30}\b(marker|overlay|annotation|caliper)\b"
                         r"|\b(model|classifier|network|head|predictor)\b[^.\n]{0,40}"
                         r"\b(uses|relies on|responds? to|is driven by)\b",
}

# The notation. Each of these is reported on its own, whatever the prose around
# it scores: a formula states the method more precisely than any sentence, and
# the paragraph scorer cannot see one.
#
# These are written to be narrow. An indexed difference on its own is ordinary
# mathematics -- it is a suboptimality gap in the bandit note, an interval
# length in the radiance-field note, a marginal contribution in the Shapley
# note -- so what is matched is a *scalar score function applied twice and
# subtracted*, and the frozen-score symbol used as a function.
NOTATION = {
    "score-difference": r"(s_?\{?f?\}?)\s*\((?:[^()]|\([^()]*\))*\)\s*[-−]\s*\1\s*\(",
    "frozen-score-symbol": r"\bs_\{?f\}?\s*\(",
    "potential-outcome-inputs": r"x_?\{?i\}?\s*(\^\{?)?\(\s*[01]\s*\)",
}

THRESHOLD = 3   # distinct signals in one window


def blocks(text):
    """Paragraphs, with a display-math block joined to the prose that
    introduces it. A bare formula is not a paragraph of its own."""
    body = text.split("---", 2)[2] if text.startswith("---") else text
    out, buf, start = [], [], 0
    for i, line in enumerate(body.split("\n")):
        if line.strip():
            if not buf:
                start = i
            buf.append(line)
        elif buf:
            out.append([start, "\n".join(buf)]); buf = []
    if buf:
        out.append([start, "\n".join(buf)])

    joined = []
    for start, para in out:
        is_math = para.lstrip().startswith("$$") or para.rstrip().endswith("$$")
        if is_math and joined:
            joined[-1][1] += "\n\n" + para
        else:
            joined.append([start, para])
    return [(s, p) for s, p in joined]


def windows(bs, width=2):
    """Consecutive blocks, scored together. A method is often one sentence of
    setup, then the quantity, then how its uncertainty is handled."""
    for i in range(len(bs)):
        for w in range(1, width + 1):
            if i + w <= len(bs):
                yield bs[i][0], "\n\n".join(p for _, p in bs[i:i + w])


def fingerprint(chunk):
    return hashlib.sha256(re.sub(r"\s+", " ", chunk).strip().encode()).hexdigest()[:16]


def collect(targets):
    """Every flagged window, as (path, line, tags, fingerprint, excerpt)."""
    found, reported = [], set()
    for p in targets:
        if not p.exists():
            print(f"  missing: {p}"); continue
        text = p.read_text(encoding="utf-8")
        for lineno, chunk in windows(blocks(text)):
            hits = [k for k, rx in SIGNALS.items() if re.search(rx, chunk, re.I | re.S)]
            notes = [k for k, rx in NOTATION.items() if re.search(rx, chunk)]
            if not notes and len(hits) < THRESHOLD:
                continue
            flat = re.sub(r"\s+", " ", chunk)
            if flat[:80] in reported:
                continue
            reported.add(flat[:80])
            try: shown = str(p.relative_to(ROOT))
            except ValueError: shown = str(p)
            found.append((shown, lineno + 1, notes + hits, fingerprint(chunk), flat[:300]))
    return found


def main(argv):
    write = "--write-baseline" in argv
    show_all = "--all" in argv
    argv = [a for a in argv if not a.startswith("--")]
    targets = [pathlib.Path(a) for a in argv] or sorted(
        list((ROOT / "_study").glob("*.md"))
        + list((ROOT / "_papers").glob("*.md"))
        + list((ROOT / "_aiblog").glob("*.md")))

    found = collect(targets)

    if write:
        # Deliberately no signal names and no excerpt. This file is public, and a
        # list of which categories fired is a shorter route to the boundary than
        # the passages themselves. Rerun the checker to see the tags.
        BASELINE.write_text(json.dumps(
            {"read": sorted({f[3] for f in found}),
             "note": "Hashes of passages that have been read and judged ordinary. "
                     "Regenerate with: python3 bin/check_disclosure.py --write-baseline",
             "entries": [{"file": f[0], "line": f[1], "hash": f[3]}
                         for f in sorted(found)]},
            indent=1), encoding="utf-8")
        print(f"baseline written: {len(found)} passage(s) accepted "
              f"-> {BASELINE.relative_to(ROOT)}")
        return 0

    read = set()
    if BASELINE.exists():
        read = set(json.loads(BASELINE.read_text(encoding="utf-8")).get("read", []))

    new = [f for f in found if f[3] not in read]
    for path, line, tags, fp, excerpt in (found if show_all else new):
        mark = "" if fp in read else "  <-- NEW"
        print(f"\n{path}:{line}  [{', '.join(tags)}]{mark}")
        print("   " + excerpt)

    still = {f[3] for f in found}
    stale = sorted(read - still)
    print(f"\n{len(targets)} files scanned. {len(found)} passage(s) flagged, "
          f"{len(found) - len(new)} previously read, {len(new)} new.")
    if stale:
        print(f"{len(stale)} baseline entr{'y' if len(stale) == 1 else 'ies'} no longer "
              f"present (edited or removed); rerun --write-baseline to tidy.")
    if new:
        print("\nA new passage is flagged. Read it, and if it is ordinary, accept it with")
        print("  python3 bin/check_disclosure.py --write-baseline")
    print("This is a prompt to look. A clean run is not a clearance.")
    return 1 if new else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
