"""
physics/presets.py
==================
Ready-to-run physics scene presets.

Run standalone:  python physics/presets.py
Run via menu:    python main.py  → option 12
"""

import sys
import os
import random
import math
import turtle

# ── Root path fix ─────────────────────────────────────────────────────────────
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from physics.particles import Particle   # full package path — works everywhere
from physics.forces    import Forces
from physics.engine    import Engine
from physics.neon      import NeonRenderer


def firework(x, y, color=None):
    """Return a burst of particles expanding from (x, y)."""
    if not color:
        color = random.choice(["red", "cyan", "yellow", "white", "hotpink"])
    particles = []
    for angle in range(0, 360, 15):
        rad = math.radians(angle)
        vx  = math.cos(rad) * random.uniform(1.5, 3.5)
        vy  = math.sin(rad) * random.uniform(1.5, 3.5)
        particles.append(Particle(x, y, vx, vy, color, life=60))
    return particles


def run():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#0d1117")
    screen.title("TurtleAnimations — Firework Presets")
    screen.tracer(0)

    t = turtle.Turtle()
    t.hideturtle()
    t.speed(0)

    neon   = NeonRenderer(t)
    engine = Engine(screen, t, renderer=neon)
    forces = Forces()

    def launch():
        x = random.randint(-300, 300)
        y = random.randint(-100, 200)
        for p in firework(x, y):
            engine.add(p)
        screen.ontimer(launch, random.randint(400, 900))

    def frame():
        engine.t.clear()
        for obj in engine.objects:
            obj.update(forces)
            if obj.life > 0:
                engine.renderer.draw(obj)
        engine.objects = [o for o in engine.objects if o.life > 0]
        screen.update()
        screen.ontimer(frame, 16)

    launch()
    frame()
    turtle.done()


if __name__ == "__main__":
    run()