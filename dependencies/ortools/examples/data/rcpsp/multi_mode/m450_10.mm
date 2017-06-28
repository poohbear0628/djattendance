************************************************************************
file with basedata            : cm450_.bas
initial value random generator: 537782191
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  138
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       17       11       17
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        4          3           8  11  13
   3        4          3           8   9  10
   4        4          3           5   8  17
   5        4          2           6   7
   6        4          3           9  10  11
   7        4          2          14  15
   8        4          1          16
   9        4          3          12  13  15
  10        4          2          12  13
  11        4          2          12  15
  12        4          1          14
  13        4          1          14
  14        4          1          16
  15        4          1          18
  16        4          1          18
  17        4          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     5       0    4    6    6
         2     5       0    2    6    7
         3     5       8    0    6    6
         4     9       3    0    6    4
  3      1     3       0    7    9    5
         2     4       5    0    7    4
         3     5       0    7    5    2
         4     6       0    6    4    2
  4      1     1       8    0    2    8
         2     5       0    4    2    7
         3     8       7    0    1    7
         4    10       0    3    1    7
  5      1     4       7    0    4   10
         2     5       5    0    3    8
         3     6       4    0    3    8
         4     8       0    6    2    5
  6      1     2       8    0    6    9
         2     3       0    7    6    5
         3     6       0    2    5    5
         4     8       7    0    5    2
  7      1     2       6    0    3   10
         2     3       0    8    3    9
         3     7       0    6    2    9
         4    10       2    0    2    7
  8      1     2       0    3    7    7
         2     5       7    0    7    7
         3     6       0    2    4    6
         4     8       5    0    4    4
  9      1     4       0   10    8    7
         2     6       8    0    6    5
         3     7       0   10    2    5
         4     7       8    0    3    5
 10      1     1       6    0    3    4
         2     5       0    2    2    4
         3    10       3    0    1    3
         4    10       0    2    1    3
 11      1     1       4    0    6    4
         2     8       4    0    5    3
         3     9       0    2    4    2
         4    10       3    0    3    1
 12      1     1      10    0    7    5
         2     6       0    5    7    5
         3     8       8    0    4    5
         4    10       6    0    2    4
 13      1     1       8    0    8    7
         2     5       5    0    8    7
         3     8       0    3    7    6
         4    10       0    2    7    5
 14      1     1       0    4    8    1
         2     3       6    0    8    1
         3     5       0    3    5    1
         4     9       3    0    5    1
 15      1     1       6    0    2    8
         2     2       0    7    2    8
         3     4       0    4    2    8
         4     7       0    2    2    8
 16      1     4      10    0    6   10
         2     5       0    7    5    9
         3     5       0    6    6    9
         4     7       0    4    5    8
 17      1     2       9    0    6    7
         2     3       5    0    5    5
         3     7       0    3    5    3
         4     9       0    1    3    3
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   15    8   82   99
************************************************************************
