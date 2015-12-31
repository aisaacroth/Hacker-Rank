#!/usr/bin/env python3
'''
Chocolate Count Program.

Author: Alexander Roth
Date:   2015-12-31
'''
import sys

def main(args):
    num_tests, tests = get_testcases(args[1])
    for test in tests:
        money = test[0]
        cost = test[1]
        wrapper_cost = test[2]
        print(count_chocolate(money, cost, wrapper_cost))


def get_testcases(filename):
    input_file = open(filename, 'r')
    num_tests = int(input_file.readline())
    tests = []

    for i in input_file:
        test_vars = i.split()
        tests.append((int(test_vars[0]), int(test_vars[1]), int(test_vars[2])))
    return (num_tests, tests)


def count_chocolate(money, cost, wrapper_cost):
    wrapper_total = money // cost
    return wrapper_total + (wrapper_total - 1) // (wrapper_cost - 1)


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
