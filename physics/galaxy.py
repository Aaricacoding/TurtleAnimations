"""
physics/galaxy.py
=================
N-body galaxy simulation with orbital mechanics.

Run standalone:  python physics/galaxy.py
Run via menu:    python main.py  → option 10
"""

import sys
import os
import random
import math
import turtle

# ── Root path fix (works via VS Code play button AND main.py) ─────────────────
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from physics.particles import Particle   # always use full package path


class Galaxy:
    def __init__(self, cx=0, cy=0):
        self.cx    = cx
        self.cy    = cy
        self.stars = []

    def spawn_star(self):
        angle  = random.uniform(0, 2 * math.pi)
        radius = random.uniform(10, 200)
        x      = self.cx + math.cos(angle) * radius
        y      = self.cy + math.sin(angle) * radius
        vx     = -math.sin(angle) * 0.5
        vy     =  math.cos(angle) * 0.5
        color  = random.choice(["white", "cyan", "yellow", "lightblue"])
        self.stars.append(Particle(x, y, vx, vy, color, life=9999))

    def update(self):
        for s in self.stars:
            dx     = self.cx - s.x
            dy     = self.cy - s.y
            s.vx  += dx * 0.00005
            s.vy  += dy * 0.00005
            s.update()


def run():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#000008")
    screen.title("TurtleAnimations — Galaxy Simulation")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    galaxy = Galaxy()
    for _ in range(300):
        galaxy.spawn_star()

    def frame():
        t.clear()
        galaxy.update()
        for star in galaxy.stars:
            t.penup()
            t.goto(star.x, star.y)
            t.pendown()
            t.dot(2, star.color)
        screen.update()
        screen.ontimer(frame, 16)

    frame()
    turtle.done()


if __name__ == "__main__":
    run()