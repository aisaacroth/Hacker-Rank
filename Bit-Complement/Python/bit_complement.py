#!/usr/bin/env python3

'''
Converts a decimal digit to its unsigned integer complement.

Author: Alexander Roth
Date:   2016-03-17
'''

import sys


def main(args):
    filename = args[1]
    line_generator = read_file(filename)

    try:
        while True:
            line = next(line_generator)
            base_list = euclid_algorithm(line, 2)
            complement_list = complement(base_list)
            complement_value = bin_to_dec(complement_list, 2)
            print(complement_value)
    except StopIteration:
        pass


def read_file(filename):
    with open(filename, 'r') as in_file:
        for line in in_file:
            yield line.strip()


def euclid_algorithm(line, base):
    value = int(line)
    base_list = []

    while value > 0:
        remainder = value % base
        base_list.append(remainder)
        value //= base
    return base_list


def complement(base_list):
    complement_list = []
    for i in base_list:
        
        if i == 1:
            complement_list.append(0)
        else:
            complement_list.append(1)
    return complement_list


def bin_to_dec(complement_list, base):
    total = 0
    for i in range(len(complement_list)):
        total += complement_list[i] * base ** i
    return total


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
