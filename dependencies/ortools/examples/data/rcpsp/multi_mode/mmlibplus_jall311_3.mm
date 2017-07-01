jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 4 R
- nonrenewable              : 4 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	11		2 3 4 5 6 7 8 9 12 13 16 
2	9	10		33 28 27 25 22 21 19 18 17 15 
3	9	5		28 21 17 11 10 
4	9	8		33 29 28 26 24 20 18 14 
5	9	8		36 32 28 27 25 23 22 17 
6	9	3		29 28 10 
7	9	5		29 25 23 22 11 
8	9	9		36 33 32 31 29 27 24 23 22 
9	9	6		32 27 26 23 22 17 
10	9	5		31 27 26 22 15 
11	9	8		38 36 35 32 31 30 27 24 
12	9	6		36 34 31 25 22 21 
13	9	3		31 22 15 
14	9	6		37 34 32 31 23 22 
15	9	6		39 36 35 34 32 23 
16	9	6		40 34 31 30 29 27 
17	9	4		40 31 29 24 
18	9	7		51 50 39 38 36 34 32 
19	9	6		51 45 40 38 37 31 
20	9	4		51 37 31 30 
21	9	6		51 48 45 39 38 37 
22	9	5		51 49 38 35 30 
23	9	5		51 49 40 38 30 
24	9	6		51 49 48 41 39 34 
25	9	9		50 49 48 46 45 44 42 40 39 
26	9	7		51 48 46 44 40 39 38 
27	9	5		50 42 41 39 37 
28	9	9		51 50 49 48 46 45 44 43 41 
29	9	5		49 48 46 45 38 
30	9	7		50 47 46 45 44 42 41 
31	9	6		50 48 43 42 41 39 
32	9	6		47 45 44 43 42 40 
33	9	4		46 45 44 38 
34	9	6		47 46 45 44 43 42 
35	9	5		47 45 43 42 41 
36	9	5		48 45 44 42 41 
37	9	4		49 46 44 43 
38	9	3		43 42 41 
39	9	1		47 
40	9	1		41 
41	9	1		52 
42	9	1		52 
43	9	1		52 
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
jobnr.	mode	dur	R1	R2	R3	R4	N1	N2	N3	N4	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	0	0	
2	1	1	2	3	3	3	11	25	27	8	
	2	2	2	2	3	3	11	25	24	7	
	3	4	2	2	3	3	9	25	22	6	
	4	5	2	2	3	3	9	25	21	5	
	5	7	2	2	3	3	8	25	20	5	
	6	18	2	1	3	3	6	25	19	5	
	7	22	2	1	3	3	6	25	16	4	
	8	23	2	1	3	3	5	25	14	4	
	9	24	2	1	3	3	4	25	13	3	
3	1	3	4	4	4	3	29	22	26	23	
	2	4	3	4	3	2	27	20	24	21	
	3	5	3	4	3	2	27	20	22	19	
	4	6	3	4	3	2	25	19	19	15	
	5	7	3	4	2	2	24	18	15	13	
	6	8	3	3	2	2	24	16	14	11	
	7	9	3	3	2	2	22	16	11	9	
	8	14	3	3	2	2	21	15	8	8	
	9	15	3	3	2	2	21	14	6	7	
4	1	1	4	5	5	4	23	26	27	24	
	2	5	3	5	4	4	22	24	26	22	
	3	9	3	5	4	4	22	22	23	21	
	4	10	3	5	4	4	22	22	20	21	
	5	11	2	5	4	4	22	18	16	18	
	6	15	2	5	3	4	21	16	14	16	
	7	19	2	5	3	4	21	14	12	16	
	8	24	1	5	3	4	21	12	9	12	
	9	25	1	5	3	4	21	12	6	11	
