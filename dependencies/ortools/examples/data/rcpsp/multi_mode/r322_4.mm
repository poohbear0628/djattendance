************************************************************************
file with basedata            : cr322_.bas
initial value random generator: 362298295
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  133
RESOURCES
  - renewable                 :  3   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       30       14       30
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   6  12
   3        3          3          15  16  17
   4        3          3           5   7   8
   5        3          3          13  14  17
   6        3          1           9
   7        3          2          12  13
   8        3          3           9  12  17
   9        3          2          10  11
  10        3          1          13
  11        3          1          14
  12        3          2          14  16
  13        3          2          15  16
  14        3          1          15
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0
  2      1     5       8    4    7    0    3
         2     6       7    4    7    9    0
         3     7       3    4    7    5    0
  3      1     2       7    3    7    4    0
         2     7       7    2    6    2    0
         3    10       7    2    5    1    0
  4      1     6       8    8    6   10    0
         2     8       8    8    5   10    0
         3    10       8    8    5    0    8
  5      1     7       3    7    5    0    7
         2     8       3    6    4    0    5
         3     8       2    7    4    3    0
  6      1     7       4    8    3    3    0
         2     8       3    5    3    3    0
         3     8       4    6    3    2    0
  7      1     2       8    8    9    0    7
         2     8       8    6    9    9    0
         3     9       7    5    9    0    6
  8      1     2       9    8    7    0    4
         2     3       9    7    7    0    4
         3     4       7    6    7   10    0
  9      1     4       9   10    8    8    0
         2     5       9   10    4    8    0
         3     5       8    9    5    8    0
 10      1     1       6    9    5    0    7
         2     5       5    8    5    6    0
         3     6       5    7    5    4    0
 11      1     5       9    8    2    0    7
         2     6       8    7    2    0    5
         3     8       8    6    2    7    0
 12      1     2       7    7   10    0   10
         2     3       5    6    8    4    0
         3    10       3    6    3    0    9
 13      1     6       7    2    4    0    4
         2    10       6    2    1    0    1
         3    10       6    1    3    0    1
 14      1     2       6    6    8    0    6
         2     4       6    3    8    0    3
         3     9       6    3    5    0    2
 15      1     6      10    3    7    0    2
         2     7       7    2    6    0    2
         3    10       3    2    4    0    2
 16      1     7       6    9    8    5    0
         2     8       6    9    7    0    3
         3    10       6    9    6    5    0
 17      1     2       8    7    8    4    0
         2     3       6    7    7    0    9
         3     9       4    5    7    0    5
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  N 1  N 2
   16   20   17   64   59
************************************************************************
