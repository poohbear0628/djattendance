jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 4 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	9		2 3 4 5 6 7 8 9 11 
2	9	5		18 16 13 12 10 
3	9	6		34 31 18 16 14 12 
4	9	11		37 35 30 26 23 22 21 20 19 17 16 
5	9	8		36 35 34 23 22 17 16 14 
6	9	7		35 34 31 24 22 16 14 
7	9	5		37 31 27 15 13 
8	9	7		36 35 25 23 22 16 14 
9	9	7		35 34 32 30 25 23 18 
10	9	6		37 35 34 29 24 17 
11	9	8		37 36 35 30 29 27 25 23 
12	9	5		35 30 26 23 17 
13	9	5		35 30 28 22 21 
14	9	6		37 32 30 29 28 27 
15	9	5		35 32 30 29 25 
16	9	6		41 40 32 29 28 27 
17	9	5		51 40 32 27 25 
18	9	5		43 37 36 33 22 
19	9	9		51 50 43 42 41 39 38 36 34 
20	9	5		43 41 39 29 27 
21	9	6		51 50 43 39 33 32 
22	9	4		48 41 40 29 
23	9	3		40 38 28 
24	9	7		51 50 48 43 42 40 38 
25	9	3		47 41 28 
26	9	5		50 49 46 42 33 
27	9	4		49 46 42 33 
28	9	5		50 49 45 43 39 
29	9	6		51 50 47 46 45 42 
30	9	4		50 46 40 38 
31	9	4		49 47 42 36 
32	9	5		49 47 46 45 42 
33	9	3		48 44 38 
34	9	2		47 40 
35	9	3		51 49 48 
36	9	3		46 45 44 
37	9	1		39 
38	9	2		47 45 
39	9	2		48 44 
40	9	2		45 44 
41	9	2		49 46 
42	9	1		44 
43	9	1		46 
44	9	1		52 
45	9	1		52 
46	9	1		52 
47	9	1		52 
48	9	1		52 
49	9	1		52 
50	9	1		52 
51	9	1		52 
52	1	0		
************************************************************************
REQUESTS/DURATIONS
jobnr.	mode	dur	R1	R2	R3	R4	N1	N2	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	
2	1	4	1	5	4	5	16	17	
	2	10	1	4	4	4	16	16	
	3	11	1	4	4	4	15	16	
	4	12	1	4	4	3	14	16	
	5	13	1	4	4	3	13	15	
	6	16	1	4	3	2	12	15	
	7	19	1	4	3	1	10	14	
	8	20	1	4	3	1	9	14	
	9	25	1	4	3	1	9	13	
3	1	4	5	3	4	3	12	19	
	2	6	4	3	4	3	12	19	
	3	7	4	3	4	3	11	18	
	4	12	3	3	3	3	9	17	
	5	13	2	2	3	2	9	16	
	6	14	2	2	3	2	8	16	
	7	15	1	2	2	1	6	15	
	8	25	1	2	2	1	5	15	
	9	26	1	2	2	1	5	14	
4	1	2	3	5	3	5	14	17	
	2	3	2	4	3	4	13	15	
	3	4	2	4	3	4	11	13	
	4	6	2	3	3	4	10	13	
	5	10	1	2	3	4	9	10	
	6	14	1	2	3	3	9	9	
	7	20	1	1	3	3	8	7	
	8	22	1	1	3	3	6	4	
	9	27	1	1	3	3	5	2	
5	1	1	4	5	2	5	5	21	
	2	4	4	4	2	5	5	21	
	3	6	4	4	2	5	5	19	
	4	11	4	3	2	5	5	19	
	5	14	4	2	2	5	5	18	
	6	15	3	2	2	5	5	16	
	7	16	3	2	2	5	5	15	
	8	23	3	1	2	5	5	15	
	9	25	3	1	2	5	5	14	
6	1	1	1	2	5	5	25	28	
	2	3	1	1	4	4	25	26	
	3	9	1	1	4	4	24	26	
	4	10	1	1	4	3	22	24	
	5	14	1	1	3	3	21	24	
	6	18	1	1	3	2	19	23	
	7	23	1	1	3	2	19	22	
	8	28	1	1	2	1	18	22	
	9	30	1	1	2	1	17	21	
7	1	7	4	2	2	4	9	10	
	2	11	3	2	2	4	8	10	
	3	14	3	2	2	4	8	9	
	4	15	3	2	2	4	7	10	
	5	16	3	2	2	3	6	10	
	6	17	2	2	2	3	6	9	
	7	20	2	2	2	3	5	9	
	8	23	2	2	2	3	4	9	
	9	28	2	2	2	3	4	8	
