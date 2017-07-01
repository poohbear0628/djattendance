jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	4		2 3 4 6 
2	3	4		14 10 7 5 
3	3	7		20 18 15 12 11 10 9 
4	3	6		18 15 14 13 10 9 
5	3	4		23 20 9 8 
6	3	5		23 15 14 13 9 
7	3	5		28 23 20 18 13 
8	3	3		16 15 13 
9	3	4		22 21 17 16 
10	3	7		28 26 24 23 22 21 19 
11	3	2		28 13 
12	3	4		23 22 21 17 
13	3	3		21 19 17 
14	3	3		28 21 17 
15	3	4		28 24 22 19 
16	3	3		28 24 19 
17	3	5		31 27 26 25 24 
18	3	3		31 26 21 
19	3	4		31 29 27 25 
20	3	3		33 24 22 
21	3	3		29 27 25 
22	3	3		30 29 27 
23	3	3		30 29 27 
24	3	4		41 40 30 29 
25	3	4		41 40 36 30 
26	3	4		41 40 36 30 
27	3	5		41 40 36 34 32 
28	3	3		39 35 31 
29	3	5		39 38 36 35 34 
30	3	2		34 32 
31	3	4		43 41 40 33 
32	3	5		45 43 39 38 35 
33	3	5		46 44 42 38 37 
34	3	4		46 43 42 37 
35	3	4		51 46 44 42 
36	3	4		50 46 43 42 
37	3	4		51 50 47 45 
38	3	4		50 49 48 47 
39	3	4		51 49 48 47 
40	3	4		50 49 48 47 
41	3	1		42 
42	3	3		49 48 47 
43	3	3		49 48 47 
44	3	3		50 48 47 
45	3	2		49 48 
46	3	1		47 
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
2	1	1	8	9	0	8	
	2	3	7	9	7	0	
	3	6	7	8	5	0	
3	1	1	9	5	0	9	
	2	4	8	3	0	9	
	3	5	5	1	6	0	
4	1	3	4	8	0	5	
	2	7	3	6	0	3	
	3	10	2	6	5	0	
5	1	7	6	8	5	0	
	2	8	6	8	4	0	
	3	10	4	8	3	0	
6	1	4	7	6	0	10	
	2	9	5	6	8	0	
	3	10	5	6	7	0	
7	1	3	7	4	6	0	
	2	4	5	3	3	0	
	3	8	5	2	0	5	
8	1	1	4	7	0	6	
	2	2	3	6	0	6	
	3	9	3	5	4	0	
9	1	2	4	8	0	7	
	2	8	3	6	8	0	
	3	9	3	5	8	0	
10	1	1	10	7	0	5	
	2	4	5	6	0	5	
	3	10	1	5	2	0	
11	1	5	6	8	6	0	
	2	8	4	6	0	7	
	3	9	3	6	0	7	
12	1	3	6	2	0	4	
	2	5	6	2	9	0	
	3	7	4	2	0	2	
13	1	7	8	5	0	10	
	2	8	7	3	6	0	
	3	9	6	3	0	6	
14	1	1	8	7	0	9	
	2	2	6	6	0	5	
	3	7	5	4	0	3	
15	1	1	5	3	0	8	
	2	3	5	3	0	7	
	3	9	5	3	0	4	
16	1	6	10	6	6	0	
	2	9	8	6	0	4	
	3	9	8	6	1	0	
17	1	1	5	9	0	4	
	2	3	5	9	0	3	
	3	8	1	8	5	0	
18	1	5	6	6	9	0	
	2	7	6	6	0	5	
	3	9	5	6	0	3	
19	1	3	7	7	0	7	
	2	5	7	4	0	5	
	3	9	7	2	0	4	
20	1	8	9	5	3	0	
	2	10	9	4	3	0	
	3	10	8	4	0	6	
21	1	1	5	8	2	0	
	2	3	4	7	0	3	
	3	9	3	5	1	0	
22	1	1	7	7	10	0	
	2	2	6	4	0	7	
	3	8	3	4	0	7	
23	1	6	2	8	9	0	
	2	7	2	5	5	0	
	3	10	2	4	3	0	
24	1	1	8	10	7	0	
	2	5	8	8	0	3	
	3	7	6	5	0	3	
25	1	6	5	6	3	0	
	2	7	3	5	1	0	
	3	9	1	5	0	8	
26	1	1	4	6	0	7	
	2	2	2	6	2	0	
	3	4	2	6	1	0	
27	1	1	7	8	0	4	
	2	2	5	8	0	3	
	3	7	3	8	9	0	
28	1	5	8	4	0	6	
	2	9	7	3	2	0	
	3	10	3	2	2	0	
29	1	4	5	8	0	8	
	2	4	5	7	9	0	
	3	9	2	7	8	0	
30	1	3	3	8	0	10	
	2	4	1	5	0	8	
	3	9	1	2	0	6	
31	1	1	6	7	6	0	
	2	1	5	4	0	7	
	3	7	5	3	0	6	
32	1	2	8	6	9	0	
	2	9	7	3	0	7	
	3	10	7	2	0	5	
33	1	6	4	6	0	2	
	2	6	2	6	6	0	
	3	10	2	2	0	2	
34	1	3	9	5	8	0	
	2	7	5	4	5	0	
	3	7	3	2	0	4	
35	1	1	7	7	0	5	
	2	5	3	6	6	0	
	3	5	3	6	0	3	
36	1	7	8	7	0	9	
	2	9	7	6	0	9	
	3	10	7	6	4	0	
37	1	1	2	3	8	0	
	2	4	1	3	7	0	
	3	6	1	3	6	0	
38	1	2	9	7	3	0	
	2	5	9	7	2	0	
	3	9	8	6	2	0	
39	1	1	9	4	0	3	
	2	9	8	2	5	0	
	3	10	8	2	3	0	
40	1	3	10	5	0	7	
	2	6	6	4	6	0	
	3	7	5	2	0	3	
41	1	7	9	6	0	7	
	2	7	9	2	7	0	
	3	10	8	2	6	0	
42	1	2	8	7	0	10	
	2	3	5	3	2	0	
	3	8	4	1	2	0	
43	1	1	10	3	8	0	
	2	8	6	3	0	7	
	3	10	5	2	0	6	
44	1	3	6	5	9	0	
	2	4	5	3	8	0	
	3	7	4	3	0	2	
45	1	5	6	7	9	0	
	2	8	5	6	0	5	
	3	9	4	3	0	3	
46	1	2	6	7	0	3	
	2	3	5	6	7	0	
	3	10	2	3	0	3	
47	1	1	7	6	0	3	
	2	4	4	4	7	0	
	3	5	3	1	7	0	
48	1	1	7	3	10	0	
	2	9	5	2	10	0	
	3	10	5	2	9	0	
49	1	3	6	8	0	9	
	2	7	4	6	3	0	
	3	8	1	6	0	6	
50	1	1	9	8	0	5	
	2	5	5	8	0	5	
	3	6	4	5	0	5	
51	1	2	8	9	0	5	
	2	6	4	7	0	4	
	3	8	3	3	0	4	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	20	17	208	212

************************************************************************
