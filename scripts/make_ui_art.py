#!/usr/bin/env python3
"""Generate the game's UI art (glossy candy theme) as PNGs.

Pure Python, no dependencies, deterministic. Re-run after changing colors:

    python3 scripts/make_ui_art.py

Writes into game/gui/ (replacing Ren'Py's default GUI images) and
game/gui/theme/ (extra pieces used by game/theme.rpy). Everything here is
original art drawn from code, so there is nothing to license; see CREDITS.md.
"""

import math
import os
import re
import struct
import zlib

ROOT = os.path.join(os.path.dirname(__file__), "..")
GUI = os.path.join(ROOT, "game", "gui")
THEME = os.path.join(GUI, "theme")

# Palette (keep in sync with THEME_* in game/theme.rpy)
PINK = "#ff5fa2"
HOT = "#ff2f86"
PINK_LIGHT = "#ffc6df"
BLUSH = "#ffe9f3"
PLUM = "#3a1640"
PLUM2 = "#62246a"
LAVENDER = "#b98cff"
VIOLET = "#8b5cf6"
CREAM = "#fff8fc"
WHITE = "#ffffff"
GOLD = "#ffd84d"


def rgb(h):
    h = h.lstrip("#")
    return tuple(int(h[i:i + 2], 16) / 255 for i in (0, 2, 4))


def mix(a, b, t):
    return tuple(x + (y - x) * t for x, y in zip(a, b))


