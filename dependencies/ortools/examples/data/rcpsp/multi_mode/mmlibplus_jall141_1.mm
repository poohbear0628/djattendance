jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 4 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	16		2 3 4 5 6 7 8 9 10 11 12 13 14 15 21 26 
2	6	11		50 47 43 31 29 28 24 20 19 18 16 
3	6	13		51 50 49 47 45 44 41 33 31 30 29 22 17 
4	6	12		50 49 47 45 44 43 32 31 29 25 23 20 
5	6	9		50 47 44 41 32 31 22 20 17 
6	6	10		47 45 44 41 36 31 30 29 23 17 
7	6	13		50 49 48 46 45 44 43 40 38 36 34 29 23 
8	6	11		47 44 43 41 39 38 36 30 29 28 27 
9	6	6		44 42 36 30 29 17 
10	6	8		45 44 41 39 35 29 27 22 
11	6	5		48 41 32 29 17 
12	6	10		47 46 44 43 42 41 38 35 29 27 
13	6	8		47 41 39 38 30 29 28 27 
14	6	8		43 39 38 36 35 30 29 27 
15	6	10		49 47 46 45 42 40 38 36 35 34 
16	6	9		51 49 46 40 37 36 35 34 33 
17	6	6		43 39 38 37 28 27 
18	6	6		45 42 41 36 35 34 
19	6	6		45 44 41 39 36 34 
20	6	5		40 38 37 35 27 
21	6	5		48 46 34 31 28 
22	6	5		46 42 38 37 36 
23	6	4		42 39 37 28 
24	6	4		48 45 36 34 
25	6	2		41 36 
26	6	2		40 34 
27	6	1		34 
28	6	1		35 
29	6	1		37 
30	6	1		40 
31	6	1		35 
32	6	1		36 
33	6	1		48 
34	6	1		52 
35	6	1		52 
36	6	1		52 
37	6	1		52 
38	6	1		52 
39	6	1		52 
40	6	1		52 
41	6	1		52 
42	6	1		52 
43	6	1		52 
44	6	1		52 
45	6	1		52 
46	6	1		52 
47	6	1		52 
48	6	1		52 
49	6	1		52 
50	6	1		52 
51	6	1		52 
52	1	0		
************************************************************************
REQUESTS/DURATIONS
jobnr.	mode	dur	R1	R2	N1	N2	N3	N4	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	
2	1	7	4	3	15	14	11	9	
	2	10	3	3	13	13	10	8	
	3	13	3	3	11	13	10	8	
	4	17	2	2	10	12	8	8	
	5	18	2	2	7	11	8	8	
	6	19	2	2	6	10	6	8	
3	1	1	5	4	16	13	12	14	
	2	2	4	3	15	12	9	13	
	3	4	3	3	11	12	9	12	
	4	7	3	2	8	12	7	11	
	5	11	1	1	5	11	3	10	
	6	13	1	1	2	10	3	9	
4	1	7	4	3	20	13	9	11	
	2	10	3	2	16	11	7	11	
	3	12	2	2	16	9	7	10	
	4	14	2	1	13	9	5	10	
	5	16	2	1	10	7	4	10	
	6	17	1	1	9	5	4	9	
5	1	3	2	2	17	16	18	13	
	2	4	2	1	14	13	17	12	
	3	8	2	1	11	10	16	11	
	4	9	2	1	9	7	16	11	
	5	15	1	1	4	4	15	9	
	6	20	1	1	4	4	15	8	
6	1	3	2	3	19	13	17	7	
	2	5	1	3	15	12	13	6	
	3	9	1	3	12	11	13	5	
	4	16	1	2	8	9	11	5	
	5	17	1	1	6	6	7	3	
	6	18	1	1	5	5	3	2	
7	1	1	3	5	9	15	18	8	
	2	5	2	4	8	15	16	8	
	3	7	2	4	8	11	14	8	
	4	11	2	4	8	8	9	8	
	5	16	2	3	8	7	8	7	
	6	17	2	3	8	2	5	7	
