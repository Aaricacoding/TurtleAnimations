"""
assets/fonts/font_styles_reference.py
=======================================
Quick reference grid: every combination of the 3 turtle font styles
(normal / bold / italic) across the best animation fonts.

Run:  python assets/fonts/font_styles_reference.py
"""

import sys, os, turtle

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

FONTS  = ["Arial", "Courier New", "Impact", "Consolas", "Verdana", "Georgia"]
STYLES = ["normal", "bold", "italic"]
COLS   = {"normal": "#8be9fd", "bold": "#ff79c6", "italic": "#50fa7b"}


def run():
    screen = turtle.Screen()
    screen.setup(960, 700)
    screen.bgcolor("#0d1117")
    screen.title("TurtleAnimations — Font Styles Reference")
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle(); pen.speed(0); pen.penup()

    # header
    pen.goto(0, 315)
    pen.color("#f8f8f2")
    pen.write("Font Styles Reference", align="center",
              font=("Arial Black", 20, "bold"))

    pen.goto(0, 285)
    pen.color("#6272a4")
    pen.write("normal  ·  bold  ·  italic", align="center",
              font=("Arial", 13, "normal"))

    col_x  = [-300, -20, 240]
    start_y = 230
    row_h   = 75

    # column headers
    for sx, style in zip(col_x, STYLES):
        pen.goto(sx, start_y + 18)
        pen.color(COLS[style])
        pen.write(style.upper(), align="left",
                  font=("Arial Black", 12, "bold"))

    # grid
    for row, fname in enumerate(FONTS):
        y = start_y - (row + 1) * row_h

        # row label
        pen.goto(-450, y + 10)
        pen.color("#6272a4")
        pen.write(fname, align="left", font=("Consolas", 10, "normal"))

        for sx, style in zip(col_x, STYLES):
            pen.goto(sx, y)
            pen.color(COLS[style])
            try:
                pen.write("Aa Bb 123", align="left",
                          font=(fname, 18, style))
            except Exception:
                pen.color("#ff5555")
                pen.write("N/A", align="left",
                          font=("Arial", 14, "normal"))

    screen.update()
    print("Style reference rendered. Close the window to exit.")
    turtle.done()


if __name__ == "__main__":
    run()