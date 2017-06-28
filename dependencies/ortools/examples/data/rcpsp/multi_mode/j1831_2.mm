************************************************************************
file with basedata            : md287_.bas
initial value random generator: 975911696
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  20
horizon                       :  128
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     18      0       16        8       16
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2          14  17
   3        3          3           5   6   7
   4        3          3           5   6   7
   5        3          2          13  16
   6        3          3           8  11  15
   7        3          2          10  18
   8        3          1           9
   9        3          1          12
  10        3          2          11  13
  11        3          1          14
  12        3          3          13  14  16
  13        3          1          19
  14        3          1          19
  15        3          3          17  18  19
  16        3          2          17  18
  17        3          1          20
  18        3          1          20
  19        3          1          20
  20        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     2       6    6    0    6
         2     4       6    6    8    0
         3     6       5    6    5    0
  3      1     1       3    6    0   10
         2     3       3    5    0   10
         3     6       3    4    0    9
  4      1     1       6    7    0    5
         2     7       6    4    4    0
         3    10       5    3    2    0
  5      1     4       7    6    0    8
         2     4       6    6    6    0
         3     5       3    6    3    0
  6      1     1       7    8    3    0
         2     3       4    5    2    0
         3     6       4    2    0    3
  7      1     3       7    7    0    8
         2     6       7    6    7    0
         3     9       6    6    7    0
  8      1     1       5    5    7    0
         2     2       4    5    7    0
         3     6       2    2    6    0
  9      1     3       4    6    0    9
         2     4       3    5    0    7
         3     8       2    2    0    6
 10      1     3       9    8    8    0
         2     8       8    7    0   10
         3     9       8    5    6    0
 11      1     3       9    8    0    9
         2     4       9    8    7    0
         3     7       8    7    6    0
 12      1     1      10    6    2    0
         2     2       8    6    1    0
         3     4       7    3    0    6
 13      1     1       3    6    0    5
         2     8       2    6    7    0
         3     9       2    5    6    0
 14      1     1       6    9    7    0
         2     4       5    8    7    0
         3     4       5    8    0    4
 15      1     7       6    5    0    5
         2     7       6    6    0    4
         3     9       5    4    9    0
 16      1     5       7    5    8    0
         2     7       7    4    0    7
         3     9       7    4    8    0
 17      1     1       5    8    7    0
         2     4       5    8    0    8
         3     6       4    7    4    0
 18      1     2       8    9    7    0
         2     7       7    5    0    2
         3     7       7    4    0    7
 19      1     5       9    5    0    9
         2     7       8    3    0    7
         3     8       7    2    0    5
 20      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   22   22   97  119
************************************************************************
