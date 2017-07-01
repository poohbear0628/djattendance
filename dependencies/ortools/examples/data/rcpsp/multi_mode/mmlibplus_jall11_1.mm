jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	9		2 3 4 5 7 11 12 13 14 
2	3	3		20 10 6 
3	3	7		30 24 20 18 17 9 8 
4	3	5		24 23 20 18 6 
5	3	9		33 30 29 22 21 19 18 16 15 
6	3	4		30 29 15 9 
7	3	9		33 30 29 27 25 24 20 18 17 
8	3	9		50 49 33 32 29 28 23 22 21 
9	3	7		33 28 26 25 22 21 19 
10	3	6		30 29 27 24 23 18 
11	3	6		48 33 26 22 20 19 
12	3	5		36 30 27 25 23 
13	3	6		36 32 31 27 26 25 
14	3	8		50 49 48 47 35 32 29 27 
15	3	5		44 36 27 26 25 
16	3	5		51 35 34 32 25 
17	3	10		51 50 49 48 47 46 38 37 34 28 
18	3	6		49 48 36 32 31 26 
19	3	8		50 49 47 45 36 34 32 31 
20	3	5		51 37 34 32 28 
21	3	7		51 48 46 42 39 38 31 
22	3	5		51 44 40 36 27 
23	3	4		51 44 42 26 
24	3	6		50 49 48 45 35 32 
25	3	10		50 49 48 47 45 42 40 39 38 37 
26	3	6		47 45 39 38 37 35 
27	3	6		46 45 43 42 37 34 
28	3	6		45 44 43 41 40 36 
29	3	5		43 40 38 36 34 
30	3	4		42 40 37 34 
31	3	3		44 37 35 
32	3	5		46 44 42 40 39 
33	3	4		51 47 40 39 
34	3	2		41 39 
35	3	2		43 40 
36	3	2		42 39 
37	3	1		41 
38	3	1		41 
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
2	1	4	5	8	8	7	
	2	5	5	8	5	6	
	3	9	3	6	4	6	
3	1	3	7	8	8	6	
	2	5	7	7	4	6	
	3	9	4	6	3	5	
4	1	2	7	8	8	7	
	2	8	5	7	6	5	
	3	9	2	5	5	5	
5	1	3	6	10	9	3	
	2	4	4	10	7	2	
	3	6	2	10	7	1	
6	1	3	2	3	4	5	
	2	5	2	1	4	4	
	3	10	2	1	2	4	
7	1	1	2	3	1	10	
	2	3	1	3	1	9	
	3	7	1	3	1	8	
8	1	6	7	8	8	4	
	2	8	7	8	5	3	
	3	9	7	5	4	3	
9	1	6	1	7	8	4	
	2	9	1	7	7	2	
	3	10	1	7	2	1	
10	1	4	5	6	7	6	
	2	5	5	5	7	5	
	3	9	5	4	7	1	
11	1	4	7	8	8	9	
	2	8	6	4	4	5	
	3	10	4	3	3	4	
12	1	5	8	5	6	10	
	2	6	8	4	3	5	
	3	8	7	4	3	4	
13	1	5	5	6	3	6	
	2	6	4	6	3	4	
	3	8	3	6	3	3	
14	1	3	7	8	8	8	
	2	5	5	7	7	5	
	3	9	2	7	7	5	
15	1	6	8	5	5	8	
	2	7	6	3	4	7	
	3	9	4	2	3	6	
16	1	1	5	9	4	6	
	2	4	4	9	3	5	
	3	8	2	8	2	4	
17	1	5	7	9	3	9	
	2	5	6	9	3	10	
	3	6	6	9	3	9	
18	1	1	5	8	7	9	
	2	7	4	7	6	9	
	3	10	4	6	6	9	
19	1	2	9	6	7	4	
	2	5	9	5	5	3	
	3	7	8	4	4	1	
20	1	2	8	4	5	5	
	2	3	7	3	2	4	
	3	8	6	3	2	4	
21	1	3	5	3	9	9	
	2	5	4	3	8	8	
	3	9	3	2	6	6	
22	1	2	9	6	6	7	
	2	3	8	5	6	3	
	3	7	6	4	6	2	
23	1	1	2	4	9	6	
	2	2	2	2	9	6	
	3	3	1	1	8	6	
24	1	6	8	4	4	3	
	2	7	6	4	4	3	
	3	8	6	4	4	2	
25	1	2	7	8	3	7	
	2	4	5	7	3	7	
	3	7	5	7	3	6	
26	1	3	9	5	5	4	
	2	4	7	4	5	4	
	3	5	7	3	5	4	
27	1	4	6	5	6	6	
	2	5	5	4	3	5	
	3	8	4	4	2	5	
28	1	6	9	9	6	4	
	2	8	3	9	6	2	
	3	10	2	9	5	1	
29	1	3	6	8	7	5	
	2	4	4	5	4	5	
	3	5	4	3	4	5	
30	1	1	6	5	8	6	
	2	2	5	3	8	6	
	3	6	5	2	8	5	
31	1	4	3	9	10	8	
	2	6	2	9	8	7	
	3	9	1	9	6	6	
32	1	5	7	7	8	3	
	2	6	6	6	7	3	
	3	10	6	5	6	3	
33	1	2	6	1	8	4	
	2	3	5	1	8	3	
	3	5	4	1	8	2	
34	1	4	7	4	3	7	
	2	5	7	2	3	5	
	3	8	5	2	3	3	
35	1	2	6	9	2	6	
	2	6	6	7	2	4	
	3	7	5	5	1	2	
36	1	2	6	2	9	6	
	2	7	5	1	7	3	
	3	8	4	1	7	2	
37	1	4	7	5	9	4	
	2	7	6	3	8	3	
	3	9	4	3	7	1	
38	1	1	10	8	8	3	
	2	4	8	6	8	3	
	3	7	8	6	8	2	
39	1	4	7	3	9	6	
	2	6	6	2	7	4	
	3	9	6	2	5	1	
40	1	2	7	7	4	8	
	2	5	4	5	3	6	
	3	7	3	2	3	5	
41	1	3	6	4	5	9	
	2	5	5	4	5	9	
	3	8	5	2	5	8	
42	1	1	5	5	4	3	
	2	5	4	5	3	2	
	3	8	4	1	2	1	
43	1	2	10	7	7	10	
	2	4	9	7	5	7	
	3	9	9	5	5	3	
44	1	7	6	5	2	5	
	2	8	6	5	2	3	
	3	10	6	1	2	2	
45	1	1	9	6	5	8	
	2	2	6	4	3	7	
	3	4	6	2	1	5	
46	1	7	6	6	6	5	
	2	8	6	3	4	5	
	3	9	6	2	4	5	
47	1	4	9	5	7	3	
	2	6	6	4	3	3	
	3	7	5	3	2	2	
48	1	3	7	8	5	6	
	2	8	4	7	3	5	
	3	9	2	7	3	5	
49	1	2	9	4	4	3	
	2	5	9	2	3	3	
	3	10	9	1	3	3	
50	1	2	8	6	10	5	
	2	3	7	5	8	5	
	3	5	6	5	7	3	
51	1	3	6	8	4	6	
	2	4	5	7	4	3	
	3	7	2	6	3	2	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	23	23	261	247

************************************************************************
