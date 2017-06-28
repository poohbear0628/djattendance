************************************************************************
file with basedata            : cn360_.bas
initial value random generator: 1853150367
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  139
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  3   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       26        2       26
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6   7  16
   3        3          3           7  14  16
   4        3          3           5   8   9
   5        3          3           6  10  11
   6        3          1          12
   7        3          3           8   9  15
   8        3          1          10
   9        3          1          17
  10        3          1          13
  11        3          3          13  14  16
  12        3          2          13  15
  13        3          1          17
  14        3          2          15  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2  N 3
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0
  2      1     2       3    0    8    9    6
         2     3       2    0    5    6    6
         3     8       0    7    5    6    6
  3      1     2       5    0    3    8    3
         2     4       2    0    2    6    3
         3     6       0    7    2    6    2
  4      1     5       0    3    7    6    9
         2     7       0    3    7    3    6
         3     7       9    0    7    5    8
  5      1     8       0    8    9    6    6
         2    10       7    0    6    5    5
         3    10       0    6    6    6    5
  6      1     6       8    0   10    8    8
         2     7       8    0    7    5    8
         3     7       0    1    8    6    8
  7      1     5       1    0    6   10    3
         2     9       1    0    6    8    2
         3    10       1    0    3    6    2
  8      1     6       8    0    7   10   10
         2    10       0    7    3    9    9
         3    10       7    0    2    8   10
  9      1     3      10    0    6    7    8
         2     7       7    0    5    7    8
         3     7       5    0    6    7    6
 10      1     5       0    4    9    9    8
         2     6       6    0    9    9    4
         3     8       4    0    9    8    1
 11      1     1       0    2    4   10    5
         2     7       0    2    4    9    5
         3    10       0    1    4    9    4
 12      1     1       0    4    4    4    5
         2     6       4    0    3    4    4
         3    10       3    0    3    4    3
 13      1     1       6    0    4    7    4
         2     7       0    2    4    6    4
         3    10       4    0    3    6    3
 14      1     6       5    0    8    9    8
         2     9       0   10    7    6    5
         3     9       3    0    7    7    5
 15      1     1       8    0    6    7    8
         2     6       8    0    5    6    7
         3     9       7    0    3    5    7
 16      1     1       0    6    7    9    6
         2    10       2    0    4    8    4
         3    10       0    6    2    9    5
 17      1     5       4    0    8    8   10
         2     7       0    2    6    7    8
         3     8       1    0    6    5    7
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2  N 3
   25   24  106  127  107
************************************************************************
