jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 4 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	18		2 3 4 5 6 7 8 9 10 11 12 13 14 17 18 19 22 29 
2	6	14		49 48 47 46 45 44 43 42 40 38 31 27 23 21 
3	6	8		50 47 45 41 31 23 16 15 
4	6	10		51 50 48 43 41 31 30 28 23 15 
5	6	14		51 50 48 47 45 44 42 40 39 34 32 30 28 23 
6	6	10		44 43 40 32 31 30 27 25 24 23 
7	6	9		49 44 41 39 31 26 24 23 20 
8	6	13		51 46 45 42 41 40 39 36 35 33 32 31 30 
9	6	13		51 50 47 46 43 42 40 39 38 35 34 33 26 
10	6	8		47 43 40 39 38 31 23 21 
11	6	10		48 46 43 42 40 39 38 37 31 23 
12	6	9		46 42 41 40 35 34 33 32 26 
13	6	6		49 45 35 30 27 25 
14	6	10		49 47 44 41 39 38 37 35 33 31 
15	6	10		49 44 42 40 39 38 36 35 34 33 
16	6	6		48 40 35 33 32 26 
17	6	5		48 41 33 31 26 
18	6	6		47 44 43 40 31 30 
19	6	7		44 43 42 39 35 34 33 
20	6	5		43 42 38 35 30 
21	6	3		41 35 26 
22	6	5		41 40 36 34 33 
23	6	3		36 35 33 
24	6	3		45 35 34 
25	6	3		41 36 34 
26	6	2		36 30 
27	6	2		39 33 
28	6	2		46 33 
29	6	2		45 33 
30	6	1		37 
31	6	1		34 
32	6	1		38 
33	6	1		52 
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
jobnr.	mode	dur	R1	R2	R3	R4	N1	N2	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	
2	1	2	2	5	2	3	14	20	
	2	9	2	5	2	3	14	19	
	3	10	2	5	2	3	14	17	
	4	14	2	5	2	3	13	16	
	5	26	1	5	2	3	12	14	
	6	30	1	5	2	3	12	13	
3	1	8	4	3	4	5	16	24	
	2	12	3	2	4	4	14	20	
	3	13	3	2	4	4	12	19	
	4	19	3	2	4	4	10	14	
	5	20	3	1	3	4	10	13	
	6	26	3	1	3	4	9	11	
4	1	4	4	4	5	5	19	12	
	2	5	4	3	4	4	18	10	
	3	9	4	3	3	4	16	8	
	4	15	3	3	2	4	16	7	
	5	20	3	3	2	4	13	7	
	6	23	2	3	1	4	13	5	
5	1	12	4	1	2	3	15	14	
	2	13	4	1	2	2	13	14	
	3	14	4	1	2	2	13	11	
	4	16	3	1	2	1	11	10	
	5	17	3	1	2	1	9	9	
	6	28	2	1	2	1	6	7	
6	1	4	5	5	4	4	10	27	
	2	14	4	4	3	4	10	22	
	3	15	4	3	2	4	8	21	
	4	20	4	2	2	4	8	16	
	5	22	4	2	1	3	6	12	
	6	27	4	1	1	3	6	9	
7	1	5	5	3	3	1	16	12	
	2	10	4	3	2	1	14	12	
	3	18	3	3	2	1	11	8	
	4	20	3	3	2	1	10	7	
	5	21	3	3	1	1	9	4	
	6	25	2	3	1	1	5	2	
8	1	1	5	4	4	1	12	21	
	2	6	5	4	3	1	11	18	
	3	11	5	4	3	1	11	13	
	4	12	5	4	3	1	10	8	
	5	21	5	4	2	1	10	6	
	6	22	5	4	2	1	9	3	
9	1	8	5	4	2	3	27	28	
	2	11	4	4	1	2	26	23	
	3	16	3	4	1	2	23	16	
	4	17	3	4	1	2	23	13	
	5	20	2	4	1	2	21	9	
	6	26	2	4	1	2	18	7	
