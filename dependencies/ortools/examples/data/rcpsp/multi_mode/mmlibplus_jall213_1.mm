jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 4 R
- nonrenewable              : 4 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	8		2 3 4 5 6 8 13 15 
2	6	4		17 12 9 7 
3	6	4		23 17 12 10 
4	6	6		26 23 17 14 12 11 
5	6	3		23 17 9 
6	6	3		23 17 9 
7	6	5		26 23 22 21 14 
8	6	4		26 22 14 11 
9	6	3		26 16 11 
10	6	3		26 16 11 
11	6	4		24 20 19 18 
12	6	4		24 22 20 18 
13	6	4		24 23 20 18 
14	6	3		24 20 18 
15	6	3		26 23 22 
16	6	3		28 24 22 
17	6	3		28 24 20 
18	6	4		30 29 28 27 
19	6	4		30 29 28 27 
20	6	3		34 30 25 
21	6	3		34 27 24 
22	6	4		37 30 29 27 
23	6	3		30 28 27 
24	6	4		37 35 31 30 
25	6	3		37 31 27 
26	6	4		37 34 32 31 
27	6	4		38 35 33 32 
28	6	3		37 35 31 
29	6	3		35 34 33 
30	6	3		38 36 32 
31	6	1		33 
32	6	4		42 41 40 39 
33	6	3		41 40 36 
34	6	3		42 40 38 
35	6	3		42 41 40 
36	6	5		51 50 49 43 42 
37	6	8		51 50 49 48 47 46 45 44 
38	6	2		48 41 
39	6	4		51 50 49 43 
40	6	6		51 50 48 47 46 44 
41	6	3		49 47 43 
42	6	4		48 47 45 44 
43	6	3		46 45 44 
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
jobnr.	mode	dur	R1	R2	R3	R4	N1	N2	N3	N4	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	0	0	
2	1	2	10	17	28	18	22	15	17	4	
	2	7	8	13	25	13	22	11	14	4	
	3	16	8	11	21	11	21	9	12	4	
	4	18	6	8	20	9	21	8	8	4	
	5	19	6	5	18	8	21	5	6	3	
	6	27	5	2	13	7	20	3	1	3	
3	1	17	7	21	27	3	14	6	26	26	
	2	18	6	20	26	3	13	6	25	23	
	3	24	6	19	26	3	13	6	25	23	
	4	25	5	17	26	2	13	6	24	21	
	5	26	5	15	26	2	12	6	23	20	
	6	30	4	13	26	2	12	6	23	20	
4	1	6	28	17	25	21	17	23	28	28	
	2	7	21	12	22	21	16	23	25	28	
	3	8	18	12	20	21	15	23	24	27	
	4	20	16	7	20	21	13	23	23	27	
	5	25	11	7	18	21	13	23	22	26	
	6	29	7	3	16	21	12	23	21	26	
5	1	6	13	19	22	25	17	29	22	10	
	2	14	10	16	22	25	17	28	17	10	
	3	18	9	15	21	23	14	26	14	9	
	4	20	5	11	21	23	14	24	11	9	
	5	25	5	11	20	22	12	20	7	8	
	6	26	3	8	20	21	11	20	3	7	
6	1	6	27	21	24	26	27	20	25	22	
	2	9	21	20	23	23	26	16	20	21	
	3	17	17	19	23	19	26	16	18	21	
	4	18	12	18	21	18	26	14	14	19	
	5	20	11	17	20	14	25	11	7	19	
	6	24	6	17	20	8	25	9	6	17	
7	1	2	17	24	17	8	11	20	21	15	
	2	22	15	19	16	6	10	19	21	14	
	3	24	12	17	15	6	8	19	17	13	
	4	26	7	13	13	5	8	19	15	13	
	5	29	4	9	10	5	6	19	10	12	
	6	30	3	8	8	4	6	19	8	11	
8	1	4	15	26	24	8	11	10	19	24	
	2	10	14	26	19	8	11	8	17	18	
	3	11	14	22	16	7	11	7	16	18	
	4	12	13	21	13	7	11	6	15	13	
	5	14	11	17	13	6	11	4	14	10	
	6	17	11	17	8	5	11	2	13	8	
9	1	9	24	20	17	27	26	16	27	18	
	2	15	23	18	17	24	23	15	26	16	
	3	16	20	18	15	19	17	14	24	10	
	4	17	19	15	15	17	14	14	22	9	
	5	19	17	13	14	12	11	12	19	5	
	6	29	14	12	12	9	9	12	15	2	
