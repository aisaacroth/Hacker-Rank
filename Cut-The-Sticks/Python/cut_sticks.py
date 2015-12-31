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
    '''Determines the number of sticks that need to be cut once the smallest
    stick has been located.
    
    Uses the following algorithm: Once we sort the list, the minimum length
    stick is at the front of the list. From here, we set that stick as the
    minimum and step through the list. Once we find a stick that is longer than
    the minimum, we set that as the new minimum to simulate the stick cutting
    and then determine how many sticks remain. Since the list is organized in
    monotonically increasing order, we know that all sticks to the left of the
    current index will be zero or negative in value, and thus, do not need to be
    considered when making feature cuts.'''
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
