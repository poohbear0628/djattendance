************************************************************************
file with basedata            : cr323_.bas
initial value random generator: 731467870
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
    1     16      0       13        9       13
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           5  11
   3        3          3           6  10  15
   4        3          2           5  10
   5        3          2           9  17
   6        3          3           7   8  11
   7        3          2          14  16
   8        3          3          12  13  14
   9        3          1          15
  10        3          2          12  13
  11        3          3          12  13  14
  12        3          2          16  17
  13        3          1          16
  14        3          1          17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0
  2      1     1       7    5    7    6    0
         2     5       7    4    7    0    6
         3     7       6    4    7    0    2
  3      1     1       4    8    2    0    7
         2     4       3    6    2    0    7
         3     8       3    4    2    0    6
  4      1     2       6    9    5    0    7
         2     5       6    8    4    0    5
         3     9       4    8    3    7    0
  5      1     1       9    7    5    0    7
         2     2       8    5    4    0    6
         3     5       6    5    3    2    0
  6      1     1       7    6    2    3    0
         2     6       6    6    2    3    0
         3    10       5    6    1    0    5
  7      1     5      10    5    3    5    0
         2     6       2    3    3    5    0
         3     6       1    4    3    0    7
  8      1     3       5    4    6    8    0
         2     7       4    4    4    8    0
         3     8       1    4    1    0    9
  9      1     1       3    5    7    5    0
         2     3       3    4    6    5    0
         3     8       2    4    4    4    0
 10      1     1      10    7    8    0    2
         2     4       8    7    8    4    0
         3     5       7    6    7    2    0
 11      1     2       2    2    9    0    4
         2    10       2    2    7    1    0
         3    10       2    1    7    0    2
 12      1     4       6    6    8    0    6
         2     6       5    6    5    8    0
         3    10       3    5    4    0    6
 13      1     6      10    4   10    8    0
         2     6      10    4   10    0    8
         3    10       7    2    8    5    0
 14      1     3       5    9    3    0    9
         2     9       3    8    2    0    2
         3    10       1    6    2   10    0
 15      1     2      10    6    6    4    0
         2     6       6    3    5    0    5
         3     7       2    2    3    0    5
 16      1     2      10    8    7    0    6
         2     6       9    4    6    0    4
         3    10       7    4    6    4    0
 17      1     2       7    8   10    8    0
         2     4       7    6    7    0    1
         3    10       7    5    4    2    0
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  N 1  N 2
   29   21   25   63   68
************************************************************************
