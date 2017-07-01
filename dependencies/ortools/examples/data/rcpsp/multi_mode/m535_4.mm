************************************************************************
file with basedata            : cm535_.bas
initial value random generator: 1282360210
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  143
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       21       10       21
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        5          1           5
   3        5          3           6  10  13
   4        5          3           7   8  10
   5        5          1           9
   6        5          2          15  16
   7        5          2           9  11
   8        5          3           9  11  15
   9        5          2          12  13
  10        5          2          12  14
  11        5          2          12  13
  12        5          2          16  17
  13        5          1          17
  14        5          3          15  16  17
  15        5          1          18
  16        5          1          18
  17        5          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     4       0    7    8    5
         2     7       1    0    7    4
         3     7       0    7    7    4
         4     9       0    7    5    3
         5    10       0    6    2    2
  3      1     2       8    0    8    7
         2     2       0    6    8    7
         3     6       8    0    8    6
         4     7       7    0    8    5
         5    10       4    0    8    4
  4      1     5       8    0    8    6
         2     7       0    3    7    5
         3     8       7    0    5    5
         4     8       6    0    6    5
         5     9       5    0    4    5
  5      1     7       0   10    8    2
         2     7       6    0    9    2
         3     9       0   10    7    1
         4     9       0    9    6    2
         5    10       6    0    5    1
  6      1     1       7    0    7    7
         2     1       0    6    7    8
         3     2       6    0    7    6
         4     3       0    4    6    6
         5     8       0    3    6    5
  7      1     3       5    0    6    4
         2     4       5    0    5    4
         3     6       4    0    3    3
         4     7       0    5    2    2
         5     9       3    0    2    2
  8      1     2       0    7    8    2
         2     2       7    0    8    2
         3     4       5    0    8    2
         4     8       0    8    7    2
         5     8       4    0    8    2
  9      1     4       9    0    8    7
         2     5       0    6    7    6
         3     5       7    0    7    4
         4     8       5    0    7    4
         5     8       0    6    7    4
 10      1     2       9    0    8    7
         2     2       0    8    7    7
         3     5       9    0    6    6
         4     5       9    0    4    7
         5     8       0    6    3    6
 11      1     3       6    0    9    7
         2     5       5    0    4    6
         3     5       0    8    4    6
         4    10       0    4    3    6
         5    10       4    0    3    6
 12      1     2       6    0    8    9
         2     3       0    7    8    9
         3     6       0    4    6    9
         4     7       2    0    5    9
         5     7       0    3    5    9
 13      1     1       2    0    5    1
         2     2       0    6    4    1
         3     7       0    5    4    1
         4     9       2    0    4    1
         5     9       0    3    4    1
 14      1     4       0    7    9    7
         2     4       0    7    8    8
         3     7       6    0    7    7
         4     8       0    5    5    6
         5    10       0    4    4    4
 15      1     6       0    4    7    2
         2     6       0    4    6    3
         3     6       9    0    6    3
         4     7       6    0    6    2
         5     8       0    4    4    2
 16      1     1       0    8    9    8
         2     2       6    0    9    7
         3     6       0    6    8    6
         4     7       5    0    7    6
         5     9       4    0    5    4
 17      1     4       7    0    3    6
         2     5       0    8    3    6
         3     8       0    8    3    5
         4    10       6    0    2    5
         5    10       0    7    2    5
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   17   23   83   69
************************************************************************
