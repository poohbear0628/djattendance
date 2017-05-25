************************************************************************
file with basedata            : md114_.bas
initial value random generator: 2062889705
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  14
horizon                       :  94
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     12      0       14        2       14
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   6   9
   3        3          2           9  13
   4        3          3           5   6   7
   5        3          2          10  13
   6        3          2           8  10
   7        3          3           9  10  11
   8        3          3          11  12  13
   9        3          1          12
  10        3          1          12
  11        3          1          14
  12        3          1          14
  13        3          1          14
  14        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     3       0    8    4    4
         2     4       0    6    4    3
         3     6       3    0    3    3
  3      1     6       6    0    6    9
         2     8       0    7    6    8
         3     9       0    3    5    6
  4      1     1       5    0    9    7
         2     6       0    4    7    7
         3    10       3    0    7    7
  5      1     1       0    5    7    5
         2     7       0    4    5    5
         3     7       6    0    5    5
  6      1     2       7    0    5    9
         2     2       0    5    5    9
         3     6       7    0    4    8
  7      1     3       8    0    5    4
         2     6       8    0    5    3
         3     6       0    4    4    3
  8      1     3       9    0    7    8
         2     7       0    3    6    5
         3     7       3    0    6    3
  9      1     3       0    6    3    9
         2     7       4    0    2    9
         3    10       1    0    1    7
 10      1     1       8    0    2    7
         2     7       0    7    2    4
         3     9       8    0    2    4
 11      1     2       0    7   10    7
         2     5      10    0    9    7
         3     7       0    4    9    4
 12      1     5       0    5    9    4
         2     9       1    0    8    2
         3     9       0    4    8    2
 13      1     4       0    8    5   10
         2     7       0    4    4   10
         3     8       0    3    4   10
 14      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   10   13   69   78
************************************************************************
