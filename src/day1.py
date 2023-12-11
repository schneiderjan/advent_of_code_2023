#! /usr/bin/python3
import sys
import re
import queue

LUT_DIGITS = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9"
}

def replace_words(line):
    replacement_candidates = queue.Queue()
    # need to fix if there are more than one digit in the line, and you loop over it and replace it but you cant find the next one.
    for key, _ in LUT_DIGITS.items():
        if key in line:
            replacement_candidates.put(key)

    while not replacement_candidates.empty():
        canditate = replacement_candidates.get()
        line = line.replace(canditate, LUT_DIGITS[canditate])
    return line


if __name__ == "__main__":
    sum = 0
    lines = sys.stdin.readlines()
    for line in lines:
        if not line:
            break
        
        line = replace_words(line)

        digits = re.findall(r'\d', line)
        if digits:
            if len(digits) == 1:
                calibration_val = int(digits[0] + digits[0])
            else:            
                calibration_val = int(digits[0] + digits[-1])
            
            sum += calibration_val
            print("\n", sum)
    print("sum is ", sum)   