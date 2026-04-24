import turtle

class Engine:
    def __init__(self, screen, turtle, renderer=None):
        self.screen = screen
        self.t = turtle
        self.objects = []
        self.renderer = renderer
        self.systems = []

    def add_system(self, sys):
        self.systems.append(sys)

    def add(self, obj):
        self.objects.append(obj)

    def update(self):

        self.t.clear()

        # apply systems
        for obj in self.objects:

            for sys in self.systems:
                if hasattr(sys, "attract"):
                    sys.attract(obj)

            obj.update()

            if obj.life > 0:

                # neon rendering if available
                if self.renderer:
                    self.renderer.draw(obj)
                else:
                    self.t.penup()
                    self.t.goto(obj.x, obj.y)
                    self.t.pendown()
                    self.t.dot(3, obj.color)

        self.objects = [o for o in self.objects if o.life > 0]

        self.screen.update()
        self.screen.ontimer(self.update, 16)