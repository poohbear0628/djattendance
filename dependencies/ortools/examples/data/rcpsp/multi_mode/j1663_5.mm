************************************************************************
file with basedata            : md255_.bas
initial value random generator: 1842549
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  118
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       15       13       15
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2          10  15
   3        3          3           6   8  10
   4        3          3           5   6   7
   5        3          2           8  11
   6        3          1           9
   7        3          2          10  13
   8        3          2           9  12
   9        3          3          13  14  16
  10        3          1          16
  11        3          1          12
  12        3          3          13  14  16
  13        3          2          15  17
  14        3          2          15  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     5       4    8    7    6
         2     6       4    6    5    3
         3    10       2    2    4    2
  3      1     2       8    2    8    3
         2     4       6    2    8    3
         3     9       5    1    6    2
  4      1     3       7    8    5    9
         2     6       6    8    5    9
         3     7       3    7    4    9
  5      1     1       4    7    8    5
         2     4       2    5    3    5
         3     4       3    5    2    5
  6      1     1       5   10    8    7
         2     9       2    6    6    6
         3    10       2    2    4    6
  7      1     1       8    8    8    7
         2     2       6    6    5    7
         3     8       5    3    4    7
  8      1     3       5    8    7    3
         2     6       5    7    4    2
         3     7       4    7    3    1
  9      1     4       8    4   10    9
         2     6       8    4    9    7
         3     7       7    3    9    6
 10      1     1       9    7    5    5
         2     3       9    6    5    5
         3     5       9    6    4    4
 11      1     1       9   10    9    3
         2     4       6   10    9    2
         3     9       5   10    8    2
 12      1     3       9    9    6    7
         2     4       7    5    6    6
         3     5       7    3    4    3
 13      1     1       4    4   10    8
         2     2       3    3    9    5
         3     4       1    1    8    3
 14      1     2       5    7    5    9
         2     7       4    4    2    7
         3     7       4    5    2    6
 15      1     2       5   10    8    4
         2     7       4    9    4    4
         3     8       4    7    3    3
 16      1     3       2   10    9    9
         2     5       2    5    9    8
         3     9       2    3    9    7
 17      1     1       9    9    7   10
         2     3       8    8    5    9
         3     9       8    5    2    9
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   18   27  120  104
************************************************************************
