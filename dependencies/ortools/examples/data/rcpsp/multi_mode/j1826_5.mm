************************************************************************
file with basedata            : md282_.bas
initial value random generator: 274628371
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  20
horizon                       :  127
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     18      0       25       13       25
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6  11  14
   3        3          2           5   9
   4        3          3           9  10  13
   5        3          1           6
   6        3          3           7  12  19
   7        3          1           8
   8        3          3          10  13  16
   9        3          3          14  15  16
  10        3          1          15
  11        3          1          17
  12        3          3          13  15  16
  13        3          2          17  18
  14        3          2          17  19
  15        3          1          18
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
  2      1     4       0    2    8    0
         2     4       0    2    0    7
         3     4       7    0    6    0
  3      1     2       8    0    9    0
         2     4       8    0    6    0
         3     4       8    0    0    7
  4      1     1       0    5    4    0
         2     3       0    4    0    4
         3     4       0    3    3    0
  5      1     1       0    8    4    0
         2     3       7    0    3    0
         3     9       0    6    0    7
  6      1     8       0    5    0    6
         2     9       6    0    0    4
         3     9       0    4    6    0
  7      1     4       0    5    3    0
         2     8       5    0    3    0
         3     8       0    2    2    0
  8      1     1       6    0    5    0
         2     1       0    5    0    3
         3     2       5    0    5    0
  9      1     4       7    0    0    5
         2     6       0    7    7    0
         3     9       6    0    2    0
 10      1     1       0    8    0    9
         2     6       0    5    0    6
         3     8       2    0    0    5
 11      1     7       0    5    0    6
         2     8       3    0    7    0
         3     9       0    2    7    0
 12      1     5       4    0    0    7
         2     6       0    4    9    0
         3    10       0    4    7    0
 13      1     4       7    0    0    6
         2     4       0    7    7    0
         3     8       8    0    6    0
 14      1     3       8    0    0    5
         2     4       0    7    0    5
         3     7       5    0    3    0
 15      1     1       9    0    0    7
         2     7       4    0    0    6
         3     8       0    1    2    0
 16      1     4       0    8    0    2
         2    10       0    7    4    0
         3    10       3    0    5    0
 17      1     1       0    6    0    6
         2     2       4    0    0    5
         3     4       3    0    7    0
 18      1     4       5    0    4    0
         2     5       0    3    4    0
         3     5       0    5    0    3
 19      1     4       7    0    0    3
         2     9       3    0    4    0
         3     9       0   10    0    2
 20      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   15   15   94   93
************************************************************************
