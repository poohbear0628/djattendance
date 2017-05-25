************************************************************************
file with basedata            : md85_.bas
initial value random generator: 83343132
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  14
horizon                       :  98
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     12      0       16        1       16
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           7   9  10
   3        3          3           5   6  10
   4        3          3           5   7   9
   5        3          1          11
   6        3          3           7   8  11
   7        3          1          12
   8        3          1          13
   9        3          2          12  13
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
  2      1     1       5    2    3    0
         2     5       4    1    0    7
         3     8       2    1    0    5
  3      1     3      10    9    0    3
         2     6       8    9    0    2
         3    10       3    8    0    1
  4      1     2       5    5   10    0
         2     8       4    4   10    0
         3    10       4    3   10    0
  5      1     5      10    5    5    0
         2     7       8    3    3    0
         3     9       4    2    0    1
  6      1     6       6    4    9    0
         2     7       6    2    0    5
         3     9       6    1    6    0
  7      1     3       8    7    3    0
         2     4       8    5    2    0
         3     4       8    5    0    9
  8      1     3       5    6    6    0
         2     5       4    4    0    6
         3     9       4    4    0    3
  9      1     5       5    7    7    0
         2     7       5    5    0    9
         3    10       5    3    2    0
 10      1     1       3    8    0    3
         2     3       3    7    5    0
         3     5       3    7    0    1
 11      1     2       9    2    8    0
         2     6       9    2    7    0
         3     8       8    1    5    0
 12      1     4       6   10    8    0
         2     8       6    7    7    0
         3    10       3    4    0    8
 13      1     1       7    8    0   10
         2     1       7    8   10    0
         3     6       6    7    0    9
 14      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   12   12   59   46
************************************************************************
