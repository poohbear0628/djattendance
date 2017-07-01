************************************************************************
file with basedata            : cr114_.bas
initial value random generator: 427023434
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  121
RESOURCES
  - renewable                 :  1   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       16        6       16
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           6   8
   3        3          3           5   7   9
   4        3          3           5  11  14
   5        3          2          10  13
   6        3          2          12  15
   7        3          3          10  11  12
   8        3          3           9  10  11
   9        3          2          12  14
  10        3          1          15
  11        3          2          16  17
  12        3          2          13  17
  13        3          1          16
  14        3          1          15
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0
  2      1     2       8    0    9
         2     7       6    7    0
         3    10       4    0    8
  3      1     4       6    0    4
         2     7       5    0    4
         3     9       5    4    0
  4      1     6       6    0    7
         2     8       6    4    0
         3    10       5    0    3
  5      1     1       6    5    0
         2     5       3    0    5
         3     9       2    0    5
  6      1     1       8    4    0
         2     1       8    0    5
         3     4       6    4    0
  7      1     6       6    0    4
         2     9       6    9    0
         3    10       5    8    0
  8      1     3       6    6    0
         2     7       5    6    0
         3     7       5    0    4
  9      1     3       5    5    0
         2     4       5    0    7
         3     8       2    0    5
 10      1     3       8    1    0
         2     3       7    4    0
         3     8       6    0    5
 11      1     2       6    9    0
         2     4       6    8    0
         3     7       5    8    0
 12      1     1       6    0    6
         2     2       5    0    6
         3     5       4    0    6
 13      1     2       8    3    0
         2     9       6    3    0
         3    10       5    3    0
 14      1     1       9   10    0
         2     6       8   10    0
         3     6       9    0    4
 15      1     1       6    0    4
         2     1       7    0    3
         3     2       5    6    0
 16      1     1      10    0    5
         2     4       9    6    0
         3     9       9    5    0
 17      1     4       2    0    6
         2     4       2    6    0
         3     7       1    2    0
 18      1     0       0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  N 1  N 2
   18   50   41
************************************************************************
