"""
physics/neon.py
===============
NeonRenderer — layered glow dots.

Run standalone:  python physics/neon.py  (neon spiral demo)
"""

import sys, os, math, turtle

_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

from physics.particles import Particle


class NeonRenderer:
    def __init__(self, t):
        self.t = t

    def draw(self, particle):
        sizes  = [8, 5, 2]
        colors = [particle.color, particle.color, "white"]
        for sz, col in zip(sizes, colors):
            self.t.penup()
            self.t.goto(particle.x, particle.y)
            self.t.dot(sz, col)


# ── Standalone demo: neon lissajous ribbon ───────────────────────────────────
class _NeonState:
    def __init__(self): self.t = 0.0; self.particles = []


def run():
    screen = turtle.Screen()
    screen.setup(800, 800)
    screen.bgcolor("#000000")
    screen.title("TurtleAnimations — Neon Lissajous")
    screen.tracer(0)

    pen   = turtle.Turtle(); pen.hideturtle(); pen.speed(0)
    neon  = NeonRenderer(pen)
    state = _NeonState()
    COLS  = ["#ff79c6","#bd93f9","#8be9fd","#50fa7b","#ffb86c","#f1fa8c","#ff5555"]

    def frame():
        state.t += 0.04
        # spawn new point on lissajous curve
        x = 280 * math.sin(3 * state.t + math.pi/4)
        y = 280 * math.sin(2 * state.t)
        ci = int(state.t * 10) % len(COLS)
        state.particles.append(Particle(x, y, 0, 0, COLS[ci], life=55))

        pen.clear()
        for p in state.particles:
            p.life -= 1
            neon.draw(p)
        state.particles = [p for p in state.particles if p.life > 0]
        screen.update()
        screen.ontimer(frame, 20)

    frame()
    turtle.done()


if __name__ == "__main__":
    run()