#! /usr/bin/python3
import sys
import re
from typing import List


if __name__ == "__main__":
    engine_parts = {}
    idx_to_skip = []
    

    lines = sys.stdin.readlines()
    for idx, line in enumerate(lines):
        if not line:
            break

        for idx_inner, char in enumerate(line):
            # skip if we already found this digit.
            while idx_to_skip:
                idx_to_skip.pop()

            if not char.isdigit():
                continue

            # check up, up-left, up-right, down, down-left, down-right, left, right
            # up: idx - 1
            # up-left: idx - 1, idx_inner - 1
            # up-right: idx - 1, idx_inner + 1
            # down: idx + 1
            # down-left: idx + 1, idx_inner - 1
            # down-right: idx + 1, idx_inner + 1
            # left: idx_inner - 1
            # right: idx_inner + 1

            if (

                lines[idx - 1][idx_inner] != "."
                or lines[idx - 1][idx_inner - 1] != "."
                or lines[idx - 1][idx_inner + 1] != "."
                or lines[idx + 1][idx_inner] != "."
                or lines[idx + 1][idx_inner - 1] != "."
                or lines[idx + 1][idx_inner + 1] != "."
                # or not lines[idx - 1][idx_inner].isdigit()
                # or not lines[idx - 1][idx_inner - 1].isdigit()
                # or not lines[idx - 1][idx_inner + 1].isdigit()
                # or not lines[idx + 1][idx_inner].isdigit()
                # or not lines[idx + 1][idx_inner - 1].isdigit()
                # or not lines[idx + 1][idx_inner + 1].isdigit()
                ):
                    # find all digits in the sequence.
                    skip_idx = idx_inner
                    while lines[idx][skip_idx].isdigit():
                        idx_to_skip.append(skip_idx)
                        skip_idx += 1
                    
