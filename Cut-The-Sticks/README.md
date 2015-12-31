Cut-The-Sticks
======
##Description##
You are given _N_ sticks, where the _length_ of each stick is a positive
integer. A _cut operation_ is performed on the sticks such that all of them are
reduced by the length of the smallest stick.

Suppose we have six sticks of the following lengths:
`5 4 4 2 2 8`

Then in, one _cut operation_ we make a cut of length 2 from each of the six
sticks. For the next _cut operation_ four sticks are left (of non-zero length),
whose lengths are the following:
`3 2 2 6`

The above step is repeated until no sticks are left.

Given the length of _N_ sticks, print the number of sticks that are left before
each subsequent _cut operations_.

_Note:_ For each _cut operation_, you have to recalculate the length of the
smallest sticks (excluding zero-length sticks).

##Input Format##
The first line contains a single integer _N_.
The next line contains _N_ integers, separated by space, where a_i represents
the length of the ith stick.

##Output Format##
For each operation, print the number of sticks that are cut, on separate lines.

###Constraints###
```
1 <= N <= 1000
1 <= a_i <= 1000
```
