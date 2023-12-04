#! /usr/bin/python3
import sys
import re

class Game:
    def __init__(self, game_id, draws):
        self.id = game_id
        self.draws = draws

        # part 1, limits of each color
        self.N_RED = 12
        self.N_GREEN = 13
        self.N_BLUE = 14

        self._is_possible = True

        # part 2, determine the fewest amount of balls needed for a game
        self._max_blue = 0
        self._max_green = 0
        self._max_red = 0

    @property
    def is_possible(self):
        return self._is_possible

    def play(self):
        for draw in self.draws:
            if not self.is_draw_possible(draw):
                self._is_possible = False
                
    def get_power_of_fewest_cubes(self):
        return self._max_red * self._max_green * self._max_blue

    def is_draw_possible(self, draw):
        pattern = re.compile(r"\d+")
        is_draw_possible = True

        for match in pattern.finditer(draw):
            if draw[match.end()] == "r": # red
                n_red = int(match.group())
                # part 2
                if n_red > self._max_red:
                    self._max_red = n_red
                # part 1
                if n_red > self.N_RED:
                    is_draw_possible = False
            elif draw[match.end()] == "g": # green
                n_green = int(match.group())
                # part 2
                if n_green > self._max_green:
                    self._max_green = n_green
                # part 1
                if n_green > self.N_GREEN:
                    is_draw_possible = False
            elif draw[match.end()] == "b": # blue
                n_blue = int(match.group())
                # part 2
                if n_blue > self._max_blue:
                    self._max_blue = n_blue
                # part 1
                if n_blue > self.N_BLUE:
                    is_draw_possible = False
                
        return is_draw_possible

if __name__ == "__main__":
    possible_games_sum = 0
    power_of_fewest_cubes_sum = 0

    lines = sys.stdin.readlines()
    for idx, line in enumerate(lines):
        if not line:
            break

        game_possible = True
        line = line.split(":")[1]
        draws = re.sub(r"\s+", "", line).split(";")
        game: Game = Game(idx + 1, draws)

        game.play()

        if game.is_possible:
            possible_games_sum += game.id

        power_of_fewest_cubes_sum += game.get_power_of_fewest_cubes()

    print("\nPart 1 answer: ", possible_games_sum)
    print("Part 2 answer: ", power_of_fewest_cubes_sum)

# SOLVED
# Part 1 answer:  2810
# Part 2 answer:  69110