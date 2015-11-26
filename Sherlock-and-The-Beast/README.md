Sherlock-and-The-Beast
======

##Description##
Sherlock Holmes suspects his archenemy, Professor Moriarity, is once again
plotting something diabolical. Sherlock's companion, Dr.Watson, suggest Moriarty
may be responsible for MI6's recent issues with their supercomputer, _The
Beast_.

Shortly after resolving to investigate, Sherlock receives a note from Moriarty
boasting about infecting _The Beast_ with a virus; however, he also gives him a
clue -- a number, _N_. Sherlock determines the key to removing the virus is to
find the largest _Decent Number_ having _N_ digits.

A _Decent Number_ ha the following properties:
1. Its digits can only be 3's and/or 5's.
2. The number of 3's it contains is divisible by 5.
3. The number of 5's it contains is divisible by 3.

Moriarty's virus shows a clock counting down to _The Beast_'s descrution, and
time is running out fast. Your task is to help Sherlock find the key before _The
Beast_ is destroyed!

###Constraints###
```
1 <= T <= 20
1 <= N <= 100000
```

###Input Format###
The first line is an integer, _T_, denoting the number of test cases.

The _T_ subsequent lines each contain an integer, _N_, detailing the number of
digits in the number.

###Output Format###
Print the largest Decent Number having _N_ digits; if no such number exists,
tell Sherlock by printing `-1`.

###Sample Input###
```
4
1
3
5
11
```

###Sample Output###
```
-1
555
33333
55555533333
```

###Explanation###
For _N = 1_, there is no such number.
For _N = 3_, 555 is the only possible number.
For _N = 5_, 33333 is the only possible number.
For _N = 11_, 55555533333 and all permutations of these digits are valid
numbers; among them, the given number is the largest one.
