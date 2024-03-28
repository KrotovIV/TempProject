from settings import *
from player import Player
from map import Map
from drawing import Drawing
from movement import Movement
from controller import Controller
import pygame
import time


if __name__ == "__main__":
    pygame.init()

    pygame.mixer.music.load(BG_MUSIC)
    pygame.mixer.music.set_volume(0.05)
    pygame.mixer.music.play(loops=999999)


    screen = pygame.display.set_mode((WIDTH, HEIGHT))

    map = Map()

    controller = Controller()

    movement = Movement(controller)

    drawing = Drawing(screen, controller)

    drawing.menu()

    clock = pygame.time.Clock()

    level_num = 0
    while True:

        # labyrinth size increases every level
        LABYRINTH_SIZE = (LABYRINTH_SIZE[0] + 2, LABYRINTH_SIZE[1] + 2)
        world_map, player_pos = map.build_labyrinth(LABYRINTH_SIZE)
        
        player = Player(player_pos)

        level_num += 1
        drawing.level(level_num)
        pygame.display.flip()
        time.sleep(1)


        # game process
        running = True
        while running:
            events = pygame.event.get()

            controller.handle_quit(events)

            # if player skipped level
            if (controller.level_skipped(events)):
                running = False
            
            # if player reached exit
            if not movement.move_player(player, world_map):
                running = False

            
            drawing.background(player.angle)
            drawing.world(player.pos, player.angle, world_map)
            drawing.fps(clock)

            pygame.display.flip()
            clock.tick(FPS)