8	1	3	3	5	5	4	13	26	
	2	10	3	4	4	4	13	22	
	3	12	3	4	4	4	13	21	
	4	13	3	4	4	3	13	19	
	5	14	3	4	4	3	13	17	
	6	15	3	4	4	3	13	12	
	7	17	3	4	4	3	13	10	
	8	21	3	4	4	2	13	7	
	9	30	3	4	4	2	13	4	
9	1	6	4	4	5	4	24	25	
	2	7	4	4	4	4	23	24	
	3	12	4	4	3	4	23	24	
	4	13	4	3	3	3	23	24	
	5	15	4	3	2	3	23	24	
	6	18	4	2	2	2	22	24	
	7	22	4	1	1	2	22	24	
	8	27	4	1	1	1	22	24	
	9	28	4	1	1	1	22	23	
10	1	3	4	3	1	3	30	14	
	2	4	4	3	1	3	26	13	
	3	9	4	3	1	3	22	13	
	4	16	4	3	1	3	19	13	
	5	17	3	2	1	3	19	12	
	6	18	3	2	1	3	14	12	
	7	19	3	2	1	3	12	11	
	8	26	3	2	1	3	9	11	
	9	27	3	2	1	3	7	11	
11	1	6	4	2	3	3	18	17	
	2	7	3	2	3	2	14	17	
	3	8	3	2	3	2	13	17	
	4	17	3	2	3	2	11	16	
	5	18	2	2	2	2	10	16	
	6	19	2	2	2	2	10	15	
	7	20	1	2	2	2	7	15	
	8	21	1	2	1	2	5	14	
	9	24	1	2	1	2	4	14	
12	1	3	4	4	1	3	26	2	
	2	5	4	4	1	3	22	2	
	3	8	4	4	1	3	21	2	
	4	12	4	4	1	3	17	2	
	5	13	4	4	1	3	15	2	
	6	14	4	4	1	3	12	1	
	7	16	4	4	1	3	9	1	
	8	23	4	4	1	3	5	1	
	9	25	4	4	1	3	1	1	
13	1	5	4	1	5	5	28	21	
	2	6	3	1	4	4	25	21	
	3	10	3	1	4	4	25	20	
	4	11	3	1	4	4	22	19	
	5	12	3	1	3	4	22	19	
	6	14	3	1	3	3	21	18	
	7	17	3	1	2	3	20	18	
	8	20	3	1	2	3	18	18	
	9	28	3	1	2	3	16	17	
14	1	10	3	4	2	5	8	18	
	2	11	3	4	2	4	7	16	
	3	12	3	4	2	3	6	16	
	4	13	3	4	2	3	6	15	
	5	14	3	4	1	2	5	14	
	6	16	3	4	1	2	5	12	
	7	17	3	4	1	1	4	12	
	8	21	3	4	1	1	4	10	
	9	26	3	4	1	1	3	10	
15	1	2	4	3	3	2	3	6	
	2	3	3	3	2	2	2	6	
	3	8	3	3	2	2	2	5	
	4	9	3	2	2	2	2	5	
	5	17	3	2	2	2	2	3	
	6	19	3	2	1	2	1	3	
	7	20	3	1	1	2	1	3	
	8	22	3	1	1	2	1	2	
	9	28	3	1	1	2	1	1	
16	1	9	3	4	2	3	29	22	
	2	12	3	4	2	2	29	22	
	3	13	3	4	2	2	29	21	
	4	17	3	4	2	2	29	20	
	5	19	3	4	2	2	29	19	
	6	20	2	4	2	1	29	22	
	7	21	2	4	2	1	29	21	
	8	22	2	4	2	1	29	20	
	9	28	2	4	2	1	29	19	
17	1	7	4	5	4	4	24	24	
	2	9	3	4	3	4	23	20	
	3	10	3	4	3	4	20	17	
	4	11	3	4	3	3	18	17	
	5	12	2	3	2	3	14	14	
	6	14	2	3	2	3	10	12	
	7	19	2	3	2	3	9	10	
	8	29	2	3	2	2	7	7	
	9	30	2	3	2	2	5	4	
18	1	3	4	1	4	3	17	29	
	2	4	4	1	4	2	17	28	
	3	11	4	1	4	2	16	28	
	4	14	4	1	3	2	15	29	
	5	15	4	1	3	2	15	28	
	6	18	4	1	2	2	15	27	
	7	23	4	1	2	2	14	27	
	8	25	4	1	1	2	14	27	
	9	30	4	1	1	2	13	27	
