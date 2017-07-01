************************************************************************
file with basedata            : c2130_.bas
initial value random generator: 1545933026
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  133
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       21        3       21
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6   9  11
   3        3          3           6   8   9
   4        3          3           5   6  10
   5        3          3           7   8   9
   6        3          3           7  13  14
   7        3          3          15  16  17
   8        3          2          11  14
   9        3          3          12  13  16
  10        3          2          11  12
  11        3          3          13  16  17
  12        3          1          14
  13        3          1          15
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
  2      1     1       7    6   10    0
         2     3       5    6    8    0
         3    10       2    5    6    0
  3      1     1       9    7    9    0
         2     5       8    6    9    0
         3     9       6    3    0    1
  4      1     3       9    7   10    0
         2     4       6    7    9    0
         3     8       4    4    7    0
  5      1     4       8    9    0    7
         2     6       7    7    3    0
         3     9       7    5    0    5
  6      1     6       4    3    3    0
         2     7       3    3    3    0
         3     8       3    2    0    3
  7      1     2       8    4    0    8
         2     5       4    4    0    7
         3     6       3    3    9    0
  8      1     4       3    7    8    0
         2     7       3    7    5    0
         3    10       3    7    0   10
  9      1     5       6    5    7    0
         2     5       6    7    5    0
         3     7       6    3    0    7
 10      1     2      10    9    8    0
         2     8      10    8    3    0
         3    10      10    6    3    0
 11      1     7       4    7    0    4
         2     8       4    4   10    0
         3    10       4    2    3    0
 12      1     2      10    6    7    0
         2     5       6    5    0    2
         3    10       2    4    3    0
 13      1     1       7    9    8    0
         2     5       6    8    5    0
         3     8       4    6    0   10
 14      1     2      10    5    0    7
         2     2       6    5    3    0
         3     4       3    3    3    0
 15      1     2       2    6    8    0
         2     4       1    6    7    0
         3     6       1    5    5    0
 16      1     2       6    7    6    0
         2     4       5    4    0   10
         3     9       3    1    0   10
 17      1     1       7    7    3    0
         2     8       4    6    3    0
         3     9       3    6    0    2
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   18   15  112   71
************************************************************************
