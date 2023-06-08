#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    total = 0
    if len(argv) - 1 == 0:
        print("{}".format(0))
    elif len(argv) - 1 == 1:
        print("{}".format(argv[1]))
    else:
        for num in range(1, len(argv)):
            total += int(argv[num])
        print("{}".format(total))
