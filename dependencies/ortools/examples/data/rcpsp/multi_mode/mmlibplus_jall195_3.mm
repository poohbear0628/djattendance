jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 4 R
- nonrenewable              : 4 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	14		2 3 4 5 6 7 8 9 10 17 18 19 20 22 
2	6	7		47 39 33 25 23 12 11 
3	6	10		49 47 43 42 40 39 27 26 23 11 
4	6	11		50 49 46 44 43 27 26 25 23 21 16 
5	6	11		49 48 46 44 38 31 30 27 25 24 16 
6	6	11		47 44 42 41 40 39 33 28 25 24 14 
7	6	12		51 50 47 44 43 42 41 40 29 26 25 21 
8	6	11		49 46 45 44 42 41 40 39 30 29 21 
9	6	14		50 48 46 45 42 41 40 39 38 37 36 35 31 29 
10	6	5		50 42 37 29 13 
11	6	4		46 45 32 15 
12	6	9		45 42 41 40 36 30 27 26 24 
13	6	8		49 41 40 39 38 34 30 25 
14	6	1		15 
15	6	5		48 35 31 29 21 
16	6	8		47 45 42 41 40 39 36 34 
17	6	8		47 44 43 40 39 37 35 34 
18	6	5		37 36 31 29 24 
19	6	5		42 39 38 37 26 
20	6	6		50 46 43 39 35 34 
21	6	4		38 37 36 34 
22	6	4		44 43 38 34 
23	6	3		41 34 30 
24	6	3		43 35 34 
25	6	2		36 35 
26	6	2		35 34 
27	6	2		37 35 
28	6	2		36 35 
29	6	1		34 
30	6	1		35 
31	6	1		34 
32	6	1		44 
33	6	1		38 
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
jobnr.	mode	dur	R1	R2	R3	R4	N1	N2	N3	N4	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	0	0	
2	1	6	3	4	4	4	9	23	27	20	
	2	9	2	3	3	4	9	23	27	16	
	3	10	2	3	3	3	9	22	24	13	
	4	11	1	3	3	3	9	21	23	8	
	5	24	1	3	3	2	9	21	21	4	
	6	29	1	3	3	1	9	20	19	3	
3	1	4	4	2	3	4	16	7	25	24	
	2	6	4	2	3	4	16	7	21	24	
	3	7	4	2	3	4	14	7	19	23	
	4	10	4	2	3	4	10	6	15	23	
	5	20	3	2	2	4	9	5	15	22	
	6	30	3	2	2	4	4	5	12	22	
4	1	3	5	2	3	5	26	14	19	30	
	2	12	4	1	3	4	26	14	19	29	
	3	13	3	1	3	4	26	13	19	28	
	4	18	3	1	3	3	26	10	19	28	
	5	19	3	1	2	3	26	10	18	27	
	6	20	2	1	2	2	26	8	18	27	
5	1	2	4	4	1	1	24	13	29	28	
	2	9	4	3	1	1	21	12	26	26	
	3	14	3	3	1	1	21	12	24	26	
	4	21	3	3	1	1	17	10	20	25	
	5	26	3	3	1	1	17	10	17	24	
	6	30	2	3	1	1	14	9	15	22	
6	1	5	4	4	4	4	30	28	12	19	
	2	9	4	4	4	4	29	27	10	19	
	3	11	4	4	4	4	27	26	10	17	
	4	12	4	4	4	4	26	25	9	16	
	5	20	4	3	4	4	26	24	6	16	
	6	28	4	3	4	4	25	24	6	15	
7	1	3	3	5	3	3	28	16	28	21	
	2	9	2	4	3	2	28	13	28	20	
	3	15	2	4	3	2	28	11	26	20	
	4	16	2	3	3	2	28	7	23	19	
	5	28	2	2	3	1	28	5	22	19	
	6	30	2	2	3	1	28	2	20	18	
8	1	3	2	4	1	1	10	13	20	24	
	2	5	2	4	1	1	9	13	16	24	
	3	12	2	4	1	1	8	12	15	22	
	4	15	2	4	1	1	8	12	12	21	
	5	17	2	4	1	1	6	10	6	21	
	6	30	2	4	1	1	6	10	5	20	
9	1	6	2	5	2	2	18	14	23	23	
	2	7	2	4	2	2	18	13	21	23	
	3	17	2	4	2	2	18	12	19	23	
	4	21	2	4	2	2	18	9	15	22	
	5	28	2	3	2	2	18	8	11	22	
	6	30	2	3	2	2	18	7	6	22	
