# 🔤 assets/fonts/

Turtle uses **system-installed fonts** via `turtle.write()` : you cannot load
`.ttf` files directly. This folder contains scripts that demonstrate and test
fonts within the turtle environment.

## Scripts

| Script                     | What it does                                                                              |
| -------------------------- | ----------------------------------------------------------------------------------------- |
| `font_showcase.py`         | Renders all recommended fonts live on a dark canvas so you can see exactly how each looks |
| `neon_text_demo.py`        | Shows how to fake a neon glow effect using layered offset text                            |
| `font_styles_reference.py` | Grid of normal / bold / italic across the best animation fonts                            |

## How to use a font in your animation

```python
import turtle

t = turtle.Turtle()
t.penup()
t.goto(0, 0)
t.color("#ff79c6")

# turtle.write(text, move, align, font)
# font = (family, size, style)   style = "normal" | "bold" | "italic" | "bold italic"
t.write("Hello!", align="center", font=("Impact", 32, "bold"))
```

## Best fonts for animations

| Font            | Style         | Best for            |
| --------------- | ------------- | ------------------- |
| `Impact`        | Ultra-bold    | Titles, banners     |
| `Arial Black`   | Heavy sans    | Headers             |
| `Courier New`   | Monospace     | Code, retro, sci-fi |
| `Consolas`      | Sharp mono    | Technical displays  |
| `Verdana`       | Wide legible  | Body labels         |
| `Georgia`       | Elegant serif | Artistic text       |
| `Comic Sans MS` | Playful       | Casual / fun        |

## Neon glow trick

Turtle has no alpha/blur — fake a glow by writing the same text multiple
times in slightly offset positions using a lighter/translucent-looking
colour first, then the bright core colour on top:

```python
GLOW_OFFSETS = [(-2,0),(2,0),(0,-2),(0,2)]

def write_neon(t, text, x, y, color, glow_color, size, font):
    for dx, dy in GLOW_OFFSETS:
        t.goto(x + dx, y + dy)
        t.color(glow_color)
        t.write(text, align="center", font=(font, size + 2, "bold"))
    t.goto(x, y)
    t.color(color)
    t.write(text, align="center", font=(font, size, "bold"))
```

Run `neon_text_demo.py` to see this live.
