************************************************************************
file with basedata            : md304_.bas
initial value random generator: 199483964
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  20
horizon                       :  140
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     18      0       17       16       17
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          2           5   6
   3        3          3           5  16  17
   4        3          2           6  14
   5        3          1           8
   6        3          3           7   9  10
   7        3          3          11  16  17
   8        3          3          10  13  14
   9        3          3          11  13  16
  10        3          1          11
  11        3          2          12  15
  12        3          2          18  19
  13        3          1          18
  14        3          1          15
  15        3          2          18  19
  16        3          1          19
  17        3          1          20
  18        3          1          20
  19        3          1          20
  20        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       9    4    6    3
         2     8       8    2    5    1
         3     8       8    1    4    3
  3      1     2       4    8    8    4
         2     7       4    7    8    4
         3     9       3    7    8    2
  4      1     3       6    7    2    4
         2     6       4    6    2    4
         3     8       3    6    2    1
  5      1     1       2    4    7    4
         2     1       2    3    9    4
         3     6       2    3    4    4
  6      1     3       6    6    8    6
         2     3       5    6    9    7
         3     6       4    6    7    2
  7      1     3       6    1   10    5
         2     8       1    1    6    5
         3     8       4    1    7    4
  8      1     4       4    7    6    8
         2     4       5    7    6    6
         3     6       4    3    2    5
  9      1     2       5   10    7    3
         2     4       5    7    4    3
         3     6       4    7    2    1
 10      1     2       5    9    3    8
         2     3       5    8    3    7
         3    10       3    8    2    6
 11      1     1       5    8    7   10
         2     3       5    4    6    8
         3    10       4    3    5    7
 12      1     2       9    8    2   10
         2     2       9    8    3    9
         3    10       6    8    2    8
 13      1     3       3    4    9    6
         2     3       3    5    9    5
         3     6       3    3    9    5
 14      1     2       4    7    4    8
         2     4       2    4    3    8
         3     4       3    7    3    7
 15      1     2       7    4    8    9
         2    10       4    3    6    8
         3    10       1    1    8    9
 16      1     3       8    6    3    7
         2     6       5    5    3    6
         3     8       4    3    3    4
 17      1     6       7   10    5   10
         2     6       9    8    5    8
         3     9       4    4    4    6
 18      1     5       7    5   10    8
         2     7       7    4    9    8
         3     9       6    4    7    7
 19      1     3       4    9    7    7
         2     3       5    7    8    6
         3     7       3    5    5    4
 20      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   36   33   99  102
************************************************************************
