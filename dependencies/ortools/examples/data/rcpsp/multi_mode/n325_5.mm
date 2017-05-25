************************************************************************
file with basedata            : cn325_.bas
initial value random generator: 795866620
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  122
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  3   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       19       13       19
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   7   8
   3        3          3          11  13  15
   4        3          2           8  14
   5        3          3           6  10  11
   6        3          3           9  12  17
   7        3          1          13
   8        3          3          12  16  17
   9        3          2          13  15
  10        3          2          12  14
  11        3          2          14  16
  12        3          1          15
  13        3          1          16
  14        3          1          17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2  N 3
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0
  2      1     5       0    6    0    0    8
         2     7       1    0    7    2    0
         3     9       0    1    7    2    0
  3      1     4       0    6    0    0    5
         2     5       6    0    4    0    0
         3     8       0    4    0    0    4
  4      1     5       0    8    0    0    8
         2     5       2    0    0    0    8
         3     9       0   10    0    0    6
  5      1     3       0    3    0    0    2
         2     4       7    0    0    0    1
         3     7       3    0    0    6    1
  6      1     2       2    0    6   10    6
         2     2       3    0    0   10    0
         3     2       0    7    6    0    0
  7      1     1       8    0    2    0    0
         2     3       0    5    0    9    3
         3     4       4    0    0    6    0
  8      1     1       6    0    0    9    7
         2     7       0    7    6    0    6
         3    10       2    0    4    0    0
  9      1     2       0    9    0    5    2
         2     8       0    8    0    5    0
         3     8       7    0    0    5    0
 10      1     1       6    0    0    0    6
         2     3       5    0    9    0    5
         3     9       0    8    7    0    5
 11      1     1       9    0   10    6    5
         2    10       0    9    0    0    4
         3    10       9    0    0    0    4
 12      1     2       0   10    6    0    4
         2     4       0    9    4    0    0
         3     5       0    9    0    6    0
 13      1     1       9    0    0    0    4
         2     9       7    0    0    3    0
         3     9       0    5    6    0    0
 14      1     2       7    0    0    8    8
         2     8       5    0    8    6    4
         3     9       0    6    4    6    0
 15      1     7       0    6    9    5    0
         2     9       0    5    8    4    7
         3    10       0    2    8    0    5
 16      1     6       3    0    0    2    6
         2     7       0    7    9    0    0
         3     9       0    7    8    0    0
 17      1     2       0    5    9    6    0
         2     3       0    4    0    0    4
         3     4       5    0    5    0    3
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2  N 3
    5   15   91   77   85
************************************************************************
