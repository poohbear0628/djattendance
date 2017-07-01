************************************************************************
file with basedata            : md306_.bas
initial value random generator: 656186467
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  20
horizon                       :  146
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     18      0       23       14       23
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6  10  12
   3        3          3           5  10  16
   4        3          3          14  18  19
   5        3          2           6  12
   6        3          3           7   8  18
   7        3          3           9  13  15
   8        3          3           9  14  19
   9        3          1          17
  10        3          1          11
  11        3          3          13  15  18
  12        3          1          15
  13        3          1          14
  14        3          1          17
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
  2      1     2       0    1    6    2
         2     2       0    1    4    3
         3     6       9    0    4    1
  3      1     1       0    2    7    5
         2     1      10    0    7    5
         3     7       0    2    3    5
  4      1     2       0    4    2    7
         2     5       0    3    2    5
         3     7       6    0    2    4
  5      1     7       0    9    8    8
         2     7       0   10    6    9
         3     8       0    6    4    3
  6      1     3       0    3    8    6
         2     4       2    0    5    4
         3    10       0    1    4    2
  7      1     3       0   10    7    4
         2     6       0    8    7    3
         3     9       0    5    7    3
  8      1     6       0    3    8    8
         2     7       6    0    7    7
         3     9       0    2    5    4
  9      1     2       0    5    4    8
         2     4       0    5    2    7
         3     8       0    4    2    4
 10      1     6       9    0    4    5
         2     7       9    0    4    3
         3    10       0    7    3    3
 11      1     8       0    2    9    5
         2     8       8    0    6    8
         3     8       0    2    4    8
 12      1     1       6    0    8    9
         2     5       0    9    6    9
         3     7       0    9    1    9
 13      1     1       0    4    6    7
         2     3       0    3    5    5
         3     6       0    2    4    4
 14      1     3       0    5    8    7
         2     6       8    0    7    6
         3     7       5    0    7    5
 15      1     2       0    6    6    2
         2     6       8    0    6    1
         3     9       0    4    6    1
 16      1     6       6    0    9    6
         2     7       0    4    9    4
         3     7       1    0    9    5
 17      1     2       7    0   10    8
         2     8       0    4    7    6
         3     8       6    0    6    6
 18      1     7       0    9    8    4
         2     8       0    7    8    4
         3    10       2    0    5    3
 19      1     4       7    0    6    6
         2     5       4    0    6    4
         3    10       3    0    6    3
 20      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   14   18  114  101
************************************************************************
