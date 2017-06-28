************************************************************************
file with basedata            : cm12_.bas
initial value random generator: 566775896
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  94
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       42        8       42
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        1          3           5   7  16
   3        1          3           5   9  16
   4        1          3           5   8  11
   5        1          3           6  10  12
   6        1          2          13  15
   7        1          2          12  13
   8        1          2           9  14
   9        1          2          10  15
  10        1          1          13
  11        1          2          12  17
  12        1          1          15
  13        1          1          17
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
  2      1     2      10    0    5    0
  3      1     6       4    0    0    3
  4      1     7       8    0    8    0
  5      1    10       0    8    8    0
  6      1     7       4    0    3    0
  7      1     4       2    0    0    7
  8      1     1       0    9    6    0
  9      1     4       0    4    0    8
 10      1    10       0    4    8    0
 11      1     1       7    0    2    0
 12      1     8       0    7    9    0
 13      1     5       4    0    0    1
 14      1     9       0   10    5    0
 15      1     3       0    2    0    7
 16      1     7       8    0    3    0
 17      1    10       7    0    0    3
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   16   16   57   29
************************************************************************
