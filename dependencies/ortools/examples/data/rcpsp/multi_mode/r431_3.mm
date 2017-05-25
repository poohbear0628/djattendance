************************************************************************
file with basedata            : cr431_.bas
initial value random generator: 351641684
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
    1     16      0       15       14       15
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6   8  10
   3        3          3           9  13  14
   4        3          3           5  10  15
   5        3          2           7   9
   6        3          3           9  11  12
   7        3          3           8  13  14
   8        3          2          16  17
   9        3          2          16  17
  10        3          2          11  12
  11        3          1          14
  12        3          1          13
  13        3          1          17
  14        3          1          16
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  R 4  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0    0
  2      1     1       7    9    6    7    8    0
         2     3       5    8    6    6    8    0
         3    10       2    6    6    5    7    0
  3      1     2       9    9    8    9    0    7
         2     7       9    7    7    8    7    0
         3     8       7    7    3    5    0    7
  4      1     2       6    2    9    7    4    0
         2     7       5    2    9    7    3    0
         3    10       3    2    8    6    1    0
  5      1     1      10    9    1   10    7    0
         2     2       9    7    1    7    0    8
         3    10       9    4    1    7    0    4
  6      1     4       7    6    6    5    0    7
         2     7       7    5    5    4    7    0
         3     9       7    3    4    4    6    0
  7      1     2       4   10    7    7    0    5
         2     4       4    9    7    7    0    5
         3     5       4    8    3    7    8    0
  8      1     3       7    8    9    6    8    0
         2     6       6    7    8    6    8    0
         3     7       5    3    8    5    0    6
  9      1     1       8    6    8    9    4    0
         2     1       8    5    8   10    0    8
         3     4       8    4    6    7    0    6
 10      1     3      10    8    4    6    0    8
         2     5       6    5    3    4    2    0
         3     8       5    4    2    2    2    0
 11      1     3       7    8    8    8    0    9
         2     5       6    7    6    5    0    6
         3     8       5    7    5    5    7    0
 12      1     6       7    3    1    9    0    8
         2     6       8    3    1   10    0    5
         3    10       4    2    1    4    7    0
 13      1     3       2    5    5   10    9    0
         2     3       3    7    6   10    0    8
         3     4       2    1    5   10    0    2
 14      1     3       8    6    8    9    8    0
         2     4       7    6    8    8    0    8
         3     9       6    6    6    5    0    7
 15      1     2       5   10    3    2    5    0
         2     4       4   10    3    2    0    6
         3     9       4    9    1    1    4    0
 16      1     4       7    6    6    6    0    1
         2     7       3    4    5    5    4    0
         3     8       1    4    5    2    4    0
 17      1     1       9    8    3   10    0   10
         2     9       9    7    3    8    0    3
         3    10       9    7    2    6    3    0
 18      1     0       0    0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  R 4  N 1  N 2
   26   28   22   28   98   99
************************************************************************
