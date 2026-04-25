"""
projections/transform.py
========================
3-D transform helpers: rotate, translate, scale.

Run standalone:  python projections/transform.py
"""

import sys, os, math, turtle

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)


def rotate_point(x, y, z, ax_deg, ay_deg):
    ax = math.radians(ax_deg); ay = math.radians(ay_deg)
    y1 =  y*math.cos(ax) - z*math.sin(ax)
    z1 =  y*math.sin(ax) + z*math.cos(ax)
    x2 =  x*math.cos(ay) + z1*math.sin(ay)
    z2 = -x*math.sin(ay) + z1*math.cos(ay)
    return x2, y1, z2

def translate(x, y, cx, cy): return x+cx, y+cy
def scale(x, y, s):          return x*s,  y*s


# ── Standalone demo: rotating platonic octahedron ────────────────────────────
class _OctState:
    def __init__(self): self.ax = 0.0; self.ay = 0.0


def run():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#0d1117")
    screen.title("TurtleAnimations — Rotating Octahedron")
    screen.tracer(0)

    pen = turtle.Turtle(); pen.hideturtle(); pen.speed(0)
    st  = _OctState()
    R   = 160
    VERTS = [(R,0,0),(-R,0,0),(0,R,0),(0,-R,0),(0,0,R),(0,0,-R)]
    EDGES = [(0,2),(0,3),(0,4),(0,5),(1,2),(1,3),(1,4),(1,5),(2,4),(2,5),(3,4),(3,5)]
    COLS  = ["#ff79c6","#bd93f9","#8be9fd","#50fa7b","#ffb86c","#f1fa8c"]

    FOV = 450

    def frame():
        st.ax += 0.014; st.ay += 0.009
        pen.clear()
        proj = []
        for (x,y,z) in VERTS:
            rx,ry,rz = rotate_point(x,y,z, math.degrees(st.ax), math.degrees(st.ay))
            d = rz + FOV
            if d <= 0: d = 0.001
            f = FOV/d
            proj.append((rx*f, ry*f))
        for i,(a,b) in enumerate(EDGES):
            pen.pencolor(COLS[i % len(COLS)]); pen.width(2)
            pen.penup(); pen.goto(proj[a]); pen.pendown(); pen.goto(proj[b])
        screen.update()
        screen.ontimer(frame, 16)

    frame()
    turtle.done()


if __name__ == "__main__":
    run()