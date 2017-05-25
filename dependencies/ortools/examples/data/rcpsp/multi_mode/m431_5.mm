************************************************************************
file with basedata            : cm431_.bas
initial value random generator: 1786011214
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  144
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       15       12       15
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        4          3           6  10  11
   3        4          3           9  11  12
   4        4          2           5   8
   5        4          3          10  13  14
   6        4          2           7  12
   7        4          2          13  15
   8        4          1          12
   9        4          3          13  15  16
  10        4          1          16
  11        4          3          14  15  17
  12        4          2          14  17
  13        4          1          17
  14        4          1          16
  15        4          1          18
  16        4          1          18
  17        4          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     2       8    8   10    0
         2     5       5    8    0    6
         3     8       3    7    0    5
         4    10       2    6    8    0
  3      1     1       2    4    0    7
         2     4       2    3    0    4
         3     7       1    3    2    0
         4     8       1    2    0    1
  4      1     1      10    7    4    0
         2     8      10    7    3    0
         3     9       9    6    0    5
         4    10       8    2    2    0
  5      1     4       7    8    7    0
         2     5       7    6    0    5
         3     8       5    4    0    4
         4    10       4    3    0    4
  6      1     4       5    9    0    7
         2     6       4    8    9    0
         3     8       4    6    7    0
         4     9       1    3    3    0
  7      1     3      10    8    6    0
         2     7      10    8    0    4
         3     8      10    7    4    0
         4     9       9    7    3    0
  8      1     1       7    7    9    0
         2     3       6    6    5    0
         3     9       5    5    0    7
         4    10       5    5    0    5
  9      1     1       2    9    0    7
         2     5       1    6    0    5
         3     7       1    3    0    4
         4     7       1    5    8    0
 10      1     5       6    8    0    8
         2     8       5    7    7    0
         3     8       4    7    0    7
         4     9       3    7    0    4
 11      1     2       7    6    0    8
         2     6       5    4    0    7
         3     9       5    4    6    0
         4    10       2    2    0    3
 12      1     2       9    9    0    7
         2     2       9    8    0   10
         3     4       8    5    0    4
         4     7       8    3    6    0
 13      1     3       9    5    0    8
         2     6       7    5    9    0
         3     8       5    4    0    8
         4     9       1    4    0    7
 14      1     3       3    9    8    0
         2     4       3    6    0    9
         3     7       3    5    0    8
         4     8       3    4    0    8
 15      1     6       7    8    0    9
         2     7       5    8    0    9
         3     8       4    4    3    0
         4    10       1    1    3    0
 16      1     4       5   10    8    0
         2     6       2   10    0    7
         3     6       2   10    5    0
         4     9       1    9    0    6
 17      1     1       7    8    0    8
         2     3       7    7    0    4
         3     5       6    6    8    0
         4     9       6    3    0    1
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   21   26  110  115
************************************************************************
