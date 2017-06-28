************************************************************************
file with basedata            : cn331_.bas
initial value random generator: 1011093634
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
    1     16      0       19        1       19
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6   9  10
   3        3          3           5   7  12
   4        3          3           5   7  10
   5        3          2          11  14
   6        3          2          13  14
   7        3          3           8  13  16
   8        3          2           9  11
   9        3          1          15
  10        3          2          12  17
  11        3          1          17
  12        3          2          14  15
  13        3          2          15  17
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
  2      1     6       7    7    4    7    0
         2     6       7    7    0    8    0
         3     9       6    5    0    4    0
  3      1     2       4    4    0    0    6
         2     6       2    4    8    0    0
         3     9       1    4    7    0    5
  4      1     1       5    7    7    4    4
         2     5       5    5    0    3    0
         3     8       4    3    4    0    0
  5      1     1       9    4    8    0    9
         2     5       7    4    0    0    7
         3     9       5    3    5    0    0
  6      1     3       4    7    6    0    7
         2     6       4    6    0    4    7
         3     7       4    2    0    4    0
  7      1     3       7    3   10    6    2
         2     5       6    2    9    0    0
         3    10       3    2    0    0    2
  8      1     2       3   10    0    0    4
         2     7       3   10    0    2    0
         3     8       3    9    2    0    4
  9      1     1       8    9    6    0    0
         2     6       4    6    0   10    0
         3     7       3    4    0    3    0
 10      1     3       9    9    5    6    0
         2     5       9    7    0    0    7
         3     6       6    2    3    3    0
 11      1     4       5    6    0    9    0
         2     6       4    3    0    0    8
         3     9       4    3    7    0    3
 12      1     1       5    9    0    0    5
         2     4       4    9    5    8    0
         3     7       4    9    5    7    0
 13      1     2       8    6    4    7    0
         2     3       5    4    4    6    0
         3     4       4    2    0    5    0
 14      1     4       5    3    7    0    0
         2     8       4    2    0    8    0
         3     9       2    2    4    8    0
 15      1     1       4    6    6    9    7
         2     1       6    4    8    0    0
         3     7       3    4    0    9    0
 16      1     5      10    4    6    0    7
         2     6       7    4    4    0    6
         3     9       5    3    0    9    5
 17      1     5       8   10    0    4    0
         2     5       8    9    8    0    6
         3     7       7    9    8    0    6
 18      1     0       0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2  N 3
   21   26  101   94   72
************************************************************************