5	1	10	3	2	5	4	25	23	18	29	
	2	16	3	2	4	4	22	23	16	28	
	3	18	3	2	4	4	20	23	15	26	
	4	21	3	2	3	4	17	23	13	22	
	5	23	3	1	3	4	14	23	11	20	
	6	24	3	1	2	4	14	23	10	18	
	7	25	3	1	2	4	12	23	9	16	
	8	26	3	1	1	4	9	23	8	16	
	9	27	3	1	1	4	6	23	7	14	
6	1	2	2	2	5	5	7	13	14	14	
	2	4	1	1	5	4	5	12	12	12	
	3	5	1	1	5	4	5	12	12	11	
	4	6	1	1	5	4	5	12	11	10	
	5	14	1	1	5	4	3	11	7	7	
	6	21	1	1	5	3	3	11	6	6	
	7	23	1	1	5	3	3	11	4	4	
	8	26	1	1	5	3	1	10	2	4	
	9	27	1	1	5	3	1	10	1	2	
7	1	2	2	2	3	4	28	15	25	30	
	2	5	2	2	3	4	25	15	24	28	
	3	6	2	2	3	4	24	15	22	27	
	4	12	2	2	3	4	20	15	21	27	
	5	13	2	2	3	3	19	15	20	25	
	6	17	2	2	3	3	18	15	19	25	
	7	20	2	2	3	3	15	15	18	24	
	8	22	2	2	3	2	14	15	18	22	
	9	29	2	2	3	2	12	15	17	21	
8	1	3	4	3	3	5	26	27	29	27	
	2	10	4	3	2	4	24	26	27	27	
	3	11	3	3	2	4	22	26	27	26	
	4	15	3	3	2	4	20	26	26	26	
	5	17	3	2	2	3	20	26	25	26	
	6	23	2	2	2	3	19	26	23	25	
	7	25	1	2	2	3	17	26	23	24	
	8	27	1	2	2	2	15	26	22	24	
	9	29	1	2	2	2	14	26	20	24	
9	1	4	3	3	4	5	19	18	17	24	
	2	15	3	2	3	4	17	18	16	20	
	3	17	3	2	3	3	16	17	16	19	
	4	21	3	2	3	3	16	15	16	17	
	5	22	3	1	2	3	15	12	16	15	
	6	23	2	1	2	2	15	11	16	12	
	7	26	2	1	2	1	13	10	16	9	
	8	28	2	1	2	1	13	8	16	8	
	9	29	2	1	2	1	12	8	16	4	
10	1	1	3	2	4	4	27	7	11	23	
	2	2	2	2	3	4	25	7	10	20	
	3	5	2	2	3	4	21	7	10	16	
	4	8	2	2	3	3	18	7	10	15	
	5	9	2	2	2	3	17	7	9	12	
	6	12	2	2	2	2	14	7	9	11	
	7	13	2	2	1	2	12	7	8	7	
	8	17	2	2	1	1	8	7	8	6	
	9	28	2	2	1	1	8	7	8	4	
11	1	1	2	3	4	2	28	21	25	18	
	2	2	1	2	4	2	26	21	24	16	
	3	3	1	2	4	2	25	21	24	13	
	4	5	1	2	4	2	23	21	22	11	
	5	9	1	2	4	2	21	20	21	9	
	6	12	1	1	4	2	20	20	19	7	
	7	18	1	1	4	2	20	20	19	5	
	8	21	1	1	4	2	17	19	16	3	
	9	26	1	1	4	2	17	19	16	2	
12	1	4	5	5	2	5	29	18	14	26	
	2	6	4	4	1	4	27	17	13	25	
	3	13	4	4	1	4	22	15	12	25	
	4	15	4	4	1	4	21	11	11	25	
	5	16	4	4	1	4	17	11	11	24	
	6	19	3	4	1	4	14	8	11	24	
	7	20	3	4	1	4	12	7	10	23	
	8	26	3	4	1	4	7	4	8	23	
	9	29	3	4	1	4	4	4	8	23	
