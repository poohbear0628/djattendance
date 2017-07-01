************************************************************************
file with basedata            : cr535_.bas
initial value random generator: 29876
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  128
RESOURCES
  - renewable                 :  5   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       23        7       23
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   6  11
   3        3          2           8  15
   4        3          3           6   9  10
   5        3          1           7
   6        3          3           8  13  16
   7        3          2           9  14
   8        3          1          12
   9        3          3          12  13  16
  10        3          3          12  14  15
  11        3          2          13  17
  12        3          1          17
  13        3          1          15
  14        3          2          16  17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  R 4  R 5  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0    0    0
  2      1     7       0    0    7    0    0    2    7
         2     8       0    5    6    0    5    2    6
         3     9       0    1    5    0    0    1    5
  3      1     1       8    4    0    3    0    4    5
         2     9       0    4    8    0    0    4    5
         3    10       7    2    5    0    0    4    4
  4      1     3       7    2    0   10    6    8    6
         2     4       0    0    0    9    0    8    5
         3    10       0    0    0    9    4    6    3
  5      1     1       0   10    8    4    6    9    6
         2     9       0    0    0    2    6    9    4
         3    10       0   10    6    2    5    8    4
  6      1     1       0    0    0    2    0    3    8
         2     6       7    2    0    0    0    3    6
         3     8       0    0    0    2    3    2    5
  7      1     4       0    0    0    3    8    9    3
         2     5       9    0    2    2    0    8    3
         3     8       4    0    0    0    0    8    3
  8      1     1       8    5    8    3    0    4    7
         2     1       0    0    8    0    6    3    7
         3     5       8    5    0    0    0    2    5
  9      1     4       6    7    0    1    4    7    7
         2     6       0    4    0    0    2    6    4
         3     8       4    0    8    0    2    6    2
 10      1     6       0    5    0    2    3    7    6
         2     7       2    3    8    0    3    7    5
         3     9       0    0    0    0    3    7    4
 11      1     3       0   10    5    3    4    8    5
         2     6       0    4    3    2    3    7    3
         3     8       7    4    0    0    0    5    3
 12      1     3       0    8    0    0    5    2   10
         2     5       0    4    0    0    3    2    7
         3     6       3    0    8    0    0    1    5
 13      1     2       6    7    0   10    0    9    6
         2     8       0    0    0    0    2    5    3
         3     8       0    4    3    0    3    7    2
 14      1     2       5    6    0    6    0    9    7
         2     4       0    5    1    0    0    8    6
         3     6       0    0    0    6    7    5    5
 15      1     2       6    0    5    0    0    5    6
         2     5       0    7    0    7    0    4    4
         3     5       0    0    0    8    1    3    1
 16      1     1       0    7    0    6    8    6    7
         2     5       5    0    0    0    0    4    6
         3    10       4    0    5    5    0    4    4
 17      1     4       4    9    0    8    9    4    5
         2     5       4    0    4    7    0    2    5
         3     8       3    8    0    7    8    1    4
 18      1     0       0    0    0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  R 4  R 5  N 1  N 2
   20   21   23   14   14   75   70
************************************************************************
