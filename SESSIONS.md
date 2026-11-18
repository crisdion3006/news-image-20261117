# Build note — news-image-20261117

## Approach

One 1024×1024 infographic for Tuesday 17 November 2026, built programmatically
with Python/PIL (`tools/build_image.py`). Flat newspaper-graphic style: navy date
header, six panels (2×3 grid), each with a hand-drawn flat icon, a headline and a
one-line summary. All text is real rendered text — no AI-generated text, so
nothing can garble.

## Research

News researched live on 18 Nov 2026 (browser search, news vertical) and
cross-checked across BBC, CNN, Al Jazeera, NPR and FNN. Six stories chosen for
consequence and breadth (war, diplomacy, Gulf security, tech, health, Asia-Pacific
airspace). Every story was reported on 17 Nov 2026; nothing is from before
13 Nov 2026.

## Revision

- v1: icons drawn at 126 px, body 18 px — icons floated in empty space, bridge and
  jet icons hard to read.
- v2 (revision pass): icons enlarged to 168 px; bridge redrawn with a wider deck
  and a clearer sagging span; plane simplified (dotted route + globe, no confusing
  arc); jet enlarged with a smaller sun and a clearer dashed boundary; fonts
  bumped (headline 26, body 19) for legibility at ~300 px. Re-rendered and
  inspected at full size and at a 300 px downscale.

## Verification

- `entry.png`: 1024×1024, RGB PNG, ~102 KB (limit 1 MiB).
- `main.ts` run twice with MAKEFUN_OUTPUT_DIR=out: byte-identical `entry.png`.
- Kit check: see parent report (transcripts_present failure expected pre-bundle).