13	1	2	5	2	2	3	24	17	25	16	
	2	4	4	2	2	2	21	17	21	14	
	3	12	4	2	2	2	21	17	20	13	
	4	15	4	2	2	2	18	17	18	12	
	5	19	4	2	2	2	18	16	13	9	
	6	22	4	2	2	1	16	16	13	7	
	7	23	4	2	2	1	15	15	9	7	
	8	29	4	2	2	1	11	15	7	6	
	9	30	4	2	2	1	10	15	5	3	
14	1	4	5	3	1	5	10	24	30	14	
	2	7	4	3	1	4	9	23	28	14	
	3	11	4	3	1	4	8	21	27	12	
	4	14	4	2	1	3	8	21	25	10	
	5	17	4	2	1	2	7	19	24	8	
	6	18	4	2	1	2	7	19	22	7	
	7	25	4	1	1	1	6	18	22	6	
	8	26	4	1	1	1	5	17	19	3	
	9	27	4	1	1	1	5	16	18	2	
15	1	3	4	3	1	3	12	30	26	6	
	2	10	3	2	1	3	12	29	26	5	
	3	11	3	2	1	3	12	29	24	5	
	4	15	2	2	1	3	12	28	23	4	
	5	22	2	2	1	3	12	28	20	4	
	6	25	2	1	1	3	12	27	18	3	
	7	27	1	1	1	3	12	27	18	3	
	8	29	1	1	1	3	12	26	15	2	
	9	30	1	1	1	3	12	26	14	1	
16	1	2	4	5	4	1	6	27	26	17	
	2	6	4	5	3	1	6	26	22	15	
	3	9	4	5	3	1	6	21	21	14	
	4	10	4	5	3	1	6	18	18	12	
	5	11	3	5	3	1	6	15	15	11	
	6	13	3	5	2	1	6	13	12	9	
	7	14	3	5	2	1	6	12	9	6	
	8	23	2	5	2	1	6	7	8	4	
	9	26	2	5	2	1	6	5	5	4	
17	1	9	3	3	2	4	16	16	27	21	
	2	10	2	2	2	3	15	14	26	18	
	3	11	2	2	2	3	15	14	25	18	
	4	12	2	2	2	3	15	12	25	15	
	5	14	1	2	1	3	14	11	23	14	
	6	16	1	2	1	2	13	11	23	13	
	7	21	1	2	1	2	13	9	22	12	
	8	22	1	2	1	2	12	9	22	9	
	9	27	1	2	1	2	12	7	21	8	
18	1	4	3	5	4	4	14	17	15	29	
	2	5	2	4	3	4	12	16	15	29	
	3	10	2	4	3	4	11	14	14	29	
	4	11	2	3	3	4	11	14	12	29	
	5	15	1	3	3	4	9	13	11	28	
	6	17	1	3	2	4	8	12	11	28	
	7	18	1	3	2	4	6	12	9	28	
	8	19	1	2	2	4	6	11	8	27	
	9	20	1	2	2	4	5	10	7	27	
19	1	4	2	4	4	4	17	7	19	17	
	2	8	2	3	3	4	16	6	16	16	
	3	9	2	3	3	4	15	5	14	16	
	4	12	2	3	3	4	14	4	14	16	
	5	21	2	3	2	3	14	4	11	16	
	6	24	2	3	2	3	12	3	9	15	
	7	25	2	3	2	3	11	2	8	15	
	8	27	2	3	1	3	11	1	8	15	
	9	30	2	3	1	3	10	1	5	15	
20	1	4	1	4	4	4	25	21	25	16	
	2	5	1	4	3	4	25	19	25	13	
	3	7	1	4	3	4	24	17	25	11	
	4	8	1	4	3	4	24	15	25	9	
	5	11	1	4	3	4	23	14	25	8	
	6	19	1	4	2	4	22	13	24	6	
	7	20	1	4	2	4	21	10	24	6	
	8	22	1	4	2	4	20	7	24	5	
	9	28	1	4	2	4	20	7	24	3	
