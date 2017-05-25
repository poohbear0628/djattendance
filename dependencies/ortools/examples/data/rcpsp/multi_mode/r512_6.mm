************************************************************************
file with basedata            : cr512_.bas
initial value random generator: 90994592
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  139
RESOURCES
  - renewable                 :  5   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       12        0       12
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           8  11  15
   3        3          3           5   6   8
   4        3          3           8  14  16
   5        3          3          10  12  13
   6        3          2           7  12
   7        3          3          10  11  13
   8        3          2           9  12
   9        3          1          17
  10        3          2          15  16
  11        3          1          17
  12        3          1          17
  13        3          2          14  16
  14        3          1          15
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  R 4  R 5  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0    0    0
  2      1     3       0    5    0    0    6    6    0
         2     8       0    0    3    0    0    0    5
         3    10       0    4    3    2    2    0    4
  3      1     1       2    0    9    0    9    6    0
         2     7       2   10    8    0    0    4    0
         3     9       0    8    4    0    7    0    3
  4      1     4       4    0    6    0    5    2    0
         2     4       0    5    6    0    0    1    0
         3    10       5    4    5    0    6    0    7
  5      1     2       0    0    7    5    0    0   10
         2     8       0    5    7    2    0    5    0
         3    10       0    4    7    0    8    0    7
  6      1     2       0    0    8    9    4    0   10
         2     3       7    5    6    9    4    0   10
         3    10       0    2    4    0    0    0   10
  7      1     1       5    0    4    8    0    0    1
         2     2       0    0    3    0    5    3    0
         3     8       0    9    3    0    5    1    0
  8      1     1       2   10    1    7    0    1    0
         2     1       0    0    5    0    0    1    0
         3     7       0   10    0    0    0    1    0
  9      1     4       4    0    4    0    0    0    9
         2     5       0    4    0    6    0    0    8
         3     6       0    4    0    0    6    7    0
 10      1     3       1    0    4    0    8    0    9
         2     5       0    4    0    0    6    8    0
         3     7       1    4    4    0    3    0    5
 11      1     3       0    0    3   10    0    6    0
         2     9       0    1    0    0    0    0    5
         3     9       0    0    0    0   10    0    4
 12      1     2       0    6    4    0    3    0    5
         2     3       3    0    0    9    0    0    2
         3     9       0    0    0    8    0    8    0
 13      1     1       0    4    0    0    0    0    9
         2     6      10    0    0    8    0    0    8
         3     8       0    0   10    8    7    0    5
 14      1     6       0    3    0    0    6    0    9
         2     8       4    0    0    0    0    4    0
         3     8       6    0    8    0    0    0    4
 15      1     1       4    0    4    9    9    9    0
         2     3       0    8    4    9    0    0    4
         3    10       0    6    0    8    8    9    0
 16      1     4       7    0    8    6    4    6    0
         2     5       0    0    4    5    0    2    0
         3    10       5    0    0    5    0    0    5
 17      1     1       3    7    0    8    0    0    9
         2     3       3    0    0    0   10    0    9
         3     8       2    5    5    4   10    0    9
 18      1     0       0    0    0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  R 4  R 5  N 1  N 2
   20   20   24   31   34   36   62
************************************************************************