10	1	3	5	25	19	13	15	16	27	17	
	2	4	5	18	18	12	15	15	23	16	
	3	14	5	14	18	11	15	15	21	16	
	4	15	4	11	17	9	15	14	18	14	
	5	16	4	11	17	9	15	14	18	13	
	6	21	4	6	16	8	15	13	15	12	
11	1	8	24	21	29	29	8	22	15	17	
	2	9	23	20	25	29	7	21	11	16	
	3	10	23	20	24	29	7	20	11	16	
	4	14	22	19	21	28	7	19	7	15	
	5	18	21	18	16	28	7	18	6	15	
	6	28	19	18	16	28	7	18	5	15	
12	1	6	22	22	25	27	9	8	10	24	
	2	7	19	21	23	22	8	8	9	23	
	3	8	19	21	19	19	7	8	7	20	
	4	9	14	20	16	15	7	8	5	18	
	5	16	13	20	14	9	7	8	3	14	
	6	20	10	19	12	8	6	8	1	12	
13	1	1	12	21	27	25	3	19	30	19	
	2	18	11	19	26	24	3	15	25	19	
	3	26	8	19	26	24	3	13	21	19	
	4	27	6	18	25	23	2	11	16	19	
	5	28	6	15	24	23	1	7	16	19	
	6	30	3	15	24	23	1	2	12	19	
14	1	6	19	24	26	23	25	9	20	18	
	2	10	18	23	26	22	23	7	20	16	
	3	21	18	20	26	20	22	5	20	13	
	4	23	17	17	26	20	20	4	20	11	
	5	25	17	12	25	18	19	3	20	8	
	6	26	17	10	25	16	17	2	20	6	
15	1	1	18	14	21	22	25	19	25	26	
	2	2	17	13	21	22	25	16	24	25	
	3	10	16	13	19	22	22	16	22	25	
	4	21	16	12	17	22	19	13	18	24	
	5	29	15	10	16	22	17	11	15	23	
	6	30	15	10	14	22	15	10	11	23	
16	1	1	18	29	9	22	17	29	30	9	
	2	3	17	23	9	18	16	29	24	7	
	3	14	17	21	7	18	13	29	20	6	
	4	23	16	19	6	13	11	28	17	5	
	5	26	16	16	5	10	10	27	13	3	
	6	29	16	10	4	8	9	27	6	2	
17	1	7	27	25	24	15	21	18	14	8	
	2	9	22	21	17	15	19	16	12	8	
	3	12	19	18	16	15	19	13	12	6	
	4	13	15	14	11	15	17	12	10	6	
	5	21	10	11	6	14	16	10	6	3	
	6	30	5	9	3	14	15	10	6	3	
18	1	6	22	19	19	25	26	22	14	16	
	2	14	21	18	16	19	26	22	12	14	
	3	15	20	15	14	15	26	19	8	12	
	4	17	19	13	12	12	26	15	8	10	
	5	18	17	11	8	7	26	12	5	7	
	6	26	16	7	8	7	26	10	4	5	
19	1	5	22	26	3	30	27	4	18	25	
	2	6	18	24	2	27	22	4	17	22	
	3	8	17	22	2	23	18	4	17	18	
	4	9	12	21	1	23	15	4	15	15	
	5	11	9	20	1	20	14	4	15	12	
	6	12	6	18	1	17	12	4	14	11	
20	1	12	24	12	3	20	28	27	25	29	
	2	14	22	11	3	20	27	27	23	26	
	3	19	17	11	3	20	24	25	19	22	
	4	22	14	10	2	20	20	25	17	22	
	5	24	11	10	2	20	19	24	10	19	
	6	30	10	9	2	20	16	23	9	18	
21	1	3	24	15	4	8	26	29	20	19	
	2	5	19	12	4	8	26	22	18	17	
	3	6	16	9	4	8	26	19	17	15	
	4	13	12	8	4	7	25	14	16	14	
	5	16	6	4	4	6	25	10	16	11	
	6	28	5	1	4	6	25	8	15	10	
22	1	5	21	17	1	14	28	10	29	29	
	2	13	21	14	1	12	21	8	24	25	
	3	15	20	10	1	12	19	8	24	23	
	4	22	20	6	1	11	13	6	21	20	
	5	26	18	6	1	11	6	4	18	20	
	6	30	18	2	1	10	1	3	15	17	
23	1	4	12	21	11	23	23	30	29	8	
	2	7	11	19	10	18	23	26	26	8	
	3	12	10	17	10	18	20	25	22	7	
	4	14	10	12	10	13	17	24	21	7	
	5	22	9	9	9	6	14	20	18	7	
	6	23	8	6	9	5	13	20	15	6	
