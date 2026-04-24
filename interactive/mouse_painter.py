import turtle
import time

screen = turtle.Screen()
screen.bgcolor("white")
screen.tracer(0)

t = turtle.Turtle()
t.speed(0)
t.pensize(3)
t.hideturtle()

# ---------- COLORS ----------
colors = [
    "red", "navy", "cyan", "yellow", "hotpink",
    "lightgreen", "brown", "black", "lavender",
    "olive", "orange", "purple"
]

color_index = 0

drawing = False

# ---------- DOUBLE TAP DETECTOR ----------
last_tap_time = 0

def change_color():
    global color_index
    color_index = (color_index + 1) % len(colors)
    t.color(colors[color_index])

# ---------- START DRAW ----------
def start(x, y):
    global drawing
    drawing = True

    t.penup()
    t.goto(x, y)
    t.pendown()

# ---------- STOP DRAW (IMPORTANT FIX) ----------
def stop(x, y):
    global drawing
    drawing = False
    t.penup()   # THIS BREAKS THE LINE

# ---------- DRAW ----------
def draw(x, y):
    if drawing:
        t.goto(x, y)

# ---------- TOUCHPAD CLICK HANDLER ----------
def click(x, y):
    global last_tap_time

    now = time.time()

    # if two clicks within 0.4 sec → treat as double tap
    if now - last_tap_time < 0.4:
        change_color()
        last_tap_time = 0
    else:
        start(x, y)
        last_tap_time = now

# ---------- BIND EVENTS ----------
screen.onscreenclick(click, 1)   # left click / tap
screen.onscreenclick(stop, 3)    # right click (extra safety fallback)

# motion tracking
screen.getcanvas().bind("<Motion>", lambda e: draw(e.x - 400, 300 - e.y))

# ---------- LOOP ----------
def loop():
    screen.update()
    screen.ontimer(loop, 10)

loop()
turtle.done()