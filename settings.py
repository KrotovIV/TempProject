import math
import pygame

# game settings
WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60
TILE = 100
FPS_POS = (WIDTH - 65, 5)

# labyrinth settings
STRAIGHT_PATH_COEFF = 3
PLAYER_TO_EXIT_LENGTH = 15
LABYRINTH_SIZE = (20, 20)

# texture settings
TEXTURE_WIDTH = 100
TEXTURE_HEIGHT = 100
TEXTURE_SCALE = TEXTURE_WIDTH // TILE

# ray casting settings
FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 300
DELTA_ANGLE = FOV / NUM_RAYS
DIST = NUM_RAYS / (2 * math.tan(HALF_FOV))
PTOJ_COEFF = 3 * DIST * TILE
SCALE = WIDTH // NUM_RAYS
POOL_SIZE = 5
TIME_TO_RETURN_FALSE = 5
TIMER_SECONDS = 0

# level num label
LEVEL_POS = (HALF_WIDTH // 1.5, HALF_HEIGHT // 1.5 + HEIGHT // 32)

# player settings
PLAYER_BASE_SPEED = 3
PLAYER_BASE_TURN_SPEED = 0.025

PLAYER_SPEED_MOD = 2
PLAYER_TURN_SPEED_MOD = 2

# keys
RUN_KEY = pygame.K_LSHIFT
GO_FORWARD_KEY = pygame.K_w
GO_BACK_KEY = pygame.K_s
GO_LEFT_KEY = pygame.K_a
GO_RIGHT_KEY = pygame.K_d
TURN_LEFT_KEY = pygame.K_LEFT
TURN_RIGHT_KEY = pygame.K_RIGHT
SKIP_LEVEL_KEY = pygame.K_c

# colors
COLORS = {
    "BLACK": (0, 0, 0),
    "WHITE": (255, 255, 255),
    "RED": (220, 0, 0),
    "GREEN": (0, 80, 0),
    "BLUE": (0, 0, 220),
    "DARKGREY": (110, 110, 110),
    "PURPLE": (120, 0, 120),
    "SKYBLUE": (0, 186, 255),
    "YELLOW": (220, 220, 0),
    "SANDY": (244, 164, 96),
    "GREY": (220, 220, 220)
}

# music
BG_MUSIC = 'sounds/bg-music.mp3'