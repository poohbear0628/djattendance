************************************************************************
file with basedata            : cm116_.bas
initial value random generator: 675244434
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  74
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       26        1       26
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        1          3           5   9  15
   3        1          3           5   7   9
   4        1          2           8  13
   5        1          3           6  12  14
   6        1          2          11  16
   7        1          2           8  14
   8        1          3          11  15  16
   9        1          3          10  11  14
  10        1          1          12
  11        1          1          17
  12        1          2          13  16
  13        1          1          17
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
  2      1     6       8    5    0    8
  3      1     5       4    7    9    0
  4      1     2       5    3    0    2
  5      1     3       6    4    3    0
  6      1     3       5    4    0    7
  7      1     4       4    8    8    0
  8      1     9       7    6    7    0
  9      1     5       3    4    0    7
 10      1     3       6    4    9    0
 11      1     2       3    4    0    9
 12      1     6       5    6    6    0
 13      1     1       8    2    0    4
 14      1    10       8    6    8    0
 15      1     7       8    4    1    0
 16      1     3       4    5    8    0
 17      1     5       3    5    5    0
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   28   20   64   37
************************************************************************
