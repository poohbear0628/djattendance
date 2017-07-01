************************************************************************
file with basedata            : md86_.bas
initial value random generator: 204074765
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
    1     12      0       16        6       16
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           7   8   9
   3        3          3           7   9  13
   4        3          3           5   7   8
   5        3          2           6  12
   6        3          1          13
   7        3          2          10  11
   8        3          3          11  12  13
   9        3          2          10  11
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
  2      1     1       5   10    0    8
         2     4       4    7    3    0
         3     6       4    7    0    7
  3      1     1       7    4    0    3
         2     4       5    4    0    3
         3     8       5    4    0    2
  4      1     5       4    8    0    5
         2     6       3    5    3    0
         3     9       2    2    2    0
  5      1     2       4    4    8    0
         2     9       4    3    5    0
         3    10       2    3    3    0
  6      1     1       9    7    6    0
         2     4       9    6    2    0
         3     5       8    6    0   10
  7      1     6       8    9    0    6
         2     8       6    5    0    4
         3    10       3    3    3    0
  8      1     1       4    3    0    7
         2     5       4    3    0    3
         3     9       4    2    1    0
  9      1     1       8    9    0   10
         2     2       8    8    8    0
         3     6       7    5    4    0
 10      1     4       8    9    0    6
         2     6       3    8    0    6
         3     8       3    7    9    0
 11      1     1       8    5    5    0
         2     5       7    3    0    4
         3    10       7    2    5    0
 12      1     1       8    5    0    7
         2     4       8    4   10    0
         3     4       8    3    0    3
 13      1     7       7    8    0    9
         2     7       6    8    5    0
         3     9       6    8    0    9
 14      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   16   15   47   57
************************************************************************
