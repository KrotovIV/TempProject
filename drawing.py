import pygame
from settings import *
from ray_casting import ray_casting


class Drawing:
    def __init__(self, sc, world_map):
        self.world_map = world_map
        self.sc = sc
        self.font = pygame.font.SysFont("Arial", 36, bold=True)
        self.font2 = pygame.font.SysFont("bell", 136, bold=True)
        self.textures = {
            "1": pygame.image.load("img/1.png").convert(),
            "2": pygame.image.load("img/2.png").convert(),
            "S": pygame.image.load("img/sky.png").convert(),
            'E':pygame.image.load("img/E.png").convert()
        }

    def background(self, angle):
        # sky
        sky_offset = -5 * math.degrees(angle) % WIDTH
        self.sc.blit(self.textures["S"], (sky_offset, 0))
        self.sc.blit(self.textures["S"], (sky_offset - WIDTH, 0))
        self.sc.blit(self.textures["S"], (sky_offset + WIDTH, 0))
        # ground
        pygame.draw.rect(
            self.sc, DARKGREY, (0, HALF_HEIGHT, WIDTH, HALF_HEIGHT)
        )

    def world(self, player_pos, player_angle):
        if ray_casting(self.sc, player_pos, player_angle, self.textures, self.world_map) is False:
            return False

    def fps(self, clock):
        display_fps = str(int(clock.get_fps()))
        render = self.font.render(display_fps, False, RED)
        self.sc.blit(render, FPS_POS)

    def level(self, level):
        self.sc.fill(GREY)
        display_level = 'level ' + str(level)
        render = self.font2.render(display_level, False, GREEN)
        self.sc.blit(render, LEVEL_POS)

    def menu(self):
        self.sc.fill(GREEN)
        rect = pygame.Rect(*self.sc.get_rect().center, 0, 0).inflate(200, 100)

        display= 'LABYRINTH'
        render = self.font2.render(display, False, YELLOW)
        self.sc.blit(render, (120, 100))

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()

                collide = rect.collidepoint(pygame.mouse.get_pos())
                if collide:
                    color = (255, 0, 0)
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:
                            return False
                if not collide:
                    color = (255, 255, 255)

            pygame.draw.rect(self.sc, color, rect)

            display = 'Играть '
            render = self.font.render(display, False, BLACK)
            self.sc.blit(render, (540, 380))

            pygame.display.flip()
