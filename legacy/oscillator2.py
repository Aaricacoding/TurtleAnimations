"""
oscillator.py
=============
Phyllotaxis Spiral Oscillator — neon green dots on black.
Recreates the breathing/rotating spiral wave animation.

Run:  python oscillator.py
"""

import turtle
import math

# ── Constants ──────────────────────────────────────────────────────────────────
NUM_PARTICLES  = 200
GOLDEN_ANGLE   = 137.508          # degrees — nature's perfect packing angle
BASE_RADIUS    = 6.0              # scale factor: radius = BASE_RADIUS * sqrt(i)
AMPLITUDE      = 38               # how far each dot pulses in/out (px)
PHASE_SHIFT    = 0.18             # radians between successive particles' phases
TIME_STEP      = 0.03             # animation speed (larger = faster)

# Colour palette: two-tone like the reference (bright white core → neon green rim)
def _particle_color(i, t):
    """Return an RGB tuple for particle i at time t."""
    # Brightness pulse: inner particles shimmer white, outer stay green
    wave = math.sin(t + i * PHASE_SHIFT)           # −1 … +1
    brightness = 0.45 + 0.55 * max(0.0, wave)      # 0.45 … 1.0

    # Inner ~30 particles get a white shimmer
    whiteness = max(0.0, 1.0 - i / 60.0) * brightness

    r = whiteness + (1.0 - whiteness) * 0.0         # green: no red channel
    g = whiteness + (1.0 - whiteness) * brightness  # full green
    b = whiteness + (1.0 - whiteness) * 0.15 * brightness  # tiny cyan hint
    return (min(r, 1.0), min(g, 1.0), min(b, 1.0))


# ── Screen setup ───────────────────────────────────────────────────────────────
screen = turtle.Screen()
screen.setup(700, 700)
screen.bgcolor("#000000")
screen.title("Oscillator — Phyllotaxis Spiral")
screen.tracer(0)                  # manual updates only
turtle.colormode(1.0)             # RGB floats 0–1


# ── Build particle pool ────────────────────────────────────────────────────────
particles = []
for i in range(NUM_PARTICLES):
    p = turtle.Turtle()
    p.hideturtle()
    p.speed(0)
    p.penup()
    p.shape("circle")
    # Dot size: inner particles larger, outer slightly smaller
    size = max(2, 9 - i // 30)
    p.shapesize(size / 10, size / 10)   # in turtle units (1 unit = 20px default)
    p.color("#00FF88")
    p.showturtle()
    particles.append(p)


# ── Pre-compute static Phyllotaxis angles ──────────────────────────────────────
#    Each particle sits at a fixed angle; only its radius oscillates.
phi_angles = [math.radians(i * GOLDEN_ANGLE) for i in range(NUM_PARTICLES)]


# ── Animation loop ─────────────────────────────────────────────────────────────
t = 0.0

while True:
    for i, p in enumerate(particles):
        # Oscillating radius — each particle breathes at a different phase
        r = BASE_RADIUS * math.sqrt(i + 1) + math.sin(t + i * PHASE_SHIFT) * AMPLITUDE

        angle = phi_angles[i]
        x = r * math.cos(angle)
        y = r * math.sin(angle)

        p.goto(x, y)

        # Dot size: pulse gently with the wave
        wave = math.sin(t + i * PHASE_SHIFT)
        sz = max(0.05, (0.25 + 0.15 * wave) * (1.0 - i / (NUM_PARTICLES * 1.6)))
        p.shapesize(sz, sz)

        # Two-tone colour
        p.color(_particle_color(i, t))

    screen.update()
    t += TIME_STEP