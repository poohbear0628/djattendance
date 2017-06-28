************************************************************************
file with basedata            : cr419_.bas
initial value random generator: 5409
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  138
RESOURCES
  - renewable                 :  4   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       16        1       16
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2          11  12
   3        3          3           6   8  14
   4        3          3           5   7  14
   5        3          3           6  10  11
   6        3          1          17
   7        3          1           9
   8        3          2          10  13
   9        3          3          10  11  13
  10        3          1          12
  11        3          2          16  17
  12        3          1          15
  13        3          3          15  16  17
  14        3          2          15  16
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  R 4  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0    0
  2      1     4       7    0    0    0    3    0
         2     8       0    0    0    3    0    8
         3    10       0    5    8    0    0    2
  3      1     1       0   10    8    5    2    0
         2     6       3    0    0    0    2    0
         3     7       0   10    6    0    0    2
  4      1     2       0    9    0    5    0   10
         2     3       0    0    5    0    8    0
         3     7       2    4    3    0    5    0
  5      1     2       0    0    0    1    7    0
         2     6       3    5    0    0    0    4
         3     8       0    5    0    0    5    0
  6      1     2       0    7    1    4    0    5
         2     8       3    0    0    0    5    0
         3    10       3    7    0    0    0    1
  7      1     1       5    9    7    0    4    0
         2     2       3    8    6    0    0   10
         3     8       0    0    3    8    0    9
  8      1     7       9    0    0    9    0    9
         2     8       0    0    5    8    4    0
         3     8       7    0    4    8    9    0
  9      1     5       0   10    0    4    6    0
         2     5       8   10    9    5    0   10
         3    10       5   10    1    0    0   10
 10      1     2       5    0    0    0    0    2
         2     3       4    7    7    0    0    2
         3     7       0    0    0    6    0    2
 11      1     1       7    4    0    8    0    8
         2     2       3    4   10    3    0    6
         3    10       0    0   10    0    0    5
 12      1     1       0    0    2    0    0    7
         2     4       0    1    0    0    4    0
         3     6       9    0    0    8    2    0
 13      1     1       0    8   10    0    5    0
         2     2       5    8    0    0    5    0
         3    10       0    0    6    0    5    0
 14      1     5       3    7    5    0    0    5
         2     6       0    0    0    4    0    5
         3     7       3    4    3    0    5    0
 15      1     3       9    4    0    0    0    8
         2     6       0    0    0    8    5    0
         3    10       8    1    0    0    0    5
 16      1     7       0   10    0    0    6    0
         2     8       1    0    7    1    5    0
         3    10       0   10    0    1    3    0
 17      1     5       4    7    9    5    8    0
         2     8       0    0    0    2    5    0
         3    10       0    7    0    0    0    1
 18      1     0       0    0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  R 4  N 1  N 2
   17   23   22   23   60   69
************************************************************************
