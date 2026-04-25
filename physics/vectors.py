"""
physics/vectors.py
==================
2-D Vector math.

Run standalone:  python physics/vectors.py  (vector field demo)
"""

import sys, os, math, turtle

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)


class Vector:
    def __init__(self, x=0, y=0): self.x=x; self.y=y
    def add(self, o):   self.x+=o.x; self.y+=o.y
    def scale(self, s): self.x*=s;   self.y*=s
    def magnitude(self): return math.sqrt(self.x**2+self.y**2)
    def normalize(self):
        m=self.magnitude()
        if m: self.x/=m; self.y/=m
    def copy(self): return Vector(self.x, self.y)
    def __repr__(self): return f"Vector({self.x:.2f}, {self.y:.2f})"


# ── Standalone demo: animated curl vector field ───────────────────────────────
class _VFState:
    def __init__(self): self.t = 0.0


def run():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#0d1117")
    screen.title("TurtleAnimations — Vector Field")
    screen.tracer(0)

    pen   = turtle.Turtle(); pen.hideturtle(); pen.speed(0)
    state = _VFState()
    COLS  = ["#8be9fd","#bd93f9","#ff79c6","#50fa7b","#ffb86c"]
    STEP  = 60
    L     = 22   # arrow length

    def draw_arrow(x, y, vx, vy, color):
        mag = math.sqrt(vx*vx + vy*vy) or 0.001
        nx  = vx/mag * L; ny = vy/mag * L
        pen.pencolor(color); pen.width(1)
        pen.penup(); pen.goto(x, y); pen.pendown()
        pen.goto(x+nx, y+ny)

    def frame():
        state.t += 0.04
        pen.clear()
        xs = range(-350, 360, STEP)
        ys = range(-350, 360, STEP)
        for i, gx in enumerate(xs):
            for j, gy in enumerate(ys):
                # curl field: vx = sin(y+t), vy = sin(x+t)
                vx =  math.sin(gy * 0.015 + state.t)
                vy =  math.cos(gx * 0.015 + state.t)
                ci = (i + j) % len(COLS)
                draw_arrow(gx, gy, vx, vy, COLS[ci])
        screen.update()
        screen.ontimer(frame, 40)

    frame()
    turtle.done()


if __name__ == "__main__":
    run()