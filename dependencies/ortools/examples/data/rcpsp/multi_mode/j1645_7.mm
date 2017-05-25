************************************************************************
file with basedata            : md237_.bas
initial value random generator: 813572206
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  122
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       19       13       19
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6  10  12
   3        3          3           5  11  12
   4        3          3           8  13  16
   5        3          3           7  13  14
   6        3          2           9  11
   7        3          2           9  17
   8        3          1          10
   9        3          2          15  16
  10        3          2          11  14
  11        3          1          15
  12        3          2          13  16
  13        3          2          15  17
  14        3          1          17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     3      10    4    6    6
         2     3       6    5    7    6
         3     5       4    2    3    5
  3      1     3       7   10    7    8
         2     7       7    9    5    5
         3     8       4    9    2    4
  4      1     4       3    4    8   10
         2     9       2    4    8   10
         3    10       1    2    8   10
  5      1     3       8    6    7    6
         2     7       7    4    6    6
         3     7       6    5    4    3
  6      1     6       7    7    8    6
         2     8       5    6    6    4
         3    10       4    6    5    3
  7      1     5       9   10    7    5
         2     8       4    5    7    4
         3     8       7    6    6    3
  8      1     1       7    6    7   10
         2     2       7    6    6    9
         3     6       6    3    6    8
  9      1     3       6    7    6    4
         2     5       3    5    5    4
         3     7       3    4    3    4
 10      1     2      10    6    2    6
         2     3       9    4    1    6
         3     9       8    4    1    5
 11      1     2       7    6    6    8
         2     2       7    5    8    7
         3     6       6    3    5    6
 12      1     1       6    8    9    7
         2     3       5    1    8    7
         3     3       5    5    5    6
 13      1     6      10    5    6    5
         2     6      10    5    5    7
         3    10      10    5    5    3
 14      1     3       9    8    3    9
         2     4       8    4    3    8
         3     6       7    4    2    7
 15      1     5       7    9    8    9
         2     6       5    8    8    7
         3    10       4    7    7    3
 16      1     4       9    8    6    5
         2     7       6    4    4    4
         3     8       5    1    2    2
 17      1     5       7    6    5    7
         2     7       5    6    4    5
         3     9       4    5    2    4
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   17   14   85   95
************************************************************************
