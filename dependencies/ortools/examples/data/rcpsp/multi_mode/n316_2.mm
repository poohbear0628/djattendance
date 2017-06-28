************************************************************************
file with basedata            : cn316_.bas
initial value random generator: 1467199512
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  128
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  3   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       17       15       17
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   9  17
   3        3          3           7   8  12
   4        3          3           7   8  10
   5        3          3           6  10  15
   6        3          2           7   8
   7        3          1          13
   8        3          1          11
   9        3          3          11  14  15
  10        3          2          11  14
  11        3          1          13
  12        3          3          13  14  15
  13        3          1          16
  14        3          1          16
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2  N 3
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0
  2      1     2      10    8    5    3    0
         2     4       6    8    0    3    0
         3     8       4    7    3    3    0
  3      1     4       7    9    8    2    0
         2     7       5    8    0    2    0
         3     7       6    9    8    0    0
  4      1     1       9    1    0    9    0
         2     2       9    1   10    7    0
         3     8       8    1    0    6    0
  5      1     3       6    5    8    0    0
         2     5       5    4    7    0    0
         3    10       4    2    2    0    0
  6      1     1       6    6    9    0    6
         2     4       5    5    9    9    0
         3     9       3    5    9    0    6
  7      1     4       8    9    3    6    0
         2     4       6   10    0    9    9
         3    10       4    7    3    0    9
  8      1     3       7    6    0    0    4
         2     4       7    6    0    7    0
         3     9       6    6    0    7    0
  9      1     1       9    8    6    0    0
         2     4       8    6    5    3    9
         3     9       6    5    0    2    5
 10      1     4       3    9    0    0    4
         2     5       2    5    6    5    0
         3     5       2    8    0    0    3
 11      1     5       9    1    0    0    8
         2    10       8    1    5    0    0
         3    10       7    1    1    4    0
 12      1     2       2    7    0    6    0
         2     4       2    3    8    0    0
         3     5       1    1    8    0    4
 13      1     1       8    5    8    0    7
         2     5       8    5    7    0    5
         3    10       8    5    5    0    0
 14      1     2       7    5    6    3    8
         2     6       4    5    4    0    0
         3    10       2    5    0    0    6
 15      1     7      10   10    4    0    0
         2     9      10   10    0    4    7
         3    10      10    9    0    2    0
 16      1     2       5    8    0    9    8
         2     3       4    7    0    0    6
         3     6       2    7    2    0    0
 17      1     1       4    8    3    0    6
         2     1       5    7    3    6    0
         3     2       2    3    2    0    8
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2  N 3
   34   35   55   44   41
************************************************************************
