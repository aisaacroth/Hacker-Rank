#!/usr/bin/env python3
'''
Find Squares Program.

Author: Alexander Roth
Date:   2015-12-28
'''
import math
import sys

def main(args):
    num_tests, tests = get_testcases(args[1])
    for test in tests:
        print(find_square_roots(test[0], test[1]))


def get_testcases(filename):
    input_file = open(filename, 'r')
    num_tests = int(input_file.readline())
    tests = [(int(i.split()[0]), int(i.split()[1])) for i in input_file]
    return (num_tests, tests)


def find_square_roots(start, end):
    start_root = math.ceil(math.sqrt(start))
    end_root = math.floor(math.sqrt(end))
    return end_root - start_root + 1


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
