************************************************************************
file with basedata            : mf21_.bas
initial value random generator: 2143855451
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  32
horizon                       :  247
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     30      0       26       23       26
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        3          3           5   7  22
   3        3          3           6   8  20
   4        3          1          23
   5        3          1          10
   6        3          3          12  14  17
   7        3          2          11  17
   8        3          3           9  13  27
   9        3          3          12  22  24
  10        3          3          18  21  27
  11        3          2          15  20
  12        3          2          15  16
  13        3          2          22  25
  14        3          2          18  26
  15        3          3          18  19  28
  16        3          2          19  29
  17        3          1          29
  18        3          1          31
  19        3          1          31
  20        3          3          23  25  29
  21        3          1          24
  22        3          1          30
  23        3          3          26  27  28
  24        3          2          25  28
  25        3          1          26
  26        3          1          31
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
  2      1     5       9    6    4    0
         2     8       8    4    0    8
         3    10       5    3    3    0
  3      1     6       7    7    0    5
         2     7       6    6    0    5
         3     9       5    5    0    4
  4      1     5       9    6    0    7
         2     5       8    8    0    5
         3     9       5    5    8    0
  5      1     1       8    8    0    8
         2     3       6    7    8    0
         3    10       1    7    7    0
  6      1     1       4    8    0    3
         2     2       4    7    5    0
         3     7       3    5    3    0
  7      1     1       5    7    9    0
         2     8       5    7    6    0
         3     9       4    6    4    0
  8      1     1      10    5    0    3
         2     2      10    5    9    0
         3     5       9    4    7    0
  9      1     3       9    4    0    9
         2     6       7    4    0    4
         3     9       4    3    0    4
 10      1     6       6    7    5    0
         2     7       4    7    5    0
         3    10       3    6    0    2
 11      1     4       6    6    6    0
         2     4       8    7    0    7
         3    10       4    4    4    0
 12      1     2       6    4    3    0
         2     8       6    3    0    4
         3     9       5    2    0    3
 13      1     2       4    7    7    0
         2     6       4    7    3    0
         3     8       2    6    0    7
 14      1     1       8    8    0    8
         2     3       8    6    8    0
         3     6       6    5    4    0
 15      1     1       6    4    0    8
         2     3       5    3    3    0
         3     8       3    3    0    2
 16      1     1       9    5    0    7
         2     8       8    5    0    5
         3    10       7    5    0    3
 17      1     3       5   10    0    2
         2     6       4    9    0    1
         3    10       3    8    0    1
 18      1     3       3    7    0    8
         2    10       3    2    0    8
         3    10       3    1    8    0
 19      1     3       6    9    0    8
         2     5       4    9    0    5
         3     6       3    8    2    0
 20      1     6       6    8    7    0
         2     9       6    4    5    0
         3    10       5    3    0    9
 21      1     1       8    7    4    0
         2     3       7    7    4    0
         3     3       8    7    0    2
 22      1     1       8    9    0    7
         2     9       8    9    5    0
         3    10       8    6    3    0
 23      1     4       6    9    0    9
         2     5       5    6    6    0
         3     9       4    4    0    8
 24      1     1       4    7    3    0
         2     2       3    5    0    4
         3     5       3    2    2    0
 25      1     1       8    5    0    3
         2     9       5    3    0    3
         3    10       4    2    7    0
 26      1     2       5    3    0    5
         2     4       4    2    6    0
         3     8       3    2    5    0
 27      1     3       4    7    5    0
         2     5       3    7    0    7
         3     6       3    7    4    0
 28      1     2       6    8    6    0
         2     6       6    7    0    8
         3     9       5    4    0    7
 29      1     2      10    4    9    0
         2     3       5    4    0   10
         3     9       3    1    0    9
 30      1     3       5    2    7    0
         2     4       5    1    6    0
         3     4       3    2    0    1
 31      1     4       5    3    0    5
         2     6       5    2    0    5
         3     9       4    2    0    4
 32      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   17   17  114  135
************************************************************************
