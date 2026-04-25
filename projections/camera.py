"""
projections/camera.py
=====================
Camera class + standalone rotating 3D wireframe cube demo.

Run standalone:  python projections/camera.py
"""

import sys, os, math, turtle

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)


class Camera:
    def __init__(self, x=0, y=0, zoom=1.0):
        self.x    = x
        self.y    = y
        self.zoom = zoom

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def zoom_in(self,  factor=1.1): self.zoom *= factor
    def zoom_out(self, factor=1.1): self.zoom /= factor

    def __repr__(self):
        return f"Camera(x={self.x}, y={self.y}, zoom={self.zoom:.2f})"


# ── 3-D math helpers (no nonlocal needed) ─────────────────────────────────────
def _rotate(x, y, z, ax, ay):
    """Rotate point around X then Y axes. Returns (rx, ry, rz)."""
    # X-axis rotation
    y1 =  y * math.cos(ax) - z * math.sin(ax)
    z1 =  y * math.sin(ax) + z * math.cos(ax)
    # Y-axis rotation
    x2 =  x * math.cos(ay) + z1 * math.sin(ay)
    z2 = -x * math.sin(ay) + z1 * math.cos(ay)
    return x2, y1, z2


def _project(x, y, z, fov=420):
    """Perspective divide."""
    d = z + fov
    if d <= 0:
        d = 0.001
    f = fov / d
    return x * f, y * f


class _CubeState:
    """Holds mutable angle — avoids nonlocal entirely."""
    def __init__(self): self.ax = 0.0; self.ay = 0.0


def run():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#0d1117")
    screen.title("TurtleAnimations — Rotating 3D Wireframe Cube")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    cam   = Camera(zoom=1.0)
    state = _CubeState()

    # Unit cube vertices  (x, y, z)
    VERTS = [
        (-120,-120,-120),(120,-120,-120),(120,120,-120),(-120,120,-120),
        (-120,-120, 120),(120,-120, 120),(120,120, 120),(-120,120, 120),
    ]
    EDGES = [(0,1),(1,2),(2,3),(3,0),(4,5),(5,6),(6,7),(7,4),
             (0,4),(1,5),(2,6),(3,7)]
    # colours cycle per edge for a rainbow cube
    COLORS = ["#ff79c6","#bd93f9","#8be9fd","#50fa7b",
              "#ffb86c","#f1fa8c","#ff5555","#ff79c6",
              "#bd93f9","#8be9fd","#50fa7b","#ffb86c"]

    def frame():
        state.ax += 0.012
        state.ay += 0.018
        t.clear()

        proj = []
        for (x, y, z) in VERTS:
            rx, ry, rz = _rotate(x, y, z, state.ax, state.ay)
            px, py     = _project(rx, ry, rz)
            sx         = (px - cam.x) * cam.zoom
            sy         = (py - cam.y) * cam.zoom
            proj.append((sx, sy))

        for i, (a, b) in enumerate(EDGES):
            t.pencolor(COLORS[i])
            t.width(2)
            t.penup();  t.goto(proj[a])
            t.pendown(); t.goto(proj[b])

        screen.update()
        screen.ontimer(frame, 16)

    frame()
    turtle.done()


if __name__ == "__main__":
    run()