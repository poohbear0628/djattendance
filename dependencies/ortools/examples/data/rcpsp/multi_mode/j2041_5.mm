************************************************************************
file with basedata            : md361_.bas
initial value random generator: 1311729872
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  22
horizon                       :  164
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     20      0       24       11       24
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6   7  15
   3        3          3           8  13  17
   4        3          3           5   9  17
   5        3          3          11  14  19
   6        3          3          12  13  14
   7        3          3          10  12  20
   8        3          1          19
   9        3          3          12  16  20
  10        3          2          11  16
  11        3          1          13
  12        3          2          19  21
  13        3          1          18
  14        3          1          16
  15        3          1          17
  16        3          1          18
  17        3          2          20  21
  18        3          1          21
  19        3          1          22
  20        3          1          22
  21        3          1          22
  22        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     2       0    7    7    8
         2     5       6    0    7    8
         3     8       5    0    5    8
  3      1     1       7    0    9    8
         2     2       7    0    6    4
         3     3       0    1    3    4
  4      1     7       0    8    5    5
         2     9       0    8    1    2
         3     9       0    7    4    2
  5      1     1       0    6    4    5
         2     7       3    0    3    4
         3     9       2    0    3    3
  6      1     2       0   10    6    6
         2    10       3    0    2    5
         3    10       5    0    2    3
  7      1     2       0    8    2    7
         2     7       0    5    2    6
         3     8       0    4    1    5
  8      1     1       3    0    6    4
         2     5       0    6    5    4
         3     8       0    3    2    4
  9      1     5       1    0    5    6
         2     7       1    0    5    5
         3    10       1    0    3    4
 10      1     2       6    0    5    2
         2     8       0    9    4    1
         3     8       5    0    4    1
 11      1     7       0    3    7    8
         2    10       5    0    7    4
         3    10       0    2    5    3
 12      1     3       5    0    5    5
         2     6       0    9    4    4
         3     8       0    9    3    4
 13      1     5       4    0   10   10
         2     5       0    4   10    6
         3    10       4    0   10    4
 14      1     6       0    5   10    4
         2     7       0    4    9    3
         3     9       2    0    9    2
 15      1     1       5    0    7    4
         2     2       4    0    6    3
         3     7       3    0    2    3
 16      1     1       5    0    8    8
         2     4       0    9    6    8
         3     8       0    9    5    8
 17      1     3       4    0    6    4
         2     6       3    0    5    4
         3    10       3    0    5    3
 18      1     3       8    0    8    7
         2     5       7    0    6    6
         3     7       7    0    3    5
 19      1     4       0    5    9    8
         2     6       7    0    7    8
         3     6       8    0    5    8
 20      1     1       7    0   10    4
         2     4       0    3    6    4
         3     6       6    0    1    3
 21      1     1       3    0    8    4
         2     2       3    0    7    3
         3    10       0    6    6    3
 22      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   10   13  108   99
************************************************************************
