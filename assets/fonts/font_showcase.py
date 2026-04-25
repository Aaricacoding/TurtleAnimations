"""
assets/fonts/font_showcase.py
==============================
Showcases all system fonts available to turtle's write() function,
rendered live on a dark canvas.

Run:  python assets/fonts/font_showcase.py
"""

import sys, os, turtle

_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

# Fonts that render well in turtle across Windows / macOS / Linux
FONTS = [
    ("Courier",          "monospace / code style"),
    ("Courier New",      "classic terminal look"),
    ("Arial",            "clean sans-serif"),
    ("Arial Black",      "heavy sans-serif"),
    ("Helvetica",        "clean sans-serif (mac)"),
    ("Times New Roman",  "elegant serif"),
    ("Georgia",          "readable serif"),
    ("Verdana",          "wide legible sans"),
    ("Trebuchet MS",     "modern humanist sans"),
    ("Comic Sans MS",    "informal / playful"),
    ("Impact",           "ultra-bold display"),
    ("Lucida Console",   "monospaced console"),
    ("Palatino Linotype","old-style serif"),
    ("Garamond",         "classical book serif"),
    ("Consolas",         "sharp programmer font"),
    ("Segoe UI",         "Windows system UI font"),
]

PALETTE = [
    "#ff79c6","#bd93f9","#8be9fd","#50fa7b",
    "#ffb86c","#f1fa8c","#ff5555","#ffffff",
]


def run():
    screen = turtle.Screen()
    screen.setup(900, 900)
    screen.bgcolor("#0d1117")
    screen.title("TurtleAnimations — Font Showcase")
    screen.tracer(0)

    pen = turtle.Turtle()
    pen.hideturtle()
    pen.speed(0)
    pen.penup()

    # Title
    pen.goto(0, 390)
    pen.color("#f8f8f2")
    pen.write("🐢  Font Showcase", align="center",
              font=("Arial Black", 18, "bold"))

    pen.goto(0, 365)
    pen.color("#6272a4")
    pen.write("fonts available to turtle.write()", align="center",
              font=("Courier New", 11, "normal"))

    start_y = 320
    gap     = 36

    for i, (fname, desc) in enumerate(FONTS):
        y     = start_y - i * gap
        color = PALETTE[i % len(PALETTE)]

        # label
        pen.goto(-430, y)
        pen.color("#6272a4")
        pen.write(f"{i+1:>2}. {desc}", align="left",
                  font=("Consolas", 9, "normal"))

        # sample in that font
        pen.goto(-10, y)
        pen.color(color)
        try:
            pen.write(f"AaBbCc 123  ← {fname}", align="left",
                      font=(fname, 14, "bold"))
        except Exception:
            pen.color("#ff5555")
            pen.write(f"(not available on this system)", align="left",
                      font=("Arial", 12, "italic"))

    screen.update()
    print("Font showcase rendered. Close the window to exit.")
    turtle.done()


if __name__ == "__main__":
    run()