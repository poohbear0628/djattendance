************************************************************************
file with basedata            : cr146_.bas
initial value random generator: 331936496
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  122
RESOURCES
  - renewable                 :  1   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       18        0       18
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   6  10
   3        3          1          15
   4        3          3           5   6  10
   5        3          2           7  16
   6        3          3           8   9  12
   7        3          1           9
   8        3          3          11  13  14
   9        3          3          11  13  17
  10        3          2          11  14
  11        3          1          15
  12        3          2          13  14
  13        3          1          15
  14        3          2          16  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0
  2      1     4       8    4    7
         2     7       8    3    5
         3     8       6    3    2
  3      1     3       7    8    6
         2     3       7    7    9
         3     6       6    4    2
  4      1     2       8    8    7
         2     9       3    6    7
         3    10       2    6    7
  5      1     2       6    8    6
         2     5       6    5    4
         3     7       3    4    1
  6      1     1       8    6   10
         2     7       8    4    7
         3     9       7    3    7
  7      1     1       7    8    9
         2     9       5    7    7
         3    10       3    6    3
  8      1     1       8    8    8
         2     4       8    7    8
         3     6       7    5    8
  9      1     3      10   10    4
         2     5       5    9    4
         3     9       3    8    2
 10      1     1       6    9    8
         2     2       5    9    8
         3     3       3    9    7
 11      1     2       7    8    6
         2     3       7    6    5
         3     8       6    4    3
 12      1     3       9    9    7
         2     8       9    8    7
         3     9       8    7    2
 13      1     2       6    4    6
         2     3       4    4    6
         3     4       4    2    5
 14      1     4       4    9    5
         2     4       5    9    4
         3     7       2    7    3
 15      1     6       8    7   10
         2     7       7    6    9
         3     9       7    5    8
 16      1     5       3    8    5
         2     6       2    4    4
         3    10       2    2    3
 17      1     2       8    9    5
         2     2       7   10    5
         3     7       5    9    2
 18      1     0       0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  N 1  N 2
   16  104   89
************************************************************************
