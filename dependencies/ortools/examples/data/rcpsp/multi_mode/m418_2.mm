************************************************************************
file with basedata            : cm418_.bas
initial value random generator: 183663457
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  135
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       16        9       16
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        4          3           5   6  10
   3        4          3          15  16  17
   4        4          3           8   9  12
   5        4          3           7   8  12
   6        4          2          11  12
   7        4          1          14
   8        4          3          14  16  17
   9        4          2          10  11
  10        4          1          13
  11        4          2          15  17
  12        4          1          13
  13        4          2          14  16
  14        4          1          15
  15        4          1          18
  16        4          1          18
  17        4          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     3       0    8    0    8
         2     4       0    8    0    3
         3     6       0    7    3    0
         4     8       8    0    3    0
  3      1     2       0    7    9    0
         2     4       0    6    6    0
         3     7       6    0    0    5
         4     8       5    0    2    0
  4      1     4       9    0    0   10
         2     5       7    0    6    0
         3     5       0    3    0    6
         4     9       4    0    9    0
  5      1     2       0    9    0    8
         2     4       8    0    0    7
         3     4       0    9    2    0
         4     9       9    0    2    0
  6      1     3       6    0    7    0
         2     6       5    0    0    4
         3     8       4    0    0    4
         4    10       0    7    3    0
  7      1     2       0    5    0    4
         2     6       0    4    0    3
         3     7       0    1    6    0
         4     7       9    0    0    3
  8      1     3       0    6    9    0
         2     3       7    0    0   10
         3     8       4    0    0   10
         4     8       0    5    0   10
  9      1     1       0    9    0   10
         2     5       6    0    0   10
         3     6       5    0    5    0
         4     8       0    7    0    9
 10      1     3      10    0   10    0
         2     5      10    0    7    0
         3     7       9    0    6    0
         4     7       0    9    7    0
 11      1     1       9    0    9    0
         2     1       0    7    0    6
         3     5       9    0    0    5
         4     7       0    2    0    2
 12      1     1       4    0    0    6
         2     4       3    0    0    6
         3     8       1    0    0    6
         4     8       0    2    0    5
 13      1     2       7    0   10    0
         2     7       5    0    0    3
         3     9       0    6   10    0
         4     9       4    0    0    3
 14      1     2       9    0    9    0
         2     2       0    8   10    0
         3     6       8    0    5    0
         4    10       0    4    0    8
 15      1     4       9    0    0    7
         2     5       0   10    0    6
         3     7       0    8    0    5
         4     8       9    0    2    0
 16      1     2       9    0    0    7
         2     6       4    0    4    0
         3     7       0    8    0    6
         4    10       0    5    0    6
 17      1     5       3    0    3    0
         2     7       3    0    0    7
         3     8       0    9    0    7
         4     9       0    9    0    6
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   14   14   75   79
************************************************************************