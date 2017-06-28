************************************************************************
file with basedata            : mf19_.bas
initial value random generator: 442399292
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  32
horizon                       :  213
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     30      0       27       17       27
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6   8  16
   3        3          3           9  12  19
   4        3          2           5  14
   5        3          2           8  16
   6        3          3           7  10  15
   7        3          3          17  20  23
   8        3          3           9  11  12
   9        3          2          15  22
  10        3          1          18
  11        3          2          24  30
  12        3          3          13  24  27
  13        3          3          20  21  23
  14        3          1          29
  15        3          3          27  29  31
  16        3          1          23
  17        3          3          18  21  29
  18        3          1          19
  19        3          3          22  25  30
  20        3          2          22  26
  21        3          1          25
  22        3          1          31
  23        3          1          25
  24        3          1          28
  25        3          1          26
  26        3          1          28
  27        3          1          30
  28        3          1          31
  29        3          1          32
  30        3          1          32
  31        3          1          32
  32        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     1       5    0    0   10
         2     2       0    9    0    7
         3     5       3    0    0    4
  3      1     3       7    0    5    0
         2     3       2    0    0    7
         3     8       0    3    4    0
  4      1     2       0    3    4    0
         2     4       8    0    3    0
         3     6       7    0    3    0
  5      1     6       5    0    9    0
         2     6       5    0    0    8
         3     8       0    9    0    7
  6      1     2       9    0    0    4
         2     3       0    5    0    3
         3     6       0    4    0    1
  7      1     6       0    7    0    8
         2    10       0    7    2    0
         3    10       5    0    5    0
  8      1     2       9    0    0    5
         2     3       0    2    7    0
         3     6       7    0    0    4
  9      1     3       0    3    0    5
         2     5       0    3    6    0
         3     6       0    1    6    0
 10      1     1       0    7    0    4
         2     3       0    2    0    2
         3    10       3    0    7    0
 11      1     1       0    3    8    0
         2     2       0    2    5    0
         3     2       0    3    0    5
 12      1     3       0    9    0    7
         2     4       0    6    9    0
         3     9       5    0    0    5
 13      1     2       4    0    0    2
         2     6       2    0    0    2
         3     7       0    6    0    1
 14      1     6       0    6    0    9
         2     7      10    0    0    7
         3     8       0    5    0    5
 15      1     5       9    0    5    0
         2     6       8    0    4    0
         3     7       8    0    3    0
 16      1     3       0    3    7    0
         2     8       2    0    0    7
         3     9       1    0    6    0
 17      1     2       7    0    4    0
         2     5       6    0    3    0
         3     7       5    0    2    0
 18      1     3       0    8    0    9
         2     4       2    0    5    0
         3     4       0    3    0    6
 19      1     2      10    0    0    7
         2     4       9    0    3    0
         3    10       8    0    0    4
 20      1     2       0    2    5    0
         2     5       8    0    0    7
         3     6       0    2    0    5
 21      1     4       2    0    7    0
         2     4       2    0    0    7
         3     9       0    5    0    5
 22      1     1       0    7    5    0
         2     3       5    0    0    4
         3     6       0    7    0    4
 23      1     3       0    9    0    6
         2     3       0   10    7    0
         3     5       8    0    3    0
 24      1     2       4    0    0   10
         2     2       5    0    8    0
         3     3       3    0    8    0
 25      1     4       9    0    1    0
         2     6       6    0    0    5
         3     9       5    0    0    4
 26      1     1       6    0    4    0
         2     6       2    0    0    1
         3    10       0    5    3    0
 27      1     4       6    0    8    0
         2     6       0    3    7    0
         3     8       0    1    0    8
 28      1     2       0    6    0    5
         2     9       0    4    0    4
         3    10       0    1    6    0
 29      1     5       0    9    0    7
         2     6       5    0    0    7
         3     9       0    8    0    7
 30      1     2       0    7    0    7
         2     4       4    0    0    4
         3     6       0    7    4    0
 31      1     1       6    0    0    8
         2     4       4    0    6    0
         3     4       0    7    5    0
 32      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   24   26  111  134
************************************************************************
