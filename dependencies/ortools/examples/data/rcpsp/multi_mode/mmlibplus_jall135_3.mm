jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	3		2 3 7 
2	6	3		12 6 4 
3	6	3		15 9 5 
4	6	3		14 10 8 
5	6	4		16 14 12 11 
6	6	2		10 9 
7	6	2		10 9 
8	6	2		16 11 
9	6	3		26 16 13 
10	6	2		17 11 
11	6	2		26 13 
12	6	2		26 13 
13	6	5		25 22 21 19 18 
14	6	2		22 17 
15	6	2		22 17 
16	6	1		17 
17	6	5		27 23 21 20 19 
18	6	5		35 31 27 24 23 
19	6	4		32 31 28 24 
20	6	6		36 35 32 30 29 28 
21	6	4		33 32 31 24 
22	6	5		37 33 31 29 27 
23	6	4		40 32 30 28 
24	6	5		46 37 36 30 29 
25	6	4		35 34 33 29 
26	6	4		37 34 33 29 
27	6	5		46 40 39 36 34 
28	6	3		51 37 33 
29	6	4		41 40 39 38 
30	6	4		50 41 39 34 
31	6	5		49 46 44 40 38 
32	6	3		46 39 34 
33	6	4		50 46 39 38 
34	6	4		51 49 44 38 
35	6	4		51 50 44 38 
36	6	5		49 48 44 43 42 
37	6	4		50 44 43 42 
38	6	3		45 43 42 
39	6	3		49 44 43 
40	6	3		51 50 42 
41	6	2		49 47 
42	6	1		47 
43	6	1		47 
44	6	1		47 
45	6	1		48 
46	6	1		47 
47	6	1		52 
48	6	1		52 
49	6	1		52 
50	6	1		52 
51	6	1		52 
52	1	0		
************************************************************************
REQUESTS/DURATIONS
jobnr.	mode	dur	R1	R2	N1	N2	
------------------------------------------------------------------------
1	1	0	0	0	0	0	
2	1	3	1	14	1	7	
	2	6	1	12	1	5	
	3	7	1	10	1	5	
	4	10	1	8	1	4	
	5	15	1	4	1	3	
	6	20	1	2	1	3	
3	1	3	10	19	20	13	
	2	7	10	16	16	13	
	3	8	9	12	16	11	
	4	12	9	9	12	10	
	5	15	8	5	12	10	
	6	18	8	1	9	9	
4	1	1	13	18	18	14	
	2	5	12	18	17	12	
	3	6	12	17	16	10	
	4	7	10	17	15	10	
	5	10	9	16	14	6	
	6	12	8	16	14	6	
5	1	2	4	18	14	7	
	2	8	4	15	14	5	
	3	9	4	12	14	4	
	4	10	3	10	14	4	
	5	13	3	8	14	2	
	6	18	2	3	14	1	
6	1	3	8	17	15	5	
	2	6	8	14	11	5	
	3	10	8	12	10	5	
	4	11	8	7	8	5	
	5	12	8	5	6	5	
	6	15	8	4	6	5	
7	1	6	6	18	16	18	
	2	7	6	16	16	17	
	3	8	5	16	15	17	
	4	9	3	14	15	16	
	5	13	2	13	14	14	
	6	20	2	13	14	13	
8	1	4	9	15	10	8	
	2	7	9	14	10	7	
	3	8	9	12	9	7	
	4	9	9	10	9	5	
	5	10	9	6	8	5	
	6	13	9	3	8	4	
9	1	3	16	13	12	2	
	2	13	14	12	9	2	
	3	14	13	11	9	2	
	4	17	9	11	7	2	
	5	19	9	11	6	2	
	6	20	7	10	5	2	
10	1	1	13	12	7	18	
	2	2	10	12	7	14	
	3	3	7	11	7	13	
	4	12	7	9	7	9	
	5	18	4	9	7	9	
	6	19	1	7	7	7	
11	1	2	13	19	8	16	
	2	11	13	17	8	14	
	3	13	12	17	6	11	
	4	14	11	15	5	8	
	5	15	10	14	4	6	
	6	19	10	14	3	2	
12	1	1	19	17	3	16	
	2	8	19	17	2	16	
	3	15	18	16	2	15	
	4	16	17	16	2	13	
	5	17	16	16	2	13	
	6	19	16	15	2	12	
