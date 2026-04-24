from core.fractal_engine import julia
from core.renderer import Renderer
from core.config import Config

def run():
    renderer = Renderer()
    cfg = Config()

    c = complex(-0.7, 0.27015)  # classic Julia seed

    width = 300
    height = 300

    for x in range(-width, width, cfg.step):
        for y in range(-height, height, cfg.step):

            z = complex(
                (x * cfg.zoom) + cfg.center_x,
                (y * cfg.zoom) + cfg.center_y
            )

            m = julia(z, c, cfg.max_iter)

            shade = m / cfg.max_iter
            color = (shade, 0.3, 1 - shade)

            renderer.draw_point(x, y, color)

        renderer.update()

    renderer.update()
    renderer.done()


if __name__ == "__main__":
    run()