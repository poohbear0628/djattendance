jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 4 R
- nonrenewable              : 4 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	4		2 7 8 9 
2	3	2		5 3 
3	3	3		20 13 4 
4	3	3		19 16 6 
5	3	4		20 14 12 10 
6	3	3		17 11 10 
7	3	3		20 19 10 
8	3	3		19 16 10 
9	3	2		16 12 
10	3	4		22 21 18 15 
11	3	4		22 21 18 15 
12	3	4		22 21 18 15 
13	3	5		24 23 22 21 18 
14	3	3		22 21 15 
15	3	4		28 25 24 23 
16	3	4		26 24 23 22 
17	3	3		24 23 21 
18	3	4		31 29 28 25 
19	3	3		29 27 21 
20	3	5		31 29 28 27 26 
21	3	4		31 30 28 26 
22	3	3		31 28 27 
23	3	6		41 39 36 33 29 27 
24	3	4		39 36 31 27 
25	3	3		33 27 26 
26	3	6		41 39 37 36 34 32 
27	3	3		37 32 30 
28	3	5		42 41 39 37 36 
29	3	4		45 40 37 34 
30	3	3		40 38 34 
31	3	3		41 35 33 
32	3	6		49 47 45 44 42 40 
33	3	5		49 44 43 42 40 
34	3	1		35 
35	3	5		50 49 44 43 42 
36	3	4		49 44 43 40 
37	3	5		50 49 48 46 43 
38	3	5		49 48 47 45 44 
39	3	3		48 45 43 
40	3	3		50 48 46 
41	3	3		48 47 46 
42	3	2		51 46 
43	3	1		47 
44	3	1		46 
45	3	1		46 
46	3	1		52 
47	3	1		52 
48	3	1		52 
49	3	1		52 
50	3	1		52 
51	3	1		52 
52	1	0		
************************************************************************
REQUESTS/DURATIONS
jobnr.	mode	dur	R1	R2	R3	R4	N1	N2	N3	N4	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	0	0	
2	1	2	1	1	2	4	15	3	15	28	
	2	10	1	1	2	4	7	2	14	28	
	3	16	1	1	2	3	3	1	10	26	
3	1	3	4	4	1	3	27	6	28	15	
	2	7	3	3	1	2	18	4	25	12	
	3	13	2	2	1	1	11	4	24	10	
4	1	11	5	4	3	4	16	21	21	21	
	2	21	3	4	2	4	15	18	19	21	
	3	22	3	4	1	4	14	11	18	20	
5	1	8	4	1	5	4	11	13	28	22	
	2	12	4	1	5	4	9	9	27	13	
	3	28	4	1	5	3	9	6	24	10	
6	1	19	3	3	3	4	19	5	13	25	
	2	25	3	3	2	3	19	4	8	21	
	3	30	2	3	2	2	19	4	7	9	
7	1	17	4	4	2	4	24	24	3	15	
	2	22	4	3	1	3	22	14	2	12	
	3	25	4	3	1	3	21	13	2	9	
8	1	4	3	5	5	1	25	27	28	4	
	2	9	3	5	3	1	19	27	18	3	
	3	26	3	5	3	1	11	25	13	1	
9	1	12	1	5	4	2	11	11	18	16	
	2	16	1	4	4	1	6	11	18	14	
	3	24	1	4	4	1	5	5	16	11	
10	1	1	5	3	5	2	20	25	20	12	
	2	4	3	2	3	2	17	19	14	9	
	3	13	3	2	2	1	11	16	11	9	
11	1	2	3	1	4	3	19	28	9	26	
	2	7	3	1	4	2	12	26	5	23	
	3	14	3	1	4	2	4	26	1	15	
12	1	6	4	3	3	2	20	17	7	22	
	2	11	3	2	1	2	16	17	4	21	
	3	13	2	2	1	1	2	15	2	17	
13	1	22	2	4	2	2	23	18	20	25	
	2	23	2	2	2	2	23	17	16	25	
	3	29	2	1	1	2	23	12	12	25	
14	1	21	5	3	3	4	26	27	13	14	
	2	23	5	3	2	4	22	12	13	9	
	3	25	5	3	1	4	21	7	13	2	
15	1	4	3	4	2	5	7	24	12	23	
	2	5	2	3	1	4	5	19	6	21	
	3	9	1	2	1	4	5	13	3	15	
16	1	1	4	4	2	3	22	26	16	19	
	2	2	4	2	1	3	14	25	12	13	
	3	30	4	1	1	3	13	22	7	12	
17	1	12	4	3	1	5	26	26	25	27	
	2	17	3	3	1	3	24	24	19	21	
	3	20	2	3	1	3	21	22	14	11	
18	1	11	4	4	2	4	13	21	7	17	
	2	17	4	4	2	3	9	14	7	14	
	3	18	4	4	2	3	6	11	5	8	
19	1	15	1	3	5	4	24	17	12	30	
	2	16	1	2	4	2	16	12	8	29	
	3	30	1	1	3	1	9	8	4	28	
20	1	17	4	4	4	2	21	25	17	10	
	2	21	2	4	3	1	20	19	15	8	
	3	25	2	2	2	1	16	14	6	8	
21	1	17	4	4	4	3	15	21	12	16	
	2	18	3	4	2	2	10	12	11	15	
	3	28	2	4	1	2	7	9	10	5	
