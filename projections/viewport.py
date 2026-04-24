def world_to_screen(x, y, camera):
    sx = (x - camera.x) * camera.zoom
    sy = (y - camera.y) * camera.zoom
    return sx, sy