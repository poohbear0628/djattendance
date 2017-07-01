************************************************************************
file with basedata            : mm22_.bas
initial value random generator: 1257526401
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  12
horizon                       :  75
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     10      0       10        3       10
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   8   9
   3        3          1           6
   4        3          2           7  11
   5        3          2          10  11
   6        3          1           9
   7        3          2           9  10
   8        3          1          11
   9        3          1          12
  10        3          1          12
  11        3          1          12
  12        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     2       0    9    9    8
         2     5       6    0    8    3
         3     5       0    3    8    4
  3      1     1       0    5    7    7
         2     8       0    5    6    7
         3    10       4    0    5    5
  4      1     5       0    7    6    6
         2     5       1    0    7    5
         3     8       0    6    5    5
  5      1     3       7    0    4    4
         2     4       0    5    3    2
         3    10       0    4    2    1
  6      1     3       0    7    8    7
         2     5       4    0    8    7
         3     6       0    6    5    6
  7      1     1       5    0    2    9
         2     3       0    8    1    5
         3     7       1    0    1    2
  8      1     1      10    0    7    7
         2     6       0    4    6    5
         3     7       0    4    6    3
  9      1     1       7    0    5    8
         2     1       0   10    4    8
         3     5       7    0    1    7
 10      1     3       0    6    9    2
         2     8      10    0    7    1
         3     8       0    6    7    1
 11      1     5       0    7    7    5
         2     8       0    7    7    3
         3     9       3    0    5    3
 12      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   18   16   55   50
************************************************************************
