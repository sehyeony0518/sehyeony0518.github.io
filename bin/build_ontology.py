#!/usr/bin/env python3
"""Build assets/json/ontology.json from _data/ontology.yml.

The corpus graph is derived from the writing; this one is asserted by hand, so it
lives in a reviewable YAML file and is compiled rather than mined. The compiler
is also the validator: domain and range are checked here, and a violation is a
build failure rather than a silently odd edge.
"""
import json, sys, yaml, collections, pathlib

SRC = pathlib.Path("_data/ontology.yml")
OUT = pathlib.Path("assets/json/ontology.json")
# Evidence at one end, the things that can undermine it at the other.
ORDER = ["EvidenceSource", "Finding", "ClinicalTarget", "Standard",
         "Method", "ModelFamily", "Metric", "Property", "Threat"]

def main():
    d = yaml.safe_load(SRC.read_text(encoding="utf-8"))
    types, rels, concepts, asserts = d["types"], d["relations"], d["concepts"], d["assertions"]

    errs = []
    if set(ORDER) != set(types):
        errs.append(f"ring order does not cover the types: {set(ORDER) ^ set(types)}")
    seen, ids = set(), set()
    for a in asserts:
        eid, s, rel, o, kind, conf, note, src = a
        if eid in ids: errs.append(f"{eid}: duplicate id")
        ids.add(eid)
        if s not in concepts: errs.append(f"{eid}: unknown subject {s!r}"); continue
        if o not in concepts: errs.append(f"{eid}: unknown object {o!r}"); continue
        if rel not in rels:   errs.append(f"{eid}: unknown relation {rel!r}"); continue
        if concepts[s] not in rels[rel]["domain"]:
            errs.append(f"{eid}: {s} is {concepts[s]}, outside domain of {rel}")
        if concepts[o] not in rels[rel]["range"]:
            errs.append(f"{eid}: {o} is {concepts[o]}, outside range of {rel}")
        if (s, rel, o) in seen: errs.append(f"{eid}: duplicate triple")
        seen.add((s, rel, o))
        if kind not in ("D", "M", "E"): errs.append(f"{eid}: bad claim kind {kind!r}")
        if conf not in ("high", "medium", "low"): errs.append(f"{eid}: bad confidence {conf!r}")
    if errs:
        print("ontology is invalid:", file=sys.stderr)
        for e in errs: print("  -", e, file=sys.stderr)
        return 1

    deg = collections.Counter()
    for _, s, _, o, *_ in asserts:
        deg[s] += 1; deg[o] += 1

    nodes = [{
        "id": f"c:{label}", "label": label, "kind": "concept",
        "sector": etype,                     # the ring and the palette key on this
        "deg": deg[label], "size": deg[label],
        "url": "/research/#graph",
    } for label, etype in concepts.items()]

    links = [{
        "source": f"c:{s}", "target": f"c:{o}", "w": 2,
        "id": eid, "rel": rel, "claim": kind, "conf": conf, "note": note, "src": src,
    } for eid, s, rel, o, kind, conf, note, src in asserts]

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps({
        "nodes": nodes, "links": links,
        "order": ORDER,
        "types": types,
        "relations": {k: v["gloss"] for k, v in rels.items()},
    }, ensure_ascii=False), encoding="utf-8")
    print(f"wrote {OUT}: {len(nodes)} concepts, {len(links)} assertions, "
          f"{sum(1 for a in asserts if a[7])} with a source")
    return 0

if __name__ == "__main__":
    sys.exit(main())
