#!/usr/bin/python3
if __name__ == "__main__":
    import sys

len_arg = len(sys.argv) - 1

sum_all = 0
for i in range(len_arg):
    sum_all += int(sys.argv[i + 1])

print("{}".format(sum_all))
