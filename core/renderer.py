"""
core/renderer.py
================
Turtle setup helper used by all new animations.

Import pattern (works from any subfolder because main.py
adds the repo root to sys.path):

    from core.renderer import setup, refresh, done
"""

import turtle

# Use importlib-safe relative import that works whether called
# directly or via main.py launcher
try:
    from core.config import (
        CANVAS_WIDTH, CANVAS_HEIGHT, BACKGROUND,
        DEFAULT_SPEED, DEFAULT_WIDTH, HIDE_TURTLE,
    )
except ModuleNotFoundError:
    # Fallback defaults if run in isolation
    CANVAS_WIDTH  = 800
    CANVAS_HEIGHT = 800
    BACKGROUND    = "#0d1117"
    DEFAULT_SPEED = 0
    DEFAULT_WIDTH = 1
    HIDE_TURTLE   = True


def setup(title: str = "TurtleAnimations") -> turtle.Turtle:
    """Initialise the screen and return a ready-to-use Turtle."""
    screen = turtle.Screen()
    screen.setup(CANVAS_WIDTH, CANVAS_HEIGHT)
    screen.bgcolor(BACKGROUND)
    screen.title(title)
    screen.tracer(0)
    t = turtle.Turtle()
    t.speed(DEFAULT_SPEED)
    t.width(DEFAULT_WIDTH)
    if HIDE_TURTLE:
        t.hideturtle()
    return t


def refresh() -> None:
    """Push current frame to the screen."""
    turtle.Screen().update()


def done() -> None:
    """Keep the window open until the user closes it."""
    turtle.done()