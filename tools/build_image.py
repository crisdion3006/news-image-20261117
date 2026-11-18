#!/usr/bin/env python3
"""Build entry.png for news-image-20261117: one image summing up the world news
of Tuesday 17 November 2026. Flat newspaper-graphic style, all text rendered
as real text with PIL (no AI-generated text, so nothing garbles).

Stories (all reported on 17 Nov 2026):
1. Kerch Bridge partly collapses after a Ukrainian missile/drone strike (BBC, CNN)
2. Trump lands in Manila, opens Asia trip with a Quad summit (NPR, BBC)
3. Bahrain says it thwarted an Iranian drone attack; a fourth tanker burns in
   the Strait of Hormuz (Al Jazeera, BBC)
4. Nvidia ex-CEO Jensen Huang offers to return after resigning over an affair
   with a suspected Chinese spy; the board refuses (NPR, BBC)
5. US loses measles elimination status after 26 years (BBC)
6. Japan scrambles fighter jets as suspected Russian planes enter its airspace (FNN)
"""
import math
from PIL import Image, ImageDraw, ImageFont

W, H = 1024, 1024
BOLD = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
REG = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"

NAVY = (16, 30, 51)
GOLD = (232, 179, 60)
WHITE = (255, 255, 255)
INK = (24, 30, 40)
GREY = (90, 100, 115)
BORDER = (205, 212, 222)
PANEL_BG = (255, 255, 255)


def font(path, size):
    return ImageFont.truetype(path, size)


def tint(color, frac=0.13):
    """Mix a color toward white for a light panel tint."""
    return tuple(int(c + (255 - c) * (1 - frac)) for c in color)


def wrap(draw, text, fnt, max_w):
    """Word-wrap text to fit max_w pixels; returns list of lines."""
    words = text.split()
    lines, cur = [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=fnt) <= max_w:
            cur = trial
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ---------------------------------------------------------------- icons
def icon_bridge(d, x, y, s, accent):
    """Suspension bridge with a collapsed middle span over water."""
    # water
    for i in range(3):
        yy = y + s * (0.80 + i * 0.06)
        d.line([(x + 4, yy), (x + s - 4, yy)], fill=(70, 130, 180), width=4)
    # towers
    d.rectangle([x + s * 0.10, y + s * 0.16, x + s * 0.17, y + s * 0.80], fill=accent)
    d.rectangle([x + s * 0.78, y + s * 0.16, x + s * 0.85, y + s * 0.80], fill=accent)
    # cables from tower tops to the break
    d.line([(x + s * 0.135, y + s * 0.16), (x + s * 0.47, y + s * 0.50)], fill=accent, width=4)
    d.line([(x + s * 0.815, y + s * 0.16), (x + s * 0.47, y + s * 0.50)], fill=accent, width=4)
    # deck: left span intact, right span sagging into the water
    d.line([(x + s * 0.02, y + s * 0.52), (x + s * 0.47, y + s * 0.52)], fill=accent, width=9)
    d.line([(x + s * 0.47, y + s * 0.52), (x + s * 0.78, y + s * 0.82)], fill=accent, width=9)
    # blast burst at the break
    cx, cy = x + s * 0.47, y + s * 0.46
    for ang in range(0, 360, 30):
        r1, r2 = s * 0.05, s * 0.14
        a = math.radians(ang)
        d.line([(cx + r1 * math.cos(a), cy + r1 * math.sin(a)),
                (cx + r2 * math.cos(a), cy + r2 * math.sin(a))],
               fill=(235, 140, 30), width=5)
    d.ellipse([cx - s * 0.06, cy - s * 0.06, cx + s * 0.06, cy + s * 0.06],
              fill=(235, 140, 30))