8	1	3	3	1	14	10	13	3	
	2	9	2	1	14	9	13	3	
	3	12	2	1	14	8	12	3	
	4	13	2	1	13	7	11	2	
	5	17	1	1	13	5	9	1	
	6	18	1	1	12	5	7	1	
9	1	3	3	4	14	2	16	9	
	2	4	2	3	13	2	13	9	
	3	8	2	3	13	2	12	9	
	4	10	2	2	12	1	10	9	
	5	12	1	2	12	1	8	8	
	6	14	1	2	12	1	6	8	
10	1	1	5	5	16	2	6	6	
	2	5	4	4	15	1	6	6	
	3	6	4	4	15	1	6	4	
	4	7	4	3	15	1	6	4	
	5	8	4	3	15	1	6	3	
	6	12	4	2	15	1	6	2	
11	1	6	1	3	19	13	13	9	
	2	9	1	2	16	13	9	8	
	3	11	1	2	11	13	9	8	
	4	16	1	2	9	12	5	8	
	5	18	1	2	7	11	5	7	
	6	20	1	2	5	11	1	7	
12	1	2	1	3	17	13	10	19	
	2	4	1	3	17	11	9	16	
	3	5	1	2	15	11	8	15	
	4	11	1	2	15	11	6	15	
	5	14	1	1	13	10	5	14	
	6	15	1	1	13	9	5	12	
13	1	10	4	4	18	16	13	15	
	2	11	3	3	15	14	11	14	
	3	12	3	3	14	14	10	14	
	4	13	3	2	13	11	8	14	
	5	14	3	2	9	10	4	14	
	6	19	3	2	8	9	3	14	
14	1	1	2	2	12	15	13	14	
	2	3	2	2	11	12	13	14	
	3	4	2	2	10	11	13	13	
	4	11	1	2	10	10	12	11	
	5	16	1	2	9	8	12	10	
	6	17	1	2	9	6	12	10	
15	1	5	4	4	8	9	15	2	
	2	6	4	4	7	8	15	2	
	3	9	4	4	5	7	15	2	
	4	10	4	3	5	6	15	2	
	5	16	3	3	4	5	14	2	
	6	18	3	3	2	5	14	2	
16	1	12	3	1	6	5	15	14	
	2	13	3	1	5	4	13	14	
	3	14	2	1	4	4	13	13	
	4	15	2	1	3	3	10	13	
	5	18	1	1	2	2	9	12	
	6	19	1	1	2	1	8	11	
17	1	10	3	1	14	6	16	19	
	2	11	3	1	11	5	16	18	
	3	16	3	1	10	4	16	17	
	4	17	2	1	8	4	16	18	
	5	18	2	1	8	4	16	17	
	6	20	2	1	7	3	16	16	
18	1	8	5	3	16	11	12	12	
	2	11	4	2	16	10	12	11	
	3	12	4	2	16	9	11	9	
	4	13	3	2	16	8	9	8	
	5	14	3	2	16	4	8	6	
	6	15	3	2	16	4	7	5	
19	1	1	4	4	18	10	13	14	
	2	5	4	4	18	9	13	13	
	3	14	4	4	17	7	9	12	
	4	15	4	3	16	6	7	10	
	5	18	4	3	14	5	6	9	
	6	20	4	3	14	5	4	8	
20	1	4	4	4	11	14	19	8	
	2	5	3	3	10	14	14	8	
	3	6	3	3	10	14	12	8	
	4	13	3	2	8	13	10	8	
	5	18	3	2	7	12	9	8	
	6	20	3	2	7	12	5	8	
21	1	4	2	1	10	16	6	10	
	2	9	2	1	10	16	5	9	
	3	12	2	1	10	14	3	9	
	4	13	2	1	10	10	2	7	
	5	17	1	1	10	9	1	6	
	6	20	1	1	10	7	1	4	
22	1	3	4	5	14	14	8	7	
	2	9	4	4	12	14	8	6	
	3	16	4	4	10	14	8	6	
	4	17	3	4	7	14	8	6	
	5	18	3	4	5	14	7	6	
	6	19	3	4	3	14	7	6	
