from settings import *
from tools import *
import random
import copy


class Map:
    def get_neighbours(self, cell_coords, board):
        poss = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        neighbours = []
        for elem in poss:
            x = cell_coords[0] + elem[0]
            y = cell_coords[1] + elem[1]
            if (
                0 <= y <= len(board) - 1
                and 0 <= x <= len(board[0]) - 1
                and board[y][x] == 0
            ):
                neighbours.append((x, y))
        return neighbours

    def has_path(self, x1, y1, x2, y2, board):
        num = 1
        board[y1 - 1][x1 - 1] = num
        while True:
            board_ = copy.deepcopy(board)
            for j in range(len(board)):
                for i in range(len(board[j])):
                    if board[j][i] == num:
                        neighbours = self.get_neighbours((i, j), board)
                        for x, y in neighbours:
                            board[y][x] = num + 1
            if board == board_:
                break
            num += 1
        return True if board[y2 - 1][x2 - 1] != 0 else False

    def generate_path(self, path_len, size, text_map):
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        dir = random.choice(directions)
        path = []

        x, y = random.randint(1, size[0] - 2), random.randint(
                1, size[1] - 2
            )
        text_map[y] = text_map[y][:x] + " " + text_map[y][x + 1 :]
        path.append((x, y))

        while len(path) < path_len:
            if random.randint(1, STRAIGHT_PATH_COEFF) == 1:
                dir = random.choice(directions)
            if (
                0 < x + dir[0] < size[0] - 3
                and 0 < y + dir[1] < size[1] - 3
            ):
                x += dir[0]
                y += dir[1]
                path.append((x, y))
                text_map[y] = text_map[y][:x] + " " + text_map[y][x + 1 :]
            else:
                x, y = random.randint(1, size[0] - 2), random.randint(
                    1, size[1] - 2
                )
        return path
    
    def generate_walls(self, size, text_map):
        board = [[0] * (size[0] - 2) for _ in range(size[1] - 2)]
        for i in range(len(text_map)):
            if "." in text_map[i]:
                for j in range(len(text_map[i])):
                    if text_map[i][j] == ".":
                        text_map[i] = (
                            text_map[i][:j]
                            + f"{random.randint(1, 2)}"
                            + text_map[i][j + 1 :]
                        )
                        board[i - 1][j - 1] = "b"
        return board
    
    def generate_exit(self, path, text_map):
        exit = random.choice(path)
        text_map[exit[1]] = (
            text_map[exit[1]][: exit[0]]
            + "E"
            + text_map[exit[1]][exit[0] + 1 :]
        )
        del path[path.index(exit)]
        return exit
    
    def generate_player(self, path, text_map):
        player = random.choice(path)
        text_map[player[1]] = (
            text_map[player[1]][: player[0]]
            + "P"
            + text_map[player[1]][player[0] + 1 :]
        )
        del path[path.index(player)]
        return player

    def path_acceptable(self, exit, player, board):
        #if the exit is reachable and the length of the straight line from the player to the exit is sufficient
        if not self.has_path(*exit, *player, board):
            return False

        x = abs(player[0] - exit[0]) ** 2
        y = abs(player[1] - exit[1]) ** 2
        straight_line_length = (x + y) ** 0.5

        return  straight_line_length >= PLAYER_TO_EXIT_LENGTH

    def generate_world_map(self, text_map):
        world_map = {}
        for j, row in enumerate(text_map):
            for i, char in enumerate(row):
                if char != "." and char != " " and char != "P":
                    world_map[(i * TILE, j * TILE)] = char
        return world_map

    def generate_text_map(self, size):
        text_map = [
            "1" + "." * (size[0] - 2) + "1" for _ in range(size[1])
        ]
        text_map[0], text_map[-1] = "1" * size[0], "1" * size[0]
        return text_map

    def build_labyrinth(self, size):
        path_len = (size[0] + size[1]) * 3
        while True:
            # empty map with external walls
            text_map = self.generate_text_map(size)


            # main path
            path = self.generate_path(path_len, size, text_map)


            # walls
            board = self.generate_walls(size, text_map)
            

            #exit
            exit = self.generate_exit(path, text_map)


            #player
            player = self.generate_player(path, text_map)


            if (self.path_acceptable(exit, player, board)):
                player_pos = (player[0] * TILE, player[1] * TILE)
                world_map = self.generate_world_map(text_map)
                return world_map, player_pos

    
