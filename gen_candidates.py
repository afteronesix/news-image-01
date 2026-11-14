#!/usr/bin/env python3
"""Draw 3 news-image-01 candidates procedurally with PIL (deterministic).
NOT part of the final entry - deleted before the final commit.
"""
import os
from PIL import Image, ImageDraw, ImageFont

W = H = 1024
PAPER = (247, 243, 234)
INK = (28, 28, 28)
NAVY = (30, 58, 92)
RED = (166, 43, 43)
GREY = (107, 107, 107)
SEA = (91, 122, 153)
SEA_DK = (60, 88, 120)
GOLD = (201, 162, 39)
GREEN = (62, 122, 78)
BROWN = (122, 90, 60)
WHITE = (255, 255, 255)
SKIN = (232, 190, 150)
DARK = (40, 40, 48)

FONT_DIR = "/usr/share/fonts/truetype/dejavu"
BOLD = os.path.join(FONT_DIR, "DejaVuSans-Bold.ttf")
REG = os.path.join(FONT_DIR, "DejaVuSans.ttf")


def fb(size):
    return ImageFont.truetype(BOLD, size)


def fr(size):
    return ImageFont.truetype(REG, size)


def tcenter(d, cx, y, s, font, fill=INK):
    """Draw text centred on cx at y; return bottom y."""
    bb = d.textbbox((0, 0), s, font=font)
    w = bb[2] - bb[0]
    d.text((cx - w / 2 - bb[0], y), s, font=font, fill=fill)
    return y + (bb[3] - bb[1])


def tlines(d, cx, y, lines, font, fill=INK, gap=6):
    for s in lines:
        y = tcenter(d, cx, y, s, font, fill)
        y += gap
    return y


def card(d, x, y, w, h, fill=WHITE, outline=(200, 192, 175), width=3):
    d.rounded_rectangle([x, y, x + w, y + h], radius=10, fill=fill,
                        outline=outline, width=width)


def flag_us(d, x, y, w, h):
    """Small US flag."""
    d.rectangle([x, y, x + w, y + h], fill=WHITE, outline=INK, width=2)
    for i in range(7):
        if i % 2 == 0:
            d.rectangle([x, y + i * h / 7, x + w, y + (i + 1) * h / 7],
                        fill=RED)
    d.rectangle([x, y, x + w * 0.4, y + h * 4 / 7], fill=NAVY)


def flag_ua(d, x, y, w, h):
    d.rectangle([x, y, x + w, y + h / 2], fill=(0, 91, 187))
    d.rectangle([x, y + h / 2, x + w, y + h], fill=(255, 213, 0))
    d.rectangle([x, y, x + w, y + h], outline=INK, width=2)


def draw_globe(d, cx, cy, r):
    d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(70, 110, 160),
              outline=NAVY, width=4)
    # latitude / longitude arcs
    for k in (-0.55, 0, 0.55):
        d.arc([cx - r, cy - r + k * r, cx + r, cy + r + k * r],
              200, 340, fill=WHITE, width=3)
    d.ellipse([cx - r * 0.55, cy - r, cx + r * 0.55, cy + r],
              outline=WHITE, width=3)
    # continents (stylised blobs)
    d.ellipse([cx - r * 0.7, cy - r * 0.55, cx - r * 0.1, cy + r * 0.1],
              fill=(127, 169, 107))
    d.ellipse([cx + r * 0.05, cy - r * 0.2, cx + r * 0.65, cy + r * 0.5],
              fill=(127, 169, 107))
    d.ellipse([cx - r * 0.3, cy + r * 0.35, cx + r * 0.25, cy + r * 0.75],
              fill=(127, 169, 107))