def icon_plane(d, x, y, s, accent):
    """Airliner on a dotted route, with a small globe below."""
    # small globe
    gx, gy, gr = x + s * 0.50, y + s * 0.78, s * 0.16
    d.ellipse([gx - gr, gy - gr, gx + gr, gy + gr], outline=(120, 160, 200), width=4)
    d.line([(gx - gr, gy), (gx + gr, gy)], fill=(120, 160, 200), width=3)
    d.ellipse([gx - gr * 0.45, gy - gr, gx + gr * 0.45, gy + gr], outline=(120, 160, 200), width=3)
    # dotted route
    for t in range(0, 13):
        px = x + s * (0.06 + 0.075 * t)
        py = y + s * (0.34 - 0.10 * math.sin(math.pi * t / 12))
        d.ellipse([px - 3, py - 3, px + 3, py + 3], fill=GOLD)
    # plane silhouette (bigger)
    bx, by = x + s * 0.60, y + s * 0.24
    d.polygon([(bx, by - s * 0.06), (bx + s * 0.34, by), (bx, by + s * 0.06),
               (bx - s * 0.20, by + s * 0.03)], fill=accent)
    d.polygon([(bx - s * 0.02, by - s * 0.03), (bx + s * 0.12, by - s * 0.20),
               (bx + s * 0.17, by - s * 0.18), (bx + s * 0.07, by - s * 0.01)],
              fill=accent)
    d.polygon([(bx - s * 0.17, by + s * 0.03), (bx - s * 0.07, by + s * 0.15),
               (bx - s * 0.02, by + s * 0.13), (bx - s * 0.07, by + s * 0.02)],
              fill=accent)


def icon_tanker(d, x, y, s, accent):
    """Oil tanker on waves with a drone above."""
    # waves
    for i in range(3):
        yy = y + s * (0.76 + i * 0.07)
        d.line([(x + 6, yy), (x + s - 6, yy)], fill=(70, 130, 180), width=3)
    # hull
    d.polygon([(x + s * 0.06, y + s * 0.58), (x + s * 0.94, y + s * 0.58),
               (x + s * 0.84, y + s * 0.74), (x + s * 0.16, y + s * 0.74)],
              fill=accent)
    # containers
    d.rectangle([x + s * 0.14, y + s * 0.44, x + s * 0.34, y + s * 0.58], fill=(200, 90, 60))
    d.rectangle([x + s * 0.38, y + s * 0.44, x + s * 0.58, y + s * 0.58], fill=(60, 120, 90))
    d.rectangle([x + s * 0.62, y + s * 0.48, x + s * 0.80, y + s * 0.58], fill=(180, 160, 60))
    # smokestack + flame
    d.rectangle([x + s * 0.82, y + s * 0.38, x + s * 0.90, y + s * 0.58], fill=(90, 100, 115))
    fx, fy = x + s * 0.86, y + s * 0.32
    d.polygon([(fx, fy - s * 0.10), (fx + s * 0.07, fy + s * 0.03),
               (fx - s * 0.07, fy + s * 0.03)], fill=(235, 140, 30))
    # drone
    dx, dy = x + s * 0.24, y + s * 0.22
    d.ellipse([dx - s * 0.04, dy - s * 0.04, dx + s * 0.04, dy + s * 0.04], fill=INK)
    for ox in (-s * 0.09, s * 0.09):
        d.line([(dx + ox - s * 0.05, dy - s * 0.06), (dx + ox + s * 0.05, dy - s * 0.06)],
               fill=INK, width=3)


