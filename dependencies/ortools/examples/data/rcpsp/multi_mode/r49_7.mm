************************************************************************
file with basedata            : cr49_.bas
initial value random generator: 13315614
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  127
RESOURCES
  - renewable                 :  4   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       22       12       22
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3          11  14  15
   3        3          3           5   6  12
   4        3          3           6   8   9
   5        3          2           7   8
   6        3          3          11  14  15
   7        3          2          10  16
   8        3          3          11  13  14
   9        3          1          16
  10        3          2          13  17
  11        3          2          16  17
  12        3          1          13
  13        3          1          15
  14        3          1          17
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  R 4  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0    0
  2      1     6       8    2    3    0    8    0
         2     8       0    1    0   10    0    8
         3     9       4    1    0    0    0    4
  3      1     8      10    7    0    0    9    0
         2     9       0    2    3    8    0    8
         3    10       8    0    0    4    6    0
  4      1     1       5    0    0    4    0    6
         2     2       0    5    0    0    0    5
         3     4       0    4    5    0    0    2
  5      1     1       0    3    0    6    6    0
         2     4       8    0    0    0    0    9
         3     5       7    3    0    4    3    0
  6      1     3       0    3    0    0    0    4
         2     3       2    0    0    1    0    3
         3     7       2    0    0    0    9    0
  7      1     3       0    5    6    0    0    4
         2     5       8    5    0   10    7    0
         3     9       0    0    6    3    0    3
  8      1     2       0    0    9    8    5    0
         2     8       9    0    4    7    5    0
         3     9       0    8    2    0    5    0
  9      1     1       4    7    0    0    4    0
         2     3       2    0    0    4    0    9
         3    10       2    4    0    4    2    0
 10      1     4       7    9    0    0    0    9
         2     5       7    9    0    2    0    6
         3     8       0    6    0    0    8    0
 11      1     2       0    0    9    0    0    7
         2     6       0    0    7    0    0    6
         3     9      10    0    3    0    8    0
 12      1     7       0   10    0    5    6    0
         2     7       3    0    0    0    6    0
         3     9       0   10    3    0    2    0
 13      1     4       0    6    7    3    7    0
         2     6       2    0    0    0    7    0
         3     8       0    0    6    2    5    0
 14      1     7       9    6    7    4    0    2
         2     7       9    6    8    0    5    0
         3     7       0    6    0    0    6    0
 15      1     2       0    0    0    8    9    0
         2     3       5    0    5    8    0    4
         3     4       0    5    2    0    0    4
 16      1     5      10    0    0   10    3    0
         2     6       9    0    0    9    0    8
         3     9       0    7    7    0    3    0
 17      1     3       5    6    0    0    9    0
         2     3       0    6    0    4    8    0
         3    10       8    0    0    0    5    0
 18      1     0       0    0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  R 4  N 1  N 2
    8   11    9    6   61   40
************************************************************************
