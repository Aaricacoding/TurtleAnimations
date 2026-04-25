"""
core/renderer.py
================
Provides TWO things:

  1. setup() / refresh() / done()  — simple turtle helpers for basic animations
  2. Renderer class                — used by fractal scripts to draw coloured points

Import patterns:
    from core.renderer import setup, refresh, done        # basic animations
    from core.renderer import Renderer                    # fractal scripts
"""

import turtle
import sys
import os

# ── Ensure repo root is on path when file is run directly via VS Code ─────────
_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if _ROOT not in sys.path:
    sys.path.insert(0, _ROOT)

try:
    from core.config import (
        CANVAS_WIDTH, CANVAS_HEIGHT, BACKGROUND,
        DEFAULT_SPEED, DEFAULT_WIDTH, HIDE_TURTLE,
    )
except ModuleNotFoundError:
    CANVAS_WIDTH  = 800
    CANVAS_HEIGHT = 800
    BACKGROUND    = "#0d1117"
    DEFAULT_SPEED = 0
    DEFAULT_WIDTH = 1
    HIDE_TURTLE   = True


# ─────────────────────────────────────────────────────────────────────────────
# Simple helpers (used by legacy / interactive / physics)
# ─────────────────────────────────────────────────────────────────────────────

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
    """Push current frame to screen."""
    turtle.Screen().update()


def done() -> None:
    """Keep window open until user closes it."""
    turtle.done()


# ─────────────────────────────────────────────────────────────────────────────
# Renderer class (used by fractal scripts)
# ─────────────────────────────────────────────────────────────────────────────

class Renderer:
    """
    Turtle-based point renderer for fractal visualisations.
    Uses colormode(1.0) so colors can be passed as (r, g, b) floats in [0,1].
    """

    def __init__(self, title: str = "TurtleAnimations — Fractal"):
        self.screen = turtle.Screen()
        self.screen.setup(CANVAS_WIDTH, CANVAS_HEIGHT)
        self.screen.bgcolor(BACKGROUND)
        self.screen.title(title)
        self.screen.tracer(0)
        turtle.colormode(1.0)

        self._t = turtle.Turtle()
        self._t.speed(0)
        self._t.hideturtle()
        self._t.penup()

    def draw_point(self, x: float, y: float, color: tuple) -> None:
        """Draw a single coloured dot at (x, y). color = (r, g, b) in [0, 1]."""
        self._t.goto(x, y)
        self._t.dot(4, color)

    def update(self) -> None:
        """Flush the current frame to the screen."""
        self.screen.update()

    def done(self) -> None:
        """Keep the window open until the user closes it."""
        turtle.done()