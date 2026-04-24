from core.fractal_engine import mandelbrot
from core.renderer import Renderer
from core.config import Config

def run():
    renderer = Renderer()
    cfg = Config()

    width = 300
    height = 300

    for x in range(-width, width, cfg.step):
        for y in range(-height, height, cfg.step):

            # map screen → complex plane
            c = complex(
                (x * cfg.zoom) + cfg.center_x,
                (y * cfg.zoom) + cfg.center_y
            )

            m = mandelbrot(c, cfg.max_iter)

            shade = m / cfg.max_iter
            color = (shade, shade, shade)

            renderer.draw_point(x, y, color)

        renderer.update()

    renderer.update()
    renderer.done()


if __name__ == "__main__":
    run()