10	1	1	2	1	5	2	25	23	28	25	
	2	6	2	1	4	2	25	22	27	23	
	3	14	2	1	4	2	23	22	26	21	
	4	17	2	1	3	2	20	20	26	20	
	5	20	2	1	3	1	19	20	25	20	
	6	23	2	1	3	1	17	18	25	19	
11	1	4	5	3	3	1	24	21	14	25	
	2	7	4	3	3	1	23	17	12	24	
	3	18	4	2	3	1	23	16	8	24	
	4	21	3	2	3	1	23	10	7	24	
	5	22	2	2	3	1	23	7	4	23	
	6	24	2	1	3	1	23	3	3	23	
12	1	6	5	5	4	5	22	27	16	22	
	2	21	3	4	4	4	22	25	16	21	
	3	25	3	4	4	4	18	24	16	20	
	4	26	2	4	3	4	18	19	16	19	
	5	28	1	4	3	4	14	19	16	19	
	6	29	1	4	2	4	13	16	16	18	
13	1	1	1	4	4	2	16	24	6	30	
	2	9	1	3	4	2	16	24	6	22	
	3	15	1	2	4	2	14	24	6	21	
	4	17	1	2	4	1	13	24	5	14	
	5	21	1	2	4	1	13	24	5	10	
	6	26	1	1	4	1	11	24	4	5	
14	1	3	2	3	4	4	23	18	18	27	
	2	7	1	2	4	4	21	18	16	22	
	3	8	1	2	3	4	19	14	15	15	
	4	18	1	2	3	3	15	13	13	11	
	5	28	1	1	2	3	12	10	9	6	
	6	30	1	1	2	2	11	6	9	5	
15	1	2	4	2	5	2	27	12	19	26	
	2	10	3	2	4	1	22	12	16	19	
	3	17	3	2	4	1	18	12	13	13	
	4	20	3	2	4	1	12	12	12	11	
	5	25	3	2	3	1	7	12	10	9	
	6	26	3	2	3	1	5	12	6	2	
16	1	1	2	5	4	5	25	23	22	13	
	2	10	1	4	4	4	21	20	18	10	
	3	13	1	4	4	4	14	20	17	9	
	4	17	1	3	3	3	13	17	16	6	
	5	21	1	3	3	3	10	11	13	4	
	6	30	1	3	3	2	1	11	12	2	
17	1	1	2	4	3	4	27	17	22	25	
	2	10	2	4	3	3	26	15	19	23	
	3	12	2	4	3	3	26	14	17	22	
	4	16	2	3	3	3	23	11	14	20	
	5	23	2	3	2	2	22	10	14	20	
	6	29	2	3	2	2	21	8	11	19	
18	1	3	2	1	3	5	27	5	26	25	
	2	9	2	1	3	5	20	4	25	24	
	3	11	2	1	3	5	18	3	18	24	
	4	18	2	1	3	5	10	3	18	23	
	5	23	2	1	3	5	9	2	11	22	
	6	29	2	1	3	5	2	1	11	20	
19	1	9	2	3	5	2	23	23	12	18	
	2	10	2	2	4	1	23	23	8	15	
	3	11	2	2	4	1	23	21	6	12	
	4	12	2	2	3	1	23	21	5	8	
	5	19	2	2	2	1	23	20	2	8	
	6	22	2	2	2	1	23	19	2	6	
20	1	8	3	5	4	3	27	24	27	12	
	2	9	3	5	4	2	27	22	22	10	
	3	17	3	5	4	2	26	19	20	10	
	4	25	3	5	4	2	26	18	17	8	
	5	26	3	5	4	2	25	17	14	8	
	6	27	3	5	4	2	25	14	14	6	
21	1	1	3	4	2	3	19	17	11	17	
	2	3	3	3	1	3	14	16	10	15	
	3	10	2	3	1	2	13	15	10	13	
	4	11	2	2	1	2	11	14	8	10	
	5	17	2	2	1	2	5	13	8	6	
	6	23	1	2	1	1	2	12	7	3	
22	1	2	4	4	5	2	11	15	17	16	
	2	10	3	4	4	1	8	15	16	14	
	3	14	3	4	4	1	8	15	15	11	
	4	25	3	3	4	1	6	15	14	9	
	5	27	1	2	4	1	6	15	12	7	
	6	29	1	2	4	1	4	15	12	6	
23	1	2	3	3	4	1	27	25	18	20	
	2	3	3	3	4	1	27	22	15	19	
	3	4	2	3	4	1	23	20	13	18	
	4	11	2	3	3	1	23	17	13	17	
	5	16	2	3	3	1	21	17	9	15	
	6	24	1	3	2	1	19	14	9	15	
