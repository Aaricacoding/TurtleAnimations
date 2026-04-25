"""
fractals/mandelbrot_visualizer.py
==================================
Mandelbrot Set — deep space color palette.
Black background, glowing boundary, vivid color bands.

Run standalone:  python fractals/mandelbrot_visualizer.py
Run via menu:    python main.py  → option 5
"""

import sys, os, math, turtle

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from core.fractal_engine import mandelbrot
from core.config         import Config


def _color(m, max_iter):
    """
    Deep-space palette — BLACK background, tight glowing boundary bands.
    Uses smooth sine-based cycling so colors never go flat.
    """
    if m == max_iter:
        return (0.0, 0.0, 0.0)      # interior = pure black

    # normalized 0..1, log-smoothed so bands are tight near boundary
    t = m / max_iter
    t = math.log(t + 1) / math.log(2)   # log smoothing

    # sine-cycle through vivid hues — phase-shifted per channel
    r = 0.5 + 0.5 * math.sin(math.pi * t * 6 + 0.0)
    g = 0.5 + 0.5 * math.sin(math.pi * t * 6 + 2.094)   # +120°
    b = 0.5 + 0.5 * math.sin(math.pi * t * 6 + 4.189)   # +240°

    # darken points that escaped very slowly (close to boundary)
    # → makes boundary glow pop against dark surroundings
    brightness = min(1.0, t * 3.5)
    return (r * brightness, g * brightness, b * brightness)


def run():
    cfg = Config(step=3, zoom=0.0045, max_iter=120,
                 center_x=-0.5, center_y=0.0)

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#000000")
    screen.title("TurtleAnimations — Mandelbrot Set")
    screen.tracer(0)
    turtle.colormode(1.0)

    pen = turtle.Turtle()
    pen.hideturtle(); pen.speed(0); pen.penup()

    width, height = 300, 300
    rows = list(range(-width, width, cfg.step))
    print(f"[Mandelbrot] Rendering {len(rows)} rows — please wait...")

    for row, x in enumerate(rows):
        for y in range(-height, height, cfg.step):
            c = complex(x * cfg.zoom + cfg.center_x,
                        y * cfg.zoom + cfg.center_y)
            m = mandelbrot(c, cfg.max_iter)
            pen.goto(x, y)
            pen.dot(cfg.step + 1, _color(m, cfg.max_iter))

        if row % 15 == 0:
            print(f"[Mandelbrot] Row {row}/{len(rows)}")
            screen.update()

    print("[Mandelbrot] Done! Close the window to exit.")
    screen.update()
    turtle.done()


if __name__ == "__main__":
    run()