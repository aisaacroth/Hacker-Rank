#!/usr/bin/env python3
'''
Decent Number program

Author: Alexander Roth
Date:   2015-11-26
'''
import sys

def main(args):
    num_tests, tests = get_testcases(sys.argv[1])
    for test in tests:
         print(generate_decent_number(test))


def get_testcases(filename):
    input_file = open(filename, 'r')
    num_tests = int(input_file.readline())
    tests = [int(i) for i in input_file]
    return (num_tests, tests)


def generate_decent_number(testcase):
    '''Generates the decent number using the following greedy algorithm:

        First, we determine the longest possible substring that is divisible by
        3. We use this index as our end point for the longest possible substring
        of 5's. Once we have reached this endpoint, we know that the remaining
        substring in the string of digits is divisible by 5; thus, we can fill
        the remaining substring with 3's.'''
    pivot = get_pivot(testcase)

    # If pivot is nonnegative, the string properties are not met.
    if pivot < 0:
        return -1

    decent_list = []

    for i in range(pivot):
        decent_list.append(5)

    for i in range(pivot, testcase):
        decent_list.append(3)

    # Return as integer value
    return int(''.join(str(i) for i in decent_list))


def get_pivot(number):
    '''Determines the index of the longest possible substring that is divisible 
    by 3'''
    pivot = number

    while pivot > 0:
        if pivot % 3 == 0:
            break
        else:
            pivot -= 5

    return pivot


def print_arguments(arg):
    print("python3 {0} <file>".format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])

