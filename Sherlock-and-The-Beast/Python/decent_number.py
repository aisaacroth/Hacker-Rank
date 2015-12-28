#!/usr/bin/env python3
'''

Author: Alexander Roth
Date:   2015-11-26
'''
import sys

def main(args):
    num_tests, tests = get_testcases(sys.argv[1])
    for test in tests:
        result = generate_decent_number(test)
        print(''.join(str(i) for i in result) if isinstance(result, list) 
              else result) 


def get_testcases(filename):
    input_file = open(filename, 'r')
    num_tests = int(input_file.readline())
    tests = [int(i) for i in input_file]
    return (num_tests, tests)


def generate_decent_number(testcase):
    pivot = get_pivot(testcase)

    if pivot < 0:
        return -1

    decent_list = []

    for i in range(pivot):
        decent_list.append(5)

    for i in range(pivot, testcase):
        decent_list.append(3)

    return decent_list


def get_pivot(number):
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