21	1	2	2	5	5	5	24	27	21	28	
	2	9	1	4	4	4	22	25	20	26	
	3	14	1	4	4	4	20	24	20	26	
	4	18	1	4	4	4	17	24	19	25	
	5	19	1	3	3	3	13	23	17	23	
	6	22	1	3	3	3	12	22	15	22	
	7	25	1	3	3	3	9	20	15	21	
	8	29	1	3	2	3	5	19	12	19	
	9	30	1	3	2	3	4	19	11	19	
22	1	1	2	4	3	5	20	25	14	7	
	2	3	1	3	3	4	19	24	14	6	
	3	4	1	3	3	4	19	24	12	5	
	4	7	1	3	3	4	19	23	11	4	
	5	16	1	2	3	4	18	22	10	4	
	6	19	1	2	3	3	18	22	10	3	
	7	20	1	2	3	3	18	22	8	2	
	8	21	1	2	3	3	17	21	8	2	
	9	30	1	2	3	3	17	21	7	1	
23	1	8	3	3	4	5	14	27	29	25	
	2	9	3	3	4	4	12	24	29	23	
	3	10	3	3	4	4	11	22	29	22	
	4	13	3	3	4	3	9	17	28	22	
	5	16	3	3	4	2	9	16	27	21	
	6	17	3	2	3	2	7	11	27	18	
	7	19	3	2	3	1	6	11	27	17	
	8	23	3	2	3	1	5	5	26	17	
	9	30	3	2	3	1	4	5	26	16	
24	1	4	4	5	3	4	17	11	23	14	
	2	10	3	4	3	4	15	10	23	13	
	3	11	3	3	3	4	13	10	23	12	
	4	13	3	3	3	3	12	10	23	12	
	5	14	3	3	3	3	9	9	23	10	
	6	18	3	2	3	3	7	8	23	10	
	7	24	3	1	3	3	6	7	23	8	
	8	28	3	1	3	2	4	6	23	8	
	9	29	3	1	3	2	3	6	23	7	
25	1	3	3	3	1	4	25	16	12	20	
	2	5	3	3	1	4	20	16	11	20	
	3	13	3	3	1	4	17	13	11	17	
	4	19	3	3	1	4	17	11	10	16	
	5	20	2	3	1	3	15	10	10	15	
	6	21	2	3	1	3	10	9	9	13	
	7	23	2	3	1	3	10	8	9	12	
	8	25	1	3	1	3	5	6	8	10	
	9	26	1	3	1	3	3	4	7	8	
26	1	1	5	4	4	5	13	26	20	23	
	2	2	5	3	4	4	12	22	17	23	
	3	5	5	3	4	4	12	22	16	22	
	4	10	5	3	4	3	12	20	15	22	
	5	15	5	3	4	3	12	18	13	20	
	6	18	5	3	4	2	11	17	13	20	
	7	21	5	3	4	2	11	14	10	19	
	8	22	5	3	4	1	11	13	10	19	
	9	25	5	3	4	1	11	12	7	18	
27	1	3	5	5	1	5	22	8	11	20	
	2	7	4	4	1	4	21	8	11	18	
	3	9	4	4	1	4	20	7	10	17	
	4	11	3	3	1	4	19	6	8	16	
	5	16	2	3	1	4	19	6	8	12	
	6	17	2	3	1	4	18	6	7	11	
	7	18	2	3	1	4	18	5	5	10	
	8	29	1	2	1	4	17	5	4	6	
	9	30	1	2	1	4	17	4	4	6	
28	1	2	4	4	3	2	7	20	24	18	
	2	5	4	3	3	1	7	18	23	18	
	3	8	4	3	3	1	7	17	18	17	
	4	19	4	2	3	1	7	16	16	17	
	5	20	3	2	3	1	6	14	15	17	
	6	22	3	2	3	1	6	13	12	16	
	7	27	2	1	3	1	6	10	7	16	
	8	28	2	1	3	1	6	9	5	15	
	9	30	2	1	3	1	6	8	1	15	