24	1	5	14	24	24	23	27	17	24	23	
	2	7	14	21	24	22	27	15	24	19	
	3	9	14	20	24	22	26	13	21	14	
	4	15	14	19	24	22	23	11	18	11	
	5	18	14	15	23	22	22	10	13	9	
	6	28	14	15	23	22	21	8	9	5	
25	1	7	26	17	30	10	8	16	22	21	
	2	8	20	14	29	9	7	14	20	17	
	3	21	17	11	29	9	7	11	15	12	
	4	24	13	8	28	8	6	10	12	12	
	5	25	6	7	28	8	6	6	12	6	
	6	30	5	3	28	8	5	5	9	3	
26	1	7	20	27	24	29	27	11	18	24	
	2	9	20	27	24	28	25	10	17	21	
	3	11	20	22	20	28	22	10	13	19	
	4	12	20	18	18	27	18	10	9	19	
	5	15	19	18	16	25	16	10	8	16	
	6	16	19	15	13	25	12	10	4	14	
27	1	6	18	27	21	18	28	27	20	7	
	2	16	17	24	17	17	22	25	20	7	
	3	20	12	21	15	16	15	24	20	7	
	4	21	7	19	10	16	14	23	20	6	
	5	22	7	17	5	15	10	23	19	6	
	6	23	4	16	5	14	6	22	19	6	
28	1	10	16	26	23	16	16	15	23	9	
	2	11	13	26	23	15	15	15	23	9	
	3	17	11	26	19	14	12	13	22	9	
	4	22	9	26	18	13	9	13	22	9	
	5	25	5	26	17	11	6	12	21	9	
	6	30	3	26	13	10	5	11	20	9	
29	1	5	19	22	19	28	18	18	16	17	
	2	6	19	22	16	27	17	18	12	17	
	3	10	17	22	12	25	16	18	12	16	
	4	15	15	22	8	24	14	18	10	16	
	5	19	12	22	5	22	11	17	7	16	
	6	24	11	22	5	20	10	17	6	15	
30	1	11	16	24	25	19	14	23	28	26	
	2	18	15	20	23	18	12	19	28	24	
	3	20	15	18	23	18	8	13	26	22	
	4	23	14	16	22	18	8	11	25	22	
	5	24	12	15	21	16	5	9	24	18	
	6	29	12	11	21	16	4	2	24	17	
31	1	4	24	9	24	3	15	21	19	6	
	2	7	19	9	20	3	15	19	17	5	
	3	12	16	9	18	3	14	19	17	4	
	4	13	13	9	15	3	13	16	14	4	
	5	17	11	9	12	2	13	16	14	2	
	6	18	7	9	11	2	12	15	12	2	
32	1	2	14	18	22	23	22	28	13	19	
	2	3	10	16	21	22	21	25	13	16	
	3	4	9	16	20	20	20	20	13	11	
	4	19	9	15	20	19	17	15	13	10	
	5	26	6	15	19	18	16	12	12	4	
	6	29	4	14	19	18	13	7	12	3	
33	1	7	15	11	28	24	30	25	20	26	
	2	12	13	11	22	21	27	22	20	26	
	3	16	9	11	20	18	25	19	20	19	
	4	17	9	10	18	16	25	17	20	15	
	5	18	6	10	15	13	22	12	19	15	
	6	27	3	9	11	9	21	10	19	8	
34	1	1	8	10	21	23	21	23	21	23	
	2	2	8	7	19	21	20	22	20	22	
	3	9	8	7	18	17	17	17	14	15	
	4	15	7	5	17	16	16	16	14	14	
	5	16	7	3	16	13	16	13	10	7	
	6	26	6	1	16	9	13	8	7	4	
35	1	1	27	9	24	16	16	4	17	12	
	2	4	27	8	20	13	16	4	15	11	
	3	7	27	8	18	12	16	4	14	9	
	4	8	27	6	14	9	16	4	14	9	
	5	24	27	5	14	7	16	4	11	8	
	6	27	27	5	9	6	16	4	11	6	
36	1	2	27	13	27	24	9	17	11	29	
	2	5	25	11	24	22	8	13	11	23	
	3	6	25	10	22	19	8	13	11	19	
	4	13	24	7	20	18	7	10	11	15	
	5	16	23	7	19	15	7	5	11	7	
	6	25	21	5	18	14	7	5	11	3	
37	1	5	3	22	10	12	17	24	25	14	
	2	6	3	19	8	11	16	24	20	12	
	3	14	3	16	8	11	12	24	17	12	
	4	17	2	13	8	10	12	24	14	9	
	5	20	1	7	6	7	8	24	10	7	
	6	21	1	7	6	7	7	24	7	5	
