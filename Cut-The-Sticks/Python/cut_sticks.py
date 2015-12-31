#/usr/bin/env python3
'''
Cut Sticks program.

Author: Alexander Roth
Date:   2015-12-31
'''

def main():
    testcase = get_testcase()
    determine_num_of_cuts(testcase)


def get_testcase():
    n = int(input().strip())
    arr = [int(arr_temp) for arr_temp in input().strip().split()]
    return arr


def determine_num_of_cuts(cut_list):
    min_cut = -1
    i = 0

    cut_list.sort()

    while i < len(cut_list):
        if min_cut < cut_list[i]:
            min_cut = cut_list[i]
            print(len(cut_list) - i)
        i += 1


if __name__ == '__main__':
    main()
