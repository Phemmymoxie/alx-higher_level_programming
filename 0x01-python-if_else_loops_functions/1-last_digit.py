#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = str(number)
length = len(num_str)
lo = "Last digit of"
hi_1 = "and is greater than 5"
hi_2 = "and is less than 6 and not 0"
if number > 0:
    if int(num_str[length - 1]) > 5:
        output = f"{lo} {number} is {num_str[length - 1]} {hi_1}"
    elif num_str[length - 1] == '0':
        output = f"{lo} {number} is {num_str[length - 1]} and is 0"
    else:
        output = f"{lo} {number} is {num_str[length - 1]} {hi_2}"
    print(output)

else:
    if num_str[length - 1] == '0':
        output = f"{lo} {number} is {num_str[length - 1]} and is 0"
    else:
        output = f"{lo} {number} is -{num_str[length - 1]} {hi_2}"
    print(output)
