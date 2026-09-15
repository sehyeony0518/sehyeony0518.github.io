#!/usr/bin/env python3
"""Build assets/json/knowledge-graph.json from the content collections.

The corpus graph says one thing: *this piece of writing discusses this concept*.
It had no generator — the committed JSON was stale by 55 study notes and 68
concepts — so this rebuilds it from the files themselves.

An edge exists when a concept's label, or one of its aliases in
_data/concept_aliases.yml, actually occurs in the text. Weight 2 when the concept
is prominent (title, description or a heading), 1 when it appears only in the body.
"""
import json, pathlib, re, sys, collections
import yaml

ROOT = pathlib.Path(__file__).resolve().parent.parent
OUT = ROOT / "assets/json/knowledge-graph.json"

# The seven display sectors, and where an ontology type lands when the concept is
# not one of the hand-curated originals.
TYPE_SECTOR = {
    "Mechanism":      ("Disease & pathology",      "clinical"),
    "Finding":        ("Imaging & acquisition",    "clinical"),
    "ClinicalTarget": ("Disease & pathology",      "clinical"),
    "EvidenceSource": ("Imaging & acquisition",    "clinical"),
    "Standard":       ("Clinical practice",        "clinical"),
    "Principle":      ("Evaluation & reliability", "computational"),
    "Method":         ("Systems & deployment",     "computational"),
    "Metric":         ("Evaluation & reliability", "computational"),
    "Property":       ("Evaluation & reliability", "computational"),
    "ModelFamily":    ("Systems & deployment",     "computational"),
    "Threat":         ("Auditing & causality",     "computational"),
}
# Curation worth keeping: these 33 were placed by hand and read better than the
# type default would. Taken from the previous JSON.
CURATED = {}

COLLECTIONS = [("_study", "note", "/study/"), ("_papers", "review", "/papers/"),
               ("_aiblog", "insight", "/blog/")]


def front_matter(text):
    if not text.startswith("---"):
        return {}, text
    end = text.find("\n---", 3)
    if end < 0:
        return {}, text
    try:
        fm = yaml.safe_load(text[3:end]) or {}
    except yaml.YAMLError:
        fm = {}
    return fm, text[end + 4:]


def main():
    onto = yaml.safe_load((ROOT / "_data/ontology.yml").read_text(encoding="utf-8"))
    aliases = yaml.safe_load((ROOT / "_data/concept_aliases.yml").read_text(encoding="utf-8")) or {}
    concepts = onto["concepts"]

    prev = json.loads(OUT.read_text(encoding="utf-8")) if OUT.exists() else {"nodes": []}
    for n in prev.get("nodes", []):
        if n.get("kind") == "concept" and n["label"] in concepts:
            CURATED[n["label"]] = (n["sector"], n["fam"])

    # One compiled matcher per concept.
    matchers = {}
    for label in concepts:
        forms = [label] + list(aliases.get(label, []))
        pats = []
        for f in forms:
            f = f.strip()
            if not f:
                continue
            # Anchor the front always. Anchor the end too unless the alias is a
            # deliberate stem ("identifiab", "annotat"), which must match its
            # inflections.
            tail = "" if f.isalpha() and f.islower() and not f.endswith(("s", "e", "y")) and len(f) > 6 else r"\b"
            pats.append(r"\b" + re.escape(f) + tail)
        matchers[label] = re.compile("|".join(pats), re.I)

    nodes, links = [], []
    deg = collections.Counter()
    pieces = []

    for folder, kind, base in COLLECTIONS:
        d = ROOT / folder
        if not d.exists():
            continue
        for path in sorted(d.glob("*.md")):
            raw = path.read_text(encoding="utf-8")
            fm, body = front_matter(raw)
            if fm.get("written") is False:
                continue
            title = str(fm.get("title") or path.stem)
            slug = path.stem
            prominent = " ".join([title, str(fm.get("description") or "")]
                                 + re.findall(r"^#{2,4} (.+)$", body, re.M))
            hits = {}
            for label, rx in matchers.items():
                nb = len(rx.findall(body))
                if not nb:
                    continue
                hits[label] = 2 if rx.search(prominent) else 1
            if not hits:
                continue
            pieces.append((kind, slug, title, base, fm, hits))

    # Concept nodes: only those something actually discusses.
    used = collections.Counter()
    for _, _, _, _, _, hits in pieces:
        used.update(hits.keys())

    for label, n in used.items():
        sector, fam = CURATED.get(label) or TYPE_SECTOR.get(concepts[label], ("Systems & deployment", "computational"))
        nodes.append({"id": f"c:{label}", "label": label, "kind": "concept", "url": None,
                      "size": round(2.2 + min(n, 60) / 22.0, 2), "fam": fam,
                      "sector": sector, "deg": 0})

    for kind, slug, title, base, fm, hits in pieces:
        # A piece sits in the sector of the concept it leans on most.
        top = max(hits.items(), key=lambda kv: (kv[1], used[kv[0]]))[0]
        sector, fam = CURATED.get(top) or TYPE_SECTOR.get(concepts[top], ("Systems & deployment", "computational"))
        fams = {CURATED.get(l, TYPE_SECTOR.get(concepts[l], ("", "")))[1] for l in hits}
        nodes.append({"id": f"{kind}:{slug}", "label": title, "kind": kind,
                      "url": f"{base}{slug}/", "size": {"note": 1.8, "review": 1.3, "insight": 1.55}[kind],
                      "fam": "bridge" if len(fams) > 1 else (fams.pop() if fams else "computational"),
                      "sector": sector, "deg": 0})
        for label, w in hits.items():
            lf = CURATED.get(label) or TYPE_SECTOR.get(concepts[label], ("", "computational"))
            links.append({"source": f"{kind}:{slug}", "target": f"c:{label}",
                          "kind": lf[1], "w": w})
            deg[f"{kind}:{slug}"] += 1
            deg[f"c:{label}"] += 1

    for n in nodes:
        n["deg"] = deg[n["id"]]

    OUT.write_text(json.dumps({"nodes": nodes, "links": links}, ensure_ascii=False, indent=1), encoding="utf-8")
    kinds = collections.Counter(n["kind"] for n in nodes)
    print(f"wrote {OUT.relative_to(ROOT)}: {len(nodes)} nodes, {len(links)} links  {dict(kinds)}")
    orphan = [c for c in concepts if c not in used]
    if orphan:
        print(f"  {len(orphan)} ontology concepts no writing discusses:")
        for c in sorted(orphan):
            print(f"    - {c} [{concepts[c]}]")


if __name__ == "__main__":
    main()
