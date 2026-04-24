import random

class Forces:
    def __init__(self):
        self.gravity = -0.03
        self.wind = 0

    def apply_gravity(self, particle):
        particle.vy += self.gravity

    def apply_wind(self, particle):
        particle.vx += self.wind

    def random_wind(self):
        self.wind = random.uniform(-0.02, 0.02)