19	1	1	4	2	5	3	27	5	
	2	4	4	2	4	3	27	5	
	3	5	4	2	4	3	26	5	
	4	6	4	2	4	3	26	4	
	5	7	4	2	3	3	25	5	
	6	8	3	1	3	3	25	4	
	7	18	3	1	2	3	24	4	
	8	19	3	1	2	3	24	3	
	9	29	3	1	2	3	23	4	
20	1	2	4	5	5	2	24	17	
	2	4	3	5	5	2	21	17	
	3	5	3	5	5	2	19	17	
	4	6	3	5	5	2	15	17	
	5	7	3	5	5	2	13	16	
	6	9	3	5	5	2	12	16	
	7	17	3	5	5	2	9	16	
	8	29	3	5	5	2	8	16	
	9	30	3	5	5	2	7	16	
21	1	3	2	3	5	3	29	8	
	2	4	2	3	4	3	26	7	
	3	7	2	3	3	3	21	7	
	4	12	2	3	3	3	17	7	
	5	23	2	3	2	3	14	6	
	6	26	2	2	2	3	13	6	
	7	27	2	2	2	3	11	5	
	8	29	2	2	1	3	7	5	
	9	30	2	2	1	3	2	4	
22	1	6	3	4	4	5	20	27	
	2	8	3	3	3	4	19	26	
	3	12	3	3	3	3	18	25	
	4	14	3	3	3	3	18	24	
	5	15	2	3	3	2	17	24	
	6	17	2	2	3	2	16	24	
	7	24	2	2	3	2	16	23	
	8	29	2	2	3	1	15	22	
	9	30	2	2	3	1	15	21	
23	1	8	4	3	4	2	20	23	
	2	11	4	2	3	2	19	23	
	3	12	4	2	3	2	16	23	
	4	15	4	2	3	2	15	22	
	5	19	3	2	2	2	13	22	
	6	20	3	1	2	2	11	22	
	7	23	3	1	2	2	10	21	
	8	28	3	1	1	2	7	21	
	9	30	3	1	1	2	7	20	
24	1	1	5	3	5	5	15	21	
	2	2	5	3	4	4	15	21	
	3	3	5	3	4	4	15	20	
	4	8	5	3	4	4	15	19	
	5	21	5	3	4	4	14	21	
	6	23	5	3	4	4	14	20	
	7	24	5	3	4	4	13	21	
	8	25	5	3	4	4	13	20	
	9	28	5	3	4	4	13	19	
25	1	1	4	4	2	4	27	28	
	2	3	4	3	2	3	23	26	
	3	4	4	3	2	3	23	25	
	4	9	4	3	2	3	22	25	
	5	10	3	3	2	3	19	23	
	6	13	3	3	2	3	18	21	
	7	18	3	3	2	3	15	19	
	8	26	3	3	2	3	15	18	
	9	30	3	3	2	3	13	16	
26	1	6	5	2	3	2	29	21	
	2	9	4	2	3	1	29	19	
	3	10	3	2	3	1	27	15	
	4	11	3	2	3	1	26	14	
	5	12	2	2	3	1	25	13	
	6	13	2	1	3	1	25	10	
	7	19	1	1	3	1	23	9	
	8	24	1	1	3	1	22	7	
	9	28	1	1	3	1	21	3	
27	1	1	5	4	4	5	25	7	
	2	8	4	4	3	4	24	6	
	3	12	4	4	3	4	23	6	
	4	13	4	4	3	4	21	5	
	5	16	3	4	2	4	19	5	
	6	19	3	3	2	3	18	4	
	7	20	3	3	2	3	17	4	
	8	21	3	3	2	3	16	3	
	9	27	3	3	2	3	13	3	
28	1	3	2	3	1	1	12	30	
	2	4	2	3	1	1	11	28	
	3	6	2	3	1	1	11	26	
	4	12	2	3	1	1	10	26	
	5	17	1	3	1	1	10	24	
	6	18	1	3	1	1	10	23	
	7	19	1	3	1	1	10	22	
	8	23	1	3	1	1	9	22	
	9	28	1	3	1	1	9	20	
29	1	1	3	2	4	1	11	30	
	2	7	3	2	4	1	11	29	
	3	8	3	2	4	1	10	27	
	4	9	3	2	4	1	9	27	
	5	11	3	2	3	1	9	25	
	6	25	3	1	3	1	8	24	
	7	26	3	1	3	1	8	23	
	8	28	3	1	3	1	6	23	
	9	29	3	1	3	1	6	22	
