************************************************************************
file with basedata            : cm119_.bas
initial value random generator: 1546918630
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
    1     16      0       41       13       41
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        1          2           9  14
   3        1          3          10  15  16
   4        1          3           5   7   9
   5        1          3           6  11  12
   6        1          3          10  13  15
   7        1          3           8  10  11
   8        1          1          12
   9        1          2          15  17
  10        1          1          17
  11        1          2          14  16
  12        1          2          13  16
  13        1          1          14
  14        1          1          17
  15        1          1          18
  16        1          1          18
  17        1          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     8       0    6    4    0
  3      1     1       4    0    8    0
  4      1     7       0    3    3    0
  5      1     9       0    3    0    3
  6      1     4       3    0    0    3
  7      1     7       0    4    0    9
  8      1     5       5    0    0    3
  9      1     4       0    2    0    5
 10      1     8       0    8    0    9
 11      1     8       0    6    0    6
 12      1     3       2    0    4    0
 13      1     8       0    9    7    0
 14      1     4       0    7    0    9
 15      1     6       2    0    7    0
 16      1     5       3    0    6    0
 17      1     7       6    0    0    8
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
    8   20   39   55
************************************************************************