38	1	3	28	24	18	25	27	16	21	9	
	2	9	25	21	18	24	22	13	21	8	
	3	10	25	17	16	24	19	13	21	8	
	4	13	21	15	15	23	13	11	21	7	
	5	16	21	15	15	23	8	8	21	6	
	6	18	18	12	14	22	6	5	21	6	
39	1	6	20	30	3	22	7	17	22	11	
	2	7	18	26	2	21	7	17	18	10	
	3	12	18	24	2	18	6	16	16	10	
	4	18	17	18	1	14	6	14	15	9	
	5	20	15	18	1	12	4	13	11	9	
	6	22	13	15	1	11	4	13	9	9	
40	1	20	25	8	21	29	25	22	27	23	
	2	22	23	8	20	28	23	20	25	23	
	3	25	22	8	19	28	22	19	24	18	
	4	26	20	7	18	27	21	18	24	17	
	5	27	18	7	18	26	21	17	22	13	
	6	29	17	7	17	26	19	15	21	11	
41	1	2	11	12	25	26	12	25	26	26	
	2	5	9	10	24	20	8	25	23	24	
	3	16	8	8	24	19	8	20	20	21	
	4	17	6	7	23	14	5	17	19	21	
	5	20	5	6	23	11	3	15	15	17	
	6	25	3	4	23	9	2	12	10	13	
42	1	6	21	25	25	22	10	9	24	9	
	2	7	20	23	23	21	9	9	24	8	
	3	13	18	22	23	20	6	9	23	8	
	4	14	16	19	21	19	5	9	23	7	
	5	24	16	14	21	19	3	9	21	7	
	6	28	15	12	20	18	2	9	21	6	
43	1	3	12	1	25	22	8	15	15	27	
	2	4	9	1	25	22	6	14	12	24	
	3	5	7	1	24	17	5	14	10	23	
	4	7	7	1	22	14	4	13	8	18	
	5	8	4	1	21	10	3	11	6	16	
	6	24	4	1	20	3	3	11	3	14	
44	1	1	28	21	27	15	18	18	14	26	
	2	10	27	15	24	11	15	17	12	25	
	3	12	26	15	23	8	14	13	12	24	
	4	13	26	10	23	6	13	9	10	21	
	5	17	25	8	21	4	10	7	8	20	
	6	28	24	4	20	1	7	3	5	19	
45	1	6	8	24	19	26	14	19	12	23	
	2	8	8	23	15	23	14	17	11	22	
	3	9	8	20	15	18	13	13	11	21	
	4	15	8	19	13	14	13	8	11	21	
	5	28	8	17	12	11	12	8	10	19	
	6	29	8	17	10	5	12	3	10	19	
46	1	11	29	26	18	19	26	28	20	14	
	2	19	28	24	16	19	22	25	16	14	
	3	20	28	22	12	17	16	25	15	11	
	4	21	28	22	11	17	13	21	12	9	
	5	25	28	20	6	15	10	18	6	7	
	6	30	28	18	2	15	4	17	5	7	
47	1	3	7	20	27	24	20	13	24	18	
	2	14	6	16	26	19	17	13	22	17	
	3	15	6	14	23	15	17	12	20	15	
	4	18	5	11	21	13	16	11	19	15	
	5	19	4	7	18	12	14	9	16	14	
	6	22	4	6	14	6	13	9	16	13	
48	1	1	17	3	20	28	22	24	20	24	
	2	5	15	3	18	24	21	21	18	18	
	3	13	13	3	15	20	19	21	15	15	
	4	17	9	2	14	14	18	17	13	11	
	5	25	9	2	11	11	14	11	11	10	
	6	30	5	2	10	8	13	10	11	4	
49	1	5	5	20	23	20	30	6	16	22	
	2	8	5	20	21	20	29	4	16	20	
	3	10	4	20	21	18	29	3	16	17	
	4	20	3	20	19	17	29	2	15	17	
	5	22	2	20	15	17	29	2	15	12	
	6	25	2	20	14	16	29	1	14	12	
50	1	2	19	13	21	18	29	5	24	29	
	2	5	18	11	20	16	29	4	23	24	
	3	7	15	10	17	14	28	4	22	19	
	4	8	12	9	17	11	28	4	18	15	
	5	9	10	8	13	11	27	3	16	7	
	6	22	9	7	10	9	27	3	14	4	
51	1	2	21	16	28	17	20	26	26	11	
	2	7	18	15	26	16	19	26	25	10	
	3	8	14	15	21	13	18	25	25	9	
	4	14	11	14	17	11	15	23	24	8	
	5	24	7	14	14	7	15	21	24	7	
	6	26	4	13	10	4	13	19	24	4	
52	1	0	0	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	R 3	R 4	N 1	N 2	N 3	N 4
	79	93	114	89	869	817	942	827

************************************************************************
