<div align="center">

<picture>
  <img src="banner.svg" alt="Turtle Animations" width="100%"/>
</picture>

<br/>

[![Status](https://img.shields.io/badge/Status-🟢%20Ongoing-brightgreen?style=for-the-badge&labelColor=0d1117)](https://github.com/Aaricacoding/TurtleAnimations)
[![Language](https://img.shields.io/badge/Language-Python-3776AB?style=for-the-badge&logo=python&logoColor=white&labelColor=0d1117)](https://python.org)
[![Library](https://img.shields.io/badge/Library-Turtle-FFA500?style=for-the-badge&labelColor=0d1117)](https://docs.python.org/3/library/turtle.html)
[![Animations](https://img.shields.io/badge/Animations-17%20%26%20Growing-FF6B9D?style=for-the-badge&labelColor=0d1117)](https://github.com/Aaricacoding/TurtleAnimations)
[![License](https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge&labelColor=0d1117)](LICENSE)

<br/>

> *"The universe is written in the language of mathematics,*
> *and its characters are triangles, circles, and geometric figures."*
>
> — **Galileo Galilei**

<br/>

⭐ **If this project sparks your imagination, please give it a star!** ⭐
*Every star fuels more animations being created.*

</div>

---

## ✦ What Is TurtleAnimations?

**TurtleAnimations** is a curated gallery of generative art and geometric animations, crafted entirely with Python's built-in `turtle` library. Each script is a small mathematical poem — a set of equations that bloom into mesmerizing visual patterns on your screen.

This project exists to prove one thing:

> **You don't need a game engine, GPU renderer, or complex framework to create beautiful art. You just need math, code, and curiosity.**

Whether you're a student learning Python, a developer exploring creative coding, or an artist fascinated by algorithms — there's something here for you.

---

## 📦 Project Structure

```
TurtleAnimations/
│
├── 📄  README.md                      ← You are here
├── 🖼️  banner.svg                     ← Animated header banner
├── 🐍  main.py                        ← Entry point / animation launcher
├── 🐍  setup_structure.py             ← Repo folder scaffolding script
│
├── ⚙️  core/                          ← Shared animation engine
│   ├── config.py                      ← Global settings & constants
│   ├── fractal_engine.py              ← Fractal computation helpers
│   └── renderer.py                    ← Turtle rendering abstraction
│
├── 🌿  fractals/                      ← Fractal animations
│   ├── julia_set_explorer.py
│   └── mandelbrot_visualizer.py
│
├── 🎮  interactive/                   ← Interactive & input-driven art
│   ├── keyboard_fireworks.py
│   ├── lissajous_controller.py
│   └── mouse_painter.py
│
├── 📦  legacy/                        ← Original hand-crafted animations ⭐
│   ├── parametric_heart.py
│   ├── arc_weave.py
│   ├── geometricRainbow_wheel.py
│   └── sunburst_spiral.py
│
├── 🌊  physics/                       ← Physics & particle simulations
│   ├── engine.py
│   ├── forces.py
│   ├── galaxy.py
│   ├── interactions.py
│   ├── neon.py
│   ├── particles.py
│   ├── presets.py
│   └── vectors.py
│
├── 🧊  projections/                   ← 3D simulated projections
│   ├── camera.py
│   ├── perspective.py
│   ├── transform.py
│   └── viewport.py
│
└── 🗂️  assets/                        ← Images, exports, previews
```

---

## 🎨 Legacy Animations — Where It All Started

These are the original hand-crafted scripts that started this project. Pure turtle, pure math, no engine.

<div align="center">

| Animation | File | Description | Complexity |
|:---------:|:----:|:------------|:----------:|
| 💖 **Parametric Heart** | `legacy/parametric_heart.py` | A heart rendered from pure parametric equations — trigonometric functions in perfect harmony. | ⭐⭐ |
| 🌀 **Arc Weave** | `legacy/arc_weave.py` | Interlocking circular arcs that layer over each other in mesmerizing woven patterns. | ⭐⭐⭐ |
| 🌈 **Rainbow Geometric Wheel** | `legacy/geometricRainbow_wheel.py` | A vibrant rotating gear painted across the full color spectrum. Geometry meets color theory. | ⭐⭐⭐ |
| ☀️ **Sunburst Spiral** | `legacy/sunburst_spiral.py` | A radial spiral erupting outward like solar rays. Powered by the golden angle. | ⭐⭐⭐⭐ |

</div>

---

## 🌿 Fractals

Mathematical infinity made visible — recursive structures that reveal new detail at every scale.

<div align="center">

| Animation | File | Description |
|:---------:|:----:|:------------|
| 🔵 **Julia Set Explorer** | `fractals/julia_set_explorer.py` | Explores the boundary of Julia sets — complex-plane structures of infinite, haunting beauty. |
| 🌑 **Mandelbrot Visualizer** | `fractals/mandelbrot_visualizer.py` | Renders the iconic Mandelbrot set, the most famous fractal in mathematics. |

</div>

---

## 🎮 Interactive Animations

These respond to *you* — move your mouse, press keys, and watch the art react in real time.

<div align="center">

| Animation | File | Description |
|:---------:|:----:|:------------|
| 🎆 **Keyboard Fireworks** | `interactive/keyboard_fireworks.py` | Press any key to launch bursts of colorful fireworks — an explosive canvas. |
| 〰️ **Lissajous Controller** | `interactive/lissajous_controller.py` | Control Lissajous figures in real time by adjusting frequency and phase ratios. |
| 🖌️ **Mouse Painter** | `interactive/mouse_painter.py` | Your cursor becomes a brush — draw generative trails wherever you move. |

</div>

---

## 🌊 Physics & Particle Simulations

A full physics engine built on top of turtle — forces, particles, gravity, and emergent behavior.

<div align="center">

| Module | File | Role |
|:------:|:----:|:-----|
| ⚙️ **Engine** | `physics/engine.py` | Core simulation loop — updates all bodies each tick |
| 🧲 **Forces** | `physics/forces.py` | Gravity, drag, repulsion, attraction force definitions |
| 🌌 **Galaxy** | `physics/galaxy.py` | N-body galaxy simulation with spiral arm formation |
| 💥 **Interactions** | `physics/interactions.py` | Collision detection and particle interaction rules |
| 🌟 **Neon** | `physics/neon.py` | Glowing neon-trail particle effects |
| 🔵 **Particles** | `physics/particles.py` | Base particle class with position, velocity, mass |
| 🎛️ **Presets** | `physics/presets.py` | Ready-to-run scene configurations |
| 📐 **Vectors** | `physics/vectors.py` | 2D vector math — add, scale, dot product, normalize |

</div>

---

## 🧊 3D Simulated Projections

A hand-rolled 3D projection pipeline — turning mathematical 3D coordinates into 2D turtle drawings.

<div align="center">

| Module | File | Role |
|:------:|:----:|:-----|
| 📷 **Camera** | `projections/camera.py` | Camera position, orientation, and view matrix |
| 🔭 **Perspective** | `projections/perspective.py` | Perspective divide and field-of-view projection |
| 🔄 **Transform** | `projections/transform.py` | Rotation, translation, and scale matrices |
| 🖥️ **Viewport** | `projections/viewport.py` | Maps projected coordinates to screen pixels |

</div>

---

## ⚙️ Core Engine

Shared utilities imported by all new animations — no boilerplate required.

<div align="center">

| Module | File | Role |
|:------:|:----:|:-----|
| 🎨 **Config** | `core/config.py` | Canvas size, background color, speed, color palette |
| 🌿 **Fractal Engine** | `core/fractal_engine.py` | L-System expander, Sierpiński helper, draw utilities |
| 🖥️ **Renderer** | `core/renderer.py` | One-call turtle setup, frame refresh, window management |

</div>

---

## 🚀 Getting Started

### Prerequisites

```bash
python --version   # 3.6+ recommended — turtle is built in, no pip needed
```

### Run

```bash
git clone https://github.com/Aaricacoding/TurtleAnimations.git
cd TurtleAnimations
python main.py
```

The launcher shows a numbered menu — pick any animation and it opens instantly.

### Run directly

```bash
# Any script can also be run standalone
python legacy/parametric_heart.py
python fractals/mandelbrot_visualizer.py
python interactive/keyboard_fireworks.py
```

> 💡 Each animation opens its own Turtle window. Close it to return.

---

## 🧮 The Math Behind the Magic

<div align="center">

| 🎨 Animation | 📐 Core Concept |
|:------------:|:----------------|
| 💖 **Parametric Heart** | `x(t) = 16·sin³(t)` · `y(t) = 13cos(t) − 5cos(2t) − 2cos(3t) − cos(4t)` |
| 🌀 **Arc Weave** | Angular offset + radius scaling · `θ ∈ [0°, 360°]`, `arc_step = 360° / n` |
| 🌈 **Rainbow Wheel** | HSL color mapping: `hue = (i / segments) × 360°` · n-fold rotational symmetry |
| ☀️ **Sunburst Spiral** | Fermat's spiral `r = a√θ` · Golden angle `φ = 137.508°` |
| 🌑 **Mandelbrot** | `z₍ₙ₊₁₎ = zₙ² + c` · iterate until `|z| > 2` or max depth |
| 🔵 **Julia Set** | Fixed `c`, varying `z₀` across the complex plane |
| 〰️ **Lissajous** | `x(t) = A·sin(aτ + δ)` · `y(t) = B·sin(bτ)` |
| 🌌 **Galaxy** | N-body gravity · `F = G·m₁m₂ / r²` with velocity verlet integration |

</div>

---

## 📅 Project Status

<div align="center">

[![Status](https://img.shields.io/badge/🟢%20ACTIVELY%20DEVELOPED-Ongoing-success?style=for-the-badge&labelColor=0d1117)](https://github.com/Aaricacoding/TurtleAnimations)

**17 scripts and growing.** New animations, physics scenes, and fractal variations are added regularly.
Watch and ⭐ star the repo to be notified of every new drop.

</div>

---

## 🔭 Coming Soon

<div align="center">

| Category | Upcoming |
|:--------:|:---------|
| 🌿 **Fractals** | Dragon Curve · Koch Snowflake · Barnsley Fern · Sierpiński Triangle |
| 🧊 **3D Projections** | Rotating Wireframe Cube · Platonic Solids · Isometric Landscapes |
| 🎮 **Interactive** | Real-time Kaleidoscope · Gravity Well Painter |
| 🌊 **Physics** | Double Pendulum · Wave Interference · Lorenz Attractor |

</div>

---

## 🤝 Contributing

1. **Fork** the repository
2. Place new scripts in the correct category folder
3. Add a docstring describing the math used
4. Submit a pull request

Guidelines:
- ✅ Python `turtle` only — no external rendering libraries
- ✅ One self-contained `.py` file per animation
- ✅ Correct folder: `fractals/`, `interactive/`, `physics/`, or `projections/`
- ✅ Include the mathematical concept in a top-of-file comment

---

## 💫 Show Your Support

<div align="center">

**If TurtleAnimations inspired you, made you smile, or taught you something new —**

### ⭐ Please Star the Repo ⭐

*It helps others discover this project and motivates more art being made!*

[![Star this repo](https://img.shields.io/github/stars/Aaricacoding/TurtleAnimations?style=for-the-badge&logo=github&color=FFD700&labelColor=0d1117)](https://github.com/Aaricacoding/TurtleAnimations/stargazers)

</div>

---

## 📜 License

Licensed under the **MIT License** — see [LICENSE](LICENSE) for details.
Free to use, modify, share, and build upon. Just spread the beauty. 🎨

---

<div align="center">

*Made with* 🐢 *Python Turtle · Math · Love*

✦ *More animations loading...* ✦

*"Every pattern has a formula. Every formula has a soul."*

</div>
