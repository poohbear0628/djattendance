************************************************************************
file with basedata            : me32_.bas
initial value random generator: 2005495739
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  130
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  0   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       21        0       21
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5  11  15
   3        3          3           6   9  10
   4        3          2           7   8
   5        3          2          13  17
   6        3          3           8  12  15
   7        3          2          10  13
   8        3          2          11  14
   9        3          3          12  14  15
  10        3          2          12  17
  11        3          2          16  17
  12        3          1          16
  13        3          1          14
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
  2      1     1       8    9
         2     1      10    8
         3     5       5    5
  3      1     4       8    6
         2     9       7    4
         3    10       7    3
  4      1     7       9    5
         2     7       7    6
         3    10       6    5
  5      1     4       8    7
         2     6       8    4
         3     9       6    1
  6      1     3       4    9
         2     4       4    8
         3     6       4    6
  7      1     4       9    7
         2     6       5    5
         3     6       7    3
  8      1     5       6    8
         2     9       6    5
         3    10       5    4
  9      1     3       6    8
         2     6       5    6
         3     9       5    4
 10      1     4       6    6
         2     5       2    6
         3     5       4    5
 11      1     1       8    2
         2     6       3    2
         3     6       5    1
 12      1     4       9    7
         2     5       8    4
         3     7       8    3
 13      1     2      10    9
         2     6       5    7
         3     9       2    7
 14      1     6       9    6
         2     8       7    5
         3    10       4    4
 15      1     7       5    4
         2     9       4    4
         3    10       3    2
 16      1     2       6    4
         2     6       6    3
         3     9       5    3
 17      1     1       9    8
         2     1      10    7
         3     9       5    6
 18      1     0       0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2
   29   30
************************************************************************
