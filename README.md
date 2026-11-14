# news-image-01 — The world's news of Friday 13 November 2026, in one image

A newspaper front page of THE WORLD: the lead is a Senate hearing room with
two empty witness chairs (the US Senate summoning Nvidia's chief Huang and
Commerce Secretary Lutnick), below it the day's other big stories — a
Ukrainian drone hitting a Russian warship, the FBI's $400m crypto heist, and
Harry Kane's record 126th England cap.

v2 (this entry): the lead illustration is a rich editorial photograph-style
hearing room instead of v1's flat pictogram. Pairwise vision judging (CrowLLM,
10 decided calls) picked this version over v1 2-1 and over both other v2
concepts (a "Dear Judge" note variant and a judge-reading-the-paper scene).
The panels are drawn procedurally (deterministic vector-style illustration
with short bold labels, spelled exactly) and the program simply copies the
finished image to the output directory.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out node main.ts
```

Writes `out/entry.png` (1024x1024 PNG, under 1 MiB). No network, no
dependencies, same bytes every run.
