# File: rainbow_starburst_orbit.py
# Description: Creates a rainbow starburst animation with orbit-like motion
# using Python Turtle Graphics and HSV color cycling.

from turtle import *
from colorsys import *

# Set up the drawing environment
bgcolor('black')       # Black background for contrast
speed(0)               # Maximum drawing speed
tracer(200)            # Control update rate for smooth animation
h = 0                  # Initial hue value for rainbow colors

# Move starting position slightly off-center
goto(150, 50)

# Main loop to generate the animation
for i in range(10000):
    # Convert HSV to RGB for rainbow effect
    color(hsv_to_rgb(h, 1, 1))
    
    # Inner loop to draw rotating starburst lines
    for j in range(75):
        h += 0.005          # Increment hue for smooth color transition
        fd(100)             # Draw forward line
        bk(100)             # Move back to center
        rt(2)               # Rotate slightly to create circular pattern
    
    # Step forward to create orbit-like motion
    fd(250)

# Finish drawing
done()
