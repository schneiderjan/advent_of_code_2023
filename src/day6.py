import math


input_time = {}  # Define input_time dictionary
input_d = 0  # Define input_d variable
counter = 0  # Define counter variable

# # brute forece solution 
# for i in input_time:
#     d = i * (input_time[i] - i)
#     if d > input_d:
#         counter += 1

def second_math_function(t, d, x1=True):
    if x1:
        return (-t + math.sqrt(math_function(t, d))) / 2
    else:
        return (-t - math.sqrt(math_function(t, d))) / 2

def math_function(t, d):
    return t * t - 4 * d