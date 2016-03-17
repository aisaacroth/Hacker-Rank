#!/usr/bin/env python3

'''

Author: Alexander Roth
Date:   2016-03-17
'''

import re
import sys


def main(args):
    filename = args[1]
    line_generator = read_line(filename)
    results = []

    try:
        while True:
            line = next(line_generator)
            results.append(check_braces(line))
    except StopIteration:
        converts = convert_results(results)
        print_results(converts)


def read_line(filename):
    with open(filename, 'r') as in_file:
        for line in in_file:
            yield line.strip()

def check_braces(line):

    stack = []
    for brace in line:

        if is_open_brace(brace):
            stack.append(brace)

        if is_close_brace(brace) and stack:
            open_brace = stack.pop()

            if not match_brace(open_brace, brace):
                return False
        elif not stack:
            return False

    if stack:
        return False
    return True


def is_open_brace(brace):
    brace_list = ['(', '{', '[']
    for i in brace_list:
        if i == brace:
            return True
    return False


def is_close_brace(brace):
    brace_list = [')', '}', ']']
    for i in brace_list:
        if i == brace:
            return True
    return False


def match_brace(open_brace, close_brace):
    brace_list = [('(', ')'), ('[', ']'), ('{', '}')]
    for item in brace_list:
        if item[0] == open_brace and item[1] == close_brace:
            return True
    return False


def convert_results(results):
    return ['YES' if item else 'NO' for item in results]


def print_results(converts):
    for item in converts:
        print(item)


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
