"""
projections/viewport.py
=======================
Maps world-space to screen-space.

Run standalone:  python projections/viewport.py
"""

import sys, os, math, turtle

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from projections.camera import Camera


def world_to_screen(x, y, camera: Camera):
    sx = (x - camera.x) * camera.zoom
    sy = (y - camera.y) * camera.zoom
    return sx, sy


# ── Standalone demo: isometric grid ──────────────────────────────────────────
class _GridState:
    def __init__(self): self.t = 0.0


def run():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#0d1117")
    screen.title("TurtleAnimations — Isometric Grid")
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)

    cam   = Camera(zoom=1.0)
    state = _GridState()
    COLS  = ["#8be9fd","#bd93f9","#50fa7b","#ff79c6","#ffb86c"]

    def draw_diamond(px, py, size, color):
        pts = [(px, py+size),(px+size, py),(px, py-size),(px-size, py)]
        pen.pencolor(color)
        pen.penup(); pen.goto(pts[0]); pen.pendown()
        for p in pts[1:]:
            pen.goto(p)
        pen.goto(pts[0])

    def frame():
        state.t += 0.03
        pen.clear()
        cols_n, rows_n = 7, 7
        sp = 80
        for row in range(rows_n):
            for col in range(cols_n):
                wx = (col - cols_n//2) * sp + (row % 2) * sp//2
                wy = (row - rows_n//2) * sp * 0.55
                pulse = math.sin(state.t + row * 0.5 + col * 0.5) * 0.3 + 0.7
                size  = int(35 * pulse)
                c     = COLS[(row + col) % len(COLS)]
                sx, sy = world_to_screen(wx, wy, cam)
                draw_diamond(sx, sy, size, c)
        screen.update()
        screen.ontimer(frame, 30)

    frame()
    turtle.done()


if __name__ == "__main__":
    run()