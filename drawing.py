from settings import *
from ray_casting import ray_casting
from textures import parse_textures
import pygame

class Drawing:
    def __init__(self, screen, controller):
        self.screen = screen
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        self.font2 = pygame.font.SysFont("bell", 136, bold=True)
        self.textures = parse_textures()
        self.controller = controller

    def background(self, angle):
        # sky
        sky_offset = -5 * math.degrees(angle) % WIDTH
        self.screen.blit(self.textures["S"], (sky_offset, 0))
        self.screen.blit(self.textures["S"], (sky_offset - WIDTH, 0))
        self.screen.blit(self.textures["S"], (sky_offset + WIDTH, 0))

        # ground
        pygame.draw.rect(
            self.screen, COLORS["DARKGREY"], (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT)
        )

    def world(self, player_pos, player_angle, world_map):
        ray_casting(
            self.screen,
            player_pos,
            player_angle,
            self.textures,
            world_map,
        )

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, False, COLORS["RED"])
        self.screen.blit(render, FPS_POS)

    def level(self, level):
        self.screen.fill(COLORS["GREY"])
        display_level = "level " + str(level)
        render = self.font2.render(display_level, False, COLORS["GREEN"])
        self.screen.blit(render, LEVEL_POS)

    def menu(self):
        self.screen.fill(COLORS["GREEN"])
        rect = pygame.Rect(*self.screen.get_rect().center, 0, 0).inflate(200, 100)

        display = "LABYRINTH"
        render = self.font2.render(display, False, COLORS["YELLOW"])
        self.screen.blit(render, (120, 100))

        while True:
            events = pygame.event.get()

            self.controller.handle_quit(events)

            if self.controller.collide_with_mouse(rect):
                color = (255, 0, 0)
                if (self.controller.left_mousebutton_pressed(events)):
                    return False
            else:
                color = (255, 255, 255)

            pygame.draw.rect(self.screen, color, rect)

            display = "Играть"
            render = self.font.render(display, False, COLORS["BLACK"])
            self.screen.blit(render, (540, 380))

            pygame.display.flip()
