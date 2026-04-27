import turtle
import math
import random

screen = turtle.Screen()
screen.bgcolor("#0A0E27") # Deep navy night
screen.title("Aurora Dots - Motion")
screen.setup(width=900, height=900)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

# Store star positions so they don't flicker
stars = [(random.randint(-440, 440), random.randint(-440, 440), 
          random.randint(1, 3)) for _ in range(150)]

def aurora_wave(x_base, y_base, width, height, color, phase, wave_id):
    """Draw one aurora curtain using dots"""
    pen.color(color)
    
    # Dots density: more at bottom, sparse at top = curtain effect
    for x in range(int(x_base), int(x_base + width), 8):
        # Wave equation for aurora flow
        wave1 = math.sin((x * 0.02) + phase + wave_id) 
        wave2 = math.sin((x * 0.01) + phase * 0.7 + wave_id * 2)
        wave3 = math.sin((x * 0.03) - phase * 0.5 + wave_id)
        
        # Combined waves create organic curtain shape
        y_offset = (wave1 * 40 + wave2 * 60 + wave3 * 30)
        base_y = y_base + y_offset
        
        # Curtain height varies - taller in some spots
        curtain_height = height * (0.5 + 0.5 * math.sin((x * 0.015) + phase))
        
        # Draw vertical line of dots - denser at bottom
        dots = int(curtain_height / 6)
        for i in range(dots):
            # Dot spacing gets wider toward top
            t = i / dots
            y = base_y + (curtain_height * t * t) # Quadratic = sparse top
            
            # Dot size fades toward top
            size = int(5 * (1 - t * 0.8))
            if size < 1: size = 1
            
            # Shimmer: random brightness
            if random.random() > 0.1:
                pen.penup()
                pen.goto(x, y)
                pen.dot(size)

def draw_stars(phase):
    """Twinkling stars background"""
    pen.color("white")
    for x, y, base_size in stars:
        # Twinkle effect
        twinkle = 0.5 + 0.5 * math.sin(phase * 2 + x * 0.1 + y * 0.1)
        size = int(base_size * twinkle)
        if size > 0:
            pen.penup()
            pen.goto(x, y)
            pen.dot(size)

def draw_frame(phase):
    pen.clear()
    
    # 1. Stars first
    draw_stars(phase)
    
    # 2. Aurora layers - back to front
    # Blue aurora - bottom
    aurora_wave(-450, -200, 900, 180, "#00BFFF", phase, 0)
    
    # Cyan aurora - middle  
    aurora_wave(-450, -50, 900, 160, "#00CED1", phase * 1.2, 1)
    
    # Magenta aurora - top
    aurora_wave(-450, 100, 900, 150, "#FF1493", phase * 0.8, 2)
    
    # White aurora wisps - top left
    aurora_wave(-450, 250, 300, 80, "#F0F8FF", phase * 1.5, 3)

# Animate: flowing aurora
for frame in range(600):
    phase = frame * 0.08 # Flow speed
    draw_frame(phase)
    screen.update()

print("Aurora complete. Click to exit.")
screen.exitonclick()