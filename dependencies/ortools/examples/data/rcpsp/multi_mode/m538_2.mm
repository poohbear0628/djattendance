************************************************************************
file with basedata            : cm538_.bas
initial value random generator: 939970452
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  138
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       16        3       16
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        5          3          11  12  16
   3        5          2           5  10
   4        5          3           8   9  16
   5        5          3           6  11  12
   6        5          1           7
   7        5          3           9  16  17
   8        5          3          10  11  13
   9        5          1          13
  10        5          2          12  14
  11        5          2          15  17
  12        5          2          15  17
  13        5          1          14
  14        5          1          15
  15        5          1          18
  16        5          1          18
  17        5          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       8    9    8    6
         2     2       7    9    8    6
         3     7       5    8    8    6
         4     8       3    8    7    5
         5     9       2    8    7    5
  3      1     2       6    6   10    9
         2     3       6    6    9    9
         3     4       4    4    8    8
         4     6       4    3    8    8
         5    10       2    2    6    8
  4      1     2       6    9    9    8
         2     3       6    7    9    7
         3     3       5    8    9    8
         4     6       4    7    8    4
         5     9       3    4    8    2
  5      1     3       7    9    9    9
         2     5       6    9    9    9
         3     6       5    9    8    8
         4    10       3    9    7    8
         5    10       2    9    8    8
  6      1     1       9    4    7    7
         2     5       8    4    6    7
         3     8       7    3    4    6
         4     9       4    3    2    5
         5     9       3    2    4    4
  7      1     3       8    4    9    7
         2     4       7    3    8    7
         3     5       6    3    7    7
         4     7       6    3    6    6
         5    10       5    2    6    6
  8      1     2       8    2    9    4
         2     3       7    2    8    4
         3     5       5    2    8    4
         4     6       5    2    7    4
         5     8       3    2    6    4
  9      1     1      10    6    3    6
         2     3       7    5    3    6
         3     9       5    4    2    5
         4     9       3    4    2    6
         5    10       2    2    2    5
 10      1     3       3    6    6    9
         2     4       3    6    3    8
         3     5       2    5    2    7
         4     5       2    6    1    7
         5     5       1    6    3    7
 11      1     5       8    5    6    8
         2     5       8    7    7    7
         3     9       8    4    6    5
         4    10       8    1    3    5
         5    10       8    3    4    3
 12      1     3       8    7    6    7
         2     3       8    8    6    6
         3     5       7    6    5    3
         4     6       7    4    3    2
         5     6       7    3    2    3
 13      1     1       8    7   10    7
         2     1       8    9    9    7
         3     6       7    5    7    7
         4     9       6    4    4    6
         5    10       4    3    3    6
 14      1     4       8    7    6   10
         2     7       7    6    6    8
         3     8       5    5    6    7
         4     9       5    4    5    5
         5    10       4    4    5    4
 15      1     1       7    5    7    9
         2     1       9    5    7    8
         3     3       6    5    7    6
         4     4       3    4    7    6
         5     5       3    3    6    3
 16      1     1       9    7    7    9
         2     4       8    7    6    8
         3     4       8    7    7    6
         4     5       8    6    4    3
         5     9       5    6    3    1
 17      1     2      10    4    3    7
         2     2       9    4    3    9
         3     4       6    4    3    5
         4     6       5    3    3    4
         5     8       2    2    2    2
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   22   19   81   84
************************************************************************
