#!/usr/bin/env python3
"""
Compare the Triplets program.

Author: Alexander Roth
Date:   2017-01-02
"""
import sys


def main(args):
    combinations = get_testcases(sys.argv[1])
    scores = compare_tuples(combinations)
    display_scores(scores)


def get_testcases(filename):
    with open(filename, 'r') as input_file:
        corpus = [convert_to_int(line.split()) for line in input_file]

    a_tuple, b_tuple = corpus
    return list(zip(a_tuple, b_tuple))


def convert_to_int(num_list):
    return [int(item) for item in num_list]


def compare_tuples(tuples):
    a_score = b_score = 0

    for a, b in tuples:
        if a < b:
            b_score += 1
        elif a > b:
            a_score += 1

    return (a_score, b_score)


def display_scores(scores):
    print("{a} {b}".format(a=scores[0], b=scores[1]))


def print_arguments(arg):
    print('python3 {0} <file>'.format(arg))
    sys.exit(1)


if __name__ == '__main__':
    if len(sys.argv) == 2:
        main(sys.argv)
    else:
        print_arguments(sys.argv[0])