23	1	4	1	3	19	17	16	16	
	2	6	1	3	16	15	13	14	
	3	8	1	3	15	14	12	10	
	4	15	1	2	12	14	10	9	
	5	18	1	2	10	11	9	4	
	6	20	1	1	10	10	6	2	
24	1	6	4	4	17	8	12	5	
	2	8	3	4	15	7	10	5	
	3	10	3	3	12	6	9	5	
	4	12	3	3	8	4	5	5	
	5	16	3	1	5	2	3	5	
	6	19	3	1	4	2	1	5	
25	1	4	4	4	15	13	14	16	
	2	6	4	4	14	10	14	11	
	3	7	3	3	12	8	10	10	
	4	12	3	3	12	6	8	7	
	5	13	2	2	11	5	4	4	
	6	20	2	2	9	2	2	4	
26	1	4	3	3	16	13	20	4	
	2	10	3	3	14	10	18	3	
	3	15	3	3	11	9	16	3	
	4	17	3	3	9	5	14	2	
	5	18	2	3	5	5	13	1	
	6	19	2	3	2	2	13	1	
27	1	1	2	5	15	16	3	4	
	2	2	2	4	15	16	3	3	
	3	7	2	4	15	16	3	2	
	4	15	2	4	15	16	3	1	
	5	18	2	4	15	15	2	4	
	6	19	2	4	15	15	2	3	
28	1	4	4	3	8	16	12	14	
	2	5	4	2	8	15	11	10	
	3	7	4	2	7	14	11	10	
	4	10	4	2	7	13	11	9	
	5	11	4	2	6	11	11	5	
	6	14	4	2	6	11	11	4	
29	1	3	2	3	17	5	16	14	
	2	6	2	3	15	5	15	12	
	3	10	2	3	13	5	15	9	
	4	14	2	2	13	5	15	5	
	5	18	2	2	12	5	15	5	
	6	19	2	2	11	5	15	1	
30	1	2	3	4	11	19	19	9	
	2	3	3	4	8	17	19	8	
	3	5	3	4	6	17	19	8	
	4	7	2	4	4	15	19	7	
	5	17	2	4	3	15	18	6	
	6	20	2	4	2	14	18	6	
31	1	2	3	3	4	12	19	15	
	2	8	3	3	3	12	15	13	
	3	11	3	3	3	12	13	12	
	4	13	3	3	2	12	12	10	
	5	16	2	3	2	11	9	8	
	6	17	2	3	2	11	9	6	
32	1	1	3	5	14	11	12	12	
	2	8	3	4	13	10	12	11	
	3	13	3	3	13	7	12	11	
	4	14	3	3	12	5	11	10	
	5	18	3	2	12	2	11	9	
	6	19	3	2	12	1	10	9	
33	1	5	3	3	18	15	4	12	
	2	15	2	3	17	15	3	10	
	3	16	2	3	16	15	3	9	
	4	17	2	2	15	15	2	8	
	5	18	1	2	14	15	1	8	
	6	19	1	1	13	15	1	7	
34	1	3	5	5	17	8	19	6	
	2	5	4	4	16	7	19	5	
	3	10	4	4	15	7	19	5	
	4	11	4	3	15	6	18	4	
	5	19	4	3	14	5	18	4	
	6	20	4	3	13	5	18	3	
35	1	8	5	4	11	17	19	18	
	2	14	4	4	10	13	17	17	
	3	16	4	4	9	12	14	17	
	4	17	4	4	9	10	12	17	
	5	19	4	4	7	7	7	16	
	6	20	4	4	6	3	6	15	
36	1	1	2	4	15	7	18	16	
	2	7	2	4	11	6	16	11	
	3	13	2	3	11	6	13	11	
	4	14	2	3	9	5	12	8	
	5	16	2	2	6	5	8	6	
	6	17	2	2	1	4	7	4	
37	1	1	2	2	15	15	17	15	
	2	13	2	1	15	12	15	14	
	3	14	2	1	13	9	13	14	
	4	15	1	1	12	8	11	14	
	5	17	1	1	11	4	8	13	
	6	18	1	1	11	4	7	13	
