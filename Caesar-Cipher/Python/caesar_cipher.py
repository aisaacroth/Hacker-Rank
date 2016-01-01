#!/usr/bin/env python3
'''
Caesar Cipher program.

Author: Alexander Roth
Date:   2016-01-01
'''
import sys

def main(args):
    num_tests, corpus, offset = get_testcases(args[1])
    print(encode(corpus, offset))


def get_testcases(filename):
    input_file = open(filename, 'r')
    num_tests = int(input_file.readline().strip())
    corpus = input_file.readline().strip()
    offset = int(input_file.readline().strip())
    return (num_tests, corpus, offset)


def encode(corpus, offset):
    offset %= 26
    encoded_string = []
    for i in corpus:
        encoded_char = i

        if i.isalpha():
            shift_val = ord(i) + offset

            if shift_val > ord('z') and i.islower():
                shift_val -= 26

            if shift_val > ord('Z') and i.isupper():
                shift_val -= 26

            encoded_char = chr(shift_val)
        encoded_string.append(encoded_char)
    return ''.join(encoded_string)


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
