************************************************************************
file with basedata            : cm457_.bas
initial value random generator: 794592779
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  129
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       17       12       17
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        4          1           8
   3        4          3           5  11  17
   4        4          3           6   7   9
   5        4          1           7
   6        4          3          10  11  14
   7        4          3          12  13  14
   8        4          3          11  12  16
   9        4          3          13  14  17
  10        4          2          12  17
  11        4          1          15
  12        4          1          15
  13        4          1          16
  14        4          2          15  16
  15        4          1          18
  16        4          1          18
  17        4          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     6       0    3    8    9
         2     7       4    0    6    9
         3     9       2    0    5    9
         4    10       0    3    4    8
  3      1     2      10    0    9    4
         2     4       9    0    7    4
         3     7       9    0    6    3
         4     7       0    8    7    3
  4      1     2       8    0    5    7
         2     3       5    0    4    7
         3     5       0    3    2    7
         4     7       0    3    1    7
  5      1     1       3    0    6    4
         2     1       0    8    6    4
         3     5       0    6    6    4
         4     8       0    4    6    4
  6      1     1       4    0    7    9
         2     1       0    6    7    7
         3     5       0    4    6    2
         4     5       0    4    7    1
  7      1     3       8    0    9   10
         2     6       5    0    9    9
         3     9       0   10    8    9
         4    10       0    7    8    7
  8      1     1       0    5    8    7
         2     3      10    0    6    5
         3     7       0    4    3    4
         4     7       9    0    3    4
  9      1     2       0    4    8    9
         2     5      10    0    8    8
         3     8       0    3    7    8
         4     9       9    0    7    7
 10      1     4       0    6    6    5
         2     7       1    0    5    4
         3     7       0    2    5    3
         4     9       1    0    5    2
 11      1     1       3    0    7    7
         2     2       2    0    7    7
         3     3       2    0    7    5
         4     4       0    7    7    4
 12      1     2       0    7    7    7
         2     4       0    6    7    3
         3     4       0    6    5    4
         4     7       0    6    3    3
 13      1     2       0    8    4    8
         2     4       4    0    3    7
         3     7       3    0    3    7
         4     9       0    6    1    6
 14      1     1       9    0    8    7
         2     3       0    9    7    7
         3     7       9    0    4    6
         4    10       8    0    3    3
 15      1     8       6    0    8    2
         2     8       0    6    9    2
         3     8       5    0    9    2
         4     8       0    8    8    2
 16      1     2       0    5    5   10
         2     3       4    0    5    5
         3     9       0    2    2    5
         4     9       0    3    2    4
 17      1     3       4    0    8    8
         2     9       0   10    4    7
         3    10       3    0    2    6
         4    10       0    6    3    6
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
    6   13  114  113
************************************************************************
