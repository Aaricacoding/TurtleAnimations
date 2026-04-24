import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# 🎨 unique color palette per character group
colors = {
    "a": "red", "b": "orange", "c": "yellow", "d": "green",
    "e": "cyan", "f": "blue", "g": "purple", "h": "pink",
    "i": "white", "j": "gold", "k": "lime", "l": "magenta",
    "m": "coral", "n": "teal", "o": "violet", "p": "skyblue",
    "q": "crimson", "r": "springgreen", "s": "deepskyblue",
    "t": "hotpink", "u": "orange", "v": "lightgreen",
    "w": "lightblue", "x": "white", "y": "yellow", "z": "purple"
}

def clear_and_draw(char):
    t.clear()

    char = char.lower()

    # fallback color
    color = colors.get(char, "white")
    t.color(color)

    # convert character → math seed
    seed = ord(char)

    # UNIQUE curve per letter
    a = (seed % 7) + 2
    b = (seed % 5) + 3
    delta = seed % 180

    # draw curve
    for i in range(0, 360, 2):
        x = 150 * math.sin(math.radians(a * i + delta))
        y = 150 * math.cos(math.radians(b * i))

        t.goto(x, y)
        t.dot(3, color)

# handle keyboard input
def handle_key(char):
    clear_and_draw(char)

# bind A–Z
for c in "abcdefghijklmnopqrstuvwxyz":
    screen.onkey(lambda c=c: handle_key(c), c)

screen.listen()

# default
clear_and_draw("a")

turtle.done()