import random
import math
from particles import Particle

def firework(x, y, color=None):
    if not color:
        color = random.choice(["red", "cyan", "yellow", "white", "hotpink"])

    particles = []

    for angle in range(0, 360, 15):
        rad = math.radians(angle)

        vx = math.cos(rad) * random.uniform(1.5, 3.5)
        vy = math.sin(rad) * random.uniform(1.5, 3.5)

        particles.append(Particle(x, y, vx, vy, color, life=60))

    return particles