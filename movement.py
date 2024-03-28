from settings import *
from tools import *
import math

class Movement:
    def __init__(self, controller):
        self.controller = controller

    def move_player(self, player, world_map):
        angle = player.angle
        x, y = player.pos

        sin_a = math.sin(angle)
        cos_a = math.cos(angle)

        keys = self.controller.handle_player_movement()

        speed = PLAYER_BASE_SPEED
        turn_speed = PLAYER_BASE_TURN_SPEED
        if keys["RUN_KEY_PRESSED"]:
            speed *= PLAYER_SPEED_MOD
            turn_speed *= PLAYER_TURN_SPEED_MOD

        delta_x = 0
        delta_y = 0
        if keys["GO_FORWARD_KEY_PRESSED"]:
            delta_x += speed * cos_a
            delta_y += speed * sin_a
        elif keys["GO_BACK_KEY_PRESSED"]:
            delta_x += -speed * cos_a
            delta_y += -speed * sin_a
        if keys["GO_LEFT_KEY_PRESSED"]:
            delta_x += speed * sin_a
            delta_y += -speed * cos_a
        elif keys["GO_RIGHT_KEY_PRESSED"]:
            delta_x += -speed * sin_a
            delta_y += speed * cos_a
        if keys["TURN_LEFT_KEY_PRESSED"]:
            player.angle -= turn_speed
        elif keys["TURN_RIGHT_KEY_PRESSED"]:
            player.angle += turn_speed

        new_x = x + delta_x
        new_y = y + delta_y

        # check collision
        mp_x = mapping(x + delta_x * 10, y)
        if mp_x in world_map:
            if world_map[mp_x] == "E":
                return False
            new_x = x

        mp_y = mapping(x, y + delta_y * 10)
        if mp_y in world_map:
            if world_map[mp_y] == "E":
                return False
            new_y = y

        player.x = new_x
        player.y = new_y

        return True