22	1	4	5	4	4	2	22	14	9	9	
	2	24	4	2	3	1	18	11	7	8	
	3	25	2	2	1	1	16	10	6	7	
23	1	3	4	2	3	4	14	16	19	27	
	2	12	3	2	2	4	11	15	17	22	
	3	18	1	2	1	4	4	11	14	22	
24	1	8	5	2	3	3	18	1	12	13	
	2	25	5	2	1	3	16	1	8	13	
	3	26	5	1	1	2	15	1	6	11	
25	1	3	4	4	2	5	29	19	21	14	
	2	13	4	4	1	3	27	12	12	14	
	3	20	4	4	1	1	23	10	4	13	
26	1	6	2	5	3	4	9	28	24	22	
	2	7	2	4	1	3	7	28	20	17	
	3	23	1	4	1	2	3	27	13	14	
27	1	3	5	5	3	2	18	18	2	24	
	2	11	5	4	3	2	17	14	1	17	
	3	29	5	3	3	2	14	14	1	8	
28	1	6	3	5	3	1	7	28	9	17	
	2	11	3	4	2	1	3	27	5	14	
	3	20	3	3	2	1	3	26	4	14	
29	1	7	4	4	4	4	15	28	18	22	
	2	15	3	4	4	4	15	21	14	18	
	3	17	2	3	3	4	13	18	11	12	
30	1	8	5	5	4	3	16	20	14	7	
	2	10	2	4	3	2	16	9	13	5	
	3	17	1	4	3	2	16	4	7	3	
31	1	3	3	5	3	3	25	25	12	26	
	2	7	3	5	3	2	21	21	10	24	
	3	8	2	5	3	1	16	19	10	20	
32	1	5	2	3	2	1	20	4	18	21	
	2	7	1	3	1	1	11	3	12	18	
	3	9	1	2	1	1	7	1	7	13	
33	1	3	2	4	1	4	26	20	17	19	
	2	26	2	3	1	3	18	19	14	14	
	3	29	1	3	1	3	13	17	11	12	
34	1	9	3	1	5	2	20	17	19	14	
	2	16	3	1	3	2	12	14	14	11	
	3	24	2	1	1	2	8	10	9	5	
35	1	19	4	4	5	5	23	14	15	19	
	2	20	2	3	4	4	17	5	7	13	
	3	24	1	2	4	4	6	2	1	9	
36	1	11	5	2	2	5	22	7	18	29	
	2	12	4	2	2	5	18	6	12	24	
	3	28	3	2	1	5	9	5	9	17	
37	1	11	4	4	3	5	27	25	19	26	
	2	16	2	4	2	4	27	17	17	22	
	3	18	1	4	2	3	27	6	14	17	
38	1	8	3	3	3	3	22	7	12	5	
	2	19	3	3	3	2	17	7	12	4	
	3	28	2	2	3	2	8	7	12	3	
39	1	20	4	3	4	4	19	17	18	15	
	2	26	3	3	4	2	15	17	17	12	
	3	27	2	1	4	1	14	17	16	9	
40	1	8	4	5	4	2	20	9	17	18	
	2	13	3	4	2	1	17	7	14	17	
	3	27	3	4	1	1	15	7	14	15	
41	1	2	2	4	2	5	11	24	24	20	
	2	9	2	3	1	2	11	20	19	19	
	3	16	2	2	1	1	11	19	11	17	
42	1	15	3	4	3	3	28	26	22	11	
	2	20	1	4	3	2	28	15	19	10	
	3	27	1	3	3	2	28	11	13	10	
43	1	6	2	4	3	3	24	19	28	19	
	2	7	2	3	2	3	21	15	23	12	
	3	28	2	2	1	3	16	13	15	8	
44	1	8	3	3	2	5	18	24	15	7	
	2	19	3	2	2	4	16	18	11	6	
	3	22	2	1	2	2	5	15	7	6	
45	1	8	5	5	2	3	23	11	18	10	
	2	9	3	2	2	3	22	8	18	8	
	3	15	1	1	2	2	20	2	18	8	
46	1	20	4	3	5	4	19	30	30	15	
	2	23	4	2	3	3	12	27	25	10	
	3	24	4	2	3	3	12	26	24	8	
47	1	19	3	4	3	4	16	10	18	16	
	2	23	3	3	2	2	11	10	10	14	
	3	30	3	3	2	1	5	7	6	9	
48	1	25	2	2	4	5	28	10	26	14	
	2	27	2	1	4	4	19	7	25	13	
	3	29	2	1	3	2	12	5	22	9	
49	1	5	4	4	4	2	10	20	13	24	
	2	20	3	3	4	2	6	19	8	10	
	3	30	2	3	4	2	3	9	5	6	
50	1	5	5	4	4	3	8	23	18	18	
	2	9	4	3	3	3	7	17	11	18	
	3	15	2	2	2	1	5	9	7	14	
51	1	5	5	5	3	2	24	26	15	15	
	2	13	4	4	3	2	23	19	14	14	
	3	28	2	4	2	1	22	15	13	14	
52	1	0	0	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	R 3	R 4	N 1	N 2	N 3	N 4
	17	17	16	18	873	840	761	823

************************************************************************
