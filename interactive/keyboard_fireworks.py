import turtle
import random
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.tracer(0)

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

# ---------- FIREWORK PARTICLES ----------
particles = []

fx, fy = 0, 0

# ---------- MOVE ORIGIN ----------
def move(dx, dy):
    global fx, fy
    fx += dx
    fy += dy

# ---------- CREATE FIREWORK (FLOW VERSION) ----------
def spawn_firework():
    color = random.choice(["cyan", "white", "yellow", "red", "hotpink", "orange"])

    new_particles = []

    for angle in range(0, 360, 15):
        rad = math.radians(angle)

        new_particles.append({
            "x": fx,
            "y": fy,
            "vx": math.cos(rad) * random.uniform(1.5, 3.5),
            "vy": math.sin(rad) * random.uniform(1.5, 3.5),
            "life": 40,
            "color": color
        })

    particles.extend(new_particles)

# ---------- UPDATE LOOP (ANIMATION ENGINE) ----------
def update():
    t.clear()

    for p in particles:
        # motion update (THIS is the flow)
        p["x"] += p["vx"]
        p["y"] += p["vy"]

        # gravity effect (smooth arc feel)
        p["vy"] -= 0.03

        p["life"] -= 1

        if p["life"] > 0:
            t.penup()
            t.goto(p["x"], p["y"])
            t.pendown()
            t.dot(4, p["color"])

    # remove dead particles
    particles[:] = [p for p in particles if p["life"] > 0]

    screen.update()
    screen.ontimer(update, 16)

# ---------- KEY CONTROLS ----------

def space():
    spawn_firework()

def up():
    spawn_firework()
    move(0, 20)

def down():
    spawn_firework()
    move(0, -20)

def left():
    spawn_firework()
    move(-20, 0)

def right():
    spawn_firework()
    move(20, 0)

# ---------- BIND ----------
screen.listen()
screen.onkey(space, "space")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.onkey(left, "Left")
screen.onkey(right, "Right")

# ---------- START LOOP ----------
update()
turtle.done()