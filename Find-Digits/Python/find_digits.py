#!/usr/bin/env python3
    pass

'''
Find digits program

Author: Alexander Roth
Date:   2015-12-28
'''

import sys

def main(args):
    num_tests, tests = get_testcases(args[1])
    for test in tests:
        print(find_divisible_digits(test))


def get_testcases(filename):
    input_file = open(filename, 'r')
    num_tests = int(input_file.readline())
    tests = [int(i) for i in input_file]
    return (num_tests, tests)


def find_divisible_digits(number):
    '''Finds the total count of digits in a number that divide said number
    evenly.'''
    digit_list = get_digits(number)

    divisible_count = 0
    for digit in digit_list:
        # As long as the digit is not zero and divides evenly
        if digit and number % digit == 0:
            divisible_count += 1

    return divisible_count


def get_digits(number):
    '''Returns a list of digits for a given number.'''
    return [int(i) for i in str(number)]


def print_arguments(arg):
    print("python3 {0} <file>".format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])

