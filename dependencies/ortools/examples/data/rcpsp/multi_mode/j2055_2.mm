************************************************************************
file with basedata            : md375_.bas
initial value random generator: 297359037
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  22
horizon                       :  144
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     20      0       21       19       21
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           9  12  16
   3        3          3           5  13  18
   4        3          3           7  13  19
   5        3          3           6   9  12
   6        3          3           8  14  19
   7        3          2          11  14
   8        3          2          10  20
   9        3          1          21
  10        3          1          11
  11        3          2          15  16
  12        3          1          15
  13        3          2          17  20
  14        3          2          15  16
  15        3          1          17
  16        3          1          17
  17        3          1          21
  18        3          3          19  20  21
  19        3          1          22
  20        3          1          22
  21        3          1          22
  22        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       6    4    8    9
         2     5       1    2    8    9
         3     5       4    1    7    9
  3      1     2       7    8    4    5
         2     3       7    8    4    3
         3     5       2    7    3    1
  4      1     3       3    6    7    6
         2     4       3    5    6    6
         3     6       2    4    4    6
  5      1     4       4    7    3    1
         2     4       3    5   10    4
         3     4       4    5    6    1
  6      1     1       9    8    6    9
         2     8       9    7    6    8
         3     9       9    7    3    8
  7      1     2       4    4    4    4
         2    10       3    3    4    3
         3    10       3    4    3    3
  8      1     1       8    6    9    7
         2     1       8    7    9    6
         3     5       6    4    4    5
  9      1     4       4    5    8    6
         2     4       5    4    7    7
         3     7       4    4    5    4
 10      1     2       4    6    4    6
         2     4       3    5    4    4
         3    10       1    3    4    3
 11      1     2       8    8    9    5
         2     7       6    8    7    3
         3    10       2    6    6    3
 12      1     1       6    8   10    9
         2     4       6    8   10    7
         3     8       4    7    9    6
 13      1     3       9    8    9    9
         2     6       9    4    8    8
         3     7       9    2    7    8
 14      1     5       6    3   10    3
         2     8       6    3    8    3
         3    10       6    3    7    1
 15      1     2       9   10    6    2
         2     2      10    7    6    2
         3     4       8    5    6    2
 16      1     2       5    8    5    8
         2     3       5    6    2    6
         3     4       3    5    1    4
 17      1     3       3    8    3    4
         2     7       3    6    3    4
         3    10       2    4    2    3
 18      1     3       5    6    4    6
         2     4       4    6    3    5
         3     6       1    4    2    4
 19      1     2       8    6    6    4
         2     3       5    5    5    3
         3    10       4    5    5    3
 20      1     3       8    4    7    5
         2     4       5    4    1    3
         3     4       6    4    3    1
 21      1     4      10    5    1    8
         2     5       8    5    1    8
         3    10       7    5    1    7
 22      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   26   21  118  111
************************************************************************
