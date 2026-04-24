from turtle import *
from colorsys import hsv_to_rgb   # Import function to convert HSV colors to RGB

# Use normalized color mode (0.0–1.0 instead of 0–255)
colormode(1.0)

# Move turtle to starting position
penup()
setposition(0, 0)
pendown()

# Set drawing speed and background
speed(0)                # Fastest speed
bgcolor('black')        # Black background
pensize(3)              # Line thickness

# Number of iterations and initial hue value
n = 100
h = 0                   # Hue starts at 0 (red in HSV)

# Outer loop: repeat the whole pattern 120 times
for j in range(120):        
    # Inner loop: draw 4 arcs per iteration
    for i in range(4):      
        color(hsv_to_rgb(h, 1, 1))   # Convert HSV to RGB for rainbow effect
        h += 0.003                   # Slightly shift hue each step for smooth color transition
        circle(40 + i * 5, 90)       # Draw quarter circle with increasing radius
        forward(250)                 # Move forward to extend the pattern
        left(90)                     # Turn left to change direction
    rt(10)                           # Rotate right 10° after each outer loop to create spiral effect

# Hide turtle cursor and finish
hideturtle()
done()
