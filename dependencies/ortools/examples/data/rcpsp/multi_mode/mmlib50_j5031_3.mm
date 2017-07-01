jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	18		2 3 4 5 6 7 8 9 10 11 13 14 15 17 18 20 25 30 
2	3	12		51 49 48 47 46 43 39 31 28 23 22 16 
3	3	11		51 48 46 45 43 31 27 26 23 22 12 
4	3	8		49 39 31 29 23 22 19 16 
5	3	7		43 37 29 24 21 19 16 
6	3	9		49 48 47 45 42 39 37 31 16 
7	3	5		45 31 26 24 12 
8	3	14		47 46 45 44 43 41 40 39 38 37 34 31 27 26 
9	3	11		50 47 44 43 41 40 39 38 36 28 23 
10	3	9		43 40 38 37 36 33 31 22 19 
11	3	7		46 43 41 31 23 22 19 
12	3	10		42 41 40 38 37 36 35 34 28 21 
13	3	10		50 49 46 43 42 41 37 35 34 21 
14	3	8		46 43 37 35 34 28 26 21 
15	3	9		45 44 41 40 39 38 35 34 27 
16	3	8		44 41 40 38 35 34 27 26 
17	3	7		49 42 38 36 34 33 32 
18	3	6		47 44 40 36 35 31 
19	3	4		48 45 42 34 
20	3	4		44 37 33 32 
21	3	3		39 33 32 
22	3	3		42 35 34 
23	3	3		37 34 33 
24	3	3		47 38 32 
25	3	3		43 35 33 
26	3	2		36 33 
27	3	2		33 32 
28	3	2		33 32 
29	3	2		46 35 
30	3	2		36 32 
31	3	1		32 
32	3	1		52 
33	3	1		52 
34	3	1		52 
35	3	1		52 
36	3	1		52 
37	3	1		52 
38	3	1		52 
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
2	1	3	9	4	0	7	
	2	4	4	3	0	6	
	3	8	1	1	0	5	
3	1	1	4	5	0	6	
	2	2	4	5	0	5	
	3	9	2	3	0	6	
4	1	4	5	10	0	8	
	2	9	4	10	7	0	
	3	10	4	10	0	3	
5	1	1	7	6	10	0	
	2	8	4	5	0	2	
	3	9	4	5	0	1	
6	1	4	1	6	7	0	
	2	5	1	4	0	7	
	3	6	1	4	0	4	
7	1	3	5	8	9	0	
	2	4	4	6	5	0	
	3	8	4	4	0	7	
8	1	1	9	1	0	10	
	2	2	5	1	4	0	
	3	8	4	1	0	9	
9	1	4	7	6	0	9	
	2	8	5	5	3	0	
	3	9	4	4	3	0	
10	1	1	9	3	10	0	
	2	3	9	2	7	0	
	3	10	9	2	6	0	
11	1	6	6	5	8	0	
	2	7	3	3	6	0	
	3	8	2	2	0	3	
12	1	1	8	5	10	0	
	2	7	7	4	0	3	
	3	8	4	2	0	3	
13	1	1	4	6	0	7	
	2	2	3	5	2	0	
	3	7	3	5	1	0	
14	1	5	3	9	10	0	
	2	5	2	5	0	2	
	3	10	2	4	10	0	
15	1	2	4	9	5	0	
	2	6	3	8	0	5	
	3	9	2	6	0	4	
16	1	1	5	10	0	2	
	2	2	5	5	0	2	
	3	4	5	4	3	0	
17	1	2	5	8	10	0	
	2	3	5	7	5	0	
	3	4	5	7	3	0	
18	1	2	10	8	10	0	
	2	3	6	7	8	0	
	3	9	4	6	0	2	
19	1	1	6	7	8	0	
	2	1	6	7	0	6	
	3	10	6	7	0	2	
20	1	2	9	10	0	7	
	2	5	9	8	0	6	
	3	6	8	6	3	0	
21	1	2	6	7	0	7	
	2	3	4	5	2	0	
	3	4	2	4	0	5	
22	1	3	6	10	6	0	
	2	5	4	9	5	0	
	3	8	3	8	4	0	
23	1	3	3	1	9	0	
	2	6	2	1	7	0	
	3	8	1	1	0	2	
24	1	3	7	6	6	0	
	2	5	5	5	0	3	
	3	8	2	1	2	0	
25	1	1	8	7	10	0	
	2	8	7	4	7	0	
	3	8	5	3	0	2	
26	1	1	5	7	7	0	
	2	3	5	6	5	0	
	3	9	3	6	5	0	
27	1	1	6	9	0	5	
	2	3	5	4	0	4	
	3	4	4	4	2	0	
28	1	7	10	2	7	0	
	2	8	9	1	6	0	
	3	9	9	1	3	0	
29	1	8	4	6	0	9	
	2	9	3	6	7	0	
	3	10	2	6	0	3	
30	1	1	8	4	9	0	
	2	4	8	4	6	0	
	3	5	8	4	4	0	
31	1	1	8	4	6	0	
	2	5	5	4	5	0	
	3	10	2	3	0	7	
32	1	1	7	9	2	0	
	2	5	3	5	0	5	
	3	10	3	4	2	0	
33	1	3	6	8	6	0	
	2	7	5	7	0	3	
	3	8	5	5	0	2	
34	1	4	3	4	0	8	
	2	5	3	4	7	0	
	3	7	3	4	0	3	
35	1	3	10	4	0	10	
	2	6	10	4	0	8	
	3	10	10	4	2	0	
36	1	1	8	6	7	0	
	2	7	6	2	0	7	
	3	9	6	2	2	0	
37	1	5	9	9	0	8	
	2	9	7	8	2	0	
	3	10	5	8	2	0	
38	1	2	4	2	6	0	
	2	3	3	2	5	0	
	3	4	3	1	0	3	
39	1	2	5	9	4	0	
	2	9	5	8	0	9	
	3	10	5	7	1	0	
40	1	2	10	7	0	7	
	2	3	9	7	0	7	
	3	8	8	7	0	6	
41	1	1	3	5	6	0	
	2	6	2	4	4	0	
	3	8	2	3	0	3	
42	1	4	6	2	0	7	
	2	5	6	1	0	6	
	3	9	6	1	0	4	
43	1	2	2	6	7	0	
	2	8	1	5	7	0	
	3	9	1	4	3	0	
44	1	3	1	7	7	0	
	2	3	1	4	0	5	
	3	8	1	4	4	0	
45	1	5	9	10	8	0	
	2	6	5	6	0	6	
	3	7	2	6	3	0	
46	1	1	3	8	0	8	
	2	4	3	5	3	0	
	3	5	2	2	0	4	
47	1	2	5	7	0	10	
	2	5	3	5	0	9	
	3	7	3	4	0	8	
48	1	1	10	6	0	4	
	2	3	9	5	2	0	
	3	5	8	2	0	2	
49	1	4	10	6	10	0	
	2	9	8	4	10	0	
	3	10	7	4	0	2	
50	1	6	10	6	6	0	
	2	9	8	6	0	4	
	3	10	6	6	0	3	
51	1	4	4	10	1	0	
	2	5	3	9	0	4	
	3	7	2	8	1	0	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	87	88	89	81

************************************************************************
