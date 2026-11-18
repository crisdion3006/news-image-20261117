# 17 November 2026 — The World in One Day

[![make.fun](https://make.fun/badge/news-image-20261117.svg)](https://make.fun/bounty/news-image-20261117)
[![Rank](https://make.fun/badge/news-image-20261117/crisdion3006/news-image-20261117/rank.svg)](https://make.fun/bounty/news-image-20261117)
[![Reward](https://make.fun/badge/news-image-20261117/crisdion3006/news-image-20261117/reward.svg)](https://make.fun/bounty/news-image-20261117)

One image summing up the world news of **Tuesday 17 November 2026**, built for the
make.fun bounty [news-image-20261117](https://make.fun/bounty/news-image-20261117).

## The image

`entry.png` (1024×1024, ~100 KB) is a newspaper-style infographic: a big date header
and six story panels, one per story, each with a flat illustration, a headline and a
one-line summary. All text is rendered as real text (drawn programmatically with
Python/PIL in `tools/build_image.py`), so nothing garbles at any size.

## The six stories

1. **Kerch Bridge hit** — Ukraine's missile and drone strike partly collapses the
   bridge to Crimea; Russia hits Kyiv bridges in reply. (BBC, CNN)
2. **Trump opens Asia trip** — He lands in Manila for a Quad summit, the first of
   his second term; about 1,500 people protest his visit. (NPR, BBC)
3. **Gulf on edge** — Bahrain says it thwarted an Iranian drone attack; a fourth
   tanker burns in the Strait of Hormuz. (Al Jazeera, BBC)
4. **Huang: I'd come back** — Nvidia's ex-CEO, who quit over an affair with a
   suspected Chinese spy, offers to return. The board says no. (NPR, BBC)
5. **Measles status lost** — The US loses its measles-free status after 26 years:
   more than 5,400 cases and 10 deaths. (BBC)
6. **Jets scrambled** — Japan sends fighter jets up after two suspected Russian
   planes enter its airspace. (FNN)

## How to run

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out node main.ts
```

`main.ts` (Node 22, standard library only) copies `entry.png` to `/output/entry.png`.
Running it twice writes byte-identical output. Rebuild the image with
`python3 tools/build_image.py`.

## License

MIT — see [LICENSE](LICENSE).
