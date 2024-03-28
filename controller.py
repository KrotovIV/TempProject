from settings import *
import pygame

class Controller:
    def __init__(self):
        pass    
    
    def handle_quit(self, events):
        for event in events:
                if event.type == pygame.QUIT:
                    exit()
    
    def level_skipped(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[SKIP_LEVEL_KEY]:
                    return True
        return False
    
    def collide_with_mouse(self, rect):
        return rect.collidepoint(pygame.mouse.get_pos())
    
    def left_mousebutton_pressed(self, events):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    return True
        return False
    
    def handle_player_movement(self):
        keys = pygame.key.get_pressed()
        response = {
            "GO_FORWARD_KEY_PRESSED": False,
            "GO_BACK_KEY_PRESSED": False,
            "GO_LEFT_KEY_PRESSED": False,
            "GO_RIGHT_KEY_PRESSED": False,
            "TURN_LEFT_KEY_PRESSED": False,
            "TURN_RIGHT_KEY_PRESSED": False,
            "RUN_KEY_PRESSED": False
        }

        if keys[GO_FORWARD_KEY]:
            response["GO_FORWARD_KEY_PRESSED"] = True
        if keys[GO_BACK_KEY]:
            response["GO_BACK_KEY_PRESSED"] = True
        if keys[GO_LEFT_KEY]:
            response["GO_LEFT_KEY_PRESSED"] = True
        if keys[GO_RIGHT_KEY]:
            response["GO_RIGHT_KEY_PRESSED"] = True
        if keys[TURN_LEFT_KEY]:
            response["TURN_LEFT_KEY_PRESSED"] = True
        if keys[TURN_RIGHT_KEY]:
            response["TURN_RIGHT_KEY_PRESSED"] = True
        if keys[RUN_KEY]:
            response["RUN_KEY_PRESSED"] = True

        return response