class Canvas:
    """Straight-alpha float RGBA canvas with 'over' compositing."""

    def __init__(self, w, h):
        self.w, self.h = w, h
        self.px = [[0.0, 0.0, 0.0, 0.0] for _ in range(w * h)]

    def blend(self, x, y, color, alpha):
        if alpha <= 0:
            return
        p = self.px[y * self.w + x]
        a0 = p[3]
        a = alpha + a0 * (1 - alpha)
        if a <= 0:
            return
        for i in range(3):
            p[i] = (color[i] * alpha + p[i] * a0 * (1 - alpha)) / a
        p[3] = a

    def save(self, path):
        os.makedirs(os.path.dirname(path), exist_ok=True)
        raw = bytearray()
        for y in range(self.h):
            raw.append(0)
            for x in range(self.w):
                r, g, b, a = self.px[y * self.w + x]
                raw += bytes((round(r * 255), round(g * 255), round(b * 255), round(min(1, a) * 255)))

        def chunk(t, d):
            return struct.pack(">I", len(d)) + t + d + struct.pack(">I", zlib.crc32(t + d) & 0xFFFFFFFF)

        ihdr = struct.pack(">IIBBBBB", self.w, self.h, 8, 6, 0, 0, 0)
        with open(path, "wb") as f:
            f.write(b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", ihdr) + chunk(b"IDAT", zlib.compress(bytes(raw), 9)) + chunk(b"IEND", b""))


def sd_round_rect(px, py, x0, y0, x1, y1, r):
    """Signed distance from point to a rounded rectangle (negative inside)."""
    cx, cy = (x0 + x1) / 2, (y0 + y1) / 2
    hx, hy = (x1 - x0) / 2 - r, (y1 - y0) / 2 - r
    qx, qy = abs(px - cx) - hx, abs(py - cy) - hy
    outside = math.hypot(max(qx, 0), max(qy, 0))
    inside = min(max(qx, qy), 0)
    return outside + inside - r


def fill_round_rect(c, x0, y0, x1, y1, r, color_fn, alpha=1.0, soft=0.5):
    """color_fn(t) -> rgb, where t is 0 at the top of the rect and 1 at the bottom."""
    for y in range(max(0, int(y0) - 2), min(c.h, int(y1) + 3)):
        t = min(1, max(0, (y + 0.5 - y0) / max(1, (y1 - y0))))
        col = color_fn(t)
        for x in range(max(0, int(x0) - 2), min(c.w, int(x1) + 3)):
            d = sd_round_rect(x + 0.5, y + 0.5, x0, y0, x1, y1, r)
            cov = min(1, max(0, soft - d)) if soft <= 0.5 else min(1, max(0, 0.5 - d / soft))
            if cov > 0:
                c.blend(x, y, col, cov * alpha)


def grad(*stops):
    cols = [rgb(s) for s in stops]

    def f(t):
        if len(cols) == 1:
            return cols[0]
        seg = min(len(cols) - 2, int(t * (len(cols) - 1)))
        lt = t * (len(cols) - 1) - seg
        return mix(cols[seg], cols[seg + 1], lt)
    return f


def glossy_panel(w, h, r, border, border_col, top, bottom, shadow=True, gloss=0.55, inset_line=True):
    """A rounded panel: drop shadow, colored border, gradient fill, top gloss."""
    pad = 10 if shadow else 0
    c = Canvas(w, h)
    x0, y0, x1, y1 = pad, pad - (3 if shadow else 0), w - pad, h - pad - (3 if shadow else 0)
    if shadow:
        fill_round_rect(c, x0, y0 + 6, x1, y1 + 6, r, grad(PLUM), alpha=0.28, soft=8)
    fill_round_rect(c, x0, y0, x1, y1, r, grad(border_col))
    b = border
    fill_round_rect(c, x0 + b, y0 + b, x1 - b, y1 - b, max(2, r - b), grad(top, bottom))
    if inset_line:
        # thin white highlight just inside the border
        fill_round_rect(c, x0 + b, y0 + b, x1 - b, y0 + b + 3, max(2, r - b), grad(WHITE), alpha=0.6)
    if gloss:
        gh = (y1 - y0 - 2 * b) * 0.45
        fill_round_rect(c, x0 + b + 4, y0 + b + 3, x1 - b - 4, y0 + b + gh, max(2, r - b - 3),
                        lambda t: rgb(WHITE), alpha=gloss * 0.6)
    return c, pad


def heart_inside(x, y):
    # classic implicit heart, x,y roughly in [-1.3, 1.3]
    return (x * x + y * y - 1) ** 3 - x * x * y ** 3 <= 0


def draw_heart(c, cx, cy, size, color, alpha=1.0, ss=3, outline=None, outline_w=0.0):
    """Antialiased heart centered at (cx, cy); size = width in pixels."""
    s = size / 2.6
    for py in range(max(0, int(cy - size)), min(c.h, int(cy + size) + 1)):
        for px in range(max(0, int(cx - size)), min(c.w, int(cx + size) + 1)):
            hit = 0
            hit_in = 0
            for sy in range(ss):
                for sx in range(ss):
                    x = (px + (sx + 0.5) / ss - cx) / s
                    y = -(py + (sy + 0.5) / ss - cy) / s + 0.15
                    if heart_inside(x, y):
                        hit += 1
                        if outline:
                            k = 1 + outline_w / s * 2.6
                            if heart_inside(x * k, (y - 0.15) * k + 0.15):
                                hit_in += 1
            if hit:
                if outline:
                    c.blend(px, py, rgb(outline), hit / ss ** 2 * alpha)
                    if hit_in:
                        c.blend(px, py, color, hit_in / ss ** 2 * alpha)
                else:
                    c.blend(px, py, color, hit / ss ** 2 * alpha)


def heart_gloss(c, cx, cy, size):
    # small white highlight ellipse on the upper-left lobe
    rx, ry = size * 0.12, size * 0.08
    hx, hy = cx - size * 0.2, cy - size * 0.2
    for py in range(int(hy - ry) - 1, int(hy + ry) + 2):
        for px in range(int(hx - rx) - 1, int(hx + rx) + 2):
            if 0 <= px < c.w and 0 <= py < c.h:
                d = ((px + 0.5 - hx) / rx) ** 2 + ((py + 0.5 - hy) / ry) ** 2
                if d < 1:
                    c.blend(px, py, rgb(WHITE), 0.7 * min(1, (1 - d) * 3))


# ---------------------------------------------------------------- pieces

def menu_background(path, top_left, bottom_right, heart_alpha, glow=True):
    w, h = 1920, 1080
    a, b = rgb(top_left), rgb(bottom_right)
    c = Canvas(w, h)
    for y in range(h):
        for x in range(w):
            t = (x / w * 0.55 + y / h * 0.45)
            col = mix(a, b, t)
            if glow:
                d = math.hypot((x - w * 0.72) / w, (y - h * 0.3) / h)
                col = mix(col, rgb(WHITE), max(0, 0.32 - d) * 0.9)
            p = c.px[y * w + x]
            p[0], p[1], p[2], p[3] = col[0], col[1], col[2], 1.0
    # heart pattern from a tile, offset every other row
    tile = Canvas(240, 240)
    draw_heart(tile, 60, 60, 46, rgb(WHITE))
    draw_heart(tile, 180, 180, 30, rgb(WHITE))
    for y in range(h):
        ty = y % 240
        for x in range(w):
            tp = tile.px[ty * 240 + (x + (y // 240) * 120) % 240]
            if tp[3]:
                c.blend(x, y, rgb(WHITE), tp[3] * heart_alpha)
    c.save(path)


def bg_overlay(path):
    """Soft light-from-above gradient + faint hearts, laid over placeholder backgrounds."""
    w, h = 1920, 1080
    c = Canvas(w, h)
    tile = Canvas(240, 240)
    draw_heart(tile, 60, 60, 40, rgb(WHITE))
    draw_heart(tile, 180, 180, 24, rgb(WHITE))
    white, plum = rgb(WHITE), rgb(PLUM)
    for y in range(h):
        top = max(0.0, 0.42 * (1 - y / (h * 0.6)))
        bottom = max(0.0, 0.16 * (y - h * 0.55) / (h * 0.45))
        ty = y % 240
        for x in range(w):
            if top:
                c.blend(x, y, white, top)
            if bottom:
                c.blend(x, y, plum, bottom)
            tp = tile.px[ty * 240 + (x + (y // 240) * 120) % 240]
            if tp[3]:
                c.blend(x, y, white, tp[3] * 0.10)
    c.save(path)


def overlay_main_menu(path):
    c = Canvas(1920, 1080)
    # soft white glow strip behind the navigation pills
    fill_round_rect(c, -200, 300, 440, 980, 200, grad(WHITE), alpha=0.22, soft=90)
    c.save(path)


def overlay_game_menu(path):
    c = Canvas(1920, 1080)
    fill_round_rect(c, 462, 172, 1898, 1052, 48, grad(PLUM), alpha=0.25, soft=14)
    fill_round_rect(c, 455, 165, 1890, 1042, 44, grad(PINK))
    fill_round_rect(c, 461, 171, 1884, 1036, 39, grad(CREAM, BLUSH), alpha=0.96)
    c.save(path)


def overlay_confirm(path):
    c = Canvas(64, 64)
    for p in c.px:
        p[:] = list(rgb(PLUM)) + [0.55]
    c.save(path)


def textbox(path):
    c, _ = glossy_panel(256, 256, 46, 7, PINK, CREAM, BLUSH, gloss=0.45)
    c.save(path)


def pill(path, w, h, border_col, top, bottom, border=4, shadow=False, gloss=0.6):
    c, _ = glossy_panel(w, h, h / 2 - (10 if shadow else 0) - 1, border, border_col, top, bottom,
                        shadow=shadow, gloss=gloss)
    c.save(path)


def check_heart(path, filled):
    c = Canvas(44, 49)
    if filled:
        draw_heart(c, 20, 25, 34, rgb(HOT), outline=WHITE, outline_w=2.5)
        heart_gloss(c, 20, 25, 34)
    else:
        draw_heart(c, 20, 25, 34, rgb(BLUSH), outline=PINK_LIGHT, outline_w=3)
    c.save(path)


def slider_parts():
    # base bar: rounded track; thumb: glossy heart
    c, _ = glossy_panel(525, 38, 15, 3, PINK_LIGHT, BLUSH, WHITE, shadow=False, gloss=0)
    c.save(os.path.join(GUI, "slider", "horizontal_idle_bar.png"))
    c, _ = glossy_panel(525, 38, 15, 3, PINK, BLUSH, WHITE, shadow=False, gloss=0)
    c.save(os.path.join(GUI, "slider", "horizontal_hover_bar.png"))
    for state, col in (("idle", PINK), ("hover", HOT)):
        t = Canvas(44, 38)
        draw_heart(t, 22, 19, 36, rgb(col), outline=WHITE, outline_w=2.5)
        heart_gloss(t, 22, 19, 36)
        t.save(os.path.join(GUI, "slider", "horizontal_%s_thumb.png" % state))
    for state, col in (("idle", PINK_LIGHT), ("hover", PINK)):
        v = Canvas(18, 1050)
        fill_round_rect(v, 3, 0, 15, 1050, 6, grad(BLUSH), alpha=0.9)
        v.save(os.path.join(GUI, "scrollbar", "vertical_%s_bar.png" % state))
        v = Canvas(18, 1050)
        fill_round_rect(v, 2, 0, 16, 1050, 7, grad(col))
        v.save(os.path.join(GUI, "scrollbar", "vertical_%s_thumb.png" % state))
        hz = Canvas(1050, 18)
        fill_round_rect(hz, 0, 3, 1050, 15, 6, grad(BLUSH), alpha=0.9)
        hz.save(os.path.join(GUI, "scrollbar", "horizontal_%s_bar.png" % state))
        hz = Canvas(1050, 18)
        fill_round_rect(hz, 0, 2, 1050, 16, 7, grad(col))
        hz.save(os.path.join(GUI, "scrollbar", "horizontal_%s_thumb.png" % state))


def window_icon(path):
    c = Canvas(250, 250)
    draw_heart(c, 125, 128, 230, rgb(HOT), outline=WHITE, outline_w=10, ss=2)
    heart_gloss(c, 125, 128, 230)
    c.save(path)


def silhouette(path):
    """Generic character silhouette (white; tinted per character in Ren'Py)."""
    w, h = 440, 860
    c = Canvas(w, h)
    white = rgb(WHITE)
    # body: rounded trapezoid made of stacked rounded rects
    fill_round_rect(c, 60, 430, 380, 900, 120, lambda t: white)
    fill_round_rect(c, 95, 360, 345, 560, 90, lambda t: white)
    # neck
    fill_round_rect(c, 185, 300, 255, 400, 30, lambda t: white)
    # head + hair volume
    for py in range(60, 360):
        for px in range(90, 350):
            d = ((px + 0.5 - 220) / 118) ** 2 + ((py + 0.5 - 200) / 138) ** 2
            if d < 1.04:
                c.blend(px, py, white, min(1, (1.04 - d) * 30))
    c.save(path)


def namebox_pills(colors):
    for cid, col in colors.items():
        light = "#%02x%02x%02x" % tuple(round(v * 255) for v in mix(rgb(col), rgb(WHITE), 0.35))
        pill(os.path.join(THEME, "namebox_%s.png" % cid), 200, 66, WHITE, light, col, border=4)


def read_signature_colors():
    src = open(os.path.join(ROOT, "game", "characters.rpy"), encoding="utf-8").read()
    return {m.group(1): m.group(2) for m in re.finditer(r'"(\w+)":\s*\{"name": "(#[0-9a-fA-F]{6})"', src)}


def main():
    os.makedirs(THEME, exist_ok=True)
    print("menu backgrounds...")
    menu_background(os.path.join(GUI, "main_menu.png"), "#ff8cc6", "#8b5cf6", 0.16)
    menu_background(os.path.join(GUI, "game_menu.png"), "#ffb3d6", "#a98bff", 0.12)
    overlay_main_menu(os.path.join(GUI, "overlay", "main_menu.png"))
    overlay_game_menu(os.path.join(GUI, "overlay", "game_menu.png"))
    overlay_confirm(os.path.join(GUI, "overlay", "confirm.png"))
    bg_overlay(os.path.join(THEME, "bg_overlay.png"))

    print("panels and buttons...")
    textbox(os.path.join(THEME, "textbox.png"))
    glossy_panel(160, 160, 40, 6, PINK, CREAM, BLUSH)[0].save(os.path.join(THEME, "panel.png"))
    glossy_panel(160, 160, 40, 6, PINK, PLUM2, PLUM, gloss=0.25)[0].save(os.path.join(THEME, "panel_dark.png"))
    glossy_panel(120, 120, 28, 4, PINK_LIGHT, WHITE, BLUSH, shadow=False, gloss=0.4)[0].save(os.path.join(THEME, "card.png"))
    glossy_panel(120, 120, 28, 4, PINK, WHITE, PINK_LIGHT, shadow=False, gloss=0.5)[0].save(os.path.join(THEME, "card_hover.png"))
    glossy_panel(120, 120, 28, 4, "#d9cfe0", "#efe9f2", "#e2d9e8", shadow=False, gloss=0.2)[0].save(os.path.join(THEME, "card_off.png"))
    frame, _ = glossy_panel(160, 160, 40, 6, PINK, CREAM, BLUSH)
    frame.save(os.path.join(GUI, "frame.png"))

    pill(os.path.join(THEME, "pill_pink.png"), 160, 72, WHITE, "#ff8cc0", HOT)
    pill(os.path.join(THEME, "pill_white.png"), 160, 72, PINK, WHITE, BLUSH)
    pill(os.path.join(THEME, "pill_plum.png"), 160, 72, WHITE, PLUM2, PLUM, gloss=0.35)
    pill(os.path.join(THEME, "pill_violet.png"), 160, 72, WHITE, "#a98bff", VIOLET)
    pill(os.path.join(THEME, "pill_gold.png"), 160, 72, WHITE, "#ffe98a", "#ffb800")
    # white pill with a slightly darker bottom; tinted per prompt style in Ren'Py
    pill(os.path.join(THEME, "badge.png"), 100, 52, WHITE, WHITE, "#d8d8d8", border=3, gloss=0.7)

    # choice buttons (taller than Ren'Py's default so text has room)
    pill(os.path.join(GUI, "button", "choice_idle_background.png"), 220, 92, PINK, WHITE, BLUSH, border=5, shadow=True)
    pill(os.path.join(GUI, "button", "choice_hover_background.png"), 220, 92, WHITE, "#ff8cc0", HOT, border=5, shadow=True)
    # generic button hover (used by navigation and preference buttons)
    pill(os.path.join(GUI, "button", "idle_background.png"), 160, 72, WHITE, WHITE, BLUSH, gloss=0.4)
    pill(os.path.join(GUI, "button", "hover_background.png"), 160, 72, WHITE, "#ff8cc0", HOT)
    pill(os.path.join(GUI, "button", "quick_idle_background.png"), 120, 44, WHITE, WHITE, BLUSH, border=2, gloss=0.3)
    pill(os.path.join(GUI, "button", "quick_hover_background.png"), 120, 44, WHITE, "#ff8cc0", HOT, border=2)
    glossy_panel(414, 309, 30, 5, PINK_LIGHT, WHITE, BLUSH, shadow=False, gloss=0.3)[0].save(os.path.join(GUI, "button", "slot_idle_background.png"))
    glossy_panel(414, 309, 30, 5, PINK, WHITE, PINK_LIGHT, shadow=False, gloss=0.4)[0].save(os.path.join(GUI, "button", "slot_hover_background.png"))
    pill(os.path.join(GUI, "notify.png"), 160, 64, WHITE, "#ff8cc0", HOT)
    pill(os.path.join(GUI, "skip.png"), 160, 64, WHITE, PLUM2, PLUM, gloss=0.3)

    check_heart(os.path.join(GUI, "button", "check_foreground.png"), False)
    check_heart(os.path.join(GUI, "button", "check_selected_foreground.png"), True)
    check_heart(os.path.join(GUI, "button", "radio_foreground.png"), False)
    check_heart(os.path.join(GUI, "button", "radio_selected_foreground.png"), True)

    print("sliders, icon, silhouette, name tags...")
    slider_parts()
    window_icon(os.path.join(GUI, "window_icon.png"))
    silhouette(os.path.join(THEME, "silhouette.png"))
    namebox_pills(dict(read_signature_colors(), default=PINK, mc=VIOLET))

    # small hearts for the HUD and notifications
    for name, size, col in (("heart_small", 30, HOT), ("heart_big", 64, HOT), ("heart_empty", 30, PINK_LIGHT)):
        hc = Canvas(size + 6, size + 6)
        draw_heart(hc, (size + 6) / 2, (size + 6) / 2, size, rgb(col), outline=WHITE, outline_w=max(2, size / 14))
        if col == HOT:
            heart_gloss(hc, (size + 6) / 2, (size + 6) / 2, size)
        hc.save(os.path.join(THEME, name + ".png"))
    print("done")


if __name__ == "__main__":
    main()
