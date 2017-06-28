jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	6		2 3 4 5 11 14 
2	3	3		17 8 6 
3	3	4		12 10 9 8 
4	3	4		17 12 10 7 
5	3	3		17 12 7 
6	3	2		10 7 
7	3	4		22 16 15 13 
8	3	3		22 15 13 
9	3	3		22 16 13 
10	3	2		16 13 
11	3	2		15 13 
12	3	5		23 22 21 20 18 
13	3	5		28 23 21 20 19 
14	3	2		25 15 
15	3	3		23 20 18 
16	3	2		25 18 
17	3	4		28 27 21 20 
18	3	5		30 28 27 26 24 
19	3	6		36 32 30 29 27 25 
20	3	3		31 26 24 
21	3	4		37 31 29 26 
22	3	3		36 31 25 
23	3	6		42 37 36 35 34 32 
24	3	4		42 37 32 29 
25	3	5		42 37 35 34 33 
26	3	4		42 36 34 32 
27	3	5		42 39 37 34 31 
28	3	4		42 39 34 31 
29	3	3		41 35 33 
30	3	5		42 41 40 38 37 
31	3	4		44 41 40 38 
32	3	1		33 
33	3	3		44 40 38 
34	3	4		50 47 44 41 
35	3	3		44 43 39 
36	3	3		51 48 39 
37	3	5		51 49 47 46 44 
38	3	4		51 49 48 43 
39	3	5		50 49 47 46 45 
40	3	3		50 47 43 
41	3	2		49 43 
42	3	3		48 47 45 
43	3	2		46 45 
44	3	2		48 45 
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
2	1	3	6	0	0	7	
	2	10	6	0	4	0	
	3	10	0	2	0	4	
3	1	3	7	0	0	6	
	2	5	5	0	0	5	
	3	8	0	7	7	0	
4	1	7	8	0	4	0	
	2	8	8	0	3	0	
	3	10	7	0	2	0	
5	1	4	0	7	9	0	
	2	7	0	6	7	0	
	3	9	7	0	0	5	
6	1	1	0	8	0	7	
	2	5	0	6	9	0	
	3	5	1	0	0	5	
7	1	3	0	10	0	4	
	2	6	0	9	3	0	
	3	10	8	0	3	0	
8	1	2	7	0	0	8	
	2	4	7	0	0	7	
	3	7	0	4	0	5	
9	1	2	0	7	4	0	
	2	3	0	5	0	3	
	3	7	3	0	0	3	
10	1	3	6	0	3	0	
	2	5	4	0	0	5	
	3	5	3	0	1	0	
11	1	2	0	5	5	0	
	2	7	6	0	4	0	
	3	8	0	2	4	0	
12	1	3	0	7	6	0	
	2	6	3	0	0	6	
	3	7	0	3	3	0	
13	1	3	6	0	0	5	
	2	7	6	0	2	0	
	3	8	6	0	1	0	
14	1	4	7	0	0	9	
	2	5	6	0	3	0	
	3	9	0	5	2	0	
15	1	1	0	2	6	0	
	2	1	4	0	0	4	
	3	9	0	1	0	2	
16	1	3	0	4	0	6	
	2	6	8	0	0	4	
	3	10	0	2	0	2	
17	1	3	0	10	0	9	
	2	9	0	9	2	0	
	3	10	0	8	2	0	
18	1	2	2	0	5	0	
	2	6	0	7	5	0	
	3	9	1	0	0	4	
19	1	1	6	0	0	6	
	2	6	0	2	7	0	
	3	10	6	0	7	0	
20	1	2	8	0	6	0	
	2	2	8	0	0	2	
	3	5	0	5	3	0	
21	1	2	8	0	10	0	
	2	3	0	6	0	8	
	3	6	0	6	8	0	
22	1	2	0	7	5	0	
	2	4	3	0	4	0	
	3	5	0	6	0	2	
23	1	2	5	0	0	8	
	2	4	0	2	0	5	
	3	10	0	2	0	2	
24	1	2	7	0	0	6	
	2	5	5	0	3	0	
	3	10	0	2	0	2	
25	1	3	0	7	0	5	
	2	5	4	0	0	3	
	3	7	0	7	2	0	
26	1	3	7	0	10	0	
	2	3	0	8	0	2	
	3	5	4	0	0	1	
27	1	2	0	6	0	5	
	2	3	4	0	0	5	
	3	6	0	6	3	0	
28	1	1	8	0	4	0	
	2	2	8	0	0	4	
	3	7	0	5	0	4	
29	1	6	0	3	0	6	
	2	8	7	0	5	0	
	3	10	0	1	5	0	
30	1	2	0	7	0	4	
	2	7	0	5	0	4	
	3	9	0	5	0	3	
31	1	3	0	10	5	0	
	2	9	9	0	0	7	
	3	10	9	0	0	6	
32	1	3	0	2	0	8	
	2	5	0	2	0	7	
	3	8	5	0	0	8	
33	1	4	0	4	0	6	
	2	9	0	4	3	0	
	3	10	4	0	0	6	
34	1	2	10	0	5	0	
	2	10	7	0	0	5	
	3	10	0	2	0	5	
35	1	2	6	0	2	0	
	2	4	0	6	0	5	
	3	5	3	0	0	4	
36	1	2	0	7	0	6	
	2	8	4	0	2	0	
	3	9	0	1	0	4	
37	1	1	5	0	0	5	
	2	4	0	5	7	0	
	3	7	0	3	7	0	
38	1	9	0	8	0	4	
	2	9	6	0	0	3	
	3	10	0	7	0	3	
39	1	1	0	7	0	4	
	2	3	2	0	5	0	
	3	7	1	0	0	2	
40	1	6	10	0	5	0	
	2	7	0	6	0	3	
	3	10	0	6	2	0	
41	1	2	0	5	0	8	
	2	5	4	0	0	6	
	3	7	0	2	3	0	
42	1	1	6	0	6	0	
	2	7	0	2	6	0	
	3	8	2	0	0	3	
43	1	4	0	7	8	0	
	2	8	0	7	0	7	
	3	9	0	7	7	0	
44	1	1	0	5	9	0	
	2	8	7	0	5	0	
	3	10	0	2	4	0	
45	1	4	6	0	0	10	
	2	5	0	8	0	7	
	3	7	3	0	3	0	
46	1	2	9	0	7	0	
	2	3	8	0	7	0	
	3	7	0	4	0	3	
47	1	2	5	0	0	5	
	2	6	4	0	0	4	
	3	8	0	6	0	4	
48	1	2	0	7	0	5	
	2	5	8	0	0	3	
	3	8	0	5	8	0	
49	1	2	0	8	0	6	
	2	6	8	0	8	0	
	3	7	6	0	7	0	
50	1	4	3	0	4	0	
	2	6	0	6	0	6	
	3	7	3	0	2	0	
51	1	2	9	0	0	5	
	2	4	6	0	4	0	
	3	7	0	4	4	0	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	19	17	115	142

************************************************************************
