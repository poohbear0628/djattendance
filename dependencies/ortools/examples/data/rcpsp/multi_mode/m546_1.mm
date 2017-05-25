************************************************************************
file with basedata            : cm546_.bas
initial value random generator: 23426
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  145
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       12       12       12
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        5          3           5   7   9
   3        5          2           8  10
   4        5          3           5   6   7
   5        5          3           8  10  11
   6        5          1          17
   7        5          3          11  12  14
   8        5          1          16
   9        5          2          11  13
  10        5          3          14  15  16
  11        5          2          15  17
  12        5          1          15
  13        5          2          14  16
  14        5          1          17
  15        5          1          18
  16        5          1          18
  17        5          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       7    7    7    7
         2     2       6    6    5    5
         3     2       5    7    7    5
         4     9       4    6    4    3
         5    10       4    6    2    3
  3      1     4       7    7    7    8
         2     4       7    6    8    7
         3     4       6    7    7    9
         4     8       6    5    7    7
         5     9       4    4    4    3
  4      1     1       3   10    3    5
         2     4       3    7    3    4
         3     4       3    8    2    4
         4     5       2    6    2    2
         5     9       2    2    2    1
  5      1     1       7    8    8    6
         2     3       7    6    6    6
         3     4       5    6    6    6
         4     8       5    5    6    5
         5     9       4    4    5    5
  6      1     3       6    3    7    4
         2     3       7    3    7    3
         3     3       6    4    7    3
         4     5       4    3    7    2
         5    10       4    2    7    2
  7      1     1       7   10    3    1
         2     2       7    9    2    1
         3     3       6    8    2    1
         4     5       6    8    1    1
         5     7       5    7    1    1
  8      1     2      10   10    4    7
         2     2       9   10    4    8
         3     5       9    9    4    7
         4     7       7    9    3    7
         5     8       4    8    3    5
  9      1     2       5    9   10    5
         2     4       3    7    8    4
         3     4       4    6    8    4
         4    10       3    5    7    2
         5    10       2    3    8    2
 10      1     2       8    9    6    8
         2     2       7    9    6    9
         3     5       7    9    5    7
         4     6       5    9    4    3
         5     8       2    9    3    2
 11      1     1       9    5    8    6
         2     7       6    4    7    6
         3     7       8    5    6    6
         4     9       5    3    3    5
         5    10       2    2    3    5
 12      1     4       9    4    8    6
         2     6       8    3    7    6
         3     6       8    4    6    6
         4     7       8    3    6    5
         5    10       7    2    3    5
 13      1     1       6    8    4   10
         2     2       5    5    4    9
         3     3       5    5    4    8
         4     4       5    2    3    7
         5     9       3    2    3    7
 14      1     5       5    8   10    6
         2     8       5    6    5    6
         3     8       5    4    8    4
         4     9       5    2    4    4
         5     9       5    1    5    4
 15      1     4       4    9    4    9
         2     6       3    8    4    9
         3     7       2    5    3    7
         4     7       3    4    3    7
         5     8       1    3    2    6
 16      1     5      10    8    7    6
         2     9       8    7    6    6
         3     9       9    6    6    4
         4    10       8    5    6    1
         5    10       7    3    6    3
 17      1     1       5    8    8    5
         2     1       5   10    7    5
         3     3       5    8    7    5
         4     5       4    5    4    5
         5     9       4    3    4    4
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   23   24   82   79
************************************************************************
