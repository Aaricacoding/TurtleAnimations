import math

class InteractionSystem:
    def __init__(self):
        self.mouse_x = 0
        self.mouse_y = 0

    def update_mouse(self, x, y):
        self.mouse_x = x
        self.mouse_y = y

    def attract(self, particle):
        dx = self.mouse_x - particle.x
        dy = self.mouse_y - particle.y

        dist = math.sqrt(dx*dx + dy*dy)

        if dist < 150:
            particle.vx += dx * 0.001
            particle.vy += dy * 0.001

    def collide(self, p1, p2):
        dx = p1.x - p2.x
        dy = p1.y - p2.y
        dist = math.sqrt(dx*dx + dy*dy)

        if dist < 10:
            p1.vx, p2.vx = p2.vx, p1.vx
            p1.vy, p2.vy = p2.vy, p1.vy