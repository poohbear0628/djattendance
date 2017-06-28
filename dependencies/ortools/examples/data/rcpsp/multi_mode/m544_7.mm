************************************************************************
file with basedata            : cm544_.bas
initial value random generator: 1899451266
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  140
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       17       13       17
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        5          3           5   6   7
   3        5          2          12  16
   4        5          3           5   6  10
   5        5          2           9  12
   6        5          1           8
   7        5          3           9  10  12
   8        5          1          17
   9        5          3          11  13  15
  10        5          3          11  13  14
  11        5          1          16
  12        5          3          13  14  15
  13        5          1          17
  14        5          1          17
  15        5          1          18
  16        5          1          18
  17        5          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       0    4    4    2
         2     6       8    0    3    2
         3     6       0    3    3    2
         4     7       9    0    2    2
         5     9       0    1    1    2
  3      1     2       0    8    7    6
         2     3       0    7    6    5
         3     4       6    0    6    4
         4     6       0    6    6    4
         5     9       0    5    5    3
  4      1     7       0    8    9    5
         2     8       0    8    8    4
         3     9       0    7    7    3
         4    10       4    0    6    3
         5    10       5    0    4    2
  5      1     1       7    0    9    7
         2     2       5    0    9    6
         3     4       0    2    8    5
         4     7       0    1    7    4
         5     8       2    0    7    4
  6      1     1       0    4    5    8
         2     4       7    0    5    8
         3     5       0    4    4    7
         4     6       0    3    4    5
         5     7       0    3    3    3
  7      1     1       0    7    8   10
         2     1       4    0    9    8
         3     2       0    7    8    6
         4     7       4    0    7    2
         5     7       3    0    6    4
  8      1     4       8    0    8   10
         2     5       0    8    7   10
         3     6       7    0    7   10
         4     7       3    0    7   10
         5    10       0    6    6   10
  9      1     1       5    0    6    5
         2     3       4    0    5    4
         3     9       3    0    4    3
         4     9       4    0    3    4
         5    10       3    0    2    2
 10      1     1       0    5    3   10
         2     7       0    4    3   10
         3     7       0    5    2   10
         4     8       1    0    2   10
         5    10       1    0    1    9
 11      1     2       7    0   10    9
         2     7       0    7    9    8
         3     8       6    0    9    7
         4    10       6    0    8    6
         5    10       0    2    9    5
 12      1     1       0    5    7    7
         2     1       6    0    7    6
         3     3       4    0    7    6
         4     4       3    0    4    6
         5     5       1    0    3    4
 13      1     1       0   10    5    8
         2     2       0    8    3    8
         3     3       0    6    3    7
         4     6       0    4    3    7
         5     7       0    3    1    6
 14      1     3       0    8    6    8
         2     4       0    6    6    7
         3     5       6    0    6    4
         4     5      10    0    5    4
         5    10       0    6    5    1
 15      1     2       0    7    8    8
         2     2       7    0    7    8
         3     6       0    8    7    7
         4     8       0    7    7    7
         5     9       0    6    6    6
 16      1     3       0   10    5    8
         2     4       3    0    4    7
         3     6       2    0    4    7
         4     7       2    0    3    7
         5     9       1    0    3    6
 17      1     5       4    0    4    9
         2     5       0    5    4    8
         3     7       4    0    4    7
         4     8       4    0    2    7
         5    10       3    0    2    5
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   20   41   84   95
************************************************************************
