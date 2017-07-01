************************************************************************
file with basedata            : md285_.bas
initial value random generator: 616700872
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  20
horizon                       :  130
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     18      0       17        1       17
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          1          12
   3        3          3           6   7   9
   4        3          3           5   6  16
   5        3          1           8
   6        3          3          12  14  17
   7        3          2          13  16
   8        3          2          10  13
   9        3          3          15  16  19
  10        3          3          11  14  17
  11        3          1          12
  12        3          2          18  19
  13        3          3          14  15  18
  14        3          1          19
  15        3          1          17
  16        3          1          18
  17        3          1          20
  18        3          1          20
  19        3          1          20
  20        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     9       7    8    6    0
         2     9       7    7    0    9
         3    10       3    4    6    0
  3      1     6       9    5    0    7
         2     6       9    5    2    0
         3     8       7    5    2    0
  4      1     2       9   10    0    9
         2     2       9   10    8    0
         3     5       8    8    0    9
  5      1     2      10    6    0    7
         2     5       9    6   10    0
         3     6       8    4    9    0
  6      1     3       4    5    0    3
         2     7       1    5    0    3
         3     7       1    5    1    0
  7      1     1       3    9    5    0
         2     2       3    7    0    7
         3     3       3    5    0    7
  8      1     1       6    6    0    2
         2     8       4    6    7    0
         3    10       2    5    7    0
  9      1     3       5    7    4    0
         2     5       5    7    1    0
         3     5       4    6    0    8
 10      1     2       3    8    6    0
         2     3       2    7    5    0
         3     9       2    5    0    2
 11      1     2       5    8    0    6
         2     4       5    8    0    5
         3     4       4    8    9    0
 12      1     4       6    9    0    5
         2     5       5    9    9    0
         3     7       5    9    7    0
 13      1     1       9    7    3    0
         2     2       9    7    0    9
         3     6       8    6    2    0
 14      1     4      10    9    4    0
         2     7       7    6    0    6
         3     7       9    7    4    0
 15      1     2       9    9    0   10
         2     7       9    5    0    9
         3    10       9    4    0    9
 16      1     1       9    2    0   10
         2     4       6    1    0   10
         3     9       6    1    5    0
 17      1     4       8    4    0    9
         2     5       8    3   10    0
         3    10       8    3    9    0
 18      1     4       9    5    7    0
         2     7       8    5    7    0
         3     9       8    5    5    0
 19      1     1       2    9    0    1
         2     3       2    9    3    0
         3     5       2    8    0    1
 20      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   15   16   99  110
************************************************************************
