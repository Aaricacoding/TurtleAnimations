from turtle import *

# Speed up drawing by reducing animation delay
tracer(50)

# Start position slightly above center
setposition(0, 25)

# Set background color
bgcolor("black")

# Define the colors to alternate between
colors = ["yellow", "red",
          "yellow", "red"]

# Hide the turtle cursor for a clean look
hideturtle()

# Outer loop: repeat the pattern 80 times
for i in range(80):
    # Inner loop: cycle through the colors list
    for c in colors:
        color(c)                  # Set current color
        circle(175 - i, 100)      # Draw an arc of a circle
        left(90)                  # Turn left 90 degrees
        circle(175 - i, 100)      # Draw another arc
        right(60)                 # Turn right 60 degrees

# Finish drawing
done()
