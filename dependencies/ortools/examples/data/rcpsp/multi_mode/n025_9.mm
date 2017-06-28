************************************************************************
file with basedata            : me25_.bas
initial value random generator: 1304585469
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  123
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  0   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       15       10       15
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   6   7
   3        3          3           5   9  15
   4        3          2           8   9
   5        3          3          10  11  14
   6        3          3           8  11  17
   7        3          3           9  10  14
   8        3          1          15
   9        3          3          11  12  17
  10        3          2          12  17
  11        3          1          13
  12        3          1          13
  13        3          1          16
  14        3          1          16
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2
------------------------------------------------------------------------
  1      1     0       0    0
  2      1     1       7    0
         2     1       0    7
         3     2       6    0
  3      1     1       0    5
         2     4       7    0
         3     8       4    0
  4      1     2       0   10
         2     9       0    9
         3    10       8    0
  5      1     1       0    6
         2     8       7    0
         3     8       0    5
  6      1     5       7    0
         2     8       4    0
         3     9       3    0
  7      1     1       6    0
         2     2       0    6
         3     6       0    4
  8      1     1       0   10
         2     9       0    9
         3     9       6    0
  9      1     6       0    9
         2     8       0    8
         3     9       7    0
 10      1     1       6    0
         2     5       4    0
         3    10       0    6
 11      1     4       0    8
         2     5       8    0
         3     7       0    7
 12      1     3       0    5
         2     4       0    3
         3     9       4    0
 13      1     1       0    6
         2     2       9    0
         3     8       0    5
 14      1     2       6    0
         2     3       3    0
         3     6       0    7
 15      1     3       6    0
         2     7       2    0
         3     8       0    5
 16      1     2       7    0
         2     3       0    4
         3     5       5    0
 17      1     3       0    4
         2     6       0    3
         3     9       4    0
 18      1     0       0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2
    9    8
************************************************************************
