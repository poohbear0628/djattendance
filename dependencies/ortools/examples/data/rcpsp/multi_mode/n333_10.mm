************************************************************************
file with basedata            : cn333_.bas
initial value random generator: 542867593
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  125
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  3   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       20        8       20
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           6   8
   3        3          3          15  16  17
   4        3          3           5   7  13
   5        3          3           8  11  16
   6        3          3           9  11  12
   7        3          3           9  10  12
   8        3          2          12  17
   9        3          2          14  17
  10        3          2          11  14
  11        3          1          15
  12        3          1          15
  13        3          1          14
  14        3          1          16
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2  N 3
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0
  2      1     7       9    0    8    6    7
         2     8       0    7    8    5    7
         3     9       8    0    8    3    6
  3      1     4       0    6    5    8    5
         2     5       6    0    4    8    4
         3     7       0    5    3    7    3
  4      1     7       7    0    6    4   10
         2     9       2    0    4    4    9
         3    10       0    2    3    2    9
  5      1     1       0    7    1    9    7
         2     3       0    4    1    9    5
         3     6       2    0    1    9    2
  6      1     2       0    7    5    9   10
         2     2       6    0    5   10   10
         3     4       0    8    4    5    9
  7      1     1       0    6    8    5    6
         2     3      10    0    5    4    4
         3     6      10    0    2    3    4
  8      1     2       0    9    8    7    8
         2     4       0    9    7    7    7
         3    10       0    8    5    7    6
  9      1     3       0    8    8    7    8
         2     6       0    7    6    6    4
         3     9       0    6    4    6    1
 10      1     3       1    0    6    3    9
         2     9       1    0    2    3    1
         3     9       0    4    3    2    2
 11      1     4       3    0    8    4    6
         2     5       3    0    4    3    3
         3     9       0    4    4    3    2
 12      1     3      10    0    9    3    7
         2     4       0    9    9    2    4
         3     4      10    0    9    2    5
 13      1     4       3    0    6    5    2
         2     5       2    0    6    4    2
         3     7       2    0    5    3    1
 14      1     2       0    6    3    5   10
         2     7       0    3    3    2    7
         3     7       8    0    3    4    7
 15      1     5       9    0   10    9    4
         2     8       0    6    9    8    4
         3     8       7    0    9    7    3
 16      1     6       5    0    3    7    8
         2     9       0    8    2    6    5
         3    10       2    0    2    4    5
 17      1     2      10    0    6    4    7
         2     3       9    0    4    4    6
         3    10       0    6    1    4    4
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2  N 3
    9   11   74   76   79
************************************************************************
