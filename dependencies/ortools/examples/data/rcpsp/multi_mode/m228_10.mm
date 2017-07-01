************************************************************************
file with basedata            : cm228_.bas
initial value random generator: 1366615320
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  123
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       33        2       33
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        2          2           5  11
   3        2          3           6   9  10
   4        2          3           5  10  11
   5        2          3           6   7  16
   6        2          2           8  14
   7        2          3           8   9  14
   8        2          1          13
   9        2          1          13
  10        2          3          12  15  17
  11        2          3          12  15  17
  12        2          1          16
  13        2          1          15
  14        2          1          17
  15        2          1          18
  16        2          1          18
  17        2          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       0   10    8    0
         2     3       0    9    0    8
  3      1     4       6    0   10    0
         2     6       3    0    0   10
  4      1     5       5    0    8    0
         2     9       0    3    0    6
  5      1     3       0    5    0   10
         2     3       0    4    7    0
  6      1     6       5    0    0    6
         2     9       4    0    6    0
  7      1     3       8    0    4    0
         2    10       4    0    0   10
  8      1     7       0    9    0    2
         2    10       0    8    5    0
  9      1     2       0    2    0    2
         2     7       4    0    0    1
 10      1    10       0    6    0    3
         2    10      10    0    2    0
 11      1     3      10    0    2    0
         2    10       7    0    0    6
 12      1     4       0    5    0    9
         2     8       0    5    0    3
 13      1     7       0    5    4    0
         2     9       0    5    0    7
 14      1     6       0    7    0    6
         2     6       0    5    8    0
 15      1     5       7    0    0    7
         2     7       0    1    0    5
 16      1     2       0    8    0    7
         2     8       7    0    0    6
 17      1     6       0    8    0    4
         2     8       5    0    0    4
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   23   25   64  103
************************************************************************
