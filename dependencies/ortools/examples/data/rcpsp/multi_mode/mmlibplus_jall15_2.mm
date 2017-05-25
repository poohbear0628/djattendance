jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	8		2 3 4 5 6 8 12 19 
2	3	6		31 21 20 14 10 7 
3	3	6		29 27 21 16 11 9 
4	3	8		34 31 27 23 22 21 18 11 
5	3	6		29 26 23 22 16 15 
6	3	6		34 31 29 27 18 13 
7	3	5		30 27 26 15 13 
8	3	8		34 33 32 31 30 28 23 22 
9	3	7		33 32 30 28 24 23 22 
10	3	6		32 30 28 27 23 22 
11	3	4		39 30 26 15 
12	3	4		33 32 22 17 
13	3	5		36 33 32 23 22 
14	3	5		34 29 28 26 22 
15	3	8		51 49 36 35 33 32 28 24 
16	3	7		49 39 35 34 32 31 30 
17	3	6		43 40 36 34 28 25 
18	3	5		43 39 32 28 25 
19	3	5		50 39 37 26 25 
20	3	7		51 49 43 38 35 32 28 
21	3	7		50 49 42 38 37 36 32 
22	3	4		48 43 40 25 
23	3	8		51 50 49 43 39 38 37 35 
24	3	6		50 46 43 42 40 37 
25	3	6		51 49 42 41 38 35 
26	3	4		49 47 43 32 
27	3	6		49 48 47 46 42 40 
28	3	5		50 46 42 41 37 
29	3	5		50 47 46 43 41 
30	3	3		43 41 36 
31	3	5		50 48 46 45 42 
32	3	4		48 46 44 40 
33	3	4		48 47 46 44 
34	3	2		45 37 
35	3	3		46 45 44 
36	3	3		48 46 45 
37	3	2		48 47 
38	3	2		47 46 
39	3	2		47 44 
40	3	1		41 
41	3	1		45 
42	3	1		44 
43	3	1		44 
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
2	1	6	6	7	8	9	
	2	7	3	6	8	9	
	3	8	3	4	5	8	
3	1	2	5	1	8	7	
	2	6	5	1	7	7	
	3	10	5	1	7	4	
4	1	2	9	7	7	6	
	2	5	8	5	6	5	
	3	9	7	5	6	4	
5	1	7	8	5	3	5	
	2	9	7	4	1	3	
	3	10	7	1	1	2	
6	1	1	9	5	7	8	
	2	7	7	3	7	8	
	3	8	6	3	5	6	
7	1	5	5	7	10	7	
	2	6	3	3	8	5	
	3	7	2	1	8	1	
8	1	6	9	7	6	8	
	2	8	7	5	3	3	
	3	10	7	2	3	2	
9	1	6	10	4	6	10	
	2	7	8	2	5	6	
	3	10	8	2	3	4	
10	1	3	8	7	9	8	
	2	8	6	7	7	5	
	3	9	3	7	6	4	
11	1	2	6	8	7	8	
	2	3	3	5	6	8	
	3	5	3	2	5	6	
12	1	4	4	3	6	6	
	2	5	4	3	5	6	
	3	9	4	2	2	6	
13	1	4	5	6	7	7	
	2	9	4	5	7	6	
	3	10	4	5	7	5	
14	1	6	8	10	7	7	
	2	7	5	6	7	5	
	3	9	3	5	4	4	
15	1	1	8	9	4	3	
	2	5	6	5	3	1	
	3	8	5	3	2	1	
16	1	3	5	7	3	10	
	2	9	5	5	3	8	
	3	10	5	3	1	8	
17	1	3	5	5	4	8	
	2	5	5	5	3	7	
	3	9	5	5	3	6	
18	1	5	7	7	3	8	
	2	8	6	7	2	7	
	3	9	6	7	2	6	
19	1	1	8	6	3	7	
	2	4	6	5	3	6	
	3	5	3	5	3	4	
20	1	8	3	2	9	1	
	2	9	3	1	5	1	
	3	10	2	1	5	1	
21	1	5	2	2	9	9	
	2	6	2	1	9	6	
	3	7	2	1	9	3	
22	1	6	5	9	7	5	
	2	8	3	8	7	5	
	3	9	3	8	7	4	
23	1	2	4	4	9	9	
	2	4	4	3	7	7	
	3	5	4	1	4	4	
24	1	1	8	4	1	7	
	2	4	7	4	1	6	
	3	7	7	2	1	5	
25	1	6	9	2	10	4	
	2	7	9	2	8	3	
	3	8	9	1	7	3	
26	1	3	9	5	9	2	
	2	8	9	3	4	2	
	3	9	9	3	3	1	
27	1	1	6	6	6	7	
	2	4	4	5	6	4	
	3	6	3	4	6	3	
28	1	3	3	5	5	7	
	2	6	3	4	3	5	
	3	9	2	3	3	4	
29	1	2	7	7	2	8	
	2	7	6	7	2	4	
	3	8	6	7	2	3	
30	1	3	10	5	5	3	
	2	4	7	4	5	3	
	3	6	4	1	5	3	
31	1	1	7	9	4	4	
	2	2	6	7	2	3	
	3	9	5	5	1	2	
32	1	2	2	7	10	6	
	2	6	2	5	9	4	
	3	7	2	2	9	3	
33	1	8	3	4	10	10	
	2	9	3	3	8	9	
	3	10	3	3	6	8	
34	1	5	7	9	2	4	
	2	9	7	9	2	3	
	3	10	7	9	2	2	
35	1	4	6	6	5	8	
	2	6	5	5	4	3	
	3	7	5	3	3	3	
36	1	5	5	2	2	1	
	2	6	4	2	1	2	
	3	7	4	2	1	1	
37	1	3	7	4	10	7	
	2	4	6	3	10	6	
	3	8	6	2	10	4	
38	1	3	6	8	6	7	
	2	5	3	8	4	7	
	3	7	3	6	3	7	
39	1	1	7	9	9	5	
	2	3	6	8	9	4	
	3	9	5	7	9	2	
40	1	2	2	9	7	3	
	2	4	2	9	5	3	
	3	5	2	8	5	1	
41	1	2	8	3	8	6	
	2	3	5	3	7	6	
	3	6	3	2	6	5	
42	1	1	9	10	2	9	
	2	5	7	7	2	8	
	3	7	4	4	2	8	
43	1	2	5	8	7	3	
	2	4	4	6	3	1	
	3	9	4	2	3	1	
44	1	3	4	5	8	4	
	2	4	4	5	5	3	
	3	8	3	5	1	3	
45	1	5	6	2	8	5	
	2	6	6	2	6	4	
	3	10	3	1	6	3	
46	1	3	7	7	7	9	
	2	4	6	6	7	5	
	3	7	4	6	6	3	
47	1	2	7	5	9	4	
	2	3	6	4	7	3	
	3	9	6	2	6	2	
48	1	2	4	7	4	4	
	2	3	4	6	2	4	
	3	4	4	6	2	2	
49	1	6	6	7	5	5	
	2	9	6	4	3	5	
	3	10	6	4	2	4	
50	1	2	8	6	10	7	
	2	6	6	6	8	7	
	3	7	6	6	8	6	
51	1	1	8	5	2	8	
	2	2	6	4	2	5	
	3	4	6	4	2	2	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	34	29	290	282

************************************************************************
