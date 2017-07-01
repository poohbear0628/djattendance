************************************************************************
file with basedata            : md117_.bas
initial value random generator: 108416233
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  14
horizon                       :  92
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     12      0       19        8       19
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           6  13
   3        3          2           7   8
   4        3          3           5   6  10
   5        3          2           8   9
   6        3          1           9
   7        3          2           9  10
   8        3          3          11  12  13
   9        3          2          11  12
  10        3          3          11  12  13
  11        3          1          14
  12        3          1          14
  13        3          1          14
  14        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     4       6    7    9    8
         2     5       6    6    8    5
         3     8       3    6    6    5
  3      1     5       1    6    7    5
         2     6       1    6    5    5
         3    10       1    6    3    4
  4      1     1       9    7    9    3
         2     4       7    6    7    2
         3     6       7    6    6    2
  5      1     5       4    3    8    8
         2     6       4    3    7    5
         3     7       3    2    6    4
  6      1     2       8    9    4    8
         2     8       6    7    4    6
         3     9       6    7    2    6
  7      1     3       9    6    7    5
         2     6       8    6    4    4
         3     9       7    6    4    4
  8      1     3       5   10    5    9
         2     8       3   10    5    8
         3    10       2   10    3    7
  9      1     4       6    9    6    3
         2     4       6    8    6    4
         3     5       6    8    5    2
 10      1     4       4    7    7   10
         2     5       4    7    6   10
         3     8       4    3    6   10
 11      1     7       6    7    9    9
         2     7       7    8    8   10
         3     8       4    6    6    7
 12      1     2       8    7    5    8
         2     3       6    5    4    8
         3     7       4    4    1    8
 13      1     1       4    3    7    5
         2     4       3    2    7    3
         3     5       2    2    7    2
 14      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   11   14   76   78
************************************************************************
