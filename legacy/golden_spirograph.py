# File: golden_spirograph.py
# Description: Creates a flower-like spiro pattern with random colors
# using Python Turtle Graphics.

from turtle import *
from random import *

# Set up the drawing environment
speed(0)                  # Maximum drawing speed
bgcolor("black")          # Black background for contrast

# Define a list of colors to choose from randomly
colors = ["orange", "gold", "white"]

# Nested loops to build the orbit-flower pattern
for i in range(20):                 # Outer loop controls size growth
    for j in range(9):              # Middle loop controls repetitions
        for k in range(2):          # Inner loop draws paired arcs
            color(choice(colors))   # Randomly select a color each time
            circle(40 + i * 5, 90)  # Draw arc with increasing radius
            fd(100)                 # Move forward to extend shape
            lt(90)                  # Turn left to reposition
        rt(45)                      # Rotate to create orbit effect
    home()                          # Return to center before next set

done()                              # Finish drawing and keep window open
