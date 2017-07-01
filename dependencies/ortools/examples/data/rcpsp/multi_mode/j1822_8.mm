************************************************************************
file with basedata            : md278_.bas
initial value random generator: 1706587797
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  20
horizon                       :  142
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     18      0       26        3       26
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          1          19
   3        3          3           5   6   8
   4        3          3          13  17  19
   5        3          3           7  11  13
   6        3          3           9  10  14
   7        3          1          10
   8        3          2          11  17
   9        3          2          11  16
  10        3          3          12  15  16
  11        3          2          12  15
  12        3          2          18  19
  13        3          1          15
  14        3          1          16
  15        3          1          18
  16        3          2          17  18
  17        3          1          20
  18        3          1          20
  19        3          1          20
  20        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     2       6    7    0    9
         2     7       6    5    0    8
         3     8       6    5    0    6
  3      1     2       7    6    0    8
         2     5       4    3    6    0
         3    10       3    2    0    6
  4      1     1       6    4    7    0
         2     7       3    4    0    5
         3     9       1    3    7    0
  5      1     3       7    6    5    0
         2     5       7    5    4    0
         3     9       7    5    0    5
  6      1     6       7    8    8    0
         2     8       3    8    0    5
         3     8       5    8    6    0
  7      1     3       9    8    4    0
         2     9       8    7    0    6
         3    10       6    5    0    6
  8      1     3       6    2   10    0
         2     5       5    2    5    0
         3     9       2    2    2    0
  9      1     9       3    1    6    0
         2     9       2    3    0    5
         3     9       3    7    0    4
 10      1     3       7    8    0   10
         2     4       4    6    0    8
         3     6       3    6    0    7
 11      1     2       8    2    9    0
         2     8       7    2    0    5
         3     9       7    2    0    4
 12      1     4       9   10    0    7
         2     5       9    9    5    0
         3     6       8    9    5    0
 13      1     4      10    7    7    0
         2    10       8    4    0    8
         3    10       8    4    6    0
 14      1     4       7   10    1    0
         2     6       7    6    0    3
         3     9       6    5    0    2
 15      1     4       4    7    7    0
         2     5       3    6    0    7
         3     9       1    6    7    0
 16      1     3       6   10    9    0
         2     4       6    7    6    0
         3     6       6    4    5    0
 17      1     2       9    4    0    7
         2     5       8    2    3    0
         3     8       8    2    0    6
 18      1     2       9    7    0    3
         2     2      10    7    7    0
         3     2      10    8    0    2
 19      1     3       9    5    0    6
         2     5       3    4   10    0
         3     5       2    4    0    6
 20      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   18   21   80   78
************************************************************************