10	1	1	5	4	2	5	19	30	
	2	2	5	3	1	4	18	29	
	3	8	5	3	1	3	15	27	
	4	17	5	3	1	2	13	27	
	5	20	5	3	1	1	13	25	
	6	22	5	3	1	1	11	25	
11	1	3	4	5	2	4	16	12	
	2	13	3	5	1	4	14	12	
	3	14	3	5	1	4	13	12	
	4	17	3	5	1	4	8	12	
	5	24	2	5	1	4	7	12	
	6	26	2	5	1	4	5	12	
12	1	10	3	3	3	3	6	22	
	2	22	3	3	2	3	5	22	
	3	23	3	2	2	3	5	22	
	4	24	3	2	1	3	4	22	
	5	26	3	2	1	2	4	22	
	6	28	3	1	1	2	3	22	
13	1	5	1	5	3	4	21	18	
	2	14	1	4	2	4	18	17	
	3	15	1	3	2	4	17	17	
	4	28	1	3	2	3	12	17	
	5	29	1	2	2	3	12	16	
	6	30	1	1	2	3	9	16	
14	1	10	2	3	3	3	20	17	
	2	14	1	3	2	2	15	16	
	3	15	1	3	2	2	13	13	
	4	21	1	3	2	2	9	9	
	5	27	1	3	2	1	6	4	
	6	28	1	3	2	1	3	3	
15	1	2	5	5	4	3	28	14	
	2	3	4	5	3	2	27	14	
	3	4	3	5	3	2	27	14	
	4	25	2	5	2	1	27	14	
	5	27	1	5	1	1	27	14	
	6	29	1	5	1	1	27	13	
16	1	8	3	4	1	3	8	13	
	2	14	3	4	1	3	8	12	
	3	15	3	4	1	3	8	11	
	4	17	3	4	1	2	8	12	
	5	23	3	4	1	2	8	11	
	6	29	3	4	1	1	8	12	
17	1	12	4	5	4	5	26	9	
	2	16	3	4	3	3	22	7	
	3	18	3	3	3	3	20	5	
	4	19	3	2	2	3	18	5	
	5	20	3	1	2	2	17	3	
	6	23	3	1	1	1	14	1	
18	1	7	4	2	3	3	27	9	
	2	9	3	2	3	3	26	8	
	3	13	3	2	3	3	24	8	
	4	14	3	2	2	3	24	8	
	5	21	3	2	2	3	23	8	
	6	27	3	2	1	3	22	8	
19	1	2	3	5	3	4	23	22	
	2	3	3	4	3	3	19	17	
	3	9	3	4	3	3	19	16	
	4	14	2	4	3	3	15	13	
	5	26	2	4	2	3	15	10	
	6	27	2	4	2	3	12	7	
20	1	2	2	5	2	2	24	11	
	2	4	2	4	1	1	22	10	
	3	7	2	4	1	1	22	9	
	4	12	2	4	1	1	18	8	
	5	26	2	3	1	1	17	7	
	6	28	2	3	1	1	16	5	
21	1	9	4	4	1	3	24	20	
	2	15	3	3	1	3	18	20	
	3	17	3	2	1	3	15	15	
	4	19	2	2	1	3	12	14	
	5	20	1	2	1	3	9	10	
	6	22	1	1	1	3	3	8	
22	1	2	2	3	5	4	14	14	
	2	5	1	2	4	4	14	14	
	3	11	1	2	4	3	14	14	
	4	17	1	2	4	2	14	14	
	5	20	1	1	3	1	14	14	
	6	23	1	1	3	1	14	13	
23	1	2	5	3	4	2	22	17	
	2	4	4	3	4	2	16	16	
	3	10	4	3	4	2	12	16	
	4	11	4	2	4	2	12	16	
	5	21	4	1	3	2	7	15	
	6	23	4	1	3	2	4	15	
