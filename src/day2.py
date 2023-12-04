#! /usr/bin/python3
import sys
import re

N_RED = 12
N_GREEN = 13
N_BLUE = 14


def is_draw_possible(draw):
    pattern = re.compile(r"\d+")
    for match in pattern.finditer(draw):
        if draw[match.end()] == "r" and int(match.group()) > N_RED:
            return False
        elif draw[match.end()] == "g" and int(match.group()) > N_GREEN:
            return False
        elif draw[match.end()] == "b" and int(match.group()) > N_BLUE:
            return False

    return True


if __name__ == "__main__":
    possible_games_sum = 0

    lines = sys.stdin.readlines()
    for idx, line in enumerate(lines):
        if not line:
            break

        game_possible = True
        line = line.split(":")[1]
        for draw in re.sub(r"\s+", "", line).split(";"):
            if not is_draw_possible(draw):
                game_possible = False
                break

        if game_possible:
            possible_games_sum += idx + 1

    print("\nAnswer: ", possible_games_sum)

# SOLVED