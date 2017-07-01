************************************************************************
file with basedata            : md78_.bas
initial value random generator: 1258429780
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  14
horizon                       :  95
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     12      0       18        4       18
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   6   8
   3        3          3           7   8  11
   4        3          3           7   8  11
   5        3          2           9  10
   6        3          2           7  10
   7        3          2           9  12
   8        3          1           9
   9        3          1          13
  10        3          3          11  12  13
  11        3          1          14
  12        3          1          14
  13        3          1          14
  14        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     3       3    8    7    0
         2     5       3    6    6    0
         3     6       3    3    0    5
  3      1     5       8    8    8    0
         2     7       8    8    7    0
         3     9       7    7    7    0
  4      1     8       4    2    2    0
         2     8       3    2    8    0
         3     8       3    1    0    5
  5      1     3       9    2    7    0
         2     4       9    2    0    3
         3    10       7    1    0    2
  6      1     4       8    8    4    0
         2     7       5    7    4    0
         3     9       5    5    4    0
  7      1     2       9    4    0    3
         2     6       8    3   10    0
         3     9       5    2    8    0
  8      1     1       7    8    0    8
         2     4       6    8    0    4
         3     6       5    5    0    4
  9      1     5       7    9    0    9
         2     9       7    9    7    0
         3    10       6    9    7    0
 10      1     1       6    6    0    6
         2     5       6    6    0    5
         3     6       6    6    0    3
 11      1     7       6    6    8    0
         2     7       6    4    9    0
         3     7       7    6    0    9
 12      1     2       6    5    0    9
         2     3       4    3    7    0
         3     5       2    1    6    0
 13      1     3       8    9    0    8
         2     6       7    9    0    4
         3    10       5    8    8    0
 14      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   18   15   43   36
************************************************************************
