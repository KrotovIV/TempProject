import pygame
from settings import *
from player import Player
import math
from map import Map
from drawing import Drawing
import time



if __name__ == "__main__":
    pygame.init()

    pygame.mixer.music.load('sounds/bg-music.mp3')
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(loops=999999)



    sc = pygame.display.set_mode((WIDTH, HEIGHT))
    level = 0
    while True:
        LABYRINTH_SIZE = (LABYRINTH_SIZE[0] + 2, LABYRINTH_SIZE[1] + 2)
        map_ = Map()
        world_map, player_pos = map_.labyrinth(LABYRINTH_SIZE)
        level += 1
        clock = pygame.time.Clock()
        drawing = Drawing(sc, world_map)
        if level == 1:
            while True:
                if not drawing.menu():
                    break
        drawing.level(level)
        pygame.display.flip()
        time.sleep(1)
        player = Player(player_pos, world_map)
        running = True

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
                if event.type == pygame.KEYDOWN:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_c]:
                        running = False



            player.movement()
            sc.fill(GREY)

            drawing.background(player.angle)
            if drawing.world(player.pos(), player.angle) is False:
                running = False
            drawing.fps(clock)

            pygame.display.flip()
            clock.tick(FPS)
