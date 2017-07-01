************************************************************************
file with basedata            : c1527_.bas
initial value random generator: 24752606
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  121
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       27       13       27
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6   9  10
   3        3          3           5  12  17
   4        3          2           7  17
   5        3          1           8
   6        3          1          11
   7        3          1          13
   8        3          1          10
   9        3          2          11  12
  10        3          1          13
  11        3          1          14
  12        3          1          16
  13        3          1          15
  14        3          3          15  16  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     3       0    7    5    0
         2     9       7    0    0   10
         3    10       0    5    5    0
  3      1     9       0    4    0    5
         2     9       3    0    4    0
         3     9       0    3    4    0
  4      1     2       0    8    0   10
         2     2       0    9    1    0
         3     3       5    0    1    0
  5      1     4       0    5    0    5
         2     6       6    0    8    0
         3     9       4    0    5    0
  6      1     5      10    0    3    0
         2     7       0    8    2    0
         3    10       7    0    0    8
  7      1     2       0    3    0    3
         2     5       0    2    6    0
         3     6       2    0    4    0
  8      1     5       7    0   10    0
         2     6       0    3    8    0
         3     8       0    3    0    6
  9      1     3       6    0    9    0
         2     5       0    5    0    1
         3     8       0    1    5    0
 10      1     2       9    0    8    0
         2     2       0    6    0    8
         3     3       0    6    9    0
 11      1     1       0    8    4    0
         2     2       9    0    0    6
         3     6       8    0    0    6
 12      1     4       6    0    8    0
         2     6       0    2    7    0
         3    10       5    0    0    7
 13      1     2       7    0    0    8
         2     8       4    0    2    0
         3     9       0    7    0    7
 14      1     1       0    2    0    3
         2     2       9    0    2    0
         3     4       2    0    2    0
 15      1     5       7    0    6    0
         2     6       0    6    0    6
         3    10       5    0    0    5
 16      1     3       8    0    6    0
         2     5       5    0    0    4
         3     7       0    9    0    4
 17      1     1       7    0    8    0
         2     6       0    4    0    5
         3     9       0    4    0    4
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   17   15   91   95
************************************************************************