def draw_senate(d, x, y, w, h):
    """Senate hearing: long desk, two empty witness chairs, mics, flag."""
    # back wall + floor
    d.rectangle([x, y, x + w, y + h], fill=(232, 226, 210))
    # wall seal (fills tall panels)
    sx, sy, sr = x + w * 0.5, y + h * 0.26, min(w, h) * 0.16
    d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=NAVY,
              outline=GOLD, width=3)
    d.ellipse([sx - sr * 0.55, sy - sr * 0.55, sx + sr * 0.55, sy + sr * 0.55],
              outline=WHITE, width=2)
    # flag on pole, left
    fx, fy = x + 14, y + 14
    d.line([fx + 4, fy, fx + 4, fy + 78], fill=INK, width=4)
    flag_us(d, fx + 8, fy + 2, 52, 32)
    # desk (position scales with box height)
    dy = y + h - 78 if h < 300 else y + int(h * 0.62)
    d.rectangle([x + 8, dy, x + w - 8, dy + 58], fill=BROWN,
                outline=INK, width=3)
    d.rectangle([x + 8, dy, x + w - 8, dy + 12], fill=(150, 116, 78))
    # two empty witness chairs behind desk
    for cx in (x + w * 0.32, x + w * 0.68):
        d.rectangle([cx - 34, dy - 74, cx + 34, dy - 6], fill=(58, 58, 66),
                    outline=INK, width=3)
        d.rectangle([cx - 34, dy - 74, cx + 34, dy - 44], fill=(74, 74, 84),
                    outline=INK, width=3)
        d.line([cx - 26, dy - 6, cx - 26, dy + 2], fill=INK, width=4)
        d.line([cx + 26, dy - 6, cx + 26, dy + 2], fill=INK, width=4)
    # microphones on desk
    for mx in (x + w * 0.32, x + w * 0.68):
        d.line([mx, dy - 2, mx - 12, dy - 34], fill=INK, width=3)
        d.ellipse([mx - 20, dy - 42, mx - 6, dy - 28], fill=INK)
    # nameplates
    for cx in (x + w * 0.32, x + w * 0.68):
        d.rectangle([cx - 26, dy + 20, cx + 26, dy + 40], fill=WHITE,
                    outline=INK, width=2)


def draw_warship(d, x, y, w, h):
    """Grey warship on a cold sea, smoke and a drone hit."""
    d.rectangle([x, y, x + w, y + h], fill=(214, 226, 236))
    # sky + smoke
    for sx, sy, sr in ((x + w * 0.62, y + 16, 22), (x + w * 0.72, y + 6, 16),
                       (x + w * 0.55, y + 30, 14)):
        d.ellipse([sx - sr, sy - sr, sx + sr, sy + sr], fill=(120, 120, 120))
    # sea
    sy = y + h * 0.62
    d.rectangle([x, sy, x + w, y + h], fill=SEA)
    for wy in (sy + 14, sy + 34, sy + 54):
        d.line([x + 8, wy, x + w - 8, wy], fill=WHITE, width=3)
    # hull
    hy = sy - 6
    d.polygon([(x + 12, hy), (x + w - 12, hy), (x + w - 34, hy + 34),
               (x + 34, hy + 34)], fill=(96, 104, 112), outline=INK, width=3)
    d.rectangle([x + 18, hy - 4, x + w - 18, hy + 2], fill=(70, 76, 84))
    # superstructure + mast
    d.rectangle([x + w * 0.42, hy - 46, x + w * 0.62, hy - 2], fill=(120, 128,
                136), outline=INK, width=3)
    d.line([x + w * 0.52, hy - 46, x + w * 0.52, hy - 78], fill=INK, width=4)
    # hit burst on the hull
    bx, by = x + w * 0.78, hy + 8
    for ang in range(0, 360, 45):
        import math
        ex = bx + 26 * math.cos(math.radians(ang))
        ey = by + 26 * math.sin(math.radians(ang))
        d.line([bx, by, ex, ey], fill=(230, 120, 30), width=5)
    d.ellipse([bx - 12, by - 12, bx + 12, by + 12], fill=(240, 160, 40),
              outline=RED, width=2)
    # small drone above
    dx, dy = x + w * 0.30, y + 22
    d.ellipse([dx - 8, dy - 5, dx + 8, dy + 5], fill=INK)
    d.line([dx - 22, dy, dx + 22, dy], fill=INK, width=3)


def draw_radar(d, x, y, w, h):
    """Radar dome + missile streak."""
    d.rectangle([x, y, x + w, y + h], fill=(226, 232, 238))
    # ground
    gy = y + h - 26
    d.rectangle([x, gy, x + w, y + h], fill=(170, 160, 140))
    # dome
    cx = x + w * 0.5
    d.pieslice([cx - 62, gy - 62, cx + 62, gy + 10], 180, 360,
               fill=(200, 206, 212), outline=INK, width=3)
    d.rectangle([cx - 70, gy - 8, cx + 70, gy + 2], fill=GREY)
    # antenna
    d.line([cx, gy - 58, cx + 34, gy - 108], fill=INK, width=4)
    d.ellipse([cx + 30, gy - 114, cx + 42, gy - 102], fill=RED)
    # missile streak from top right
    d.line([x + w - 16, y + 10, x + w * 0.55, y + h * 0.42], fill=RED,
           width=6)
    d.polygon([(x + w * 0.55, y + h * 0.42), (x + w * 0.55 - 22, y + h * 0.42 + 6),
               (x + w * 0.55 - 8, y + h * 0.42 + 20)], fill=(240, 140, 30))


