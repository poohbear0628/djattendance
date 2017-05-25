jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	7		2 3 5 6 11 12 13 
2	3	5		21 18 14 8 4 
3	3	5		25 24 20 9 7 
4	3	5		26 20 19 16 10 
5	3	4		25 19 17 8 
6	3	7		36 31 28 25 22 21 19 
7	3	3		26 16 15 
8	3	7		36 35 32 29 28 24 15 
9	3	5		38 35 33 22 16 
10	3	8		41 36 35 31 30 25 24 22 
11	3	7		30 29 28 27 26 25 24 
12	3	7		37 35 33 31 30 29 25 
13	3	7		36 35 34 29 28 27 24 
14	3	8		51 41 37 35 33 30 28 25 
15	3	7		41 40 38 34 33 30 22 
16	3	5		34 32 30 28 23 
17	3	4		33 28 27 23 
18	3	6		41 38 36 34 28 24 
19	3	4		38 30 29 24 
20	3	8		49 48 47 39 38 36 31 28 
21	3	8		51 46 39 38 35 34 33 32 
22	3	6		51 48 45 44 43 27 
23	3	5		48 47 39 31 29 
24	3	7		51 49 48 43 40 37 33 
25	3	7		50 48 46 43 39 38 34 
26	3	5		51 44 42 37 35 
27	3	4		50 49 39 37 
28	3	5		50 45 44 43 40 
29	3	5		46 45 44 42 41 
30	3	4		47 46 45 39 
31	3	4		51 45 43 40 
32	3	4		49 44 43 42 
33	3	3		50 44 42 
34	3	3		49 47 45 
35	3	3		48 45 43 
36	3	3		46 44 43 
37	3	2		47 46 
38	3	2		44 42 
39	3	1		42 
40	3	1		42 
41	3	1		43 
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
2	1	1	5	5	8	10	
	2	5	4	5	6	5	
	3	7	1	5	5	3	
3	1	2	4	9	3	8	
	2	9	4	8	2	8	
	3	10	3	7	2	7	
4	1	2	3	10	7	3	
	2	9	3	9	7	2	
	3	10	2	9	7	1	
5	1	1	2	3	5	7	
	2	2	2	3	2	6	
	3	3	2	3	2	5	
6	1	2	7	9	7	5	
	2	6	7	8	7	5	
	3	8	6	6	7	2	
7	1	4	10	8	2	7	
	2	5	6	6	2	6	
	3	9	3	3	2	6	
8	1	2	8	9	8	5	
	2	5	7	8	8	4	
	3	7	7	7	8	3	
9	1	1	9	8	5	8	
	2	2	7	8	3	6	
	3	6	7	8	3	5	
10	1	1	7	6	9	7	
	2	4	3	6	7	7	
	3	7	2	6	4	7	
11	1	5	3	3	8	8	
	2	6	2	2	8	5	
	3	9	2	2	6	4	
12	1	4	10	8	7	8	
	2	5	8	7	7	7	
	3	9	8	6	7	5	
13	1	1	4	5	7	3	
	2	3	3	4	6	3	
	3	8	2	4	2	1	
14	1	3	7	5	6	5	
	2	5	4	3	6	3	
	3	6	4	2	6	2	
15	1	5	5	6	10	5	
	2	7	5	5	8	4	
	3	10	5	4	5	2	
16	1	1	7	6	9	7	
	2	2	6	5	6	5	
	3	9	5	5	5	3	
17	1	2	8	7	6	5	
	2	6	6	6	5	3	
	3	8	6	6	3	2	
18	1	5	9	1	6	8	
	2	6	8	1	6	7	
	3	7	8	1	4	7	
19	1	5	5	5	1	8	
	2	8	4	5	1	7	
	3	10	3	5	1	5	
20	1	5	9	6	6	2	
	2	6	7	5	5	1	
	3	10	5	3	5	1	
21	1	2	7	7	7	9	
	2	4	7	5	5	9	
	3	8	6	5	3	8	
22	1	2	9	6	3	2	
	2	4	9	5	2	2	
	3	5	9	5	2	1	
23	1	1	5	5	5	5	
	2	2	5	4	4	5	
	3	5	4	2	4	3	
24	1	5	7	9	8	6	
	2	9	6	7	7	5	
	3	10	5	5	6	5	
25	1	2	5	2	5	10	
	2	8	4	2	5	8	
	3	9	3	2	5	8	
26	1	1	9	7	7	6	
	2	6	6	6	5	4	
	3	7	3	5	4	3	
27	1	2	10	7	7	3	
	2	5	8	7	7	3	
	3	9	6	6	4	3	
28	1	2	5	4	9	6	
	2	3	5	4	7	4	
	3	4	4	1	4	2	
29	1	8	6	9	7	2	
	2	9	5	7	5	2	
	3	10	5	6	5	2	
30	1	3	2	9	6	7	
	2	4	1	7	4	6	
	3	7	1	7	4	5	
31	1	3	4	5	9	2	
	2	6	2	4	7	1	
	3	9	2	3	5	1	
32	1	2	6	8	9	7	
	2	4	5	5	4	4	
	3	7	4	3	2	1	
33	1	2	9	9	8	9	
	2	3	9	4	7	8	
	3	8	9	4	7	7	
34	1	1	10	7	5	5	
	2	3	6	5	4	4	
	3	7	6	5	3	4	
35	1	5	8	9	8	10	
	2	9	7	8	7	10	
	3	10	7	7	7	10	
36	1	5	8	10	6	8	
	2	7	8	7	3	8	
	3	8	8	1	2	7	
37	1	4	7	6	5	10	
	2	5	4	4	4	8	
	3	10	3	4	3	7	
38	1	3	10	5	8	10	
	2	7	8	4	7	8	
	3	8	5	4	7	4	
39	1	1	10	4	5	6	
	2	7	7	3	5	6	
	3	8	2	3	5	5	
40	1	1	10	6	3	4	
	2	4	9	5	3	4	
	3	7	7	4	1	3	
41	1	1	5	8	6	2	
	2	2	4	6	3	2	
	3	9	4	3	2	1	
42	1	1	10	2	7	2	
	2	8	7	1	5	2	
	3	9	4	1	4	1	
43	1	5	8	7	9	7	
	2	7	7	4	4	6	
	3	10	5	2	3	6	
44	1	2	3	9	9	7	
	2	3	2	7	7	6	
	3	10	2	3	5	4	
45	1	1	6	4	10	5	
	2	4	5	4	8	5	
	3	8	3	4	6	5	
46	1	1	6	5	10	10	
	2	2	5	5	7	6	
	3	8	3	5	4	2	
47	1	1	7	5	7	7	
	2	2	6	5	5	5	
	3	3	4	2	5	4	
48	1	7	5	8	9	10	
	2	8	5	7	7	10	
	3	9	1	6	5	10	
49	1	3	8	9	4	5	
	2	6	5	6	2	4	
	3	8	3	2	2	2	
50	1	5	5	4	4	8	
	2	7	4	3	2	7	
	3	8	4	3	1	5	
51	1	1	7	8	9	10	
	2	2	6	8	9	5	
	3	7	6	7	9	4	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	58	52	243	233

************************************************************************
