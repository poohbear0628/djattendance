************************************************************************
file with basedata            : cn349_.bas
initial value random generator: 1133733565
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  125
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  3   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       18       10       18
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           5   6
   3        3          2           6   7
   4        3          2          11  14
   5        3          3           7   9  10
   6        3          3           8   9  14
   7        3          3           8  12  17
   8        3          2          15  16
   9        3          3          13  16  17
  10        3          2          12  14
  11        3          1          12
  12        3          1          13
  13        3          1          15
  14        3          2          16  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2  N 3
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0
  2      1     1       0    8    4    5    5
         2     7       6    0    4    5    5
         3     9       0    3    3    1    3
  3      1     2       9    0    7    6    6
         2     3       0    1    5    6    4
         3     3       8    0    7    3    5
  4      1     1       9    0    5    2    3
         2     6       5    0    5    2    2
         3     9       0    3    4    2    2
  5      1     2       0    5    2    3    3
         2     3       0    4    2    3    3
         3     6       0    3    1    3    3
  6      1     2       0    4    9    7    7
         2     4       0    3    7    6    7
         3     6       0    3    5    5    5
  7      1     4       0    7    7    9    8
         2     4       6    0    4   10    8
         3     9       0    6    3    5    8
  8      1     2       7    0    4    6    4
         2     4       0    1    4    6    4
         3     8       1    0    3    6    4
  9      1     4       0    8    7    5    2
         2     9       0    8    7    4    2
         3    10       0    5    5    4    2
 10      1     5       6    0    3    7    7
         2     6       0    9    3    5    6
         3     8       6    0    2    3    5
 11      1     3       0    5    5    9    3
         2     5       9    0    4    8    2
         3     6       0    4    4    7    2
 12      1     8       8    0    7    4    6
         2     9       6    0    4    3    4
         3     9       0    7    5    2    5
 13      1     1       0    6    5    6    8
         2     2       0    5    4    6    8
         3     4       4    0    2    4    7
 14      1     1       7    0    6    4    9
         2     9       0    6    6    4    9
         3    10       0    6    5    4    8
 15      1     1       4    0    4    3    9
         2     5       0    5    3    3    7
         3    10       1    0    3    3    7
 16      1     1       8    0    5    3    9
         2     1       0    6    5    4    9
         3     8       8    0    5    2    8
 17      1     4       0    9    4    4    6
         2     9       0    8    4    3    4
         3    10       0    6    1    2    3
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2  N 3
    6   11   77   78   90
************************************************************************
