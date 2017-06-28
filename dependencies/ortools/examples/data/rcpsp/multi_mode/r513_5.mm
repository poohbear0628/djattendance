************************************************************************
file with basedata            : cr513_.bas
initial value random generator: 874498758
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  138
RESOURCES
  - renewable                 :  5   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       17       12       17
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   6   8
   3        3          3           9  10  15
   4        3          2           5   9
   5        3          3          11  12  14
   6        3          3           7  10  11
   7        3          2          12  17
   8        3          3           9  10  12
   9        3          2          13  17
  10        3          1          16
  11        3          2          15  17
  12        3          1          13
  13        3          1          16
  14        3          1          15
  15        3          1          18
  16        3          1          18
  17        3          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  R 3  R 4  R 5  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0    0    0    0
  2      1     3       5    8    9    2    8    8    0
         2     7       4    8    9    2    7    6    0
         3     8       1    4    8    2    6    0    2
  3      1     2       7    6    7    7    5    4    0
         2     3       7    5    7    5    4    4    0
         3     8       7    2    6    3    3    0    1
  4      1     2       3    8    8    2    7    2    0
         2     3       3    7    6    2    5    2    0
         3     9       3    7    4    1    3    1    0
  5      1     2       4    8    2    5    8    7    0
         2     7       4    5    2    5    7    6    0
         3    10       3    4    1    4    7    0    9
  6      1     1       6    4    6    8    3    0    7
         2     6       6    4    5    7    2    7    0
         3     9       5    3    3    6    1    6    0
  7      1     4       3    5    7    6    5    0    8
         2     9       3    4    5    6    5    1    0
         3    10       2    2    1    6    5    0    5
  8      1     1       5    4    6    4    6    0    7
         2     3       5    4    6    4    6    0    4
         3    10       5    3    6    2    6    6    0
  9      1     1       9    7    9    4    3    0    9
         2     6       9    7    8    4    3    0    7
         3     9       9    6    8    1    2    0    7
 10      1     7      10    2    9   10    8    0    3
         2     8      10    2    9    4    4    7    0
         3    10       9    2    8    3    4    0    3
 11      1     1       9    7    3    2    3    3    0
         2     4       8    6    3    2    3    3    0
         3     5       6    2    3    2    2    2    0
 12      1     2       5    9    6    3   10    9    0
         2     3       4    7    6    3    6    0   10
         3     3       5    7    6    3    1    0   10
 13      1     2       3    1    4    5    9    7    0
         2     5       3    1    2    4    8    0    6
         3    10       2    1    1    3    8    0    5
 14      1     2       5    4    2    9    8    0    2
         2     8       3    4    1    8    7    0    2
         3    10       3    4    1    6    6    1    0
 15      1     3       5    8    4    4    8    9    0
         2     7       3    6    3    3    5    0    8
         3     9       3    5    1    2    4    6    0
 16      1     5       8    3    7    6    5    0    6
         2     6       7    2    7    4    5    0    5
         3     9       7    1    4    1    4    2    0
 17      1     5      10    9    3    8    8    4    0
         2     7       9    6    3    4    7    3    0
         3     9       8    5    3    1    7    0    2
 18      1     0       0    0    0    0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  R 3  R 4  R 5  N 1  N 2
   14   12   13   11   15   40   44
************************************************************************
