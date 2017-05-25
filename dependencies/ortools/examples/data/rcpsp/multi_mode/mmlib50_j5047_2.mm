jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	10		2 3 4 5 6 7 8 11 12 18 
2	3	7		28 26 24 19 17 13 10 
3	3	9		36 31 28 26 24 23 17 16 13 
4	3	5		28 26 19 14 9 
5	3	5		37 36 29 26 9 
6	3	8		36 30 28 25 23 22 19 15 
7	3	8		31 27 26 24 23 22 19 16 
8	3	7		36 32 24 22 21 20 19 
9	3	7		32 31 24 23 22 21 20 
10	3	5		37 32 27 23 14 
11	3	7		37 36 32 30 29 27 22 
12	3	7		36 34 32 30 29 27 23 
13	3	5		34 30 29 22 20 
14	3	6		51 47 36 31 30 29 
15	3	6		51 33 32 31 27 26 
16	3	7		51 50 37 35 34 33 32 
17	3	5		51 38 34 30 27 
18	3	3		44 29 20 
19	3	6		51 49 48 44 33 29 
20	3	5		50 48 38 33 27 
21	3	5		42 40 38 34 30 
22	3	7		51 49 48 44 38 35 33 
23	3	7		51 49 48 44 38 35 33 
24	3	4		51 48 35 30 
25	3	4		44 38 33 27 
26	3	7		50 47 46 43 41 35 34 
27	3	7		49 47 46 45 43 41 35 
28	3	6		50 47 43 41 40 34 
29	3	6		50 46 45 43 41 35 
30	3	4		49 45 44 33 
31	3	4		42 41 40 34 
32	3	5		49 47 44 42 39 
33	3	4		46 43 41 39 
34	3	4		48 45 44 39 
35	3	3		42 40 39 
36	3	2		42 40 
37	3	2		47 40 
38	3	1		47 
39	3	1		52 
40	3	1		52 
41	3	1		52 
42	3	1		52 
43	3	1		52 
44	3	1		52 
45	3	1		52 
46	3	1		52 
47	3	1		52 
48	3	1		52 
49	3	1		52 
50	3	1		52 
51	3	1		52 
52	1	0		
************************************************************************
REQUESTS/DURATIONS
jobnr.	mode	dur	R1	R2	N1	N2	
------------------------------------------------------------------------
1	1	0	0	0	0	0	
2	1	1	9	4	7	0	
	2	3	8	4	0	4	
	3	7	8	4	2	0	
3	1	5	7	4	5	0	
	2	5	6	3	0	4	
	3	10	6	2	5	0	
4	1	1	6	8	6	0	
	2	5	4	7	0	6	
	3	10	3	4	0	4	
5	1	4	6	2	10	0	
	2	8	4	2	0	4	
	3	9	4	1	10	0	
6	1	5	7	6	2	0	
	2	8	7	6	1	0	
	3	10	5	4	0	7	
7	1	6	3	8	2	0	
	2	7	2	8	0	6	
	3	10	1	8	2	0	
8	1	3	9	6	0	10	
	2	5	5	4	4	0	
	3	10	5	2	0	6	
9	1	2	7	2	0	3	
	2	6	4	2	4	0	
	3	10	3	2	2	0	
10	1	3	8	8	0	3	
	2	5	8	8	0	1	
	3	5	6	7	4	0	
11	1	2	8	2	10	0	
	2	3	6	1	0	5	
	3	4	2	1	0	5	
12	1	2	8	6	0	6	
	2	6	7	6	0	6	
	3	8	5	6	0	4	
13	1	4	4	8	8	0	
	2	8	3	6	3	0	
	3	10	3	4	1	0	
14	1	5	9	7	9	0	
	2	6	7	5	7	0	
	3	10	7	4	0	9	
15	1	2	3	9	7	0	
	2	5	2	8	0	2	
	3	6	2	8	0	1	
