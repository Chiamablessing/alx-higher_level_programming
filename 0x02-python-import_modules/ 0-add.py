#!/usr/bin/python3
def print_sum():
    from add_0 import add
    a = 1
    b = 2
    print("{:d} + {:d} = {:d}".format(a, b, add(a, b)))


if __name__ == "__main__":
    print_sum()