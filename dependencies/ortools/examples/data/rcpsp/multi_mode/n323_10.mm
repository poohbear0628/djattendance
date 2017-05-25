************************************************************************
file with basedata            : cn323_.bas
initial value random generator: 757792493
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  137
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  3   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       21       13       21
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   7   9
   3        3          3          12  14  16
   4        3          2           6  11
   5        3          3           8  10  11
   6        3          2           7  10
   7        3          2           8  13
   8        3          2          12  14
   9        3          3          10  11  17
  10        3          1          13
  11        3          1          16
  12        3          1          17
  13        3          2          15  16
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
  2      1     3       2    5    3    7    8
         2     9       1    5    3    0    0
         3     9       2    5    0    5    0
  3      1     3       9    8    0   10    0
         2     5       7    5    7    0    3
         3     9       7    4    5    0    0
  4      1     1       4    5    0    3    0
         2     8       4    3    0    0    2
         3    10       3    2    1    0    0
  5      1     4       9    7    9    7    0
         2     9       8    4    0    3    0
         3     9       9    3    5    0    2
  6      1     1       4   10    0    0    4
         2     5       4   10    0    2    3
         3    10       3    9    8    0    2
  7      1     7       8    9    3    8    0
         2     7      10    9    4    0    0
         3     8       7    9    2    0    0
  8      1     2       6    9    3    8    0
         2     4       5    8    2    7    0
         3     7       4    6    2    6    8
  9      1     6       4    7    0    7    0
         2     6       5    9    0    5    0
         3     9       4    6    0    0    5
 10      1     1       9    7    1    3    0
         2     9       9    7    1    0    1
         3    10       9    6    1    0    0
 11      1     4       4    8    5    9    3
         2     5       2    6    1    9    0
         3    10       2    4    0    9    2
 12      1     1       5    7    5    0    8
         2     6       4    7    4    7    0
         3     6       4    6    0    7    7
 13      1     2      10    6    5    7    4
         2     9       5    4    2    0    0
         3     9       6    5    1    0    0
 14      1     3       8    8    0    6    0
         2     6       7    7    0    2    8
         3     6       8    8    7    0    0
 15      1     2       4    8    0    2    0
         2     2       4    8    0    0    6
         3     8       4    4    0    2    2
 16      1     6       5    5    0    0    6
         2     8       3    5    6    0    0
         3     9       3    4    6    0    0
 17      1     6       7    8    0    0    3
         2     7       5    6    0    0    2
         3     8       3    4    0    9    0
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2  N 3
   20   21   50   75   54
************************************************************************
