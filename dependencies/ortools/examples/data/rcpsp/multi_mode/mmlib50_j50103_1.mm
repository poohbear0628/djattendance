jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	6		2 3 5 6 9 10 
2	3	3		16 13 4 
3	3	2		7 4 
4	3	4		14 12 11 8 
5	3	5		21 19 17 15 14 
6	3	2		18 8 
7	3	4		20 19 16 14 
8	3	5		26 21 19 17 15 
9	3	4		22 21 20 14 
10	3	3		26 16 15 
11	3	3		23 19 18 
12	3	3		22 21 18 
13	3	3		23 22 18 
14	3	4		28 25 23 18 
15	3	4		30 24 23 20 
16	3	3		23 22 21 
17	3	5		32 30 28 25 23 
18	3	4		31 27 26 24 
19	3	3		31 27 22 
20	3	5		32 31 28 27 25 
21	3	5		32 31 30 29 27 
22	3	3		32 28 25 
23	3	4		39 35 31 29 
24	3	3		35 32 29 
25	3	2		35 29 
26	3	4		36 35 34 30 
27	3	6		43 40 37 36 35 34 
28	3	6		41 40 39 37 36 34 
29	3	5		43 40 37 34 33 
30	3	3		41 39 37 
31	3	4		51 43 41 36 
32	3	2		39 37 
33	3	2		41 36 
34	3	2		51 38 
35	3	5		51 50 48 47 41 
36	3	1		38 
37	3	1		38 
38	3	7		50 49 48 47 46 45 42 
39	3	7		51 49 47 46 45 44 43 
40	3	6		51 50 47 46 45 42 
41	3	4		49 46 45 44 
42	3	1		44 
43	3	1		48 
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
2	1	1	4	8	0	8	
	2	6	4	7	4	0	
	3	10	4	4	2	0	
3	1	2	6	8	0	4	
	2	6	5	6	0	4	
	3	8	5	6	7	0	
4	1	4	10	5	0	7	
	2	8	10	5	7	0	
	3	9	10	5	4	0	
5	1	5	5	8	0	7	
	2	6	4	4	0	5	
	3	7	4	3	0	3	
6	1	1	1	8	0	8	
	2	2	1	7	3	0	
	3	10	1	5	3	0	
7	1	7	7	4	0	3	
	2	8	5	2	0	3	
	3	10	4	1	4	0	
8	1	5	9	9	2	0	
	2	6	7	8	2	0	
	3	7	6	8	0	8	
9	1	1	6	2	6	0	
	2	2	5	1	5	0	
	3	6	1	1	3	0	
10	1	2	8	8	10	0	
	2	8	8	4	0	6	
	3	9	8	4	0	3	
11	1	1	7	8	6	0	
	2	6	7	7	4	0	
	3	9	4	6	0	2	
12	1	4	3	4	5	0	
	2	9	2	4	4	0	
	3	10	2	3	4	0	
13	1	1	9	10	5	0	
	2	5	6	4	3	0	
	3	9	3	3	3	0	
14	1	5	8	3	7	0	
	2	6	7	3	0	9	
	3	9	5	3	2	0	
15	1	6	7	6	2	0	
	2	7	5	6	0	7	
	3	10	4	5	1	0	
16	1	1	5	4	4	0	
	2	2	5	4	3	0	
	3	6	5	2	0	2	
17	1	4	2	8	0	7	
	2	7	2	7	4	0	
	3	10	2	6	1	0	
18	1	2	6	6	0	4	
	2	6	5	5	4	0	
	3	9	2	3	1	0	
19	1	2	6	7	0	6	
	2	5	5	5	0	5	
	3	6	1	5	0	4	
20	1	3	8	6	0	5	
	2	5	6	3	0	4	
	3	10	6	3	0	3	
21	1	3	8	5	0	6	
	2	3	5	5	6	0	
	3	5	4	4	0	4	
22	1	3	9	8	10	0	
	2	3	9	5	0	3	
	3	6	9	3	0	3	
23	1	2	7	7	0	7	
	2	7	7	7	2	0	
	3	8	7	7	1	0	
24	1	4	8	1	10	0	
	2	9	6	1	0	2	
	3	9	5	1	10	0	
25	1	2	9	7	5	0	
	2	6	8	6	0	5	
	3	8	7	6	0	4	
26	1	8	6	5	0	2	
	2	9	4	5	0	2	
	3	9	4	5	3	0	
27	1	2	5	6	10	0	
	2	3	3	5	5	0	
	3	7	3	5	3	0	
28	1	2	7	1	10	0	
	2	6	6	1	8	0	
	3	7	6	1	0	2	
29	1	1	3	8	8	0	
	2	1	3	7	0	6	
	3	9	3	6	0	2	
30	1	2	7	7	0	7	
	2	8	5	5	0	6	
	3	10	4	4	3	0	
31	1	4	4	9	0	7	
	2	6	3	6	2	0	
	3	6	3	5	0	5	
32	1	2	4	5	0	6	
	2	3	4	3	0	6	
	3	4	4	2	1	0	
33	1	3	8	4	0	8	
	2	4	7	3	0	6	
	3	10	6	2	0	5	
34	1	2	2	3	7	0	
	2	3	1	3	7	0	
	3	6	1	3	6	0	
35	1	2	9	6	7	0	
	2	3	9	5	0	2	
	3	9	7	3	4	0	
36	1	3	3	5	0	8	
	2	4	2	5	0	3	
	3	10	1	4	8	0	
37	1	7	6	6	0	4	
	2	8	5	5	7	0	
	3	9	5	5	0	3	
38	1	3	8	7	0	4	
	2	4	8	5	0	3	
	3	7	8	4	4	0	
39	1	3	5	9	0	9	
	2	7	5	8	5	0	
	3	8	5	8	4	0	
40	1	2	9	3	0	8	
	2	5	6	2	0	6	
	3	5	3	2	3	0	
41	1	3	8	8	6	0	
	2	4	6	6	6	0	
	3	8	4	6	6	0	
42	1	1	10	3	3	0	
	2	4	10	3	2	0	
	3	5	10	3	1	0	
43	1	1	1	9	0	10	
	2	6	1	5	0	6	
	3	10	1	5	0	4	
44	1	1	6	6	0	3	
	2	2	4	6	6	0	
	3	4	4	3	0	1	
45	1	6	8	4	0	8	
	2	8	6	4	6	0	
	3	8	5	1	0	4	
46	1	4	10	6	9	0	
	2	5	8	4	0	5	
	3	10	8	1	6	0	
47	1	5	7	10	5	0	
	2	8	6	7	5	0	
	3	9	3	5	4	0	
48	1	3	9	9	6	0	
	2	4	6	7	0	5	
	3	10	4	3	1	0	
49	1	5	8	5	0	10	
	2	6	5	4	0	7	
	3	10	3	4	3	0	
50	1	5	5	10	0	5	
	2	5	5	9	6	0	
	3	10	5	8	4	0	
51	1	3	6	6	0	6	
	2	8	6	5	5	0	
	3	10	6	4	0	2	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	45	40	83	74

************************************************************************
