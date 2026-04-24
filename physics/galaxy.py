import random
import math
from physics.particles import Particle

class Galaxy:
    def __init__(self, cx=0, cy=0):
        self.cx = cx
        self.cy = cy
        self.stars = []

    def spawn_star(self):
        angle = random.uniform(0, 2 * math.pi)
        radius = random.uniform(10, 200)

        x = self.cx + math.cos(angle) * radius
        y = self.cy + math.sin(angle) * radius

        # orbital velocity (key for galaxy effect)
        vx = -math.sin(angle) * 0.5
        vy = math.cos(angle) * 0.5

        color = random.choice(["white", "cyan", "yellow", "lightblue"])

        self.stars.append(Particle(x, y, vx, vy, color, life=9999))

    def update(self):
        for s in self.stars:
            dx = self.cx - s.x
            dy = self.cy - s.y

            # gravity pull to center
            s.vx += dx * 0.00005
            s.vy += dy * 0.00005

            s.update()