24	1	10	4	3	3	4	10	22	21	22	
	2	12	4	2	2	3	9	19	19	18	
	3	16	4	2	2	3	7	16	17	13	
	4	17	4	1	2	3	6	16	15	11	
	5	18	4	1	2	2	6	14	15	7	
	6	19	4	1	2	2	5	11	13	3	
25	1	3	1	3	4	4	23	14	8	23	
	2	9	1	3	3	4	16	14	7	22	
	3	10	1	3	3	4	14	11	6	18	
	4	19	1	3	3	4	12	10	3	16	
	5	25	1	3	2	4	10	8	3	10	
	6	30	1	3	2	4	7	5	1	9	
26	1	4	2	3	3	3	10	24	22	8	
	2	9	2	3	2	3	10	22	19	8	
	3	15	2	3	2	3	9	21	19	8	
	4	18	2	2	2	2	9	19	15	8	
	5	28	2	2	2	2	7	15	13	8	
	6	29	2	1	2	1	7	15	8	8	
27	1	1	3	5	2	4	27	4	24	21	
	2	5	3	5	2	3	21	4	21	20	
	3	16	3	5	2	3	20	4	21	18	
	4	19	2	5	1	2	16	4	19	17	
	5	22	2	5	1	2	13	4	15	16	
	6	28	2	5	1	1	9	4	14	14	
28	1	12	4	4	3	1	21	26	29	9	
	2	13	4	4	2	1	19	23	27	9	
	3	14	4	4	2	1	18	18	25	9	
	4	20	3	3	2	1	17	16	22	9	
	5	21	3	2	2	1	15	8	19	9	
	6	26	3	2	2	1	13	7	18	9	
29	1	1	4	3	5	2	14	24	29	8	
	2	11	4	2	4	2	11	22	23	7	
	3	16	3	2	4	2	10	22	19	5	
	4	18	2	2	4	2	7	22	19	4	
	5	24	2	2	4	2	7	20	14	3	
	6	29	1	2	4	2	4	20	9	3	
30	1	8	5	3	4	3	29	12	12	26	
	2	11	4	3	4	2	24	12	10	26	
	3	13	4	3	4	2	19	12	10	24	
	4	17	4	3	3	2	15	11	8	24	
	5	24	4	3	3	1	13	11	6	23	
	6	29	4	3	3	1	9	10	4	22	
31	1	1	2	1	3	3	20	21	19	21	
	2	10	2	1	2	3	19	17	19	18	
	3	17	2	1	2	3	16	14	18	17	
	4	20	2	1	2	3	14	8	18	12	
	5	27	2	1	2	3	13	5	17	10	
	6	28	2	1	2	3	10	1	16	8	
32	1	5	4	3	2	5	25	20	22	28	
	2	11	4	3	2	5	24	18	20	26	
	3	12	4	2	2	5	19	12	18	24	
	4	14	4	2	2	5	12	8	14	20	
	5	16	4	2	2	5	8	5	12	19	
	6	30	4	1	2	5	6	2	11	16	
33	1	3	4	5	5	4	23	27	14	17	
	2	5	3	4	5	4	20	27	13	16	
	3	9	3	4	5	3	18	26	11	11	
	4	11	3	4	5	2	17	25	7	10	
	5	21	2	4	5	2	13	23	6	6	
	6	23	2	4	5	1	11	22	4	4	
34	1	4	4	4	2	1	28	25	22	14	
	2	6	4	4	1	1	28	23	19	14	
	3	9	3	4	1	1	28	17	17	10	
	4	11	2	4	1	1	28	17	16	10	
	5	22	1	4	1	1	28	12	15	6	
	6	23	1	4	1	1	28	5	13	5	
35	1	5	3	3	4	2	12	20	13	23	
	2	6	3	2	4	1	10	19	11	23	
	3	14	3	2	3	1	9	15	10	21	
	4	20	2	1	2	1	7	13	8	21	
	5	24	1	1	1	1	6	12	6	19	
	6	26	1	1	1	1	5	10	4	19	
36	1	8	3	5	4	5	23	21	13	21	
	2	11	3	4	3	5	22	19	12	19	
	3	14	3	4	3	5	21	16	12	17	
	4	15	2	3	3	5	20	14	12	13	
	5	21	2	3	1	5	19	14	12	12	
	6	30	1	3	1	5	18	11	12	10	
37	1	2	3	2	4	1	26	20	20	22	
	2	5	2	2	4	1	25	18	17	21	
	3	8	2	2	4	1	23	17	15	19	
	4	13	2	2	4	1	21	15	13	18	
	5	20	1	2	4	1	17	13	11	17	
	6	26	1	2	4	1	15	12	10	16	
