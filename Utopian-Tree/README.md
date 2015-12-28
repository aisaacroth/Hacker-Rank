Utopian Tree
======
##Description##
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it
_doubles_ in height. Each summer, its height increases by 1 meter.

Laura plants a Utopian Tree sapling with a height of 1 meter at the onset of
spring. How tall will her tree be after _N_ growth cycles?

###Input Format###
The first line contains an integer, _T_, the number of test cases.
_T_ subsequent lines each contain an integer, _N_, denoting the number of cycles
for that test case.

###Constraints###
` 1 <= T <= 10`
` 0 <= N <= 60`

###Output Format###
For each test case, print the height of the Utopian Tree after _N_ cycles. Each
height must be printed on a new line.

####Sample Input####
```
3
0
1
4
```

####Sample Output####
```
1
2
7
```

####Explanation####
There are _3_ test cases.
In the first case (_N_ = 0), the initial height (_H_ = 1) of the tree remains
unchanged.
In the second case (_N_ = 1), the tree doubles in height and is 2 meters tall
after the spring cycle.
In the third case (_N_ = 4), the tree doubles its height in spring (_H_ = 2),
then grows a meter in summer (_H_ = 3), then doubles after the next spring (_H_
= 6), and grows another meter after summer (_H_ = 7). Thus, at the end of 4
cycles, its height is 7 meters.