30	1	5	5	3	4	2	14	24	
	2	6	4	3	3	2	14	23	
	3	9	3	3	3	2	13	22	
	4	13	3	3	2	2	12	22	
	5	21	2	3	2	1	11	21	
	6	22	2	3	2	1	11	20	
	7	26	2	3	2	1	10	19	
	8	27	1	3	1	1	9	19	
	9	28	1	3	1	1	9	18	
31	1	4	5	5	4	4	25	26	
	2	6	4	4	3	4	23	26	
	3	14	4	4	3	4	21	26	
	4	20	3	4	3	3	20	26	
	5	21	3	3	3	3	17	25	
	6	22	2	3	3	3	16	25	
	7	24	1	3	3	2	14	26	
	8	25	1	3	3	2	14	25	
	9	26	1	3	3	2	12	25	
32	1	2	2	5	4	2	25	6	
	2	5	2	5	4	1	23	4	
	3	10	2	5	4	1	22	4	
	4	11	2	5	4	1	19	4	
	5	15	2	5	4	1	18	3	
	6	18	1	5	4	1	18	2	
	7	24	1	5	4	1	16	2	
	8	26	1	5	4	1	14	2	
	9	27	1	5	4	1	12	1	
33	1	5	4	4	2	4	18	25	
	2	7	4	3	2	4	17	24	
	3	9	4	3	2	4	15	22	
	4	11	4	3	2	4	13	22	
	5	12	4	3	2	4	12	20	
	6	13	4	3	2	4	11	18	
	7	20	4	3	2	4	9	18	
	8	24	4	3	2	4	8	15	
	9	30	4	3	2	4	7	15	
34	1	6	4	3	3	4	27	18	
	2	15	4	3	2	4	24	18	
	3	17	4	3	2	4	24	15	
	4	18	3	2	2	4	22	13	
	5	20	3	2	2	4	19	12	
	6	21	2	2	2	4	18	10	
	7	23	2	2	2	4	16	6	
	8	26	1	1	2	4	16	5	
	9	29	1	1	2	4	15	4	
35	1	5	5	3	2	5	26	28	
	2	8	4	2	2	5	25	26	
	3	11	4	2	2	5	21	24	
	4	15	4	2	2	5	19	22	
	5	16	3	2	2	5	16	19	
	6	17	3	2	2	5	15	16	
	7	23	3	2	2	5	13	15	
	8	24	3	2	2	5	11	13	
	9	27	3	2	2	5	8	12	
36	1	1	2	5	4	4	24	17	
	2	6	1	4	3	4	22	16	
	3	7	1	4	3	4	22	15	
	4	8	1	4	3	4	19	16	
	5	9	1	4	2	3	16	15	
	6	10	1	4	2	3	15	15	
	7	16	1	4	2	3	12	15	
	8	17	1	4	2	2	12	15	
	9	18	1	4	2	2	10	15	
37	1	1	2	4	3	3	27	22	
	2	9	2	4	3	3	26	22	
	3	14	2	4	3	3	25	22	
	4	19	2	4	3	3	23	22	
	5	20	2	4	3	3	22	21	
	6	21	1	3	3	3	21	21	
	7	22	1	3	3	3	18	21	
	8	23	1	3	3	3	17	21	
	9	24	1	3	3	3	15	21	
38	1	1	2	2	1	2	24	29	
	2	3	2	2	1	2	24	28	
	3	5	2	2	1	2	24	27	
	4	6	2	2	1	2	24	26	
	5	11	2	2	1	2	24	25	
	6	23	2	2	1	2	24	24	
	7	24	2	2	1	2	24	23	
	8	25	2	2	1	2	24	22	
	9	30	2	2	1	2	24	21	
39	1	3	4	5	4	4	20	11	
	2	5	4	4	4	3	19	10	
	3	7	4	4	4	3	18	9	
	4	9	4	4	4	3	15	9	
	5	11	3	4	3	3	14	7	
	6	19	3	4	3	3	12	7	
	7	22	3	4	2	3	8	5	
	8	28	3	4	2	3	6	4	
	9	30	3	4	2	3	5	4	
40	1	2	4	2	4	3	14	12	
	2	3	4	2	4	3	11	11	
	3	4	4	2	4	3	11	10	
	4	10	4	2	4	3	9	11	
	5	12	4	2	4	2	8	10	
	6	14	4	2	4	2	8	9	
	7	21	4	2	4	2	6	9	
	8	22	4	2	4	2	6	8	
	9	24	4	2	4	2	5	8	
