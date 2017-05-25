************************************************************************
file with basedata            : cm428_.bas
initial value random generator: 103422516
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  147
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       17        8       17
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        4          3           7   9  13
   3        4          3           5  10  17
   4        4          2           8   9
   5        4          3           6   8  11
   6        4          2          12  16
   7        4          2          10  17
   8        4          2          12  13
   9        4          2          11  14
  10        4          2          11  16
  11        4          1          12
  12        4          1          15
  13        4          2          15  16
  14        4          2          15  17
  15        4          1          18
  16        4          1          18
  17        4          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       0    8    4    0
         2     5       0    6    0    6
         3     8       6    0    0    4
         4    10       4    0    0    2
  3      1     7       0    7    6    0
         2     8       0    6    3    0
         3     9       0    5    0    3
         4     9       8    0    0    1
  4      1     3       0    8    7    0
         2     4       0    7    1    0
         3     8       0    4    0   10
         4     9       6    0    0    8
  5      1     3       6    0    6    0
         2     3       0   10    0   10
         3     8       7    0    0   10
         4    10       4    0    0   10
  6      1     2       6    0    6    0
         2     4       0    9    0   10
         3     5       5    0    0    9
         4     7       0    5    0    8
  7      1     5       0    7    3    0
         2     5       0    8    0    6
         3     6       0    5    0    4
         4    10       0    2    0    3
  8      1     1       9    0    0    8
         2     6       0    6    0    7
         3     6       0    7    7    0
         4     9       0    4    0    8
  9      1     3       9    0    6    0
         2     9       0    3    0    3
         3     9       0    6    2    0
         4     9       9    0    3    0
 10      1     2       6    0    0    8
         2     5       0    7    0    6
         3     6       0    7    3    0
         4    10       6    0    0    5
 11      1     1       7    0    4    0
         2     1       8    0    0    8
         3     2       6    0    0    7
         4     6       2    0    0    6
 12      1     2       0    5    0    3
         2     5       8    0    0    3
         3     7       6    0    0    3
         4    10       5    0    5    0
 13      1     5       4    0    7    0
         2     7       0    7    0    5
         3     7       4    0    5    0
         4     9       4    0    0    7
 14      1     3       9    0    0    3
         2     4       0    8    7    0
         3     6       0    8    6    0
         4    10       5    0    6    0
 15      1     1       0    6    7    0
         2     4       0    5    7    0
         3     8       0    3    6    0
         4    10       4    0    5    0
 16      1     1       0    4    0    1
         2     7       0    4    6    0
         3    10       0    3    0    1
         4    10      10    0    6    0
 17      1     3       6    0    0    7
         2     5       4    0    1    0
         3     6       0    7    0    7
         4     9       0    4    1    0
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   29   29   85   93
************************************************************************
