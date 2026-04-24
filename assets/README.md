# 🗂️ Assets

This folder stores all static and generated files for the TurtleAnimations project.

## Folder Purpose

| Subfolder   | What goes here                                             |
| ----------- | ---------------------------------------------------------- |
| `previews/` | Screenshot PNGs of each animation (used in README / docs)  |
| `exports/`  | Saved canvas exports — PostScript (.eps) or converted PNGs |
| `fonts/`    | Any custom fonts used in turtle text rendering             |
| `palettes/` | JSON color palette files shared across animations          |

## How to Save a Turtle Canvas

Add this to the end of any animation script to export it:

```python
import turtle

# After your animation finishes:
canvas = turtle.getscreen().getcanvas()
canvas.postscript(file="assets/exports/my_animation.eps")
```

Then convert to PNG with:

```bash
# Using ImageMagick (install once: https://imagemagick.org)
magick assets/exports/my_animation.eps assets/previews/my_animation.png
```

Or use Python Pillow:

```python
from PIL import Image
img = Image.open("assets/exports/my_animation.eps")
img.save("assets/previews/my_animation.png")
```
