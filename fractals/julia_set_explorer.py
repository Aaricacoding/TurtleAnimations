"""
fractals/julia_set_explorer.py
================================
Julia Set — deep black background, fire + electric boundary colors.

Run standalone:  python fractals/julia_set_explorer.py
Run via menu:    python main.py  → option 6
"""

import sys, os, math, turtle

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from core.fractal_engine import julia
from core.config         import Config


def _color(m, max_iter):
    """
    Fire-electric palette on pure black.
    Slow-escape points → deep red/purple glow
    Fast-escape points → electric white-yellow
    Interior           → black
    """
    if m == max_iter:
        return (0.0, 0.0, 0.0)      # interior = black

    t = m / max_iter
    t = math.log(t + 1) / math.log(2)   # log smooth

    # fire palette: black → deep red → orange → yellow → white
    if t < 0.25:
        s = t / 0.25
        return (s * 0.8, 0.0, s * 0.3)             # black → deep red-purple
    elif t < 0.5:
        s = (t - 0.25) / 0.25
        return (0.8 + s * 0.2, s * 0.4, 0.3 - s * 0.3)  # red → orange
    elif t < 0.75:
        s = (t - 0.5) / 0.25
        return (1.0, 0.4 + s * 0.5, s * 0.2)       # orange → yellow
    else:
        s = (t - 0.75) / 0.25
        return (1.0, 0.9 + s * 0.1, 0.2 + s * 0.8) # yellow → white


def run():
    cfg = Config(step=3, zoom=0.005, max_iter=120)

    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#000000")
    screen.title("TurtleAnimations — Julia Set Explorer")
    screen.tracer(0)
    turtle.colormode(1.0)

    pen = turtle.Turtle()
    pen.hideturtle(); pen.speed(0); pen.penup()

    # Seeds to try — uncomment one:
    c = complex(-0.7,    0.27015)  # ← classic spiral (current)
    # c = complex(-0.4,  0.6)      # ← dendrite / lightning bolt
    # c = complex(0.285, 0.01)     # ← rabbit fractal
    # c = complex(-0.8,  0.156)    # ← star burst

    width, height = 300, 300
    rows = list(range(-width, width, cfg.step))
    print(f"[Julia] Rendering {len(rows)} rows — please wait...")
    print(f"[Julia] Seed c = {c}  (change in script to explore other shapes)")

    for row, x in enumerate(rows):
        for y in range(-height, height, cfg.step):
            z = complex(x * cfg.zoom + cfg.center_x,
                        y * cfg.zoom + cfg.center_y)
            m = julia(z, c, cfg.max_iter)
            pen.goto(x, y)
            pen.dot(cfg.step + 1, _color(m, cfg.max_iter))

        if row % 15 == 0:
            print(f"[Julia] Row {row}/{len(rows)}")
            screen.update()

    print("[Julia] Done! Close the window to exit.")
    screen.update()
    turtle.done()


if __name__ == "__main__":
    run()