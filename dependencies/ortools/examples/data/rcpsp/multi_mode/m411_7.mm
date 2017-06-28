************************************************************************
file with basedata            : cm411_.bas
initial value random generator: 755910108
************************************************************************
projects                      :  1
jobs (incl. supersource/sink ):  18
horizon                       :  135
RESOURCES
  - renewable                 :  2   R
  - nonrenewable              :  2   N
  - doubly constrained        :  0   D
************************************************************************
PROJECT INFORMATION:
pronr.  #jobs rel.date duedate tardcost  MPM-Time
    1     16      0       18       11       18
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
   1        1          3           2   3   4
   2        4          3           5   9  11
   3        4          3          11  12  17
   4        4          2           8  11
   5        4          3           6   7  17
   6        4          3           8  13  14
   7        4          3          10  12  15
   8        4          1          15
   9        4          3          10  14  17
  10        4          1          13
  11        4          2          15  16
  12        4          1          14
  13        4          1          16
  14        4          1          16
  15        4          1          18
  16        4          1          18
  17        4          1          18
  18        1          0        
************************************************************************
REQUESTS/DURATIONS:
jobnr. mode duration  R 1  R 2  N 1  N 2
------------------------------------------------------------------------
  1      1     0       0    0    0    0
  2      1     5       4    0    0    6
         2     5       8    0    3    0
         3     9       0    7    0    7
         4    10       0    5    0    6
  3      1     4       3    0    6    0
         2     4       0    5    9    0
         3     6       4    0    0    7
         4     9       3    0    0    6
  4      1     1      10    0    6    0
         2     8       0    3    5    0
         3    10      10    0    5    0
         4    10      10    0    0    1
  5      1     2       0    5    9    0
         2     3       0    5    0    5
         3     6       0    4    8    0
         4     8       3    0    0    3
  6      1     3       0    7    0    9
         2     5      10    0    0    9
         3     8       0    5    0    7
         4    10       9    0    0    6
  7      1     4       5    0    0    6
         2     7       4    0    5    0
         3     8       0    5    4    0
         4     9       0    5    0    5
  8      1     1      10    0    0    8
         2     2       0    7    0    7
         3     2       9    0    0    8
         4     7       9    0    0    5
  9      1     3       0    5    8    0
         2     6       6    0    8    0
         3     6       9    0    0    6
         4     7       5    0    8    0
 10      1     2       0    7    8    0
         2     4       0    5    0    8
         3     5       0    3    8    0
         4     8       3    0    0    8
 11      1     4       9    0    5    0
         2     4       0    9    5    0
         3     9       0    9    3    0
         4     9       0    8    0    4
 12      1     4       0    5    0    5
         2     4      10    0    0    5
         3     6       0    5    8    0
         4     8       6    0    4    0
 13      1     1      10    0    7    0
         2     3      10    0    0    9
         3     5      10    0    6    0
         4    10       0    7    0    8
 14      1     1       0    7    0    7
         2     4       3    0    0    6
         3     5       0    6    0    5
         4     6       0    4    8    0
 15      1     3       9    0    8    0
         2     6       0    8    5    0
         3     6       8    0    6    0
         4     7       0    9    0   10
 16      1     2       0   10    0    8
         2     2       0   10    9    0
         3     6       5    0    0    6
         4     9       0    8    3    0
 17      1     1       0    5    0    2
         2     1       8    0   10    0
         3     2       8    0    5    0
         4     8       6    0    5    0
 18      1     0       0    0    0    0
************************************************************************
RESOURCEAVAILABILITIES:
  R 1  R 2  N 1  N 2
   17   20   52   57
************************************************************************
