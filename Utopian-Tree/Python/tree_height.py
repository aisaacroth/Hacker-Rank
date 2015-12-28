#!/usr/bin/env python3

'''
Utopian Tree program

Author: Alexander Roth
Date:   2015-12-28
'''
import sys

def main(args):
    num_tests, tests = get_testcases(args[1])
    for test in tests:
        print(determine_tree_height(test))


def get_testcases(filename):
    input_file = open(filename, 'r')
    num_tests = int(input_file.readline())
    tests = [int(i) for i in input_file]
    return (num_tests, tests)


def determine_tree_height(number):
    total_height = 1

    for i in range(number):
        if i % 2 == 0:
            total_height *= 2
        else:
            total_height += 1
    
    return total_height


def print_arguments(arg):
    print("python3 {0} <file>".format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