41	1	5	1	5	4	4	30	24	
	2	6	1	4	4	3	27	24	
	3	7	1	4	4	3	26	22	
	4	8	1	4	4	3	26	20	
	5	9	1	4	3	2	24	18	
	6	14	1	4	3	2	24	17	
	7	16	1	4	3	2	23	14	
	8	20	1	4	3	1	21	13	
	9	26	1	4	3	1	20	12	
42	1	1	4	5	2	4	15	25	
	2	5	3	4	2	3	14	25	
	3	7	3	4	2	3	13	24	
	4	11	3	4	2	3	12	23	
	5	12	2	3	2	3	12	20	
	6	13	2	3	2	2	12	19	
	7	19	2	3	2	2	11	18	
	8	24	1	3	2	2	10	17	
	9	28	1	3	2	2	10	15	
43	1	4	4	2	3	5	14	21	
	2	11	4	2	3	4	12	17	
	3	12	4	2	3	4	10	16	
	4	13	3	2	2	4	9	15	
	5	14	3	1	2	4	9	13	
	6	19	3	1	2	3	6	11	
	7	20	3	1	1	3	6	8	
	8	21	2	1	1	3	4	6	
	9	26	2	1	1	3	4	5	
44	1	6	4	4	4	4	17	16	
	2	7	4	4	4	4	15	15	
	3	12	4	4	4	4	14	15	
	4	14	4	3	3	4	13	15	
	5	19	4	3	3	3	11	14	
	6	24	4	3	2	3	11	14	
	7	25	4	3	2	3	9	13	
	8	26	4	2	1	3	9	13	
	9	27	4	2	1	3	7	13	
45	1	2	3	5	1	5	25	17	
	2	6	2	5	1	4	22	16	
	3	11	2	5	1	4	19	16	
	4	12	2	5	1	3	19	15	
	5	17	2	5	1	3	16	14	
	6	20	1	5	1	3	15	12	
	7	23	1	5	1	3	12	12	
	8	25	1	5	1	2	10	10	
	9	30	1	5	1	2	10	9	
46	1	7	5	4	4	4	24	30	
	2	10	4	3	3	3	21	28	
	3	19	4	3	3	3	19	27	
	4	20	3	2	3	3	15	26	
	5	21	3	2	2	2	14	26	
	6	24	2	2	2	2	9	25	
	7	25	1	2	2	2	9	25	
	8	27	1	1	2	2	6	24	
	9	30	1	1	2	2	2	23	
47	1	2	3	4	4	3	20	22	
	2	3	2	4	4	3	19	22	
	3	4	2	4	4	3	17	22	
	4	5	2	4	4	3	15	22	
	5	8	2	3	4	3	11	22	
	6	11	2	3	3	3	10	22	
	7	19	2	3	3	3	7	22	
	8	26	2	3	3	3	4	22	
	9	29	2	3	3	3	3	22	
48	1	3	2	4	2	3	25	9	
	2	5	2	4	2	2	23	8	
	3	8	2	3	2	2	23	8	
	4	14	2	3	2	2	20	7	
	5	17	2	3	2	2	20	6	
	6	23	1	2	2	2	17	7	
	7	24	1	2	2	2	16	7	
	8	26	1	1	2	2	13	6	
	9	28	1	1	2	2	13	5	
49	1	5	4	4	1	1	28	23	
	2	7	4	4	1	1	27	20	
	3	13	4	4	1	1	25	18	
	4	21	3	4	1	1	23	16	
	5	22	3	4	1	1	23	13	
	6	23	2	3	1	1	20	12	
	7	25	1	3	1	1	18	9	
	8	29	1	3	1	1	17	8	
	9	30	1	3	1	1	16	4	
50	1	1	1	2	5	4	21	20	
	2	11	1	1	4	3	21	19	
	3	13	1	1	4	3	18	18	
	4	16	1	1	4	2	16	17	
	5	17	1	1	3	2	13	17	
	6	19	1	1	3	2	11	14	
	7	23	1	1	3	1	10	14	
	8	27	1	1	3	1	7	12	
	9	29	1	1	3	1	5	11	
51	1	1	2	4	4	4	8	28	
	2	8	2	4	3	4	6	27	
	3	11	2	4	3	3	6	27	
	4	12	2	4	3	3	5	27	
	5	16	2	4	2	2	5	27	
	6	17	2	4	2	2	5	26	
	7	24	2	4	1	1	4	27	
	8	25	2	4	1	1	3	28	
	9	26	2	4	1	1	3	27	
52	1	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	R 3	R 4	N 1	N 2
	25	19	22	22	630	738

************************************************************************