def draw_hack(d, x, y, w, h):
    """Laptop + masked face + falling gold coins."""
    d.rectangle([x, y, x + w, y + h], fill=(28, 28, 36))
    # laptop
    lx, ly, lw, lh = x + w * 0.18, y + h * 0.42, w * 0.64, h * 0.34
    d.rectangle([lx, ly, lx + lw, ly + lh], fill=(70, 90, 130),
                outline=WHITE, width=3)
    d.rectangle([lx - 14, ly + lh, lx + lw + 14, ly + lh + 12], fill=(120, 128,
                136), outline=INK, width=2)
    # masked face on screen
    cx, cy = lx + lw / 2, ly + lh / 2
    d.ellipse([cx - 26, cy - 24, cx + 26, cy + 24], fill=SKIN)
    d.rectangle([cx - 26, cy - 8, cx + 26, cy + 8], fill=INK)
    d.ellipse([cx - 16, cy - 2, cx - 6, cy + 4], fill=WHITE)
    d.ellipse([cx + 6, cy - 2, cx + 16, cy + 4], fill=WHITE)
    # falling coins
    for cx2, cy2, r in ((x + w * 0.16, y + 22, 16), (x + w * 0.82, y + 14, 18),
                        (x + w * 0.88, y + h * 0.62, 14)):
        d.ellipse([cx2 - r, cy2 - r, cx2 + r, cy2 + r], fill=GOLD,
                  outline=(150, 115, 20), width=3)
        d.text((cx2 - 6, cy2 - 11), "$", font=fb(20), fill=INK)


def draw_kane(d, x, y, w, h):
    """Footballer in white raising arms, ball, big 126."""
    d.rectangle([x, y, x + w, y + h], fill=(236, 240, 236))
    # pitch
    py = y + h - 34
    d.rectangle([x, py, x + w, y + h], fill=GREEN)
    d.line([x, py, x + w, py], fill=WHITE, width=3)
    # figure
    cx = x + w * 0.5
    d.ellipse([cx - 20, y + 22, cx + 20, y + 62], fill=SKIN, outline=INK,
              width=2)
    # raised arms
    d.line([cx - 14, y + 74, cx - 52, y + 30], fill=WHITE, width=12)
    d.line([cx + 14, y + 74, cx + 52, y + 30], fill=WHITE, width=12)
    d.line([cx - 14, y + 74, cx - 52, y + 30], fill=INK, width=2)
    d.line([cx + 14, y + 74, cx + 52, y + 30], fill=INK, width=2)
    # shirt + shorts + legs
    d.polygon([(cx - 26, y + 68), (cx + 26, y + 68), (cx + 20, y + 128),
               (cx - 20, y + 128)], fill=WHITE, outline=INK, width=3)
    d.rectangle([cx - 20, y + 128, cx + 20, y + 150], fill=NAVY)
    d.line([cx - 10, y + 150, cx - 12, py], fill=INK, width=6)
    d.line([cx + 10, y + 150, cx + 14, py], fill=INK, width=6)
    # ball
    bx, by = x + w * 0.82, py - 16
    d.ellipse([bx - 14, by - 14, bx + 14, by + 14], fill=WHITE, outline=INK,
              width=2)
    d.polygon([(bx, by - 7), (bx + 7, by), (bx, by + 7), (bx - 7, by)],
              fill=INK)
    # big number
    tcenter(d, cx, y + h - 30, "126", fb(30), fill=RED)


def draw_table(d, x, y, w, h):
    """Round table with US + Ukraine flags (Zelensky talks)."""
    d.rectangle([x, y, x + w, y + h], fill=(232, 226, 210))
    # table
    d.ellipse([x + 8, y + h * 0.52, x + w - 8, y + h - 12], fill=BROWN,
              outline=INK, width=3)
    d.ellipse([x + 8, y + h * 0.52, x + w - 8, y + h * 0.66], fill=(150, 116,
              78))
    # flags
    d.line([x + w * 0.3, y + 10, x + w * 0.3, y + h * 0.55], fill=INK, width=4)
    flag_us(d, x + w * 0.3 + 4, y + 12, 54, 34)
    d.line([x + w * 0.7, y + 10, x + w * 0.7, y + h * 0.55], fill=INK, width=4)
    flag_ua(d, x + w * 0.7 - 58, y + 12, 54, 34)


def draw_scene(d, kind, x, y, w, h):
    fn = {"senate": draw_senate, "warship": draw_warship,
          "radar": draw_radar, "hack": draw_hack, "kane": draw_kane,
          "table": draw_table}[kind]
    fn(d, x, y, w, h)


# ---------------- Concept A: front-page montage ----------------

