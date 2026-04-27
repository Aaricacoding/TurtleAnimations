import turtle
import math

screen = turtle.Screen()
screen.bgcolor("#0A0510") # Deep purple-black for glow
screen.title("Torus / Lotus of Life - Motion")
screen.setup(width=800, height=800)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def draw_glow_circle(x, y, r, rotation):
    """Draw one circle with outer glow + inner bright line"""
    # Outer glow - thick faint gold
    pen.color("#FFD700")
    pen.pensize(4)
    pen.penup()
    pen.goto(x, y - r)
    pen.setheading(0)
    pen.pendown()
    pen.circle(r)
    
    # Inner bright core - thin white-gold
    pen.color("#FFF8DC")
    pen.pensize(2)
    pen.penup()
    pen.goto(x, y - r)
    pen.setheading(0)
    pen.pendown()
    pen.circle(r)

def draw_torus_lotus(rotation, pulse):
    """Overlapping circles forming torus pattern"""
    num_circles = 24 # Number of circles in the torus
    radius = 120 * pulse # Radius of each circle
    torus_radius = 100 # Distance from center to circle centers
    
    # Rotate the whole pattern
    rot_rad = math.radians(rotation)
    
    for i in range(num_circles):
        angle = (i / num_circles) * 360
        angle_rad = math.radians(angle)
        
        # Position circle on torus ring
        cx = torus_radius * math.cos(angle_rad)
        cy = torus_radius * math.sin(angle_rad)
        
        # Apply global rotation
        rx = cx * math.cos(rot_rad) - cy * math.sin(rot_rad)
        ry = cx * math.sin(rot_rad) + cy * math.cos(rot_rad)
        
        draw_glow_circle(rx, ry, radius, rotation)

def draw_center_star(phase, pulse):
    """Bright center star like your image"""
    # Outer glow
    pen.penup()
    pen.goto(0, 0)
    pen.color("#FFD700")
    pen.dot(int(40 * pulse))
    
    # Inner bright core
    pen.color("#FFFFFF")
    pen.dot(int(20 * pulse))
    
    # Rays
    for i in range(8):
        angle = i * 45 + phase * 2
        angle_rad = math.radians(angle)
        
        pen.color("#FFD700")
        pen.pensize(3)
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        pen.goto(60 * pulse * math.cos(angle_rad), 60 * pulse * math.sin(angle_rad))
        
        pen.color("#FFFFFF")
        pen.pensize(1)
        pen.penup()
        pen.goto(20 * math.cos(angle_rad), 20 * math.sin(angle_rad))
        pen.pendown()
        pen.goto(60 * pulse * math.cos(angle_rad), 60 * pulse * math.sin(angle_rad))

def draw_frame(frame):
    pen.clear()
    
    # Rotation + breathing pulse
    rotation = frame * 0.5
    pulse = 1.0 + 0.1 * math.sin(math.radians(frame * 3))
    
    # Draw torus/lotus pattern
    draw_torus_lotus(rotation, pulse)
    
    # Draw center star
    draw_center_star(frame, pulse)
    
    # Label
    pen.penup()
    pen.goto(0, -300)
    pen.color("#FFD700")
    pen.write("TORUS / LOTUS OF LIFE", align="center", font=("Arial", 18, "bold"))

# Animate: rotating + pulsing lotus
for frame in range(720):
    draw_frame(frame)
    screen.update()

print("Torus Lotus complete. Click to exit.")
screen.exitonclick()