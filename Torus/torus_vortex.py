import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Torus Vortex - Pulse + Star")
screen.setup(width=900, height=900)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def project_3d(x, y, z, scale, angle_x, angle_y):
    cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
    x_rot = x * cos_y + z * sin_y
    z_rot = -x * sin_y + z * cos_y
    
    cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
    y_rot = y * cos_x - z_rot * sin_x
    z_final = y * sin_x + z_rot * cos_x
    
    factor = scale / (scale + z_final)
    x_proj = x_rot * factor
    y_proj = y_rot * factor
    return x_proj, y_proj, z_final

def draw_torus(rotation_y, rotation_x, pulse_scale):
    """Main torus wireframe with pulse"""
    R = 120 * pulse_scale  # Pulse affects major radius
    r = 50 * pulse_scale   # Pulse affects minor radius
    scale = 300
    
    neon = "#00D4FF"
    cyan = "#00FFFF"
    
    # Wireframe grid
    for i in range(0, 360, 12):
        pen.color(neon)
        pen.pensize(1)
        pen.penup()
        first = True
        for j in range(0, 361, 10):
            u = math.radians(i)
            v = math.radians(j)
            x = (R + r * math.cos(v)) * math.cos(u)
            y = (R + r * math.cos(v)) * math.sin(u)
            z = r * math.sin(v)
            px, py, pz = project_3d(x, y, z, scale, rotation_x, rotation_y)
            
            if first:
                pen.goto(px, py)
                pen.pendown()
                first = False
            else:
                pen.goto(px, py)
    
    for j in range(0, 360, 15):
        pen.color(neon)
        pen.pensize(1)
        pen.penup()
        first = True
        for i in range(0, 361, 10):
            u = math.radians(i)
            v = math.radians(j)
            x = (R + r * math.cos(v)) * math.cos(u)
            y = (R + r * math.cos(v)) * math.sin(u)
            z = r * math.sin(v)
            px, py, pz = project_3d(x, y, z, scale, rotation_x, rotation_y)
            
            if first:
                pen.goto(px, py)
                pen.pendown()
                first = False
            else:
                pen.goto(px, py)
    
    # Grid intersection dots
    for i in range(0, 360, 24):
        for j in range(0, 360, 30):
            u = math.radians(i)
            v = math.radians(j)
            x = (R + r * math.cos(v)) * math.cos(u)
            y = (R + r * math.cos(v)) * math.sin(u)
            z = r * math.sin(v)
            px, py, pz = project_3d(x, y, z, scale, rotation_x, rotation_y)
            
            brightness = 0.4 + 0.6 * (pz + 200) / 400
            pen.color(cyan)
            pen.penup()
            pen.goto(px, py)
            pen.dot(int((3 + 3 * brightness) * pulse_scale))

def draw_center_star(rotation, pulse_scale):
    """8-point star in center hole of torus"""
    neon = "#00D4FF"
    white = "#FFFFFF"
    
    # Star scales with pulse and rotates
    star_size = 25 * pulse_scale
    
    for i in range(8):
        angle = i * 45 + rotation * 4 # Spins fast
        angle_rad = math.radians(angle)
        
        # Inner point
        x1 = (star_size * 0.4) * math.cos(angle_rad)
        y1 = (star_size * 0.4) * math.sin(angle_rad)
        
        # Outer point
        x2 = star_size * math.cos(angle_rad)
        y2 = star_size * math.sin(angle_rad)
        
        # Draw ray with glow
        pen.color(neon)
        pen.pensize(3)
        pen.penup()
        pen.goto(0, 0)
        pen.pendown()
        pen.goto(x2, y2)
        
        pen.color(white)
        pen.pensize(1)
        pen.penup()
        pen.goto(x1, y1)
        pen.pendown()
        pen.goto(x2, y2)
    
    # Center dot
    pen.penup()
    pen.goto(0, 0)
    pen.color(white)
    pen.dot(int(8 * pulse_scale))

def draw_spiral_trail(angle_offset, rotation, pulse_scale):
    neon = "#00D4FF"
    cyan = "#00BFFF"
    
    for arm in range(8):
        base_angle = arm * 45 + angle_offset
        for t in range(30):
            radius = (180 + t * 8) * pulse_scale # Spirals also pulse
            angle = math.radians(base_angle + t * 8 + rotation * 2)
            
            wave = 20 * math.sin(math.radians(t * 15 + rotation * 4))
            x = (radius + wave) * math.cos(angle)
            y = (radius + wave) * math.sin(angle)
            
            size = int((6 - t * 0.15) * pulse_scale)
            if size < 1: size = 1
            
            pen.penup()
            pen.goto(x, y)
            pen.color(cyan)
            pen.dot(size)

def draw_ornaments(rotation, pulse_scale):
    neon = "#00D4FF"
    
    # Top-left spiral ornaments
    for i, pos in enumerate([(-250, 200), (-200, 250)]):
        cx, cy = pos
        for j in range(8):
            angle = j * 45 + rotation * 3 + i * 30
            x = cx + 25 * math.cos(math.radians(angle))
            y = cy + 25 * math.sin(math.radians(angle))
            pen.penup()
            pen.goto(x, y)
            pen.color(neon)
            pen.dot(int(3 * pulse_scale))
    
    # Bottom-right burst
    cx, cy = 220, -180
    for i in range(24):
        angle = i * 15 + rotation
        for r in range(0, 60, 8):
            x = cx + r * pulse_scale * math.cos(math.radians(angle))
            y = cy + r * pulse_scale * math.sin(math.radians(angle))
            pen.penup()
            pen.goto(x, y)
            pen.color(neon)
            pen.dot(int((4 - r * 0.05) * pulse_scale))

def draw_frame(frame):
    pen.clear()
    rot_y = math.radians(frame * 1.0)
    rot_x = math.radians(20 + 10 * math.sin(frame * 0.02))
    
    # PULSE: 0.85 to 1.15 scale breathing
    pulse_scale = 1.0 + 0.15 * math.sin(math.radians(frame * 4))
    
    draw_spiral_trail(0, frame, pulse_scale)
    draw_torus(rot_y, rot_x, pulse_scale)
    draw_center_star(frame, pulse_scale)
    draw_ornaments(frame, pulse_scale)

# Animate: rotating + pulsing torus with star
for frame in range(720):
    draw_frame(frame)
    screen.update()

print("Torus Vortex complete. Click to exit.")
screen.exitonclick()