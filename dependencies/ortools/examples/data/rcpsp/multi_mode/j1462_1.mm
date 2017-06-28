************************************************************************
file with basedata            : md190_.bas
initial value random generator: 4550
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  16
horizon                       :  112
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     14      0       23        0       23
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   6  11
   3        3          2           7  11
   4        3          3           6   9  11
   5        3          3           9  14  15
   6        3          3           7  10  13
   7        3          2           8  15
   8        3          1          12
   9        3          1          13
  10        3          1          12
  11        3          3          13  14  15
  12        3          1          14
  13        3          1          16
  14        3          1          16
  15        3          1          16
  16        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     8       5    8    9    9
         2     9       3    7    5    7
         3     9       5    7    4    8
  3      1     4       3    9    8   10
         2     4       3    9   10    9
         3     9       3    9    6    7
  4      1     1       7   10    7    4
         2     2       5    9    5    3
         3     8       1    8    4    1
  5      1     2       4    8    8    9
         2     6       3    7    7    7
         3     9       1    6    5    6
  6      1     1       4    8    6    2
         2     5       4    7    5    2
         3     6       4    5    4    1
  7      1     4       4   10    8   10
         2     5       3    9    7    9
         3     8       3    8    7    9
  8      1     1       9    7    7    5
         2     2       5    5    6    5
         3    10       4    4    6    4
  9      1     5       9    8    6   10
         2     6       8    5    6    8
         3     7       5    4    5    5
 10      1     1       8    8    5    9
         2     3       7    8    2    8
         3     7       6    6    2    7
 11      1     5       7    9    5    5
         2     8       3    6    4    2
         3     8       6    4    4    5
 12      1     5       9    4    9    1
         2     7       7    4    7    1
         3     9       3    3    6    1
 13      1     7       9    2    6    9
         2     9       7    2    4    8
         3     9       6    1    5    8
 14      1     4       9    4    4    5
         2     7       9    4    1    5
         3     7       9    3    2    5
 15      1     2      10    8    8    8
         2     6       7    4    3    6
         3     6       8    7    2    5
 16      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   19   22   98   96
************************************************************************
