import math
from turtle import *

# Define the parametric equations for the heart curve
def hearta(k):
    # X-coordinate of the heart
    return 15 * math.sin(k) ** 3

def heartb(k):
    # Y-coordinate of the heart
    return (12 * math.cos(k)
            - 5 * math.cos(2 * k)
            - 2 * math.cos(3 * k)
            - math.cos(4 * k))

# Set turtle speed (1000 is very fast)
speed(1000)

# Set background color to black
bgcolor("black")

# Main loop to draw the heart
for i in range(6000):  # Loop 6000 times to plot points
    # Move turtle to the calculated (x, y) position
    goto(hearta(i) * 20, heartb(i) * 20)

    # Inner loop (not really needed, but sets the color repeatedly)
    for j in range(5):
        color("#f73487")  # Pinkish-red color for the heart

    # Return to the center after each point
    goto(0, 0)

# Finish drawing
done()