24	1	3	2	5	3	5	11	26	
	2	4	1	4	3	4	11	26	
	3	22	1	4	2	4	8	26	
	4	24	1	4	2	3	7	26	
	5	25	1	4	2	3	7	25	
	6	30	1	4	1	2	5	25	
25	1	15	4	4	2	4	21	25	
	2	16	4	4	2	4	17	20	
	3	17	4	4	2	4	16	18	
	4	19	4	4	2	3	11	17	
	5	24	3	4	1	2	11	9	
	6	25	3	4	1	2	6	7	
26	1	7	5	1	5	2	14	15	
	2	8	5	1	3	1	12	12	
	3	12	5	1	3	1	11	12	
	4	21	5	1	3	1	8	7	
	5	26	5	1	1	1	7	7	
	6	30	5	1	1	1	5	4	
27	1	2	2	1	2	5	8	18	
	2	13	2	1	1	4	7	16	
	3	18	2	1	1	4	6	14	
	4	22	2	1	1	4	5	12	
	5	26	2	1	1	4	3	11	
	6	29	2	1	1	4	3	6	
28	1	8	1	2	4	3	21	20	
	2	9	1	2	4	2	17	18	
	3	14	1	2	4	2	15	15	
	4	15	1	2	4	2	15	12	
	5	18	1	2	4	1	12	10	
	6	19	1	2	4	1	11	9	
29	1	2	3	4	4	3	19	2	
	2	2	3	4	4	3	16	3	
	3	3	3	4	4	3	16	2	
	4	5	2	4	4	3	14	1	
	5	14	1	4	4	3	13	1	
	6	17	1	4	4	3	12	1	
30	1	1	3	2	1	2	11	6	
	2	3	2	2	1	2	10	5	
	3	11	2	2	1	2	10	4	
	4	13	2	1	1	2	10	5	
	5	15	2	1	1	2	10	4	
	6	20	2	1	1	2	10	3	
31	1	3	4	4	2	4	20	28	
	2	4	4	3	2	4	18	26	
	3	15	3	3	2	4	17	25	
	4	20	2	2	1	4	15	22	
	5	22	2	2	1	4	12	20	
	6	28	1	2	1	4	11	16	
32	1	4	3	4	4	5	8	25	
	2	10	2	4	3	4	6	23	
	3	24	2	4	3	3	5	21	
	4	25	2	4	3	3	5	19	
	5	27	2	4	3	1	3	15	
	6	29	2	4	3	1	3	14	
33	1	2	2	2	5	1	8	19	
	2	4	2	2	5	1	7	16	
	3	5	2	2	5	1	6	16	
	4	6	2	2	5	1	6	14	
	5	14	2	2	5	1	5	9	
	6	19	2	2	5	1	5	7	
34	1	4	4	3	2	4	23	12	
	2	5	4	2	2	4	19	12	
	3	9	4	2	2	4	16	12	
	4	12	4	1	1	4	15	12	
	5	18	4	1	1	4	9	12	
	6	22	4	1	1	4	8	12	
35	1	12	4	4	4	5	5	12	
	2	18	3	4	3	5	5	10	
	3	21	3	4	2	5	5	7	
	4	24	3	4	2	5	5	6	
	5	26	2	4	2	5	4	4	
	6	30	2	4	1	5	4	3	
36	1	1	4	2	5	3	29	24	
	2	4	4	2	4	2	26	19	
	3	8	4	2	4	2	25	16	
	4	9	4	2	3	1	23	15	
	5	11	4	2	2	1	20	12	
	6	19	4	2	2	1	20	10	
37	1	1	4	5	4	2	23	25	
	2	2	3	4	4	2	21	22	
	3	10	3	3	4	2	20	18	
	4	16	3	3	3	2	20	16	
	5	24	3	2	2	1	16	11	
	6	26	3	2	2	1	15	11	
