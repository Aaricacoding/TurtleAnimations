"""
physics/engine.py
=================
Core simulation loop.

Run standalone:  python physics/engine.py  (mouse-attraction particle demo)
"""

import sys, os, turtle, random

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from physics.particles import Particle
from physics.neon      import NeonRenderer


class Engine:
    def __init__(self, screen, t, renderer=None):
        self.screen   = screen
        self.t        = t
        self.objects  = []
        self.renderer = renderer
        self.systems  = []

    def add_system(self, sys_obj): self.systems.append(sys_obj)
    def add(self, obj):            self.objects.append(obj)

    def update(self):
        self.t.clear()
        for obj in self.objects:
            for s in self.systems:
                if hasattr(s, "attract"): s.attract(obj)
            obj.update()
            if obj.life > 0:
                if self.renderer: self.renderer.draw(obj)
                else:
                    self.t.penup(); self.t.goto(obj.x, obj.y)
                    self.t.pendown(); self.t.dot(3, obj.color)
        self.objects = [o for o in self.objects if o.life > 0]
        self.screen.update()
        self.screen.ontimer(self.update, 16)


# ── Standalone demo: continuous neon particle fountain ────────────────────────
class _FountainState:
    def __init__(self): self.tick = 0


def run():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#0d1117")
    screen.title("TurtleAnimations — Particle Engine Demo")
    screen.tracer(0)

    t = turtle.Turtle(); t.hideturtle(); t.speed(0)
    neon   = NeonRenderer(t)
    engine = Engine(screen, t, renderer=neon)
    state  = _FountainState()
    COLS   = ["#ff79c6","#bd93f9","#8be9fd","#50fa7b","#ffb86c","#f1fa8c"]

    def spawn():
        import math
        for i in range(8):
            ang = math.radians(i * 45 + state.tick * 3)
            vx  = math.cos(ang) * random.uniform(2, 5)
            vy  = math.sin(ang) * random.uniform(2, 5)
            engine.add(Particle(0, -200, vx, vy+4,
                                random.choice(COLS), life=80))
        state.tick += 1
        screen.ontimer(spawn, 80)

    def frame():
        engine.t.clear()
        for obj in engine.objects:
            obj.vy -= 0.08          # gravity
            obj.update()
            if obj.life > 0:
                engine.renderer.draw(obj)
        engine.objects = [o for o in engine.objects if o.life > 0]
        screen.update()
        screen.ontimer(frame, 16)

    spawn(); frame()
    turtle.done()


if __name__ == "__main__":
    run()