29	1	1	3	4	1	5	11	25	26	15	
	2	7	2	4	1	4	11	24	24	14	
	3	11	2	4	1	4	11	24	23	14	
	4	13	2	4	1	3	11	23	20	14	
	5	18	1	4	1	3	11	23	15	14	
	6	23	1	4	1	3	11	22	13	13	
	7	24	1	4	1	3	11	22	10	13	
	8	29	1	4	1	2	11	22	8	13	
	9	30	1	4	1	2	11	21	7	13	
30	1	3	2	4	4	4	19	21	28	22	
	2	9	2	4	4	4	18	21	28	21	
	3	10	2	4	4	4	18	19	28	21	
	4	17	2	4	4	4	17	18	28	21	
	5	20	2	4	4	4	17	16	28	21	
	6	23	2	3	3	3	17	16	28	21	
	7	25	2	3	3	3	16	15	28	21	
	8	26	2	3	3	3	16	14	28	21	
	9	27	2	3	3	3	16	12	28	21	
31	1	10	4	3	2	4	24	16	28	12	
	2	11	4	2	1	3	23	16	27	12	
	3	15	4	2	1	3	22	14	27	12	
	4	18	4	2	1	3	22	11	27	12	
	5	20	4	1	1	3	22	10	27	11	
	6	20	4	1	1	2	21	8	27	12	
	7	21	4	1	1	2	21	8	27	11	
	8	22	4	1	1	2	20	5	27	11	
	9	28	4	1	1	2	20	5	27	10	
32	1	10	5	3	5	5	11	29	17	19	
	2	11	4	3	4	4	10	27	17	19	
	3	12	4	3	4	4	10	24	14	16	
	4	15	3	3	4	3	8	21	13	16	
	5	16	3	2	4	3	8	20	11	12	
	6	18	3	2	4	2	8	19	9	11	
	7	21	2	2	4	1	7	15	5	10	
	8	28	2	1	4	1	6	15	4	8	
	9	29	2	1	4	1	5	13	2	6	
33	1	5	4	5	4	5	27	29	20	13	
	2	11	3	4	4	4	27	29	19	13	
	3	18	3	3	4	4	26	28	17	13	
	4	19	3	3	4	3	25	26	17	13	
	5	20	2	3	4	3	23	26	16	13	
	6	25	2	2	4	3	23	25	15	13	
	7	27	1	2	4	3	22	23	14	13	
	8	29	1	1	4	2	20	23	14	13	
	9	30	1	1	4	2	19	22	13	13	
34	1	3	5	3	4	4	25	24	15	4	
	2	6	5	3	4	3	23	23	14	4	
	3	7	5	3	3	3	22	23	13	4	
	4	8	5	3	3	3	20	21	11	4	
	5	14	5	3	3	2	19	20	9	4	
	6	15	5	3	2	2	18	17	8	4	
	7	20	5	3	1	2	16	15	7	4	
	8	25	5	3	1	2	14	14	6	4	
	9	26	5	3	1	2	14	13	5	4	
35	1	9	5	5	4	2	9	29	8	28	
	2	11	4	4	4	2	9	28	7	28	
	3	14	4	4	3	2	7	26	7	28	
	4	15	3	3	3	2	6	25	6	28	
	5	20	3	3	3	2	6	25	6	27	
	6	22	3	3	2	2	5	25	5	27	
	7	26	3	2	1	2	4	24	5	26	
	8	28	2	2	1	2	3	22	5	26	
	9	29	2	2	1	2	1	22	4	26	
36	1	1	3	3	1	4	14	14	28	26	
	2	2	2	2	1	3	14	12	28	25	
	3	3	2	2	1	3	13	12	28	22	
	4	5	2	2	1	3	13	11	28	19	
	5	15	1	2	1	2	13	11	28	17	
	6	19	1	2	1	2	12	10	28	15	
	7	24	1	2	1	2	11	9	28	15	
	8	27	1	2	1	2	11	8	28	13	
	9	28	1	2	1	2	11	8	28	11	
