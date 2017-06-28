************************************************************************
file with basedata            : cr355_.bas
initial value random generator: 1080484934
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  133
RESOURCES
  - renewable                 :  3   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       29       10       29
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6   9  13
   3        3          3           6   7  15
   4        3          3           5   9  11
   5        3          3           6   7   8
   6        3          1          10
   7        3          2          13  16
   8        3          2          10  15
   9        3          3          14  15  17
  10        3          2          12  17
  11        3          2          13  16
  12        3          1          14
  13        3          1          17
  14        3          1          16
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0
  2      1     3       5    5    8    7    3
         2     9       3    5    6    7    2
         3    10       1    4    6    7    1
  3      1     2       7    9    7    8    3
         2     5       7    9    6    5    3
         3     6       4    8    6    4    3
  4      1     3      10   10    6    7   10
         2     5       5   10    6    7    4
         3    10       2    9    5    4    2
  5      1     6       8    6    6   10    5
         2     6       6    6    7    8    5
         3     8       4    5    5    8    4
  6      1     5       9    3    8    6   10
         2     6       7    3    4    5    8
         3     9       6    3    3    4    6
  7      1     2       2    2    3    7    9
         2     7       2    2    3    5    7
         3     9       2    2    1    2    7
  8      1     6       5    8   10    7    5
         2     7       5    8    6    7    2
         3    10       3    6    4    6    2
  9      1     2       9    9    9    8    4
         2     3       5    9    6    7    4
         3    10       1    8    2    7    4
 10      1     1       8    9    3   10    6
         2     2       7    8    3    7    6
         3     6       4    7    2    7    5
 11      1     3       9    8    3    8    6
         2     5       5    6    3    8    4
         3     7       2    5    2    7    3
 12      1     5       3    8    9    7    7
         2     5       3    9    9    6    8
         3     9       3    7    9    4    7
 13      1     3       9    6    7    7    4
         2     3       9    6    8    6    4
         3     6       8    5    6    5    2
 14      1     5       4    9   10    9    7
         2     5       4    8   10    7    8
         3     6       2    6    9    7    6
 15      1     5       9    4    4    3    7
         2     7       6    4    4    3    4
         3     8       3    3    3    2    2
 16      1     3       7    5    8    6    5
         2     4       7    5    7    3    3
         3     9       7    4    7    1    2
 17      1     1       8    5    7    9    2
         2     7       7    5    6    8    2
         3    10       6    4    2    7    2
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  N 1  N 2
   22   20   22  110   86
************************************************************************
