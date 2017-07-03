************************************************************************
file with basedata            : me37_.bas
initial value random generator: 509800340
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  20
horizon                       :  157
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  0   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     18      0       37        2       37
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           5   6
   3        3          2          15  19
   4        3          3           7   9  12
   5        3          3           7   8  10
   6        3          3          12  14  15
   7        3          2          13  19
   8        3          3           9  11  15
   9        3          1          14
  10        3          3          11  16  18
  11        3          2          12  19
  12        3          1          13
  13        3          1          17
  14        3          2          16  18
  15        3          1          18
  16        3          1          17
  17        3          1          20
  18        3          1          20
  19        3          1          20
  20        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2
------------------------------------------------------------------------
  1      1     0       0    0
  2      1     2       8    5
         2     5       6    4
         3     7       3    4
  3      1     1       2   10
         2     8       2    7
         3    10       2    6
  4      1     2       9    3
         2     7       7    3
         3    10       5    2
  5      1     3       2    8
         2     5       2    6
         3     8       1    3
  6      1     4       6    6
         2     5       5    5
         3    10       4    5
  7      1     4       8   10
         2     5       8    9
         3     6       7    8
  8      1     3       6   10
         2     5       6    9
         3     8       5    9
  9      1     1       7    9
         2     1       8    8
         3    10       4    6
 10      1     6      10    6
         2     9       9    3
         3    10       9    2
 11      1     9       6    8
         2     9       5    9
         3    10       4    8
 12      1     8       7    7
         2    10       1    6
         3    10       5    5
 13      1     2       7   10
         2     3       7    5
         3     7       6    5
 14      1     1      10    3
         2     3       6    2
         3     4       3    1
 15      1     1       8   10
         2     3       8    7
         3     8       7    7
 16      1     2       8    8
         2     9       8    7
         3    10       6    5
 17      1     7       6    9
         2     7       8    8
         3     9       4    4
 18      1     7       7    5
         2     7       6    7
         3    10       6    4
 19      1     4       9    5
         2     5       8    4
         3    10       6    3
 20      1     0       0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2
   15   16
************************************************************************