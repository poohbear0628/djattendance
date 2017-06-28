************************************************************************
file with basedata            : cm17_.bas
initial value random generator: 1198096924
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  74
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       32        4       32
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        1          2          13  14
   3        1          2           7  16
   4        1          3           5   6   9
   5        1          3           8  11  12
   6        1          3          10  12  13
   7        1          2          11  13
   8        1          1          10
   9        1          2          11  12
  10        1          3          14  15  17
  11        1          1          15
  12        1          3          14  15  17
  13        1          1          17
  14        1          1          16
  15        1          1          18
  16        1          1          18
  17        1          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       6    3    4    0
  3      1     6       5    6    0    5
  4      1     7      10   10    0    5
  5      1     3       8    4    6    0
  6      1     3       6    4    5    0
  7      1     3       8    8    3    0
  8      1     2       1    7    3    0
  9      1     2       2    7    0    4
 10      1     4       6    8    0    9
 11      1     6       2    6    0    1
 12      1     3       8    7    0    7
 13      1     4       2    9    3    0
 14      1     9       6    8    5    0
 15      1     9      10    4    9    0
 16      1     7       9    2    0    7
 17      1     5       2    3    0    9
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   21   25   38   47
************************************************************************
