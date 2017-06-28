************************************************************************
file with basedata            : cm447_.bas
initial value random generator: 574323097
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  128
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       22       12       22
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        4          3           5  13  14
   3        4          3           8  10  13
   4        4          3           7   9  11
   5        4          3           6   8  17
   6        4          1          12
   7        4          3          14  15  17
   8        4          2           9  11
   9        4          1          16
  10        4          3          11  12  14
  11        4          1          15
  12        4          2          15  16
  13        4          1          17
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
  2      1     6       6    6    3   10
         2     7       5    6    3    9
         3     8       5    6    2    8
         4     9       5    6    1    8
  3      1     1       6    8    5    8
         2     6       5    7    5    7
         3     6       6    5    5    7
         4     9       3    5    3    6
  4      1     2       5   10    9    8
         2     9       5    9    8    6
         3     9       5    9    9    5
         4    10       4    8    7    4
  5      1     2       8    4    3    8
         2     3       7    4    2    7
         3     5       5    4    2    7
         4     6       3    4    1    6
  6      1     7       8    6    7   10
         2     7       7    6    8   10
         3     8       6    4    7    9
         4    10       4    2    5    9
  7      1     2       7    9    5    8
         2     3       6    8    4    7
         3     6       4    8    2    4
         4     7       4    6    1    2
  8      1     6       6    6    7   10
         2     9       2    5    4    9
         3     9       4    4    6   10
         4     9       5    3    5   10
  9      1     3       8    9    9    5
         2     5       6    8    9    3
         3     5       8    7    8    4
         4     7       6    7    8    2
 10      1     1       7    9   10    6
         2     1       7    9    8    8
         3     7       7    8    8    2
         4     7       7    9    6    2
 11      1     1       9    9    8    7
         2     2       8    6    8    6
         3     6       8    4    8    5
         4    10       8    3    8    3
 12      1     2       3   10    6    9
         2     6       2    9    3    6
         3     8       1    9    3    4
         4     8       1    9    2    6
 13      1     5       7    7    9    5
         2     6       5    5    6    3
         3     6       5    4    6    4
         4     9       3    3    6    1
 14      1     2       4    6    9    9
         2     3       3    3    8    5
         3     3       3    4    8    4
         4     4       2    2    8    3
 15      1     4       9    7    8    8
         2     6       8    6    6    8
         3     7       5    6    4    7
         4     8       4    4    2    7
 16      1     5       3    8   10    6
         2     7       3    8    5    3
         3     7       1    5    7    4
         4     7       2    5    6    3
 17      1     4       2    9    7   10
         2     5       2    9    6    7
         3     7       2    8    5    4
         4     8       2    7    4    3
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   22   27   94  101
************************************************************************
