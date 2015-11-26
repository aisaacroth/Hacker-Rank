#!/usr/bin/env python3

'''

Author: Alexander Roth
Date:   2015-11-25
'''
def main():
    num = read_dim()
    matrix = gen_matrix(num)
    print(diag_sum(matrix))


def read_dim():
    return int(input("Please input dimensions for the matrix: ").strip())


def gen_matrix(dim):
    matrix = []
    for i in range(dim):
        tmp = [int(j) for j in input().strip().split(' ')]
        matrix.append(i)
    return matrix


def diag_sum(matrix):
    prim_diag = 0
    second_diag = 0
    for i in range(len(matrix)):
        prim_diag += matrix[i][i]
        second_diag += matrix[(len(matrix) - 1) - i][i]
    return abs(prim_diag - second_diag)


if __name__ == '__main__':
    main()
