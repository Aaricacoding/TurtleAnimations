import turtle

# --- Screen setup ---
screen = turtle.Screen()
screen.setup(1080, 1024)       # Set window size
screen.bgcolor("black")        # Background color is black

# --- Turtle setup ---
turtle.color("white")          # Initial turtle color
turtle.speed(1000)             # Very fast drawing speed

# --- Color counters ---
a = 1
b = 3
c = 1
r = 1
g = 1

# --- Drawing loop ---
for i in range(1000):
    # Change turtle color dynamically using r and g values
    turtle.color(r/5, g/25, 1)

    # Draw circles with varying radius and angles
    turtle.circle(1 * i, -30)   # Circle with radius increasing by i
    turtle.left(-200)           # Rotate left
    turtle.circle(-1 * i, -60)  # Circle in opposite direction
    turtle.right(-200)          # Rotate right
    turtle.circle(1, -90)       # Small circle
    turtle.circle(10, -90)      # Slightly larger circle

    # Update color counters for gradient effect
    r += 1
    if r == 6:                  # Reset after 5 steps
        r = 0
    g += 1
    if g == 26:                 # Reset after 25 steps
        g = 0

# Hide the turtle cursor at the end
turtle.hideturtle()
