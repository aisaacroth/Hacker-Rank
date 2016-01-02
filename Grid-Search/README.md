Grid-Search
======
##Description##
Given a 2D array of digits, try to find the location of a given 2D pattern of
digits. For example, consider the following 2D matrix:
```
1234567890
0987654321
1111111111
1111111111
2222222222
```

Assume we need to look for the following 2D pattern:
```
876543
111111
111111
```
If we scan through the original array, we observe that the 2D pattern begins at
the second row and the third column of the larger grid (the 8 in the second row
and third column of the larger grid is the top-left corner of the pattern we are
searching for).

So, a 2D pattern of _P_ digits is said to be present in a larger grid _G_, if
the latter contains a contiguous, rectangular 2D grid of digits matching with
the pattern _P_, similar to the example shown above.

##Input Format##
The first line contains an integer, _T_, which is the number of test cases. _T_
test cases follow, each having a structure as described below:
The first line contains two space-separated integer, _R_ and _C_, indicating the
number of rows and columns in the grid _G_, respectively.
This is followed by _R_ lines, each with a string of _C_ digits, which represent
the grid _G_.
The following line contains two space-separated integers, _r_ and _c_,
indicating the number of rows and columns in the pattern grid _P_.
This is followed by _r_ lines, each with a string of _c_ digits, which represent
the pattern _P_.

##Constraints##
```
1 <= T <= 5
1 <= R, r, C, c <= 1000
1 <= r <= R
1 <= c <= C
```