16	1	7	6	6	0	2	
	2	9	6	6	4	0	
	3	9	6	6	0	1	
17	1	5	2	7	0	5	
	2	6	1	5	0	5	
	3	8	1	3	0	3	
18	1	1	7	6	2	0	
	2	4	7	5	0	4	
	3	8	6	5	0	2	
19	1	5	3	3	7	0	
	2	9	3	2	0	4	
	3	10	3	1	5	0	
20	1	2	5	8	9	0	
	2	5	4	7	0	6	
	3	7	4	6	2	0	
21	1	1	8	10	0	3	
	2	2	4	8	0	2	
	3	8	2	8	0	1	
22	1	4	5	9	6	0	
	2	4	5	9	0	8	
	3	9	4	9	0	6	
23	1	4	4	5	0	7	
	2	9	3	5	2	0	
	3	10	3	5	1	0	
24	1	1	4	9	5	0	
	2	1	4	7	0	4	
	3	7	3	5	0	3	
25	1	2	8	8	10	0	
	2	3	4	8	8	0	
	3	4	2	8	0	5	
26	1	3	7	6	10	0	
	2	4	6	5	7	0	
	3	5	5	3	0	5	
27	1	5	7	5	8	0	
	2	8	7	4	6	0	
	3	10	6	4	6	0	
28	1	1	1	7	0	8	
	2	5	1	6	0	6	
	3	9	1	5	0	6	
29	1	3	7	6	5	0	
	2	8	4	5	0	8	
	3	10	2	4	1	0	
30	1	6	2	6	10	0	
	2	7	2	6	0	8	
	3	10	1	5	0	6	
31	1	1	5	8	0	8	
	2	5	5	4	3	0	
	3	10	3	1	3	0	
32	1	1	7	2	0	8	
	2	4	7	2	0	7	
	3	9	6	2	6	0	
33	1	4	6	6	0	10	
	2	6	4	5	0	10	
	3	6	4	5	2	0	
34	1	2	6	7	0	8	
	2	9	6	7	3	0	
	3	10	3	7	0	5	
35	1	3	9	7	7	0	
	2	3	7	4	0	9	
	3	4	3	4	0	9	
36	1	3	7	8	5	0	
	2	6	6	8	0	8	
	3	10	5	6	2	0	
37	1	5	10	9	0	5	
	2	7	7	6	0	5	
	3	10	5	4	3	0	
38	1	1	1	10	0	7	
	2	2	1	7	8	0	
	3	4	1	5	0	3	
39	1	5	7	8	4	0	
	2	9	7	5	3	0	
	3	10	7	4	2	0	
40	1	6	6	7	3	0	
	2	9	3	6	3	0	
	3	10	1	5	3	0	
41	1	5	8	6	0	8	
	2	5	6	6	5	0	
	3	10	1	6	0	4	
42	1	3	7	5	0	9	
	2	7	5	5	0	7	
	3	10	3	5	5	0	
43	1	2	5	7	0	9	
	2	3	4	4	0	4	
	3	7	4	4	4	0	
44	1	3	7	3	6	0	
	2	4	7	3	5	0	
	3	6	5	3	5	0	
45	1	2	7	10	0	8	
	2	8	5	8	6	0	
	3	9	1	5	3	0	
46	1	1	8	8	0	9	
	2	4	5	7	0	5	
	3	5	4	7	2	0	
47	1	1	9	5	7	0	
	2	2	7	3	7	0	
	3	4	1	3	6	0	
48	1	4	9	6	10	0	
	2	6	6	6	8	0	
	3	9	3	4	7	0	
49	1	7	9	9	4	0	
	2	8	7	4	3	0	
	3	9	7	4	2	0	
50	1	2	7	5	0	7	
	2	2	6	3	6	0	
	3	3	6	2	4	0	
51	1	1	4	9	5	0	
	2	5	2	9	0	6	
	3	10	2	8	4	0	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	25	25	202	201

************************************************************************
