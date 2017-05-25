************************************************************************
file with basedata            : c1518_.bas
initial value random generator: 1677983845
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  121
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       23       13       23
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           8  10
   3        3          1           5
   4        3          1           7
   5        3          1           6
   6        3          2          10  13
   7        3          3          15  16  17
   8        3          2           9  11
   9        3          2          12  17
  10        3          2          15  17
  11        3          1          13
  12        3          1          14
  13        3          1          14
  14        3          2          15  16
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     5       3    0    0    9
         2     9       0    7    0    7
         3    10       2    0    2    0
  3      1     2       7    0    0    7
         2     6       5    0    0    4
         3    10       5    0    7    0
  4      1     1       0    8    9    0
         2     1       5    0    0    8
         3     2       0    8    7    0
  5      1     6       3    0    9    0
         2     7       0   10    7    0
         3     8       1    0    0    3
  6      1     3       0    4    0    7
         2     5       6    0    5    0
         3    10       0    3    5    0
  7      1     4       6    0    0    4
         2     7       0   10    0    4
         3     8       0    3    7    0
  8      1     3       0    2    5    0
         2     3      10    0    0    7
         3     5      10    0    5    0
  9      1     7       0    5    6    0
         2     7       0    4    0    4
         3     9       0    2   10    0
 10      1     2       0   10    7    0
         2     2       0   10    0    4
         3     5       0    9    7    0
 11      1     2       4    0    9    0
         2     4       0    8    0    6
         3     7       2    0    0    5
 12      1     4       9    0    5    0
         2     5       0    2    0    9
         3     7       9    0    0    4
 13      1     5       9    0    0    9
         2    10       8    0    0    5
         3    10       9    0    6    0
 14      1     1       0    2    0    4
         2     2       5    0    5    0
         3     4       4    0    5    0
 15      1     3       0    3    0    3
         2     3       8    0    7    0
         3     9       6    0    6    0
 16      1     3       8    0    5    0
         2     3       0    8    4    0
         3     8       8    0    3    0
 17      1     4       0    4    0    7
         2     8       5    0    8    0
         3     9       2    0    0    7
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   16   18   80   68
************************************************************************
