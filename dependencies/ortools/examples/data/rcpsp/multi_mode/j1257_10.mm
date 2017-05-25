************************************************************************
file with basedata            : md121_.bas
initial value random generator: 1313106533
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  14
horizon                       :  99
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     12      0       17       11       17
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   7  13
   3        3          3           6   8  10
   4        3          3           5   6   8
   5        3          1          12
   6        3          3           9  11  13
   7        3          2           8  10
   8        3          2           9  11
   9        3          1          12
  10        3          2          11  12
  11        3          1          14
  12        3          1          14
  13        3          1          14
  14        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       0    5    8    8
         2     4       7    0    8    7
         3     8       0    3    7    6
  3      1     2       0    9   10   10
         2     6       7    0   10    7
         3     7       0    5   10    5
  4      1     4       9    0    4    9
         2     7       0    4    4    8
         3     9       9    0    4    8
  5      1     3       0    6    7    8
         2     5       6    0    6    8
         3     8       2    0    5    7
  6      1     3       6    0    8    8
         2     8       5    0    8    8
         3    10       0    4    8    5
  7      1     3       4    0    3    4
         2     5       0    2    3    3
         3     5       0    4    2    3
  8      1     1       0    6    4    4
         2     4       6    0    3    4
         3     6       0    4    2    3
  9      1     6       2    0    7    8
         2     7       0    6    6    7
         3     8       0    3    6    6
 10      1     3       6    0    6    7
         2     6       0    7    4    6
         3     9       4    0    3    3
 11      1     6       0    4    8    9
         2     8       0    3    5    8
         3     9       0    3    2    8
 12      1     4       0    5    6    2
         2     9       0    4    6    2
         3    10       0    3    5    1
 13      1     3       9    0    6    9
         2     7       0    4    6    9
         3    10       7    0    4    8
 14      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
    6    8   77   86
************************************************************************