38	1	6	3	5	5	1	9	4	
	2	10	2	4	4	1	8	3	
	3	14	2	4	4	1	7	3	
	4	18	2	4	4	1	6	3	
	5	21	2	4	4	1	6	1	
	6	22	2	4	4	1	5	1	
39	1	2	1	5	3	4	18	14	
	2	5	1	4	2	3	18	13	
	3	8	1	4	2	3	16	9	
	4	18	1	4	1	3	14	9	
	5	24	1	4	1	3	10	6	
	6	25	1	4	1	3	9	3	
40	1	5	2	3	2	1	15	28	
	2	11	2	3	2	1	14	27	
	3	18	2	3	2	1	12	25	
	4	21	2	2	2	1	10	25	
	5	22	2	1	2	1	8	23	
	6	30	2	1	2	1	8	22	
41	1	3	4	3	4	5	14	19	
	2	4	4	3	3	4	13	19	
	3	10	4	3	3	3	12	18	
	4	15	3	2	3	3	12	15	
	5	17	3	1	2	3	11	14	
	6	27	3	1	2	2	11	12	
42	1	6	3	1	3	1	24	24	
	2	12	2	1	3	1	24	17	
	3	15	2	1	3	1	24	14	
	4	19	2	1	3	1	23	9	
	5	29	2	1	3	1	23	4	
	6	30	2	1	3	1	23	3	
43	1	11	4	5	4	5	17	26	
	2	12	3	4	4	4	17	23	
	3	13	3	4	4	4	17	20	
	4	14	2	4	4	4	17	19	
	5	16	2	3	4	4	16	17	
	6	27	2	3	4	4	16	14	
44	1	13	4	4	2	5	25	24	
	2	19	4	3	2	4	24	23	
	3	20	4	3	2	4	22	19	
	4	21	4	3	1	3	22	17	
	5	22	4	2	1	3	20	14	
	6	28	4	1	1	2	19	10	
45	1	6	4	5	4	5	28	24	
	2	8	4	4	4	4	25	16	
	3	14	4	3	4	4	19	15	
	4	16	4	3	4	3	14	9	
	5	18	4	2	4	3	10	7	
	6	30	4	2	4	3	8	3	
46	1	1	3	5	2	4	29	23	
	2	8	3	3	2	4	29	23	
	3	9	3	3	2	4	28	22	
	4	12	3	2	2	4	26	20	
	5	20	3	1	2	4	25	20	
	6	22	3	1	2	4	25	19	
47	1	1	4	3	4	3	14	28	
	2	2	3	3	4	3	13	26	
	3	8	3	3	4	3	13	23	
	4	21	3	2	3	3	13	20	
	5	26	3	2	3	2	13	20	
	6	28	3	2	3	2	13	16	
48	1	9	3	4	2	3	29	3	
	2	11	2	4	2	3	22	3	
	3	17	2	3	2	3	20	3	
	4	22	1	2	2	3	15	2	
	5	26	1	1	2	3	13	2	
	6	28	1	1	2	3	9	2	
49	1	7	5	1	5	4	15	25	
	2	9	4	1	4	4	13	22	
	3	14	4	1	3	4	10	21	
	4	16	3	1	3	3	8	19	
	5	19	3	1	3	3	7	18	
	6	21	2	1	2	3	6	16	
50	1	9	4	2	2	2	22	12	
	2	12	4	2	2	2	22	10	
	3	13	4	2	2	2	20	8	
	4	14	4	2	2	2	19	6	
	5	18	4	2	2	1	18	6	
	6	19	4	2	2	1	18	4	
51	1	2	5	3	4	4	13	11	
	2	5	4	3	4	4	10	10	
	3	15	3	3	3	3	9	8	
	4	19	2	3	3	3	7	7	
	5	22	2	2	3	2	5	3	
	6	24	1	2	2	2	2	3	
52	1	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	R 3	R 4	N 1	N 2
	35	36	31	34	614	586

************************************************************************
