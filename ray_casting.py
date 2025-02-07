from settings import *
from tools import *
import pygame
import math


def ray_casting(sc, player_pos, player_angle, textures, world_map):
    # ERROR IS HERE!!!!!
    ox, oy = player_pos
    xm, ym = mapping(ox, oy)
    cur_angle = player_angle - HALF_FOV
    for ray in range(NUM_RAYS):
        texture_v, texture_h = " ", " "
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)

        # vertical
        x, dx = (xm + TILE, 1) if cos_a >= 0 else (xm, -1)
        depth_v = 0
        yv = 0
        for i in range(0, 4000, TILE):
            depth_v = (x - ox) / cos_a
            yv = oy + depth_v * sin_a
            tile_v = mapping(x + dx, yv)
            if tile_v in world_map:
                texture_v = world_map[tile_v]
                break
            x += dx * TILE

        # horizontal
        y, dy = (ym + TILE, 1) if sin_a >= 0 else (ym, -1)
        depth_h = 0
        xh = 0
        for i in range(0, 4000, TILE):
            depth_h = (y - oy) / sin_a
            xh = ox + depth_h * cos_a
            tile_h = mapping(xh, y + dy)
            if tile_h in world_map:
                texture_h = world_map[tile_h]
                break
            y += dy * TILE

        # projection
        depth, offset, texture = (
            (depth_v, yv, texture_v)
            if depth_v < depth_h
            else (depth_h, xh, texture_h)
        )

        offset = int(offset) % TILE
        depth *= math.cos(player_angle - cur_angle)
        depth = max(depth, 0.00001)
        proj_height = min(int(PTOJ_COEFF / depth), 2 * HEIGHT)

        wall_column = textures[texture].subsurface(
            offset * TEXTURE_SCALE, 0, TEXTURE_SCALE, TEXTURE_HEIGHT
        )
        wall_column = pygame.transform.scale(wall_column, (SCALE, proj_height))
        sc.blit(wall_column, (ray * SCALE, HALF_HEIGHT - proj_height // 2))

        cur_angle += DELTA_ANGLE
