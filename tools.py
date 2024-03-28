from settings import *

def mapping(x, y):
    # the corresponding tile position
    return (x // TILE) * TILE, (y // TILE) * TILE