import pygame

def parse_textures():
    # key = symbol in text map
    textures = {
    "1": pygame.image.load("img/wall_1.png").convert(),
    "2": pygame.image.load("img/wall_2.png").convert(),
    "S": pygame.image.load("img/sky.png").convert(),
    "E": pygame.image.load("img/exit.png").convert(),
    }
    return textures