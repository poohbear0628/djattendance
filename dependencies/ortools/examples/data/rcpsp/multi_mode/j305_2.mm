************************************************************************
file with basedata            : mf5_.bas
initial value random generator: 1352851046
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  32
horizon                       :  234
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     30      0       27       14       27
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           6   7  22
   3        3          2           5  26
   4        3          3           8  21  24
   5        3          3          18  23  27
   6        3          3           9  11  15
   7        3          3          13  16  17
   8        3          2          17  19
   9        3          3          10  19  30
  10        3          1          12
  11        3          3          12  13  25
  12        3          2          14  18
  13        3          3          14  26  31
  14        3          1          23
  15        3          1          18
  16        3          1          25
  17        3          3          20  27  28
  18        3          2          20  31
  19        3          2          20  23
  20        3          1          29
  21        3          2          25  28
  22        3          2          26  31
  23        3          1          29
  24        3          1          29
  25        3          1          27
  26        3          1          28
  27        3          1          30
  28        3          1          30
  29        3          1          32
  30        3          1          32
  31        3          1          32
  32        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     2       5    7    8    0
         2     4       3    5    0    1
         3    10       1    3    8    0
  3      1     3       9    4    0    7
         2     7       4    3    0    4
         3     9       4    2    0    4
  4      1     3       7   10    0    7
         2     3       6   10    0    9
         3     7       5    9    3    0
  5      1     3       4    7    0    3
         2     3       6    6    0    4
         3    10       3    4    6    0
  6      1     2       4    8    0    7
         2    10       1    6    0    7
         3    10       3    7    0    6
  7      1     1      10    9    0    7
         2     2       7    7    0    2
         3     2       8    6    5    0
  8      1     1       8    6    2    0
         2     1       7    6    6    0
         3     3       5    6    0    6
  9      1     2       7    7    7    0
         2     2       6    7    0    3
         3     4       6    5    0    3
 10      1     5       9    4    5    0
         2     8       6    4    0    2
         3     9       6    4    5    0
 11      1     4       8    9    0    6
         2     4      10    8    0    6
         3     8       8    7    2    0
 12      1     3       7   10    0    5
         2     7       7    9    0    4
         3     8       6    9    0    4
 13      1     4       2    8    8    0
         2     5       2    6    8    0
         3    10       2    6    0    9
 14      1     3       5    9    0    5
         2     3       6    8   10    0
         3     6       4    2    5    0
 15      1     3       9    2    4    0
         2     9       8    2    0    4
         3     9       8    1    2    0
 16      1     2      10    7    0    3
         2     3       9    7    5    0
         3    10       8    6    3    0
 17      1     6      10    9    0    2
         2     8       9    8    0    2
         3    10       9    7    0    2
 18      1     3      10    5    7    0
         2     4      10    5    0    5
         3     8      10    5    6    0
 19      1     1       6    7    0    7
         2     8       6    4    0    7
         3     9       6    3    5    0
 20      1     6       8    2    6    0
         2     6       7    2    7    0
         3     8       6    2    0    4
 21      1     4       6    8    0    6
         2     4       5    6    0    7
         3     4       6    8    6    0
 22      1     1       5    7    7    0
         2     7       2    6    6    0
         3     9       2    3    6    0
 23      1     5       3   10    0    5
         2     7       3    9   10    0
         3    10       2    8   10    0
 24      1     5       9    9    7    0
         2     5       8    8    0    6
         3     9       6    7    7    0
 25      1     2       8    9    0    9
         2     4       6    8    0    6
         3     5       2    7    0    4
 26      1     8       9    7    8    0
         2     8       8    6    0    7
         3     8       9    7    0    4
 27      1     2       7    6    6    0
         2     5       6    6    0    6
         3     7       2    3    6    0
 28      1     2       5    9   10    0
         2     4       4    9    8    0
         3     5       3    9    4    0
 29      1     4      10    8    4    0
         2     6       8    8    0    6
         3    10       6    8    3    0
 30      1     2       8    9    5    0
         2     7       7    9    0    8
         3    10       6    9    0    6
 31      1     2       9    7    5    0
         2     7       9    3    0    7
         3     7       8    2    1    0
 32      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   24   21   47   54
************************************************************************
