"""
physics/forces.py
=================
Force definitions: gravity, wind, drag.

Run standalone:  python physics/forces.py  (wind-driven particles demo)
"""

import sys, os, math, random, turtle

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from physics.particles import Particle
from physics.neon      import NeonRenderer


class Forces:
    def __init__(self):
        self.gravity = -0.05
        self.wind    = 0.0

    def apply_gravity(self, p): p.vy += self.gravity
    def apply_wind(self, p):    p.vx += self.wind
    def random_wind(self):      self.wind = random.uniform(-0.04, 0.04)


# ── Standalone demo: snowstorm ────────────────────────────────────────────────
class _SnowState:
    def __init__(self): self.tick = 0


def run():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#000814")
    screen.title("TurtleAnimations — Forces: Snowstorm")
    screen.tracer(0)

    t = turtle.Turtle(); t.hideturtle(); t.speed(0)
    neon   = NeonRenderer(t)
    forces = Forces()
    forces.gravity = -0.02
    particles = []
    state = _SnowState()

    def spawn():
        for _ in range(5):
            x  = random.randint(-380, 380)
            vx = random.uniform(-0.5, 0.5)
            vy = random.uniform(-1.5, -0.5)
            c  = random.choice(["white","#aac4ff","#8be9fd"])
            particles.append(Particle(x, 400, vx, vy, c, life=220))
        state.tick += 1
        if state.tick % 40 == 0:
            forces.random_wind()
        screen.ontimer(spawn, 60)

    def frame():
        t.clear()
        forces.apply_gravity  # bound but applied per-particle below
        for p in particles:
            p.vx += forces.wind * 0.1
            p.vy += forces.gravity
            p.update()
            if p.life > 0:
                neon.draw(p)
        particles[:] = [p for p in particles if p.life > 0 and p.y > -420]
        screen.update()
        screen.ontimer(frame, 16)

    spawn(); frame()
    turtle.done()


if __name__ == "__main__":
    run()