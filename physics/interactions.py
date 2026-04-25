"""
physics/interactions.py
=======================
Mouse attraction + collision logic.

Run standalone:  python physics/interactions.py  (mouse gravity well demo)
"""

import sys, os, math, random, turtle

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from physics.particles import Particle
from physics.neon      import NeonRenderer


class InteractionSystem:
    def __init__(self):
        self.mouse_x = 0
        self.mouse_y = 0

    def update_mouse(self, x, y):
        self.mouse_x = x
        self.mouse_y = y

    def attract(self, p):
        dx   = self.mouse_x - p.x
        dy   = self.mouse_y - p.y
        dist = math.sqrt(dx*dx + dy*dy) or 0.001
        if dist < 200:
            p.vx += dx * 0.002
            p.vy += dy * 0.002

    def collide(self, p1, p2):
        dx = p1.x-p2.x; dy = p1.y-p2.y
        if math.sqrt(dx*dx+dy*dy) < 10:
            p1.vx, p2.vx = p2.vx, p1.vx
            p1.vy, p2.vy = p2.vy, p1.vy


# ── Standalone demo: mouse gravity well ──────────────────────────────────────
def run():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#0d1117")
    screen.title("TurtleAnimations — Mouse Gravity Well")
    screen.tracer(0)

    t = turtle.Turtle(); t.hideturtle(); t.speed(0)
    neon   = NeonRenderer(t)
    system = InteractionSystem()
    particles = []
    COLS = ["#ff79c6","#bd93f9","#8be9fd","#50fa7b","#ffb86c"]

    screen.listen()
    screen.onscreenclick(lambda x,y: system.update_mouse(x,y))

    # spawn orbiting particles
    for i in range(60):
        ang = math.radians(i * 6)
        r   = random.randint(80, 300)
        x   = math.cos(ang) * r
        y   = math.sin(ang) * r
        vx  = -math.sin(ang) * 2
        vy  =  math.cos(ang) * 2
        particles.append(Particle(x, y, vx, vy, random.choice(COLS), life=9999))

    def on_motion(x, y): system.update_mouse(x, y)

    import tkinter as tk
    cv = screen.getcanvas()
    cv.bind("<Motion>", lambda e: system.update_mouse(
        e.x - screen.window_width()//2,
        -(e.y - screen.window_height()//2)))

    def frame():
        t.clear()
        for p in particles:
            system.attract(p)
            p.vx *= 0.98; p.vy *= 0.98    # damping
            p.update()
            p.life = 9999                  # immortal
            neon.draw(p)
        screen.update()
        screen.ontimer(frame, 16)

    frame()
    turtle.done()


if __name__ == "__main__":
    run()