def icon_chip(d, x, y, s, accent):
    """Computer chip with pins and a red down arrow (troubled chip giant)."""
    # pins
    for i in range(4):
        px = x + s * (0.30 + i * 0.14)
        d.rectangle([px, y + s * 0.08, px + s * 0.05, y + s * 0.20], fill=GREY)
        d.rectangle([px, y + s * 0.80, px + s * 0.05, y + s * 0.92], fill=GREY)
        py = y + s * (0.30 + i * 0.14)
        d.rectangle([x + s * 0.08, py, x + s * 0.20, py + s * 0.05], fill=GREY)
        d.rectangle([x + s * 0.80, py, x + s * 0.92, py + s * 0.05], fill=GREY)
    # body
    d.rectangle([x + s * 0.20, y + s * 0.20, x + s * 0.80, y + s * 0.80],
                fill=accent, outline=(20, 90, 50), width=3)
    d.rectangle([x + s * 0.36, y + s * 0.36, x + s * 0.64, y + s * 0.64],
                fill=(255, 255, 255))
    # circuit traces inside
    d.line([(x + s * 0.36, y + s * 0.50), (x + s * 0.64, y + s * 0.50)], fill=accent, width=3)
    d.line([(x + s * 0.50, y + s * 0.36), (x + s * 0.50, y + s * 0.64)], fill=accent, width=3)
    # red down arrow
    ax = x + s * 0.86
    d.polygon([(ax - s * 0.05, y + s * 0.06), (ax + s * 0.05, y + s * 0.06),
               (ax + s * 0.05, y + s * 0.16), (ax + s * 0.10, y + s * 0.16),
               (ax, y + s * 0.28), (ax - s * 0.10, y + s * 0.16),
               (ax - s * 0.05, y + s * 0.16)], fill=(192, 57, 43))


def icon_virus(d, x, y, s, accent):
    """Virus: spiked circle, with a cracked shield behind it."""
    cx, cy = x + s * 0.50, y + s * 0.52
    for ang in range(0, 360, 30):
        a = math.radians(ang)
        x1, y1 = cx + s * 0.20 * math.cos(a), cy + s * 0.20 * math.sin(a)
        x2, y2 = cx + s * 0.30 * math.cos(a), cy + s * 0.30 * math.sin(a)
        d.line([(x1, y1), (x2, y2)], fill=accent, width=5)
        d.ellipse([x2 - s * 0.035, y2 - s * 0.035, x2 + s * 0.035, y2 + s * 0.035],
                  fill=accent)
    d.ellipse([cx - s * 0.20, cy - s * 0.20, cx + s * 0.20, cy + s * 0.20], fill=accent)
    d.ellipse([cx - s * 0.09, cy - s * 0.11, cx - s * 0.01, cy - s * 0.03], fill=(255, 255, 255))
    d.ellipse([cx + s * 0.03, cy + s * 0.02, cx + s * 0.09, cy + s * 0.08], fill=(255, 255, 255))


def icon_jet(d, x, y, s, accent):
    """Fighter jet crossing a dashed airspace line, red sun (Japan) behind."""
    # rising sun disc (smaller, upper right)
    d.ellipse([x + s * 0.62, y + s * 0.06, x + s * 0.94, y + s * 0.38], fill=(200, 60, 50))
    # dashed boundary (vertical, left third)
    for i in range(7):
        yy = y + s * (0.10 + i * 0.12)
        d.line([(x + s * 0.12, yy), (x + s * 0.12, yy + s * 0.07)], fill=GREY, width=4)
    # jet silhouette (bigger, nose to the right, crossing the line)
    jx, jy = x + s * 0.44, y + s * 0.58
    d.polygon([(jx - s * 0.30, jy), (jx + s * 0.34, jy - s * 0.05),
               (jx + s * 0.24, jy + s * 0.03), (jx - s * 0.14, jy + s * 0.13),
               (jx - s * 0.24, jy + s * 0.20), (jx - s * 0.27, jy + s * 0.10)],
              fill=accent)
    d.polygon([(jx - s * 0.03, jy - s * 0.03), (jx + s * 0.08, jy - s * 0.22),
               (jx + s * 0.14, jy - s * 0.19), (jx + s * 0.07, jy - s * 0.01)],
              fill=accent)
    # second, smaller jet behind and below
    jx2, jy2 = x + s * 0.30, y + s * 0.80
    d.polygon([(jx2 - s * 0.20, jy2), (jx2 + s * 0.22, jy2 - s * 0.04),
               (jx2 + s * 0.15, jy2 + s * 0.02), (jx2 - s * 0.10, jy2 + s * 0.09)],
              fill=(90, 100, 115))


