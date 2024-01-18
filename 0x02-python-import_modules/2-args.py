#!/usr/bin/python3
if __name__ == "__main__":
    import sys

len_arg = len(sys.argv) - 1

if len_arg == 1:
    print("{} argument:".format(len_arg))
elif len_arg == 0:
    print("{} arguments.".format(len_arg))
else:
    print("{} arguments.".format(len_arg))

print(len_arg)
for i in range(len_arg):
    print("{}: {}".format(i + 1, sys.argv[i + 1]))
