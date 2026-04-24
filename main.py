"""
TurtleAnimations — Main Launcher
=================================
Run this file from the repo root:
    python main.py

Works for ALL animations, including those that import from core/,
physics/, projections/, etc. — because we add the project root to
sys.path before loading any script.
"""

import os
import sys
import importlib.util

# ── Make sure every sub-module can find 'core', 'physics', etc. ──────────────
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

# ── Full animation menu ───────────────────────────────────────────────────────
MENU = {
    # Legacy
    "1":  ("💖  Parametric Heart",          "legacy/parametric_heart.py"),
    "2":  ("🌀  Arc Weave",                 "legacy/arc_weave.py"),
    "3":  ("🌈  Rainbow Geometric Wheel",   "legacy/geometricRainbow_wheel.py"),
    "4":  ("☀️   Sunburst Spiral",           "legacy/sunburst_spiral.py"),
    # Fractals
    "5":  ("🌑  Mandelbrot Visualizer",     "fractals/mandelbrot_visualizer.py"),
    "6":  ("🔵  Julia Set Explorer",        "fractals/julia_set_explorer.py"),
    # Interactive
    "7":  ("🎆  Keyboard Fireworks",        "interactive/keyboard_fireworks.py"),
    "8":  ("〰️   Lissajous Controller",     "interactive/lissajous_controller.py"),
    "9":  ("🖌️   Mouse Painter",            "interactive/mouse_painter.py"),
    # Physics
    "10": ("🌌  Galaxy Simulation",         "physics/galaxy.py"),
    "11": ("🌟  Neon Particles",            "physics/neon.py"),
    "12": ("🔵  Particle Presets",          "physics/presets.py"),
}

BANNER = r"""
  ╔════════════════════════════════════════════════════╗
  ║   🐢   T U R T L E   A N I M A T I O N S   🐢     ║
  ║          Where Mathematics Becomes Art             ║
  ╠════════════════════════════════════════════════════╣
  ║  github.com/Aaricacoding/TurtleAnimations          ║
  ╚════════════════════════════════════════════════════╝
"""

CATEGORIES = [
    ("📦  LEGACY",       ["1", "2", "3", "4"]),
    ("🌿  FRACTALS",     ["5", "6"]),
    ("🎮  INTERACTIVE",  ["7", "8", "9"]),
    ("🌊  PHYSICS",      ["10", "11", "12"]),
]


def run_script(path: str) -> None:
    """Dynamically load and run an animation script with ROOT on sys.path."""
    abs_path = os.path.join(ROOT, path)
    if not os.path.exists(abs_path):
        print(f"\n  ⚠  File not found: {abs_path}\n")
        return
    spec = importlib.util.spec_from_file_location("animation", abs_path)
    mod  = importlib.util.module_from_spec(spec)
    # Give the loaded module the same root path awareness
    sys.modules["animation"] = mod
    spec.loader.exec_module(mod)


def print_menu() -> None:
    print(BANNER)
    for category, keys in CATEGORIES:
        print(f"  {category}")
        for k in keys:
            label, _ = MENU[k]
            print(f"    [{k:>2}]  {label}")
        print()
    print("    [ q]  Quit\n")


def main() -> None:
    while True:
        print_menu()
        choice = input("  Enter a number to launch: ").strip().lower()

        if choice == "q":
            print("\n  See you next time! ✦\n")
            break

        if choice not in MENU:
            print("\n  ⚠  Invalid choice — try again.\n")
            input("  Press Enter to continue...")
            print("\033[2J\033[H")   # clear terminal
            continue

        label, path = MENU[choice]
        print(f"\n  ► Launching {label} ...\n")
        run_script(path)
        print("\n  Animation closed.")
        input("  Press Enter to return to menu...")
        print("\033[2J\033[H")       # clear terminal


if __name__ == "__main__":
    main()