13	1	1	18	18	11	17	
	2	3	18	17	7	16	
	3	4	18	14	7	13	
	4	5	17	10	4	10	
	5	18	17	6	2	7	
	6	19	17	5	2	3	
14	1	2	12	12	9	16	
	2	3	11	11	8	14	
	3	4	9	11	8	12	
	4	5	9	11	7	10	
	5	6	8	10	7	8	
	6	17	5	10	7	6	
15	1	6	6	15	12	19	
	2	12	6	14	11	17	
	3	13	5	14	9	13	
	4	14	5	13	8	10	
	5	15	4	13	5	7	
	6	19	4	13	5	6	
16	1	3	4	7	16	11	
	2	4	4	7	15	10	
	3	5	3	7	11	9	
	4	9	3	7	9	8	
	5	15	2	6	8	6	
	6	16	2	6	6	4	
17	1	7	17	5	17	7	
	2	8	17	4	14	6	
	3	9	16	4	12	6	
	4	10	16	4	10	5	
	5	16	15	3	7	4	
	6	19	14	3	6	4	
18	1	2	12	20	17	15	
	2	6	10	17	14	14	
	3	9	10	16	12	13	
	4	16	6	15	11	12	
	5	17	4	13	7	11	
	6	19	3	12	6	11	
19	1	2	11	10	11	11	
	2	3	7	9	10	9	
	3	13	6	9	10	7	
	4	14	4	8	7	6	
	5	17	2	8	6	5	
	6	20	1	8	5	3	
20	1	1	20	16	3	16	
	2	9	16	14	2	14	
	3	12	13	13	2	14	
	4	15	10	12	2	12	
	5	19	7	9	1	11	
	6	20	1	8	1	9	
21	1	1	15	4	15	18	
	2	2	14	4	13	17	
	3	4	13	4	11	17	
	4	5	11	3	7	17	
	5	8	11	3	7	16	
	6	17	9	3	5	17	
22	1	4	18	15	10	18	
	2	10	15	14	10	18	
	3	11	14	13	10	18	
	4	12	10	12	9	17	
	5	16	10	12	9	16	
	6	17	6	11	9	16	
23	1	1	14	12	12	20	
	2	3	12	12	12	19	
	3	4	12	10	11	18	
	4	5	10	9	11	17	
	5	12	9	8	11	17	
	6	19	8	8	10	16	
24	1	4	18	16	6	16	
	2	5	17	12	6	15	
	3	6	17	10	5	15	
	4	7	15	7	5	15	
	5	8	14	5	4	14	
	6	12	14	4	3	14	
25	1	4	14	8	9	13	
	2	7	14	8	8	13	
	3	11	12	6	8	13	
	4	14	8	6	8	13	
	5	15	7	4	8	13	
	6	20	4	4	8	13	
26	1	1	15	17	16	9	
	2	7	12	16	16	9	
	3	9	12	16	14	7	
	4	10	11	16	13	6	
	5	15	8	14	13	6	
	6	19	8	14	11	4	
27	1	1	11	10	17	14	
	2	4	10	10	17	11	
	3	6	9	10	16	11	
	4	10	8	10	16	9	
	5	11	6	10	16	8	
	6	13	4	10	15	8	
28	1	4	12	13	15	9	
	2	5	10	13	14	9	
	3	6	7	12	13	9	
	4	7	5	12	10	9	
	5	11	5	11	10	9	
	6	19	2	11	7	9	
29	1	9	14	5	11	19	
	2	11	11	5	9	18	
	3	14	11	4	7	17	
	4	15	9	4	5	16	
	5	19	8	3	4	15	
	6	20	7	2	1	15	
30	1	2	17	20	7	19	
	2	8	16	18	6	16	
	3	14	16	16	6	13	
	4	15	16	15	5	11	
	5	17	15	15	4	7	
	6	19	15	13	4	4	
31	1	4	18	14	10	16	
	2	7	14	14	10	14	
	3	14	13	13	7	11	
	4	15	11	12	6	9	
	5	16	8	10	5	7	
	6	17	3	10	2	5	
