************************************************************************
file with basedata            : cr455_.bas
initial value random generator: 1354790410
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  129
RESOURCES
  - renewable                 :  4   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       25        4       25
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          1           8
   3        3          3          12  14  15
   4        3          2           5   9
   5        3          3           6   7   8
   6        3          3          11  13  17
   7        3          2          11  16
   8        3          3          10  14  15
   9        3          3          12  13  14
  10        3          3          12  13  17
  11        3          1          15
  12        3          1          16
  13        3          1          16
  14        3          1          17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  R 4  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0    0
  2      1     2       6    6    8    9    6    4
         2     2       5    6    9    9    8    4
         3     8       4    6    6    6    6    3
  3      1     7       9   10    8    6    9    9
         2     8       8    9    5    6    7    9
         3    10       8    9    5    6    6    8
  4      1     2       9    4    3    6    6   10
         2     3       6    2    2    3    6   10
         3     9       3    2    2    2    6    9
  5      1     4      10    8    8    9    4    5
         2     6       8    3    4    9    1    5
         3     6       8    6    2    7    1    4
  6      1     2       9    7    8    8    7    8
         2     6       8    6    7    7    7    7
         3     7       7    1    6    4    7    7
  7      1     1       7    9    5    3    8    3
         2     3       6    6    5    2    6    2
         3    10       5    5    3    2    2    2
  8      1     7       8    9    5    3    8    8
         2     9       6    7    5    3    4    8
         3    10       5    6    5    3    3    7
  9      1     4       6   10    9    8   10    9
         2     8       4    7    8    6    9    5
         3     8       4    6    7    4   10    6
 10      1     2       5   10    8    9    8   10
         2     2       5   10    8   10    5   10
         3     6       4    8    5    9    3    8
 11      1     1       5    6    8    6    6    4
         2     2       3    6    8    4    6    3
         3     6       2    5    7    3    5    1
 12      1     2       6    8    5    4    4    7
         2     5       4    7    5    2    3    6
         3     7       3    5    4    1    2    3
 13      1     5       5    5   10    8    6    1
         2     8       5    5   10    7    4    1
         3     9       2    4    9    7    2    1
 14      1     4       9    4    6    6    6    6
         2     5       7    3    5    5    3    5
         3     9       2    2    3    4    2    5
 15      1     2       8   10    3    7    4    8
         2     5       7    9    3    6    4    5
         3     9       5    8    3    4    3    4
 16      1     2       6    9    7    8    7    8
         2     5       3    7    7    7    6    6
         3     6       2    5    6    7    6    4
 17      1     8       8    7    5    8    4    5
         2     9       6    6    1    8    2    3
         3     9       6    3    3    8    3    1
 18      1     0       0    0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  R 4  N 1  N 2
   27   29   22   20   95   97
************************************************************************
