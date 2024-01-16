#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num_str = str(number)
length = len(num_str)
if number > 0:
    if int(num_str[length - 1]) > 5:
        output = f"Last digit of {number} is {num_str[length - 1]} and is greater than 5"
    elif num_str[length - 1] == '0':
        output = f"Last digit of {number} is {num_str[length - 1]} and is 0"
    else:
        output = f"Last digit of {number} is {num_str[length - 1]} and is less than 6 and not 0"
    print(output)

else:
    if num_str[length - 1] == '0':
        output = f"Last digit of {number} is {num_str[length - 1]} and is 0"
    else:
        output = f"Last digit of {number} is -{num_str[length - 1]} and is less than 6 and not 0"
    print(output)
