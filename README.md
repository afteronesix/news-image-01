# news-image-01 — The world's news of Friday 13 November 2026, in one image

A front-page montage: the date across the top, a globe at the centre, and six
labelled vignettes around it covering the day's most consequential stories —
the US Senate summoning Nvidia's chief, Zelensky meeting US envoys, a Ukrainian
drone hitting a Russian warship, Iran striking a US radar base in Bahrain, the
FBI's $400m crypto heist, and Harry Kane's record 126th England cap.

The image is drawn procedurally (deterministic vector-style illustration with
short bold labels, spelled exactly) and the program simply copies it to the
output directory.

## Run

```sh
MAKEFUN_OUTPUT_DIR=out node main.ts
```

Writes `out/entry.png` (1024x1024 PNG, under 1 MiB). No network, no
dependencies, same bytes every run.
