************************************************************************
file with basedata            : cm154_.bas
initial value random generator: 16823
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  83
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       33        8       33
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        1          2          12  17
   3        1          3           5   6   7
   4        1          2           5   8
   5        1          2           9  13
   6        1          3           8   9  12
   7        1          3           9  14  15
   8        1          1          10
   9        1          2          16  17
  10        1          3          11  13  14
  11        1          1          15
  12        1          1          13
  13        1          2          15  16
  14        1          2          16  17
  15        1          1          18
  16        1          1          18
  17        1          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     6       2    6    7    1
  3      1     4       3    1    7    1
  4      1     2      10    2    1    6
  5      1     7       8    2    5    3
  6      1     2       4    7    6    4
  7      1     6       4    4    8    2
  8      1     5       6    6    8    9
  9      1     6       1    4    6    4
 10      1     8       9    7    8   10
 11      1     6       6    2    4    8
 12      1     9      10    1    7    9
 13      1     2       6    8    9    4
 14      1     5       3    7    6    2
 15      1     5       7    9    8    5
 16      1     9       3    3    7    3
 17      1     1       1    5    6    5
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   19   14  103   76
************************************************************************
