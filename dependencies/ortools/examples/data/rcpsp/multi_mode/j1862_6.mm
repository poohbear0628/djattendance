************************************************************************
file with basedata            : md318_.bas
initial value random generator: 1618092329
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  20
horizon                       :  155
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     18      0       17       10       17
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2          11  12
   3        3          3           5  13  16
   4        3          3           6  10  12
   5        3          3           7   9  17
   6        3          3           8  13  14
   7        3          1          18
   8        3          2           9  18
   9        3          1          19
  10        3          3          11  13  14
  11        3          2          16  18
  12        3          2          15  16
  13        3          2          15  17
  14        3          1          15
  15        3          1          19
  16        3          1          17
  17        3          1          20
  18        3          1          20
  19        3          1          20
  20        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     5       8    6    9    7
         2     8       8    6    9    6
         3     9       7    5    9    4
  3      1     3       6    3    8    5
         2     3       5    3    9    4
         3     9       4    3    8    3
  4      1     1       4   10    8    9
         2     6       2   10    7    5
         3    10       2    9    2    2
  5      1     7       7    7    8   10
         2     8       6    5    7    5
         3     8       6    7    6    5
  6      1     6       9   10    8   10
         2     8       8    9    8    8
         3    10       8    7    5    6
  7      1     1       8    5    5    2
         2     2       7    5    3    2
         3     7       6    3    3    2
  8      1     2       5    5   10    9
         2     6       4    2    9    9
         3     8       2    1    9    8
  9      1     5       5    7    4    2
         2     8       3    5    4    2
         3     9       2    2    4    2
 10      1     6       3    9    7    2
         2     8       3    5    6    2
         3    10       3    4    3    1
 11      1     1       9    7    4    4
         2     6       8    5    3    3
         3     7       6    4    2    1
 12      1     2      10   10    9    6
         2     3       7    9    7    6
         3     8       7    9    5    6
 13      1     2      10    7    8    8
         2     3       9    7    8    8
         3     5       8    6    5    7
 14      1     4       7   10    3    3
         2     4       9    7    3    4
         3     8       7    5    2    1
 15      1     2       6    7   10    7
         2     8       6    7    9    5
         3     9       1    7    9    3
 16      1     7       5    9    9    5
         2     8       3    9    9    4
         3    10       2    9    8    3
 17      1     2       7    4    6    7
         2     6       5    3    5    7
         3     9       2    1    5    7
 18      1     6       9    6    9    6
         2    10       6    4    6    3
         3    10       4    5    4    5
 19      1     1       7    6    7    2
         2     6       4    5    5    1
         3     9       4    4    3    1
 20      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   24   24  133  105
************************************************************************
