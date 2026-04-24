class Particle:
    def __init__(self, x, y, vx, vy, color, life=50):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.color = color
        self.life = life

    def update(self, forces=None):
        if forces:
            forces.apply_gravity(self)
            forces.apply_wind(self)

        self.x += self.vx
        self.y += self.vy
        self.life -= 1