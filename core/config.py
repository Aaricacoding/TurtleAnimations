"""
core/config.py
==============
Global canvas settings AND the Config class used by fractal scripts.
"""

# ── Flat constants (used by renderer.py) ─────────────────────────────────────
CANVAS_WIDTH  = 800
CANVAS_HEIGHT = 800
BACKGROUND    = "#0d1117"
DEFAULT_SPEED = 0
DEFAULT_WIDTH = 1
HIDE_TURTLE   = True

PALETTE = [
    "#ff79c6",
    "#bd93f9",
    "#8be9fd",
    "#50fa7b",
    "#ffb86c",
    "#f1fa8c",
    "#ff5555",
]


# ── Config class (used by fractal scripts) ────────────────────────────────────
class Config:
    """Fractal rendering configuration."""
    def __init__(
        self,
        step: int   = 4,       # pixel step — lower = sharper but slower
        zoom: float = 0.005,   # world-space zoom factor
        max_iter: int = 64,    # iteration depth
        center_x: float = 0.0,
        center_y: float = 0.0,
    ):
        self.step     = step
        self.zoom     = zoom
        self.max_iter = max_iter
        self.center_x = center_x
        self.center_y = center_y