def concept_a():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # header
    d.rectangle([0, 0, W, 108], fill=NAVY)
    tcenter(d, W // 2, 28, "FRIDAY 13 NOVEMBER 2026", fb(50), fill=WHITE)
    d.rectangle([0, 108, W, 116], fill=RED)
    # globe centre
    draw_globe(d, W // 2, 296, 138)
    tcenter(d, W // 2, 448, "THE WORLD IN ONE DAY", fb(30), fill=INK)
    # six vignette cards, 2 rows x 3 cols
    cells = [
        ("senate", ["SENATE SUMMONS", "NVIDIA CHIEF"]),
        ("table", ["ZELENSKY MEETS", "US ENVOYS"]),
        ("warship", ["DRONE HITS", "RUSSIAN WARSHIP"]),
        ("radar", ["IRAN STRIKES", "US RADAR BASE"]),
        ("hack", ["FBI: $400M", "CRYPTO HEIST"]),
        ("kane", ["KANE: 126", "ENGLAND CAPS"]),
    ]
    xs = [36, 356, 676]
    ys = [500, 748]
    cw, ch = 312, 232
    for i, (kind, lines) in enumerate(cells):
        x = xs[i % 3]
        y = ys[i // 3]
        card(d, x, y, cw, ch)
        draw_scene(d, kind, x + 10, y + 10, cw - 20, 128)
        tlines(d, x + cw // 2, y + 146, lines, fb(27), fill=INK, gap=2)
    return img


# ---------------- Concept B: three-panel editorial strip ----------------

def concept_b():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # banner
    d.rectangle([0, 0, W, 96], fill=RED)
    tcenter(d, W // 2, 24, "FRIDAY 13 NOVEMBER 2026", fb(46), fill=WHITE)
    d.rectangle([0, 96, W, 104], fill=NAVY)
    # three big panels
    panels = [
        ("senate", ["SENATE", "SUMMONS", "NVIDIA CHIEF"]),
        ("warship", ["DRONE HITS", "RUSSIAN", "WARSHIP"]),
        ("hack", ["FBI: $400M", "CRYPTO", "HEIST"]),
    ]
    xs = [36, 356, 676]
    for i, (kind, lines) in enumerate(panels):
        x = xs[i]
        y = 120
        card(d, x, y, 312, 770)
        draw_scene(d, kind, x + 12, y + 14, 288, 520)
        tlines(d, x + 156, y + 560, lines, fb(32), fill=INK, gap=4)
    # bottom strip: three more stories (short labels, must fit the column)
    d.rectangle([0, 910, W, H], fill=NAVY)
    strips = ["ZELENSKY TALKS", "IRAN HITS RADAR", "KANE: 126 CAPS"]
    for i, s in enumerate(strips):
        tcenter(d, xs[i] + 156, 948, s, fb(22), fill=WHITE)
    return img


# ---------------- Concept C: newspaper front page ----------------

def concept_c():
    img = Image.new("RGB", (W, H), PAPER)
    d = ImageDraw.Draw(img)
    # masthead
    tcenter(d, W // 2, 14, "THE WORLD", fb(96), fill=INK)
    tcenter(d, W // 2, 122, "FRIDAY 13 NOVEMBER 2026", fb(34), fill=RED)
    d.rectangle([36, 168, W - 36, 174], fill=INK)
    # lead illustration: senate hearing
    draw_senate(d, 36, 190, W - 72, 330)
    tlines(d, W // 2, 536, ["SENATE SUMMONS", "NVIDIA CHIEF & LUTNICK"],
           fb(38), fill=INK, gap=4)
    d.rectangle([36, 648, W - 36, 654], fill=INK)
    # three smaller stories
    smalls = [
        ("warship", ["DRONE HITS", "RUSSIAN WARSHIP"]),
        ("hack", ["$400M CRYPTO", "HEIST"]),
        ("kane", ["KANE: 126", "ENGLAND CAPS"]),
    ]
    xs = [36, 356, 676]
    for i, (kind, lines) in enumerate(smalls):
        x = xs[i]
        card(d, x, 676, 312, 312)
        draw_scene(d, kind, x + 10, y := 686, 292, 170)
        tlines(d, x + 156, 872, lines, fb(28), fill=INK, gap=2)
    return img


def main():
    os.makedirs("candidates", exist_ok=True)
    for name, fn in (("a_montage", concept_a), ("b_panels", concept_b),
                     ("c_frontpage", concept_c)):
        img = fn()
        path = f"candidates/{name}.png"
        img.save(path, "PNG")
        print(name, img.size, os.path.getsize(path), "bytes")


if __name__ == "__main__":
    main()