32	1	1	10	18	14	20	
	2	2	10	16	13	17	
	3	3	8	15	10	16	
	4	4	7	13	7	15	
	5	11	7	12	7	15	
	6	15	5	10	3	13	
33	1	1	11	16	14	17	
	2	4	11	13	11	15	
	3	13	9	10	11	14	
	4	15	7	6	9	14	
	5	16	3	5	5	12	
	6	18	3	3	5	12	
34	1	2	17	19	11	19	
	2	3	16	17	10	19	
	3	11	16	16	10	19	
	4	12	14	15	10	19	
	5	13	14	15	9	18	
	6	15	13	14	9	18	
35	1	3	11	19	10	8	
	2	4	8	15	8	8	
	3	7	6	15	7	5	
	4	8	4	12	7	5	
	5	11	3	11	5	3	
	6	14	1	10	5	1	
36	1	3	19	15	12	12	
	2	4	15	15	10	9	
	3	7	15	15	9	9	
	4	9	13	15	8	6	
	5	11	9	14	6	5	
	6	14	8	14	6	4	
37	1	13	18	5	4	3	
	2	15	18	4	4	2	
	3	16	17	4	4	2	
	4	17	17	4	4	1	
	5	17	16	4	4	2	
	6	19	16	4	4	1	
38	1	11	18	11	7	18	
	2	12	17	10	6	15	
	3	13	12	8	4	12	
	4	14	11	5	3	10	
	5	18	8	4	2	7	
	6	20	5	3	2	4	
39	1	1	14	17	17	18	
	2	5	11	14	14	17	
	3	6	10	9	13	16	
	4	7	9	8	9	15	
	5	10	9	5	8	13	
	6	19	8	1	4	13	
40	1	1	19	5	15	12	
	2	2	17	5	15	12	
	3	3	16	5	15	12	
	4	15	15	5	15	12	
	5	16	15	5	15	11	
	6	18	14	5	15	11	
41	1	4	18	18	18	6	
	2	10	16	17	18	6	
	3	11	15	17	18	5	
	4	13	14	16	18	4	
	5	15	12	15	18	2	
	6	18	12	15	18	1	
42	1	5	19	14	18	16	
	2	6	19	13	16	12	
	3	7	18	12	16	10	
	4	8	17	10	15	8	
	5	9	15	10	13	6	
	6	10	15	9	12	6	
43	1	2	15	9	19	7	
	2	11	14	8	19	7	
	3	16	14	7	19	7	
	4	17	13	6	19	7	
	5	18	11	4	19	7	
	6	19	9	3	19	7	
44	1	3	7	11	12	17	
	2	6	7	9	12	16	
	3	9	5	7	12	14	
	4	10	4	6	12	11	
	5	11	2	3	12	7	
	6	19	1	1	12	6	
45	1	1	15	17	15	19	
	2	2	15	15	11	15	
	3	7	13	15	9	11	
	4	8	9	14	8	9	
	5	9	6	12	7	7	
	6	16	4	11	4	5	
46	1	2	18	7	19	18	
	2	3	18	6	15	16	
	3	12	18	5	14	14	
	4	13	18	4	12	10	
	5	17	18	3	10	7	
	6	19	18	3	8	7	
47	1	3	19	9	16	17	
	2	8	14	8	16	15	
	3	13	14	7	16	14	
	4	14	11	6	16	11	
	5	16	9	4	16	11	
	6	17	6	4	16	10	
48	1	8	17	20	5	16	
	2	10	16	18	5	14	
	3	11	16	18	4	14	
	4	12	16	16	4	12	
	5	17	15	15	2	12	
	6	18	15	15	2	11	
49	1	5	17	16	4	17	
	2	6	17	15	3	16	
	3	10	16	13	2	16	
	4	11	16	10	2	16	
	5	17	16	7	2	15	
	6	18	15	3	1	15	
50	1	3	12	7	6	9	
	2	5	11	7	5	8	
	3	6	11	7	5	7	
	4	16	10	7	5	6	
	5	17	9	7	5	2	
	6	19	8	7	5	1	
51	1	5	6	13	6	15	
	2	9	5	10	6	15	
	3	10	4	7	6	15	
	4	11	4	6	5	15	
	5	13	2	4	5	15	
	6	16	1	2	5	15	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	70	75	530	616

************************************************************************