STORIES = [
    dict(accent=(192, 57, 43), icon=icon_bridge,
         head="KERCH BRIDGE HIT",
         body="Ukraine's missile and drone strike partly collapses the bridge to Crimea; Russia hits Kyiv bridges in reply."),
    dict(accent=(36, 113, 163), icon=icon_plane,
         head="TRUMP OPENS ASIA TRIP",
         body="He lands in Manila for a Quad summit, the first of his second term; about 1,500 people protest his visit."),
    dict(accent=(183, 149, 11), icon=icon_tanker,
         head="GULF ON EDGE",
         body="Bahrain says it thwarted an Iranian drone attack; a fourth tanker burns in the Strait of Hormuz."),
    dict(accent=(30, 132, 73), icon=icon_chip,
         head="HUANG: I'D COME BACK",
         body="Nvidia's ex-CEO, who quit over an affair with a suspected Chinese spy, offers to return. The board says no."),
    dict(accent=(125, 60, 152), icon=icon_virus,
         head="MEASLES STATUS LOST",
         body="The US loses its measles-free status after 26 years: more than 5,400 cases and 10 deaths."),
    dict(accent=(20, 143, 119), icon=icon_jet,
         head="JETS SCRAMBLED",
         body="Japan sends fighter jets up after two suspected Russian planes enter its airspace."),
]


def build(out_path):
    img = Image.new("RGB", (W, H), (240, 242, 245))
    d = ImageDraw.Draw(img)

    # ---- header (full bleed) ----
    d.rectangle([0, 0, W, 118], fill=NAVY)
    d.rectangle([0, 118, W, 124], fill=GOLD)
    f_title = font(BOLD, 52)
    d.text((32, 22), "TUESDAY 17 NOVEMBER 2026", font=f_title, fill=WHITE)
    f_sub = font(REG, 22)
    d.text((34, 82), "THE WORLD IN ONE DAY  ·  SIX STORIES THAT MATTERED",
           font=f_sub, fill=(190, 200, 215))

    # ---- story grid: 2 cols x 3 rows ----
    margin, gap = 16, 12
    grid_top = 140
    grid_bottom = 972
    pw = (W - 2 * margin - gap) // 2
    ph = (grid_bottom - grid_top - 2 * gap) // 3
    f_head = font(BOLD, 26)
    f_body = font(REG, 19)

    for i, st in enumerate(STORIES):
        col, row = i % 2, i // 2
        x0 = margin + col * (pw + gap)
        y0 = grid_top + row * (ph + gap)
        x1, y1 = x0 + pw, y0 + ph
        accent = st["accent"]
        # panel
        d.rectangle([x0, y0, x1, y1], fill=PANEL_BG, outline=BORDER, width=2)
        d.rectangle([x0, y0, x1, y0 + 6], fill=accent)
        # icon zone (left)
        ix0, ix1 = x0, x0 + 150
        d.rectangle([ix0, y0 + 6, ix1, y1], fill=tint(accent, 0.10))
        d.line([(ix1, y0 + 6), (ix1, y1)], fill=BORDER, width=2)
        st["icon"](d, ix0 - 9, y0 + 6 + (ph - 6 - 168) // 2, 168, accent)
        # text zone (right)
        tx = ix1 + 16
        tw = x1 - tx - 14
        lines = wrap(d, st["head"], f_head, tw)
        ty = y0 + 22
        for ln in lines[:2]:
            d.text((tx, ty), ln, font=f_head, fill=INK)
            ty += 30
        ty += 4
        for ln in wrap(d, st["body"], f_body, tw)[:5]:
            d.text((tx, ty), ln, font=f_body, fill=(52, 62, 78))
            ty += 23

    # ---- footer ----
    f_foot = font(REG, 16)
    d.text((32, 982), "Sources: BBC · CNN · Al Jazeera · NPR · FNN  —  Events of Tuesday 17 November 2026",
           font=f_foot, fill=GREY)

    img.save(out_path, "PNG", optimize=True)
    return out_path


if __name__ == "__main__":
    import os
    out = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "entry.png")
    build(out)
    print("wrote", out)