38	1	3	2	1	3	4	10	20	15	9	
	2	5	2	1	2	4	10	19	13	9	
	3	6	2	1	2	4	10	17	13	9	
	4	9	2	1	2	3	10	17	8	9	
	5	18	1	1	2	3	9	16	7	9	
	6	19	1	1	2	3	9	15	5	9	
39	1	3	2	4	4	3	26	28	29	20	
	2	7	2	4	3	3	25	26	28	19	
	3	14	2	3	3	3	25	22	28	18	
	4	16	2	3	2	2	25	21	27	17	
	5	25	1	2	2	2	25	19	27	16	
	6	28	1	2	1	2	25	14	27	16	
40	1	1	2	5	1	5	24	30	26	25	
	2	3	2	5	1	5	22	26	25	25	
	3	10	2	5	1	5	22	21	24	23	
	4	12	2	5	1	5	21	19	20	20	
	5	24	2	5	1	5	19	14	19	18	
	6	30	2	5	1	5	18	13	18	16	
41	1	1	5	3	5	4	26	17	16	13	
	2	10	4	3	5	3	20	14	13	12	
	3	21	3	3	5	3	17	12	13	12	
	4	28	3	3	5	3	11	9	11	10	
	5	29	1	3	5	1	11	7	6	9	
	6	30	1	3	5	1	3	5	6	7	
42	1	5	5	5	4	4	25	17	24	19	
	2	6	5	4	4	3	25	14	22	19	
	3	12	5	4	4	3	24	13	21	14	
	4	19	5	3	3	3	22	12	21	12	
	5	26	5	3	3	3	21	10	19	10	
	6	27	5	2	2	3	20	9	19	5	
43	1	15	4	4	3	4	24	22	28	6	
	2	18	4	3	2	4	22	20	23	6	
	3	24	4	3	2	3	18	19	21	5	
	4	27	4	2	2	3	9	14	19	4	
	5	28	4	2	1	2	6	11	16	3	
	6	29	4	2	1	2	1	10	16	3	
44	1	2	5	4	4	2	23	26	20	25	
	2	9	5	4	4	2	22	24	19	25	
	3	17	5	4	4	2	21	19	19	24	
	4	19	5	3	4	1	20	16	19	24	
	5	20	5	3	4	1	20	15	18	23	
	6	29	5	2	4	1	19	10	17	23	
45	1	4	4	4	4	2	26	27	21	22	
	2	5	4	4	3	2	24	21	20	20	
	3	16	4	3	3	2	21	17	17	20	
	4	17	4	3	2	2	19	11	16	19	
	5	18	4	2	2	1	19	11	15	17	
	6	30	4	2	1	1	17	3	12	15	
46	1	1	5	4	5	4	5	21	13	18	
	2	3	4	3	4	4	4	17	13	17	
	3	6	4	3	3	4	4	12	13	15	
	4	8	4	2	3	3	3	12	13	14	
	5	16	4	2	2	3	3	5	13	14	
	6	21	4	1	2	2	2	4	13	13	
47	1	2	4	5	1	4	9	28	29	6	
	2	3	4	4	1	4	9	24	25	6	
	3	9	4	4	1	4	9	20	22	5	
	4	19	4	4	1	4	8	13	16	5	
	5	25	4	4	1	4	8	7	16	4	
	6	27	4	4	1	4	8	1	12	3	
48	1	15	2	2	5	5	9	23	16	26	
	2	17	2	2	3	3	9	18	15	25	
	3	18	2	2	3	3	9	17	12	24	
	4	19	2	2	3	2	9	13	12	20	
	5	20	1	2	2	2	9	11	8	19	
	6	28	1	2	1	1	9	10	6	17	
49	1	6	5	4	4	1	26	25	28	17	
	2	14	4	3	4	1	23	18	27	16	
	3	18	4	3	4	1	16	17	27	16	
	4	21	3	3	4	1	11	12	26	16	
	5	29	3	2	4	1	11	11	25	16	
	6	30	3	2	4	1	7	6	23	16	
50	1	5	5	5	4	3	28	23	19	12	
	2	6	4	4	3	3	28	21	19	12	
	3	12	4	3	2	3	28	17	16	11	
	4	18	3	2	2	3	28	13	10	9	
	5	26	3	1	1	3	28	10	6	7	
	6	28	3	1	1	3	28	6	5	6	
51	1	1	5	4	2	5	12	26	7	16	
	2	12	4	3	2	5	10	24	6	12	
	3	15	4	3	2	5	9	21	4	12	
	4	23	3	3	2	5	8	21	3	10	
	5	25	3	2	2	5	7	17	3	8	
	6	28	2	1	2	5	4	16	1	6	
52	1	0	0	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	R 3	R 4	N 1	N 2	N 3	N 4
	29	29	27	28	942	890	888	890

************************************************************************
