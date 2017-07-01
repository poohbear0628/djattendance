************************************************************************
file with basedata            : cm218_.bas
initial value random generator: 897705473
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  109
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       27        2       27
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        2          2           9  11
   3        2          3           5   6   8
   4        2          3           5   7  10
   5        2          2          11  12
   6        2          3           7  11  12
   7        2          2          16  17
   8        2          2          10  15
   9        2          1          10
  10        2          2          14  16
  11        2          2          13  17
  12        2          3          13  14  15
  13        2          1          16
  14        2          1          17
  15        2          1          18
  16        2          1          18
  17        2          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     4       9    0    2    0
         2     8       0    9    0    6
  3      1     9       0    8    7    0
         2    10       0    5    7    0
  4      1     4       0    3   10    0
         2     9       1    0    0    5
  5      1     3       0    5    0    6
         2     9       5    0   10    0
  6      1     2       3    0    0    6
         2     5       2    0    0    2
  7      1     6       0   10    0    4
         2     8       9    0    4    0
  8      1     6       0    9    0    6
         2     8       5    0    7    0
  9      1     3       0    4    6    0
         2     5       0    4    0    6
 10      1     8       6    0    9    0
         2     9       4    0    0    4
 11      1     3       0    7    5    0
         2     4       0    2    0    8
 12      1     1      10    0    0    8
         2    10       9    0    8    0
 13      1     5       5    0    4    0
         2     7       0    9    1    0
 14      1     2       8    0    0    8
         2     4       4    0    6    0
 15      1     4       0    9    0    8
         2     4       9    0    0    8
 16      1     2       8    0    8    0
         2     4       0    2    0    1
 17      1     2       0    2    7    0
         2     5       6    0    6    0
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   17   17   73   60
************************************************************************
