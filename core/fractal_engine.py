"""
core/fractal_engine.py
======================
Math functions + L-System helpers for all fractal animations.

Import pattern:
    from core.fractal_engine import mandelbrot, julia
    from core.fractal_engine import l_system, draw_l_system
"""

import turtle
import sys
import os

# ── Make sure repo root is on path (needed when run via VS Code play button) ──
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)


# ─────────────────────────────────────────────────────────────────────────────
# Fractal math
# ─────────────────────────────────────────────────────────────────────────────

def mandelbrot(c: complex, max_iter: int) -> int:
    """
    Return the escape iteration count for point c in the Mandelbrot set.
    z_(n+1) = z_n^2 + c,  starting from z=0.
    Returns max_iter if the point never escapes |z| > 2.
    """
    z = 0j
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


def julia(z: complex, c: complex, max_iter: int) -> int:
    """
    Return the escape iteration count for point z with fixed seed c.
    z_(n+1) = z_n^2 + c.
    Returns max_iter if the point never escapes |z| > 2.
    """
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


# ─────────────────────────────────────────────────────────────────────────────
# L-System helpers
# ─────────────────────────────────────────────────────────────────────────────

def l_system(axiom: str, rules: dict, iterations: int) -> str:
    """Expand an L-System string for `iterations` steps."""
    result = axiom
    for _ in range(iterations):
        result = "".join(rules.get(ch, ch) for ch in result)
    return result


def draw_l_system(
    t: turtle.Turtle,
    instructions: str,
    angle: float,
    step: float,
) -> None:
    """
    Draw an L-System string using turtle.
      F/G — forward   + — left   - — right   [ — push   ] — pop
    """
    stack = []
    for cmd in instructions:
        if cmd in ("F", "G"):
            t.forward(step)
        elif cmd == "+":
            t.left(angle)
        elif cmd == "-":
            t.right(angle)
        elif cmd == "[":
            stack.append((t.position(), t.heading()))
        elif cmd == "]":
            pos, heading = stack.pop()
            t.penup()
            t.setposition(pos)
            t.setheading(heading)
            t.pendown()


def sierpinski_triangle(t: turtle.Turtle, size: float, depth: int) -> None:
    """Draw a Sierpiński triangle recursively."""
    if depth == 0:
        for _ in range(3):
            t.forward(size)
            t.left(120)
        return
    half = size / 2
    sierpinski_triangle(t, half, depth - 1)
    t.forward(half)
    sierpinski_triangle(t, half, depth - 1)
    t.backward(half)
    t.left(60)
    t.forward(half)
    t.right(60)
    sierpinski_triangle(t, half, depth - 1)
    t.left(60)
    t.backward(half)
    t.right(60)