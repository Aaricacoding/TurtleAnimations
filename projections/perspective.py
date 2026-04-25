"""
projections/perspective.py
==========================
Perspective projection helpers.

Run standalone:  python projections/perspective.py
"""

import sys, os, math, turtle

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)


def perspective(x, y, depth, fov=400):
    """Maps 3-D (x,y,depth) → 2-D (px,py) via perspective divide."""
    if depth <= 0: depth = 0.001
    f = fov / depth
    return x * f, y * f


# ── Standalone demo: spinning galaxy of dots receding in 3-D ─────────────────
class _StarState:
    def __init__(self): self.angle = 0.0


def run():
    import random
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#000008")
    screen.title("TurtleAnimations — Perspective Star Field")
    screen.tracer(0)

    pen   = turtle.Turtle()
    pen.hideturtle(); pen.speed(0)
    state = _StarState()

    STARS = [(random.uniform(-300,300), random.uniform(-300,300),
              random.uniform(50, 500)) for _ in range(200)]
    COLS  = ["white","#aac4ff","#fff4a3","#ffb347","#da70d6"]

    def frame():
        state.angle += 0.008
        pen.clear()
        for (x, y, z) in STARS:
            rx =  x * math.cos(state.angle) - y * math.sin(state.angle)
            ry =  x * math.sin(state.angle) + y * math.cos(state.angle)
            px, py = perspective(rx, ry, z)
            size   = max(1, int(8 * (1 - z/500)))
            c      = COLS[int(z/100) % len(COLS)]
            pen.penup(); pen.goto(px, py)
            pen.dot(size, c)
        screen.update()
        screen.ontimer(frame, 16)

    frame()
    turtle.done()


if __name__ == "__main__":
    run()