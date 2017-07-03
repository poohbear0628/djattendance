************************************************************************
file with basedata            : cn158_.bas
initial value random generator: 2049003270
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  127
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  1   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       22        0       22
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           6   8
   3        3          3           8  13  17
   4        3          3           5   8   9
   5        3          3           6  10  11
   6        3          2           7  17
   7        3          2          14  16
   8        3          2          15  16
   9        3          3          10  11  14
  10        3          1          12
  11        3          2          13  17
  12        3          2          13  15
  13        3          1          16
  14        3          1          15
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1
------------------------------------------------------------------------
  1      1     0       0    0    0
  2      1     3       0    9    7
         2     8       0    9    6
         3     9       2    0    6
  3      1     5       4    0    7
         2     6       0    5    5
         3     9       4    0    4
  4      1     3       5    0    8
         2     7       0    9    7
         3     8       0    5    4
  5      1     3       3    0    4
         2     4       3    0    2
         3     9       0    4    2
  6      1     3       0    7    5
         2     4       2    0    5
         3     7       0    4    5
  7      1     1       0    4    9
         2     6       5    0    6
         3    10       0    3    4
  8      1     3       0    9    7
         2     8       0    6    3
         3     8       8    0    4
  9      1     2       0    8    4
         2     4       2    0    3
         3     7       0    4    3
 10      1     4       0   10    7
         2     5       0    6    7
         3    10       5    0    7
 11      1     2       4    0    9
         2     4       0    5    9
         3     9       4    0    8
 12      1     3       0    5    9
         2     5       2    0    5
         3     7       2    0    1
 13      1     2       0    4    8
         2     7       6    0    6
         3     8       0    3    2
 14      1     2       4    0    9
         2     5       0    6    6
         3     8       3    0    5
 15      1     2       0   10    9
         2     2       6    0    5
         3     5       0   10    3
 16      1     7       0    6    7
         2     9       8    0    6
         3     9       0    4    6
 17      1     3       7    0    6
         2     4       4    0    5
         3     4       0    5    3
 18      1     0       0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1
   13   12  115
************************************************************************