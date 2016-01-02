#!/usr/bin/env python3
'''
Grid Search program.

Author: Alexander Roth
Date:   2016-01-01
'''
import sys

def main(args):
    num_tests, tests = get_testcases(args[1])
    for i in tests:
        grid_row, grid_col, G, pat_row, pat_col, P = i
        print(find_pattern(grid_row, grid_col, G, pat_row, pat_col, P))


def get_testcases(filename):
    input_file = open(filename, 'r')
    num_tests = input_file.readline()
    tests = []

    for i in num_tests:
        grid_row, grid_col = input_file.readline().strip().split()
        grid_row, grid_col = [int(grid_row), int(grid_col)]

        G = []
        for j in range(grid_row):
            G.append(str(input_file.readline().strip()))

        pattern_row, pattern_col = input_file.readline().strip().split()
        pattern_row, pattern_col = [int(pattern_row), int(pattern_col)]

        P = []
        for k in range(pattern_row):
            P.append(str(input_file.readline().strip()))

        tests.append((grid_row, grid_col, G, pattern_row, pattern_col, P))

    return (num_tests, tests)


def find_pattern(grid_row, grid_col, grid, pattern_row, pattern_col, pattern):
    pass


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
