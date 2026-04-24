def perspective(x, y, depth):
    factor = 1 / (1 + depth * 0.01)
    return x * factor, y * factor
