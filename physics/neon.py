class NeonRenderer:
    def __init__(self, turtle):
        self.t = turtle

    def draw(self, particle):
        # glow layers (fake blur)
        sizes = [6, 4, 2]
        alpha_colors = [particle.color, particle.color, "white"]

        for i in range(3):
            self.t.penup()
            self.t.goto(particle.x, particle.y)
            self.t.pendown()
            self.t.dot(sizes[i], alpha_colors[i])