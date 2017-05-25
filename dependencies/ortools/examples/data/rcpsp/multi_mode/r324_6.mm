************************************************************************
file with basedata            : cr324_.bas
initial value random generator: 545414249
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  126
RESOURCES
  - renewable                 :  3   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       13        5       13
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           7   8
   3        3          3           5   6   8
   4        3          3           9  16  17
   5        3          1          11
   6        3          2           9  12
   7        3          3          10  11  13
   8        3          3           9  10  11
   9        3          2          13  14
  10        3          2          12  15
  11        3          3          12  14  17
  12        3          1          16
  13        3          1          15
  14        3          1          15
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0
  2      1     1       5    2    7    1    0
         2     8       5    2    4    0    7
         3     9       4    1    4    1    0
  3      1     2       9    2    8    0    8
         2     5       9    2    8    0    4
         3     7       8    2    7    0    3
  4      1     2       6    1   10    0    1
         2     3       6    1   10    2    0
         3     5       5    1    9    0    1
  5      1     2      10    6   10    0    5
         2     3       9    4    9    0    3
         3     8       9    4    8    0    3
  6      1     1      10    9    6    8    0
         2     2       9    8    5    0    9
         3     6       8    7    4    0    3
  7      1     5       7    6    8    6    0
         2     8       7    6    7    5    0
         3     9       7    5    6    5    0
  8      1     1       6    6    6    0    2
         2     5       5    3    4    0    2
         3     5       2    3    4    2    0
  9      1     2      10    8    8    0    9
         2     4      10    6    6    0    5
         3    10       9    3    5    5    0
 10      1     3       9    4    4    8    0
         2     5       9    4    3    5    0
         3     8       9    3    3    5    0
 11      1     2       6    5    9    0    5
         2     3       5    4    8    4    0
         3    10       4    4    7    2    0
 12      1     1       9    7    4    0    4
         2     2       6    5    3    0    4
         3     8       2    4    3    9    0
 13      1     2       8    8   10    7    0
         2     9       5    5    9    0    7
         3     9       7    6    9    0    3
 14      1     1       7    8    7    8    0
         2     4       5    6    6    8    0
         3     7       4    5    3    5    0
 15      1     3       8    8    8    6    0
         2     8       7    6    5    0    5
         3    10       7    1    4    0    4
 16      1     1       9    9    3    0    5
         2     6       8    9    3    9    0
         3     7       5    9    2    7    0
 17      1     5       6    6    9    0    7
         2     7       5    4    9    7    0
         3     8       3    2    9    0    5
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  N 1  N 2
   33   27   30   65   57
************************************************************************
