#! /usr/bin/python3
import sys
import re


sum = 0
lines = sys.stdin.readlines()
for line in lines:
    if not line:
        break

    digits = re.findall(r'\d+', line)
    if digits:
        if len(digits) == 1:
            calibration_val = int(digits[0] + digits[0])
        else:            
            calibration_val = int(digits[0] + digits[-1])
        
        sum += calibration_val
    
print("sum is ", sum)