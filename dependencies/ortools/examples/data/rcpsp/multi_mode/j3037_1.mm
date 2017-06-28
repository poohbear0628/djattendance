************************************************************************
file with basedata            : mf37_.bas
initial value random generator: 22320
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  32
horizon                       :  241
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     30      0       25        3       25
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3          12  15  29
   3        3          2           5   6
   4        3          2          13  19
   5        3          3           7   9  11
   6        3          3          16  17  27
   7        3          3           8  10  13
   8        3          1          17
   9        3          2          12  21
  10        3          2          16  20
  11        3          3          15  18  23
  12        3          1          31
  13        3          3          14  18  25
  14        3          2          20  24
  15        3          3          16  20  22
  16        3          1          30
  17        3          2          24  25
  18        3          1          26
  19        3          3          27  28  30
  20        3          2          21  30
  21        3          1          31
  22        3          1          31
  23        3          3          24  25  26
  24        3          1          28
  25        3          1          28
  26        3          1          27
  27        3          1          29
  28        3          1          29
  29        3          1          32
  30        3          1          32
  31        3          1          32
  32        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     3       2   10    6    7
         2     4       2    9    5    7
         3     9       1    9    3    6
  3      1     2       7    5    2    8
         2     4       5    5    1    5
         3     7       5    5    1    3
  4      1     1       4    9   10    9
         2     9       3    4   10    7
         3    10       3    4    9    2
  5      1     3      10    9    5    5
         2     8       9    8    4    3
         3    10       8    7    4    3
  6      1     1       6    9    9    4
         2     4       6    9    9    2
         3     5       5    8    8    2
  7      1     2      10    8   10    2
         2     5       9    5    5    2
         3     6       6    5    4    1
  8      1     3       2    4    6    8
         2     5       2    4    6    7
         3    10       1    4    6    4
  9      1     1       9    6    6   10
         2     2       7    5    4    7
         3     5       5    5    3    6
 10      1     4       3    3    6    9
         2     6       2    3    5    8
         3    10       2    3    4    5
 11      1     4       2    7    8   10
         2     9       2    4    5    9
         3    10       1    4    4    6
 12      1     7       5    9    7    8
         2     8       4    7    4    5
         3     9       2    7    4    4
 13      1     2       5    6   10    7
         2    10       4    4    8    5
         3    10       4    3    9    5
 14      1     1       7    5    8    2
         2     5       7    5    6    2
         3     7       7    3    6    1
 15      1     8       8    6   10    2
         2     9       8    3    9    2
         3    10       7    3    9    2
 16      1     6       7    9    9    9
         2     9       4    6    9    4
         3     9       4    4    9    7
 17      1     1       6    7    4    9
         2     1       8    6    4    9
         3     2       5    6    3    8
 18      1     1       8    6    8    4
         2     5       6    2    7    4
         3     5       7    1    8    3
 19      1     5       7    8   10    7
         2     7       6    3    9    7
         3     9       3    3    8    6
 20      1     2       7    9    4    8
         2     9       6    9    4    8
         3    10       6    8    3    8
 21      1     3       6    9    7    7
         2     4       6    5    5    6
         3     5       6    4    5    6
 22      1     2       8    8    6    6
         2     9       4    8    5    6
         3    10       3    8    4    6
 23      1     2       5    9    2    8
         2     3       3    5    2    6
         3     7       2    3    1    5
 24      1     4       9    9    7    3
         2     6       7    9    5    3
         3     7       4    9    3    3
 25      1     7       5    8    5    9
         2     7       4    9    5    9
         3    10       2    8    3    9
 26      1     1       8    6    2    5
         2     3       6    3    1    5
         3     4       3    3    1    5
 27      1     1       8    5    9    5
         2     8       6    4    7    4
         3    10       5    1    4    3
 28      1     3       4    6   10    8
         2     4       3    4   10    7
         3     9       1    3    9    4
 29      1     1      10    8    3   10
         2     4       7    7    3    6
         3     7       3    7    2    5
 30      1     2       5    8    4   10
         2     9       5    6    4    9
         3    10       4    3    3    7
 31      1     1       6   10    5    7
         2     2       5    8    4    6
         3     9       5    7    4    2
 32      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   16   17  156  152
************************************************************************
