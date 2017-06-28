************************************************************************
file with basedata            : mm26_.bas
initial value random generator: 1551061939
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  12
horizon                       :  86
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     10      0       11        1       11
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           6   7
   3        3          2           7   9
   4        3          3           5   7  11
   5        3          2           6  10
   6        3          1           8
   7        3          1          10
   8        3          1           9
   9        3          1          12
  10        3          1          12
  11        3          1          12
  12        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       8    0    9    0
         2     4       0    8    0    8
         3     6       6    0    0    4
  3      1     3       0    8    0   10
         2     8       5    0    9    0
         3    10       0    6    0   10
  4      1     1       8    0    3    0
         2     7       5    0    2    0
         3    10       0    3    2    0
  5      1     1       0    8    0   10
         2     6       0    6    9    0
         3     9       0    1    0    8
  6      1     5       7    0    0    9
         2     7       0    1    0    8
         3    10       0    1    0    6
  7      1     1       0    2    0    2
         2     1       9    0    0    3
         3     7       6    0    0    2
  8      1     3       0    7    9    0
         2     4      10    0    0    4
         3     7       0    4    0    3
  9      1     1       0    7    7    0
         2     3       0    6    6    0
         3     8       0    3    0    7
 10      1     1       8    0    8    0
         2     2       8    0    0    8
         3    10       6    0    0    4
 11      1     2       0   10    0    3
         2     6       2    0    4    0
         3     9       0    6    0    2
 12      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   21   20   30   35
************************************************************************
