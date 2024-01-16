#!/usr/bin/python3
import random
number = random.randint(-10, 10)
if number > 0:
    output = f"{number} is positive"
    print(output)
elif number < 0:
    output = f"{number} is negative"
    print(output)
else:
    output = f"{number} is zero"
    print(output)
