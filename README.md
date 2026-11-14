# news-image-01 — The world's news of Friday 13 November 2026, in one image

A newspaper front page of THE WORLD: the lead is a Senate hearing room with
two empty witness chairs (the US Senate summoning Nvidia's chief Huang and
Commerce Secretary Lutnick), below it the day's other big stories — a
Ukrainian drone hitting a Russian warship, the FBI's $400m crypto heist, and
Harry Kane's record 126th England cap.

v3 (this entry): a full-bleed redesign of the v2 photo lead. v2 ranked
#2,557 of 3,118 (7W-4L-1D, 58% win rate) — the photo lead lifted the win
rate from v1's 50%, but at thumbnail scale v2's photo was only ~40% of the
page and the multi-column layout below it shrank to noise. v3 pushes the same
Senate photograph to ~70% of the page with the masthead and headline overlaid
on it, and reduces the rest to three big bold story lines. Three v3 concepts
were pairwise-judged against each other and v2 (CrowLLM vision, 27 pairs,
6 decided — the gateway dropped image parts on 21 calls): the full-bleed
page beat the BREAKING dark edition 2-0 in both orders, the dark edition
beat the Editor's Note variant 2-0, and v2 beat both of those once each;
B vs v2 never got a decided call. The full-bleed page also won the direct
thumbnail inspection: cleanest and most readable at 300px.

The program simply copies the finished image to the output directory and
verifies the copy byte-for-byte (size, PNG signature, full equality), then
logs the output's SHA-256.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out node main.ts
```

Writes `out/entry.png` (1024x1024 PNG, under 1 MiB). No network, no
dependencies, same bytes every run.
