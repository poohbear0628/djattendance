************************************************************************
file with basedata            : c1512_.bas
initial value random generator: 23606
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  129
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       27       13       27
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           5   9
   3        3          1           7
   4        3          3           5   6  10
   5        3          1          11
   6        3          2           8  14
   7        3          3           9  12  13
   8        3          1          12
   9        3          1          10
  10        3          1          15
  11        3          1          16
  12        3          3          15  16  17
  13        3          1          17
  14        3          1          16
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     3       0    9    0    7
         2     4       0    8    3    0
         3     5       0    7    0    7
  3      1     2       0    5    8    0
         2     4       0    3    8    0
         3     8       0    2    0    8
  4      1     2       0   10    8    0
         2     2       6    0    0    7
         3     8       0   10    0    7
  5      1     2       0   10    0    3
         2     9       9    0    0    2
         3    10       0   10    0    2
  6      1     7       5    0    0    3
         2     7       3    0    8    0
         3     9       0    9    5    0
  7      1     1       0    2    0    8
         2     4      10    0    0    7
         3     5      10    0    0    3
  8      1     5       2    0    6    0
         2     5       0    3    0    3
         3     5       1    0    0    3
  9      1     1       0    9    6    0
         2     3       0    6    4    0
         3     9       0    5    4    0
 10      1     1       0    6    8    0
         2     2       0    6    6    0
         3     6       6    0    3    0
 11      1     8       8    0    0    5
         2     8       9    0    5    0
         3     9       7    0    5    0
 12      1     4       9    0    8    0
         2     6       0    7    8    0
         3    10       7    0    7    0
 13      1     4      10    0    0    4
         2     5       0    5    5    0
         3    10       0    3    4    0
 14      1     1       0    9    7    0
         2     6       0    8    3    0
         3     8       0    6    0    3
 15      1     3       0    7    7    0
         2     7       2    0    0    6
         3     8       0    5    0    4
 16      1     1       0    8    4    0
         2     7       4    0    0    6
         3     9       0    5    0    3
 17      1     9       8    0    0    5
         2    10       0    9    0    5
         3    10       8    0    5    0
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   30   33   51   37
************************************************************************