37	1	1	5	1	5	2	9	13	14	26	
	2	2	4	1	4	2	8	11	14	25	
	3	3	4	1	4	2	8	11	14	24	
	4	3	4	1	3	2	8	11	14	25	
	5	17	3	1	2	2	8	10	14	25	
	6	19	3	1	2	2	8	10	14	24	
	7	21	2	1	1	2	8	9	14	25	
	8	27	2	1	1	2	8	9	14	24	
	9	28	2	1	1	2	8	8	14	25	
38	1	1	5	3	1	4	26	18	10	24	
	2	3	4	3	1	4	22	18	9	23	
	3	6	4	3	1	4	21	16	7	21	
	4	11	4	2	1	4	20	15	6	20	
	5	14	3	2	1	3	19	14	6	20	
	6	18	3	2	1	3	16	12	4	20	
	7	25	3	1	1	2	16	12	3	18	
	8	27	3	1	1	2	13	10	2	18	
	9	28	3	1	1	2	13	9	1	17	
39	1	2	4	3	4	3	18	13	16	1	
	2	3	4	3	4	3	17	12	15	1	
	3	5	4	3	4	3	16	12	14	1	
	4	9	4	3	3	2	15	12	14	1	
	5	15	4	2	3	2	14	11	13	1	
	6	19	4	2	3	2	14	10	12	1	
	7	23	4	2	2	2	12	10	12	1	
	8	26	4	1	2	1	11	9	12	1	
	9	27	4	1	2	1	11	9	11	1	
40	1	3	5	4	3	2	24	25	15	9	
	2	7	5	4	2	1	21	21	14	9	
	3	8	5	4	2	1	20	17	14	7	
	4	13	5	4	2	1	17	16	14	6	
	5	15	5	3	2	1	14	11	14	5	
	6	24	5	3	1	1	13	11	13	5	
	7	25	5	3	1	1	10	8	13	3	
	8	29	5	3	1	1	7	6	13	3	
	9	30	5	3	1	1	6	2	13	2	
41	1	2	4	5	2	4	19	26	25	28	
	2	3	4	4	1	4	19	24	24	26	
	3	9	4	4	1	4	19	21	22	26	
	4	10	4	4	1	4	19	18	22	25	
	5	11	3	4	1	4	19	14	21	24	
	6	12	3	4	1	3	19	13	20	22	
	7	16	3	4	1	3	19	11	20	21	
	8	20	3	4	1	3	19	6	19	21	
	9	25	3	4	1	3	19	5	18	20	
42	1	4	1	4	5	4	16	24	16	25	
	2	9	1	4	4	4	14	23	15	24	
	3	10	1	4	4	4	14	23	15	23	
	4	11	1	4	3	4	13	22	14	21	
	5	22	1	3	3	3	12	22	13	20	
	6	23	1	3	3	3	12	22	11	19	
	7	28	1	2	2	3	12	21	10	19	
	8	29	1	2	2	2	10	21	9	18	
	9	30	1	2	2	2	10	20	9	17	
43	1	1	4	4	4	4	28	14	10	26	
	2	2	4	4	3	4	28	14	10	25	
	3	4	4	4	3	4	27	14	10	25	
	4	10	4	4	3	4	24	13	10	25	
	5	15	4	4	2	4	22	13	10	25	
	6	17	4	4	2	4	22	13	10	24	
	7	19	4	4	1	4	19	12	10	25	
	8	20	4	4	1	4	18	12	10	25	
	9	21	4	4	1	4	17	12	10	25	
