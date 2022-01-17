from settings import *
import pygame
import math


def mapping(x, y):
    """Return the corresponding tile position"""
    return (x // TILE) * TILE, (y // TILE) * TILE


class Player:
    def __init__(self, pos, world_map):
        self.world_map = world_map
        self.x, self.y = pos
        self.angle = PLAYER_ANGLE

    def pos(self):
        return self.x, self.y

    def movement(self):
        sin_a = math.sin(self.angle)
        cos_a = math.cos(self.angle)
        keys = pygame.key.get_pressed()

        speed = PLAYER_BASE_SPEED
        turn_speed = PLAYER_BASE_TURN_SPEED
        if keys[pygame.K_LSHIFT]:
            speed *= PLAYER_SPEED_MOD
            turn_speed *= PLAYER_TURN_SPEED_MOD

        delta_x = 0
        delta_y = 0
        if keys[pygame.K_w]:
            delta_x += speed * cos_a
            delta_y += speed * sin_a
        elif keys[pygame.K_s]:
            new_pos_delta = (cos_a, sin_a)
            delta_x += -speed * cos_a
            delta_y += -speed * sin_a
        if keys[pygame.K_a]:
            new_pos_delta = (cos_a, sin_a)
            delta_x += speed * sin_a
            delta_y += -speed * cos_a
        elif keys[pygame.K_d]:
            new_pos_delta = (cos_a, sin_a)
            delta_x += -speed * sin_a
            delta_y += speed * cos_a
        if keys[pygame.K_LEFT] or keys[pygame.K_q]:
            self.angle -= turn_speed
        elif keys[pygame.K_RIGHT] or keys[pygame.K_e]:
            self.angle += turn_speed

        new_x = self.x + delta_x
        new_y = self.y + delta_y

        # check collision
        if mapping(new_x, self.y) in self.world_map:
            new_x = self.x
        if mapping(self.x, new_y) in self.world_map:
            new_y = self.y

        self.x = new_x
        self.y = new_y