38	1	2	3	4	6	12	12	8	
	2	4	3	3	6	11	12	7	
	3	6	3	3	5	8	12	6	
	4	11	3	3	3	7	12	5	
	5	17	3	2	2	4	12	3	
	6	20	3	2	1	3	12	2	
39	1	3	5	5	15	16	13	11	
	2	9	4	4	13	15	10	9	
	3	10	4	4	10	12	10	7	
	4	14	4	4	9	10	8	5	
	5	16	3	4	7	8	5	4	
	6	19	3	4	5	4	5	3	
40	1	3	3	5	18	13	7	8	
	2	4	3	4	18	12	5	7	
	3	6	3	4	16	10	4	7	
	4	11	2	3	15	9	3	7	
	5	13	2	2	15	8	3	7	
	6	17	2	2	14	8	2	7	
41	1	3	3	2	10	17	2	9	
	2	4	3	2	9	15	2	9	
	3	12	3	2	9	14	2	7	
	4	13	2	1	8	14	2	7	
	5	17	2	1	7	12	2	5	
	6	19	1	1	6	11	2	4	
42	1	1	5	4	18	4	10	5	
	2	4	4	3	18	4	9	4	
	3	9	4	3	15	3	8	4	
	4	10	3	3	12	3	6	3	
	5	11	3	3	11	2	5	3	
	6	20	2	3	10	2	5	3	
43	1	10	5	1	9	12	19	18	
	2	11	4	1	8	12	16	18	
	3	13	4	1	8	12	14	17	
	4	14	3	1	6	12	12	16	
	5	15	3	1	5	12	10	16	
	6	19	3	1	4	12	7	15	
44	1	10	2	2	20	17	16	19	
	2	11	1	2	19	15	15	17	
	3	12	1	2	19	13	13	15	
	4	14	1	2	19	12	12	15	
	5	19	1	1	19	11	11	13	
	6	20	1	1	19	9	11	12	
45	1	1	4	3	16	19	9	19	
	2	2	4	3	16	16	8	15	
	3	3	4	3	13	13	8	13	
	4	10	4	3	11	11	6	11	
	5	14	3	3	8	10	5	7	
	6	17	3	3	7	8	4	7	
46	1	2	2	5	12	11	15	3	
	2	4	2	4	8	9	15	3	
	3	11	2	3	8	7	14	3	
	4	12	2	3	6	5	12	3	
	5	16	2	1	4	4	12	3	
	6	17	2	1	3	1	10	3	
47	1	11	5	2	13	8	13	12	
	2	13	4	2	11	8	12	10	
	3	15	4	2	10	6	11	6	
	4	16	4	1	8	5	10	6	
	5	18	4	1	7	4	10	2	
	6	20	4	1	6	4	9	2	
48	1	3	4	4	19	20	18	3	
	2	11	4	4	17	18	15	3	
	3	15	4	4	15	15	13	2	
	4	17	3	3	12	15	10	2	
	5	19	3	2	9	13	7	1	
	6	20	3	2	9	10	3	1	
49	1	6	4	1	17	16	13	17	
	2	8	3	1	16	13	11	15	
	3	10	3	1	13	11	10	15	
	4	11	2	1	11	9	10	14	
	5	12	2	1	5	7	9	13	
	6	16	2	1	5	2	8	12	
50	1	8	3	2	19	18	5	17	
	2	10	3	2	18	17	4	14	
	3	11	3	2	18	16	4	13	
	4	15	3	2	18	13	3	13	
	5	18	3	2	18	12	2	11	
	6	19	3	2	18	11	1	11	
51	1	2	4	2	16	16	13	14	
	2	6	4	2	15	12	12	14	
	3	11	4	2	15	10	12	13	
	4	14	4	2	14	7	12	11	
	5	15	4	2	13	6	12	10	
	6	16	4	2	13	3	12	7	
52	1	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2	N 3	N 4
	26	27	643	553	582	504

************************************************************************
