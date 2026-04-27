# File: orbital_flower_pattern.py
# Description: Creates a colorful orbital flower animation
# using Python Turtle Graphics and HSV color cycling.

from turtle import *
import colorsys as cs

# Set up the drawing environment
bgcolor('black')       # Black background for contrast
tracer(20)             # Control update rate for smoother animation
pensize(4)             # Thickness of the drawing pen
h = 0                  # Initial hue value for color cycling

# Function to draw arcs with rotation
def draw(ang, n):
    circle(5 + n, 90)  # Draw an arc with radius adjusted by n
    left(ang)          # Rotate turtle by given angle
    circle(5 + n, 60)  # Draw another arc

# Move starting position slightly off-center
goto(-10, 0)

# Main loop to generate the flower-like orbital pattern
for i in range(700):
    c = cs.hsv_to_rgb(h, 1, 1)  # Convert HSV to RGB for color
    h += 0.005                  # Increment hue for smooth color transition
    color(c)                    # Set pen color

    up()                        # Lift pen to reposition without drawing
    draw(90, i / 5)             # Draw arcs with varying radius
    draw(180, i / 2)
    down()                      # Put pen down to draw

    fillcolor('black')          # Fill shapes with black for contrast
    begin_fill()
    draw(1 / 2, 0)
    draw(180, i / 2)
    draw(90, i / 2)
    end_fill()

    draw(60, i)                 # Additional arc for petal-like effect

done()                          # Finish drawing and keep window open
