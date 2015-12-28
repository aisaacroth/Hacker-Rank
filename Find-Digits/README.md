Find Digits
======
##Description##
Given an integer, _N_, traverse its digits (d_1, d_2,..., d_n) and determine how
many digits evenly divide _N_ (i.e.: count the number of times _N_ divided by
each digit d_i has a remainder of 0). Print the number of evenly divisible
digits.

**Note**: Each digit is considered to be unique, so each occurrence of the same
evenly divisible digit should be counted (i.e.: for _N_ = 111, the answer is 3).

###Input Format###
The first line is an integer, _T_, indicating the number of test cases.
The _T_ subsequent lines each contain an integer, _N_.

###Constraints###
```
1 <= T <= 15
0 <= N <= 10^10
```

###Output Format###
For every test case, count and print (on a new line) the number of digits in _N_
that are able to evenly divide _N_.

####Sample Input####
```
2
12
1012
```

####Sample Output####
```
2
3
```

####Explanation####
The number 12 is broken into two digits, 1 and 2. WHen 12 is divided by either
of those digits, the calculation's remainder is 0; thus, the number of evenly-
divisible digits in 12 is 2.

The number 1012 is broken into four digits, 1, 0, 1, and 2. 1012 is evenly
divisible by its digits 1, 1, and 2, but it is _not_ divisible by 0 as
**division by zero is undefined**; thus, our count of evenly divisible digits is
3.
