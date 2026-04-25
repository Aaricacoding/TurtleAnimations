"""
assets/fonts/neon_text_demo.py
================================
Renders animated neon-glow text using turtle write().
Demonstrates how to fake a glow effect with layered colored text.

Run:  python assets/fonts/neon_text_demo.py
"""

import sys, os, turtle, time

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)


LINES = [
    ("TURTLE",      "#ff79c6",  "#ff79c620", 52, "Impact"),
    ("ANIMATIONS",  "#8be9fd",  "#8be9fd20", 36, "Impact"),
    ("✦  where math becomes art  ✦", "#bd93f9", "#bd93f920", 16, "Arial"),
]

GLOW_OFFSETS = [(-2,0),(2,0),(0,-2),(0,2),(-1,-1),(1,1),(-1,1),(1,-1)]


def write_glowing(pen, text, x, y, color, glow_color, size, font):
    """Write text with a fake glow halo by layering offset copies."""
    # glow layer
    pen.color(glow_color)
    for dx, dy in GLOW_OFFSETS:
        pen.goto(x + dx*2, y + dy*2)
        pen.write(text, align="center", font=(font, size + 2, "bold"))

    # core text
    pen.color(color)
    pen.goto(x, y)
    pen.write(text, align="center", font=(font, size, "bold"))


def run():
    screen = turtle.Screen()
    screen.setup(860, 500)
    screen.bgcolor("#000000")
    screen.title("TurtleAnimations — Neon Text Demo")
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    positions = [120, 30, -60]

    for i, (text, color, glow, size, font) in enumerate(LINES):
        write_glowing(pen, text, 0, positions[i], color, glow, size, font)

    # separator line
    pen.color("#6272a4")
    pen.goto(-380, -100)
    pen.pendown()
    pen.goto(380, -100)
    pen.penup()

    # usage hint
    pen.color("#6272a4")
    pen.goto(0, -130)
    pen.write("Use turtle.write(text, font=(name, size, style)) in your animations",
              align="center", font=("Courier New", 11, "normal"))

    pen.goto(0, -160)
    pen.color("#50fa7b")
    pen.write("Recommended animation fonts:  Impact · Arial Black · Courier New · Consolas",
              align="center", font=("Arial", 12, "normal"))

    screen.update()
    print("Neon text demo rendered. Close the window to exit.")
    turtle.done()


if __name__ == "__main__":
    run()