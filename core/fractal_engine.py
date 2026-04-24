"""
core/fractal_engine.py
======================
Recursive and iterative helpers for fractal animations.

Import pattern:
    from core.fractal_engine import l_system, draw_l_system, sierpinski_triangle
"""

import turtle
import math


def l_system(axiom: str, rules: dict, iterations: int) -> str:
    """
    Expand an L-System string.
      axiom      : starting string  e.g. "F"
      rules      : replacement dict e.g. {"F": "F+F-F-F+F"}
      iterations : expansion steps
    """
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
    Draw an L-System string.
      F / G  — forward
      +      — left  by angle
      -      — right by angle
      [      — push state
      ]      — pop  state
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