44	1	1	5	3	1	4	29	27	8	19	
	2	2	4	3	1	4	27	26	7	18	
	3	9	4	3	1	4	25	24	6	17	
	4	13	4	3	1	4	22	24	6	15	
	5	14	3	2	1	3	21	22	4	13	
	6	16	3	2	1	3	19	20	4	12	
	7	21	3	1	1	3	18	19	3	11	
	8	27	2	1	1	3	17	18	3	8	
	9	30	2	1	1	3	15	16	2	6	
45	1	2	3	1	1	4	28	18	6	28	
	2	6	3	1	1	4	25	16	6	28	
	3	7	3	1	1	4	22	13	5	28	
	4	8	3	1	1	4	16	11	5	27	
	5	9	3	1	1	4	13	10	3	27	
	6	12	3	1	1	4	12	10	3	27	
	7	16	3	1	1	4	10	8	3	27	
	8	18	3	1	1	4	7	7	2	26	
	9	30	3	1	1	4	3	5	1	26	
46	1	3	5	2	4	2	28	8	18	19	
	2	4	4	2	3	2	26	7	17	17	
	3	5	4	2	3	2	25	7	17	16	
	4	8	3	2	3	2	23	7	17	15	
	5	12	3	2	2	2	22	7	16	13	
	6	19	3	2	2	2	21	6	16	13	
	7	25	2	2	2	2	19	6	16	10	
	8	28	2	2	1	2	19	6	16	10	
	9	30	2	2	1	2	17	6	16	9	
47	1	8	3	3	4	4	6	19	28	27	
	2	9	3	2	3	4	6	18	26	25	
	3	10	3	2	3	4	6	16	25	24	
	4	11	3	2	3	4	6	16	25	22	
	5	14	2	2	3	4	6	15	24	20	
	6	15	2	2	3	4	6	14	22	19	
	7	20	2	2	3	4	6	13	22	17	
	8	21	1	2	3	4	6	12	21	17	
	9	29	1	2	3	4	6	11	20	16	
48	1	3	4	1	3	5	29	28	9	21	
	2	13	4	1	2	4	29	27	8	20	
	3	14	4	1	2	4	29	27	7	18	
	4	18	4	1	2	3	28	26	7	17	
	5	23	3	1	2	3	27	26	7	17	
	6	24	3	1	2	3	27	26	6	16	
	7	25	3	1	2	3	26	25	6	15	
	8	29	3	1	2	2	26	25	5	14	
	9	30	3	1	2	2	26	25	5	13	
49	1	15	1	5	2	2	29	22	10	28	
	2	16	1	4	2	1	29	22	10	26	
	3	17	1	4	2	1	28	22	9	24	
	4	18	1	3	2	1	28	22	8	22	
	5	20	1	3	1	1	27	22	7	21	
	6	26	1	3	1	1	26	22	6	17	
	7	27	1	3	1	1	26	22	5	15	
	8	28	1	2	1	1	25	22	3	13	
	9	29	1	2	1	1	25	22	2	13	
50	1	6	2	4	1	2	24	26	23	30	
	2	7	1	4	1	2	23	26	23	26	
	3	8	1	4	1	2	18	26	19	23	
	4	11	1	4	1	2	18	26	17	22	
	5	17	1	4	1	2	13	26	14	19	
	6	20	1	4	1	2	12	25	12	18	
	7	22	1	4	1	2	9	25	9	15	
	8	23	1	4	1	2	7	25	6	12	
	9	26	1	4	1	2	2	25	3	10	
51	1	3	3	2	1	2	10	9	26	25	
	2	5	3	2	1	2	9	9	23	23	
	3	13	3	2	1	2	9	9	22	22	
	4	16	3	2	1	2	8	9	20	22	
	5	19	3	2	1	2	8	8	19	21	
	6	21	3	2	1	2	7	8	17	20	
	7	26	3	2	1	2	7	7	15	19	
	8	29	3	2	1	2	6	7	13	19	
	9	30	3	2	1	2	6	7	12	18	
52	1	0	0	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	R 3	R 4	N 1	N 2	N 3	N 4
	24	24	25	28	763	819	769	802

************************************************************************
