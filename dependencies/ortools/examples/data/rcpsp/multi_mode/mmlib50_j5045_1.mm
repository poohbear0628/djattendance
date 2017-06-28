jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	11		2 3 4 5 6 7 8 11 12 13 20 
2	3	5		22 16 15 10 9 
3	3	7		29 28 27 25 24 21 14 
4	3	9		34 32 31 29 28 27 26 25 18 
5	3	7		29 28 27 26 25 24 19 
6	3	3		32 18 9 
7	3	7		34 32 31 29 28 25 18 
8	3	5		32 29 27 22 16 
9	3	7		42 34 31 30 29 28 25 
10	3	5		32 31 27 26 23 
11	3	5		31 29 28 25 19 
12	3	5		32 30 29 22 17 
13	3	8		51 42 40 36 34 32 30 25 
14	3	6		37 36 34 32 30 22 
15	3	6		40 36 34 33 32 27 
16	3	6		51 42 37 36 34 26 
17	3	8		50 42 41 40 37 36 34 33 
18	3	6		42 41 40 36 35 30 
19	3	5		51 40 36 32 30 
20	3	3		35 29 27 
21	3	4		41 35 31 30 
22	3	7		51 50 45 41 40 39 35 
23	3	7		51 50 41 38 37 36 33 
24	3	5		50 47 37 36 34 
25	3	6		50 47 45 41 37 35 
26	3	2		49 30 
27	3	8		51 50 48 46 45 42 38 37 
28	3	6		49 46 40 39 38 36 
29	3	6		51 49 47 46 38 36 
30	3	4		50 48 38 33 
31	3	6		49 46 45 43 40 39 
32	3	4		47 45 44 35 
33	3	5		47 46 45 43 39 
34	3	2		45 35 
35	3	3		49 46 38 
36	3	3		48 45 44 
37	3	1		39 
38	3	1		43 
39	3	1		44 
40	3	1		47 
41	3	1		48 
42	3	1		43 
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
2	1	1	10	10	0	7	
	2	1	6	7	6	0	
	3	7	4	6	0	4	
3	1	3	9	7	0	10	
	2	4	8	5	0	9	
	3	8	6	3	0	9	
4	1	2	7	5	9	0	
	2	3	6	3	6	0	
	3	5	5	1	1	0	
5	1	1	5	6	0	6	
	2	6	4	5	8	0	
	3	10	2	5	8	0	
6	1	3	10	5	6	0	
	2	8	9	4	5	0	
	3	9	8	4	5	0	
7	1	5	4	6	0	8	
	2	7	3	6	0	8	
	3	7	3	6	6	0	
8	1	7	4	6	5	0	
	2	8	4	5	5	0	
	3	10	4	5	0	4	
9	1	2	6	2	0	4	
	2	8	3	1	8	0	
	3	9	2	1	0	4	
10	1	3	4	6	0	6	
	2	6	3	5	6	0	
	3	7	2	2	0	4	
11	1	1	10	7	8	0	
	2	4	7	6	6	0	
	3	10	6	5	4	0	
12	1	1	3	2	0	5	
	2	8	3	2	9	0	
	3	9	3	2	0	2	
13	1	1	2	7	0	8	
	2	2	1	7	2	0	
	3	6	1	4	0	6	
14	1	3	9	3	5	0	
	2	6	9	2	5	0	
	3	9	9	1	4	0	
15	1	9	7	6	0	10	
	2	10	7	5	0	9	
	3	10	7	5	8	0	
16	1	1	3	8	6	0	
	2	6	3	7	4	0	
	3	9	2	7	0	3	
17	1	2	10	6	0	7	
	2	6	5	4	8	0	
	3	8	5	4	6	0	
18	1	4	1	3	0	6	
	2	6	1	2	1	0	
	3	9	1	2	0	4	
19	1	3	9	6	7	0	
	2	9	8	4	0	4	
	3	10	4	2	3	0	
20	1	1	8	2	0	10	
	2	2	7	1	0	8	
	3	4	2	1	0	8	
21	1	4	9	9	0	6	
	2	7	8	9	0	4	
	3	10	5	9	3	0	
22	1	2	6	10	0	3	
	2	5	5	7	2	0	
	3	10	1	3	1	0	
23	1	8	6	7	4	0	
	2	9	5	7	0	6	
	3	9	5	7	4	0	
24	1	1	5	5	9	0	
	2	9	4	4	0	4	
	3	9	4	4	7	0	
25	1	2	9	5	0	6	
	2	7	7	5	0	5	
	3	9	7	3	4	0	
26	1	1	9	7	6	0	
	2	4	7	7	6	0	
	3	10	6	7	0	2	
27	1	5	10	9	0	8	
	2	6	9	8	0	8	
	3	10	9	6	3	0	
28	1	5	3	5	9	0	
	2	7	2	5	6	0	
	3	8	1	5	0	2	
29	1	3	7	6	0	4	
	2	6	6	5	7	0	
	3	10	4	3	0	3	
30	1	1	7	1	6	0	
	2	2	7	1	0	1	
	3	6	7	1	3	0	
31	1	1	10	7	0	5	
	2	4	6	6	3	0	
	3	9	3	6	0	4	
32	1	8	3	8	5	0	
	2	9	2	6	4	0	
	3	9	2	6	0	3	
33	1	4	9	8	0	1	
	2	6	6	8	5	0	
	3	9	1	7	0	1	
34	1	3	3	8	0	8	
	2	6	1	6	0	7	
	3	9	1	4	1	0	
35	1	4	6	9	4	0	
	2	5	6	8	3	0	
	3	6	5	7	0	6	
36	1	3	8	10	5	0	
	2	5	6	5	0	2	
	3	8	6	5	0	1	
37	1	5	3	9	0	7	
	2	10	2	8	6	0	
	3	10	2	7	0	4	
38	1	7	9	8	8	0	
	2	10	9	4	3	0	
	3	10	8	2	0	2	
39	1	2	8	7	6	0	
	2	10	5	6	6	0	
	3	10	4	5	0	9	
40	1	3	8	8	0	7	
	2	4	7	5	7	0	
	3	6	6	4	7	0	
41	1	6	10	7	5	0	
	2	7	6	7	4	0	
	3	8	5	7	3	0	
42	1	6	5	6	4	0	
	2	8	5	6	0	4	
	3	9	5	5	0	4	
43	1	3	4	7	0	4	
	2	6	4	7	0	3	
	3	7	4	5	0	3	
44	1	1	8	6	5	0	
	2	6	7	5	0	4	
	3	9	7	2	0	2	
45	1	1	6	8	7	0	
	2	5	5	4	6	0	
	3	6	5	1	6	0	
46	1	3	6	6	3	0	
	2	7	6	6	2	0	
	3	9	3	3	0	5	
47	1	5	9	5	0	7	
	2	8	7	3	5	0	
	3	9	5	3	0	5	
48	1	4	8	7	0	7	
	2	8	7	5	0	4	
	3	9	1	2	0	4	
49	1	3	3	7	0	5	
	2	4	3	5	5	0	
	3	6	3	4	0	2	
50	1	2	6	3	8	0	
	2	6	2	2	7	0	
	3	10	2	2	6	0	
51	1	3	9	7	8	0	
	2	5	8	7	0	2	
	3	10	6	7	7	0	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	25	23	145	125

************************************************************************
