************************************************************************
file with basedata            : md106_.bas
initial value random generator: 203851114
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
    1     12      0       10        8       10
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   6  11
   3        3          3           5   7  10
   4        3          1           9
   5        3          2           8  12
   6        3          3           8   9  12
   7        3          3           8   9  11
   8        3          1          13
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
  2      1     1       7    0    7    4
         2     1       0    1    7    5
         3     8       5    0    4    4
  3      1     1       0   10    9    8
         2     3       0   10    9    4
         3     6       0   10    9    1
  4      1     5       7    0    6    7
         2     7       0    3    5    6
         3     9       4    0    3    6
  5      1     5       7    0   10    8
         2     6       0    8    9    6
         3    10       7    0    6    3
  6      1     3       0    6    7    2
         2     4       6    0    6    2
         3    10       3    0    5    1
  7      1     4       6    0    7    7
         2     9       0    6    3    5
         3    10       4    0    2    4
  8      1     2       4    0    7    5
         2     5       4    0    6    5
         3    10       1    0    5    4
  9      1     3       4    0    4    6
         2     7       0    9    3    4
         3     9       4    0    2    3
 10      1     1      10    0    7    7
         2     1       0    7    6    7
         3     5       9    0    5    4
 11      1     2       0    6    2   10
         2     3       0    4    2    4
         3     3       7    0    2    1
 12      1     3       0    6    9    3
         2     6       0    3    6    3
         3     8       2    0    3    2
 13      1     2       0    9    6    8
         2     5       5    0    5    8
         3     7       0    7    5    8
 14      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   19   20   66   59
************************************************************************
