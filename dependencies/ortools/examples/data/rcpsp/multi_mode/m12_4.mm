************************************************************************
file with basedata            : cm12_.bas
initial value random generator: 2128647277
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  88
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       41        9       41
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        1          2           5   9
   3        1          3           6   7  12
   4        1          3           5  12  13
   5        1          1           6
   6        1          2           8  14
   7        1          3          10  11  17
   8        1          2          10  11
   9        1          3          12  13  16
  10        1          2          15  16
  11        1          1          16
  12        1          2          15  17
  13        1          2          14  15
  14        1          1          17
  15        1          1          18
  16        1          1          18
  17        1          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       5    0    0    8
  3      1     8       0    5    0    4
  4      1     1       4    0   10    0
  5      1    10       0    2    0    5
  6      1     2       0    5    0    3
  7      1     2       0    4    5    0
  8      1     9       0    1    0    5
  9      1     1       0    9    8    0
 10      1    10       4    0    6    0
 11      1     6       3    0    0    6
 12      1     5       2    0    0    5
 13      1     6      10    0    0    3
 14      1     8       5    0    0    9
 15      1     9       0    4    0    7
 16      1     7       4    0    0    6
 17      1     3       0    8    0    6
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   10   13   29   67
************************************************************************