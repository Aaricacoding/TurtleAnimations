import turtle
import math

screen = turtle.Screen()
screen.bgcolor("#0A0A1A") # Dark indigo
screen.title("Star Tetrahedron - Building Motion")
screen.setup(width=800, height=800)
screen.tracer(0)

pen = turtle.Turtle()
pen.hideturtle()
pen.speed(0)

def project_3d(x, y, z, scale, angle_y, angle_x):
    """3D to 2D with rotation"""
    # Y rotation
    cos_y, sin_y = math.cos(angle_y), math.sin(angle_y)
    x_rot = x * cos_y + z * sin_y
    z_rot = -x * sin_y + z * cos_y
    
    # X rotation
    cos_x, sin_x = math.cos(angle_x), math.sin(angle_x)
    y_rot = y * cos_x - z_rot * sin_x
    z_final = y * sin_x + z_rot * cos_x
    
    factor = scale / (scale + z_final)
    return x_rot * factor, y_rot * factor, z_final

def draw_glow_line(x1, y1, x2, y2, color, pulse):
    """Line with glow effect"""
    # Outer glow
    pen.color(color)
    pen.pensize(int(4 * pulse))
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)
    
    # Inner bright
    pen.color("#FFFFFF")
    pen.pensize(int(2 * pulse))
    pen.penup()
    pen.goto(x1, y1)
    pen.pendown()
    pen.goto(x2, y2)

def get_tetrahedron_points(size, invert=False):
    """4 vertices of tetrahedron. invert=True flips it"""
    h = size * math.sqrt(2/3)
    if invert:
        # Downward tetrahedron
        return [
            (0, -h, 0),
            (size, h/3, 0),
            (-size/2, h/3, size*math.sqrt(3)/2),
            (-size/2, h/3, -size*math.sqrt(3)/2)
        ]
    else:
        # Upward tetrahedron
        return [
            (0, h, 0),
            (size, -h/3, 0),
            (-size/2, -h/3, size*math.sqrt(3)/2),
            (-size/2, -h/3, -size*math.sqrt(3)/2)
        ]

def draw_frame(frame):
    pen.clear()
    
    # Animation timing
    build_phase = min(frame / 180, 1.0) # 0 to 1 over first 180 frames
    rotation_y = math.radians(frame * 0.8)
    rotation_x = math.radians(20 + 15 * math.sin(frame * 0.015))
    pulse = 1.0 + 0.12 * math.sin(math.radians(frame * 3))
    
    scale = 250
    size = 150
    
    # Colors: upward = cyan, downward = gold
    cyan = "#00FFFF"
    gold = "#FFD700"
    
    # Get both tetrahedrons
    tetra_up = get_tetrahedron_points(size, invert=False)
    tetra_down = get_tetrahedron_points(size, invert=True)
    
    # Project to 2D
    proj_up = [project_3d(x, y, z, scale, rotation_y, rotation_x) for x, y, z in tetra_up]
    proj_down = [project_3d(x, y, z, scale, rotation_y, rotation_x) for x, y, z in tetra_down]
    
    # BUILD ANIMATION: draw edges one by one
    edges_up = [(0,1), (0,2), (0,3), (1,2), (2,3), (3,1)]
    edges_down = [(0,1), (0,2), (0,3), (1,2), (2,3), (3,1)]
    
    total_edges = len(edges_up) + len(edges_down)
    edges_to_draw = int(total_edges * build_phase)
    
    # Draw upward tetrahedron edges
    for i, (a, b) in enumerate(edges_up):
        if i < edges_to_draw:
            x1, y1, z1 = proj_up[a]
            x2, y2, z2 = proj_up[b]
            draw_glow_line(x1, y1, x2, y2, cyan, pulse)
    
    # Draw downward tetrahedron edges
    for i, (a, b) in enumerate(edges_down):
        if i + len(edges_up) < edges_to_draw:
            x1, y1, z1 = proj_down[a]
            x2, y2, z2 = proj_down[b]
            draw_glow_line(x1, y1, x2, y2, gold, pulse)
    
    # Draw vertices as glowing dots
    all_points = proj_up + proj_down
    for i, (x, y, z) in enumerate(all_points):
        brightness = 0.5 + 0.5 * (z + 200) / 400 # Depth shading
        size_dot = int((6 + 4 * brightness) * pulse)
        
        pen.penup()
        pen.goto(x, y)
        pen.color(cyan if i < 4 else gold)
        pen.dot(size_dot)
        pen.color("#FFFFFF")
        pen.dot(int(size_dot * 0.5))
    
    # Label only after build complete
    if build_phase >= 1.0:
        pen.penup()
        pen.goto(0, -280)
        pen.color("#FFFFFF")
        pen.write("STAR TETRAHEDRON", align="center", font=("Arial", 18, "bold"))

# Animate: builds over 180 frames, then spins + pulses
for frame in range(720):
    draw_frame(frame)
    screen.update()

print("Merkaba complete. Click to exit.")
screen.exitonclick()