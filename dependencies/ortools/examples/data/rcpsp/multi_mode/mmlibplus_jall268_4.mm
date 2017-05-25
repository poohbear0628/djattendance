jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 4 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	5		2 3 4 5 6 
2	9	4		14 10 9 7 
3	9	4		14 10 9 8 
4	9	3		14 12 8 
5	9	4		15 14 13 10 
6	9	3		19 13 9 
7	9	3		24 13 12 
8	9	2		13 11 
9	9	5		24 20 17 16 15 
10	9	1		11 
11	9	8		24 23 22 21 20 19 18 17 
12	9	4		20 19 17 15 
13	9	4		23 22 21 17 
14	9	4		23 22 20 18 
15	9	3		23 22 18 
16	9	3		28 22 21 
17	9	7		35 33 29 28 27 26 25 
18	9	7		35 32 30 29 28 27 26 
19	9	6		35 34 33 29 28 25 
20	9	5		35 33 27 26 25 
21	9	5		35 29 27 26 25 
22	9	5		35 34 33 27 25 
23	9	5		32 30 28 27 26 
24	9	4		33 29 27 25 
25	9	4		40 36 32 31 
26	9	3		40 34 31 
27	9	5		49 44 39 38 37 
28	9	2		38 36 
29	9	7		49 44 42 41 40 39 38 
30	9	4		49 44 40 37 
31	9	6		50 49 42 41 39 38 
32	9	3		49 38 37 
33	9	3		49 38 37 
34	9	1		36 
35	9	6		50 49 43 41 40 39 
36	9	4		49 47 44 37 
37	9	4		50 43 42 41 
38	9	4		51 47 46 43 
39	9	3		48 47 46 
40	9	3		51 47 45 
41	9	2		46 45 
42	9	2		48 45 
43	9	1		45 
44	9	1		45 
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
jobnr.	mode	dur	R1	R2	N1	N2	N3	N4	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	
2	1	1	5	4	26	30	20	27	
	2	2	4	3	26	29	17	25	
	3	6	4	3	24	29	15	23	
	4	8	3	3	24	28	14	22	
	5	10	3	3	23	28	11	19	
	6	14	2	3	22	28	10	17	
	7	16	2	3	20	28	9	16	
	8	25	1	3	19	27	6	15	
	9	26	1	3	18	27	6	12	
3	1	5	5	2	16	11	28	26	
	2	6	4	2	16	11	25	26	
	3	8	4	2	13	11	25	24	
	4	9	4	2	11	11	23	21	
	5	15	4	2	11	11	22	19	
	6	16	3	1	8	11	21	18	
	7	17	3	1	7	11	19	17	
	8	28	3	1	6	11	19	15	
	9	30	3	1	4	11	18	12	
4	1	1	5	4	29	21	26	13	
	2	4	4	4	24	18	24	11	
	3	9	4	3	20	16	20	11	
	4	16	4	3	19	15	18	9	
	5	20	4	2	16	13	16	8	
	6	24	3	2	12	12	15	7	
	7	25	3	2	10	12	12	7	
	8	26	3	1	8	9	10	6	
	9	28	3	1	4	9	10	5	
5	1	3	3	4	24	7	16	24	
	2	4	3	4	22	7	15	23	
	3	7	3	4	21	7	15	20	
	4	11	3	4	20	7	14	19	
	5	13	3	4	20	7	13	16	
	6	16	3	4	18	7	13	16	
	7	17	3	4	18	7	13	12	
	8	24	3	4	17	7	11	11	
	9	27	3	4	16	7	11	10	
6	1	10	3	2	14	9	23	19	
	2	14	3	2	13	8	21	18	
	3	15	3	2	12	8	21	18	
	4	16	3	2	12	7	19	18	
	5	20	3	1	12	5	19	17	
	6	21	3	1	11	5	17	16	
	7	27	3	1	11	4	17	16	
	8	28	3	1	10	3	16	15	
	9	29	3	1	10	2	15	15	
7	1	2	3	5	13	24	14	25	
	2	4	2	4	13	24	13	24	
	3	5	2	4	12	24	11	20	
	4	14	2	3	12	23	10	18	
	5	15	2	3	11	23	7	15	
	6	16	1	2	10	22	6	13	
	7	17	1	2	10	22	6	10	
	8	21	1	1	9	21	3	7	
	9	24	1	1	9	21	1	6	
8	1	8	5	5	29	10	23	6	
	2	9	4	4	28	9	22	5	
	3	10	3	4	28	7	22	5	
	4	11	3	4	28	6	21	5	
	5	16	2	3	27	6	19	5	
	6	18	2	3	27	6	19	4	
	7	19	2	3	27	4	17	5	
	8	21	1	2	27	4	17	5	
	9	27	1	2	27	3	15	5	
9	1	1	2	3	5	29	18	22	
	2	4	1	3	5	27	17	21	
	3	10	1	3	5	23	16	21	
	4	11	1	3	5	20	16	20	
	5	12	1	2	5	18	14	19	
	6	22	1	2	5	17	14	19	
	7	24	1	2	5	13	12	18	
	8	28	1	2	5	12	11	18	
	9	29	1	2	5	7	11	18	
10	1	3	4	5	23	10	22	20	
	2	4	3	4	22	9	21	19	
	3	6	3	4	21	8	19	19	
	4	11	2	4	20	7	18	19	
	5	13	2	3	16	6	16	19	
	6	25	2	3	15	5	15	19	
	7	26	2	2	14	4	15	19	
	8	28	1	2	11	4	13	19	
	9	30	1	2	11	3	11	19	
11	1	15	2	4	20	27	8	18	
	2	20	2	4	20	26	8	18	
	3	22	2	3	19	25	8	16	
	4	23	2	3	19	23	8	15	
	5	24	2	2	17	18	7	12	
	6	27	2	2	17	18	7	11	
	7	28	2	2	17	16	7	9	
	8	29	2	1	16	11	7	8	
	9	30	2	1	15	11	7	6	
12	1	6	2	5	7	24	25	23	
	2	8	2	4	6	22	25	22	
	3	10	2	4	6	21	23	21	
	4	11	2	4	6	18	22	19	
	5	12	2	3	6	17	20	19	
	6	13	2	3	5	14	20	16	
	7	15	2	3	5	13	19	15	
	8	25	2	3	5	11	18	15	
	9	29	2	3	5	10	17	14	
13	1	1	4	4	12	27	13	28	
	2	2	3	3	12	26	13	28	
	3	3	3	3	12	25	12	28	
	4	8	3	3	12	23	11	27	
	5	9	2	2	12	19	11	27	
	6	15	2	2	11	18	10	27	
	7	19	2	2	11	16	9	27	
	8	26	2	1	11	13	8	26	
	9	30	2	1	11	13	8	25	
14	1	4	5	3	11	22	19	7	
	2	17	4	3	11	20	16	7	
	3	18	4	3	10	19	15	7	
	4	19	4	2	10	19	12	7	
	5	21	4	2	9	17	11	7	
	6	22	4	2	9	16	10	6	
	7	25	4	1	8	15	6	6	
	8	27	4	1	7	14	5	6	
	9	29	4	1	7	14	4	6	
15	1	4	4	2	29	24	7	26	
	2	9	3	2	28	24	7	26	
	3	10	3	2	28	23	7	25	
	4	11	3	2	28	23	7	24	
	5	12	3	2	27	21	7	24	
	6	17	2	2	26	21	7	23	
	7	20	2	2	26	20	7	23	
	8	24	2	2	24	19	7	22	
	9	29	2	2	24	19	7	21	
16	1	4	3	4	25	20	29	6	
	2	5	3	4	24	19	27	5	
	3	8	3	4	24	18	26	5	
	4	9	2	3	24	17	24	5	
	5	11	2	3	23	16	24	5	
	6	13	2	3	23	15	23	5	
	7	15	1	3	23	13	22	5	
	8	21	1	2	23	13	21	5	
	9	27	1	2	23	12	20	5	
17	1	3	3	5	26	27	22	19	
	2	4	3	4	26	24	21	18	
	3	5	3	4	22	20	19	18	
	4	8	3	3	20	18	19	18	
	5	12	3	3	18	14	18	17	
	6	13	3	2	14	13	16	17	
	7	15	3	2	13	12	14	16	
	8	20	3	1	7	8	14	16	
	9	30	3	1	6	5	13	16	
18	1	1	3	4	12	23	12	27	
	2	2	2	3	11	23	12	26	
	3	5	2	3	10	23	11	25	
	4	7	2	3	9	23	10	25	
	5	13	2	2	8	23	10	24	
	6	14	1	2	8	23	9	23	
	7	18	1	2	7	23	9	22	
	8	24	1	2	7	23	7	22	
	9	30	1	2	6	23	7	21	
19	1	2	4	4	28	17	18	17	
	2	3	4	3	25	16	18	16	
	3	10	4	3	23	15	18	16	
	4	11	4	2	23	13	17	16	
	5	12	4	2	21	13	17	15	
	6	13	4	2	18	12	16	14	
	7	16	4	2	17	11	16	13	
	8	17	4	1	17	10	15	13	
	9	23	4	1	14	9	15	12	
20	1	7	4	3	17	13	16	20	
	2	8	4	3	17	11	14	18	
	3	9	4	3	17	10	12	15	
	4	10	3	3	17	8	10	14	
	5	13	3	2	17	6	8	12	
	6	25	3	2	17	5	7	9	
	7	26	3	2	17	3	6	9	
	8	27	2	1	17	3	4	7	
	9	30	2	1	17	1	2	4	
21	1	9	3	2	21	2	11	18	
	2	10	2	2	19	2	10	16	
	3	11	2	2	18	2	10	16	
	4	12	2	2	18	2	8	13	
	5	14	2	2	17	2	8	12	
	6	16	2	2	15	2	7	9	
	7	24	2	2	15	2	5	6	
	8	28	2	2	13	2	4	4	
	9	30	2	2	13	2	4	3	
22	1	3	4	4	18	12	17	4	
	2	4	4	3	17	12	13	4	
	3	11	4	3	16	10	12	4	
	4	13	4	2	15	9	10	4	
	5	14	4	2	14	9	9	4	
	6	15	4	2	14	8	7	3	
	7	16	4	2	14	6	7	3	
	8	22	4	1	12	6	5	3	
	9	23	4	1	12	5	3	3	
23	1	3	4	5	27	16	17	9	
	2	8	3	5	25	14	15	9	
	3	11	3	5	25	14	13	8	
	4	16	3	5	23	12	12	8	
	5	19	3	5	23	9	10	6	
	6	21	2	5	21	8	10	6	
	7	22	2	5	21	5	8	5	
	8	26	2	5	20	3	6	5	
	9	28	2	5	18	2	4	4	
24	1	2	3	5	10	4	22	25	
	2	3	2	4	10	4	20	24	
	3	6	2	4	10	4	20	23	
	4	13	2	3	10	4	19	22	
	5	19	1	3	10	4	19	20	
	6	20	1	2	9	4	19	18	
	7	21	1	1	9	4	18	17	
	8	22	1	1	9	4	17	16	
	9	26	1	1	9	4	17	14	
25	1	5	5	4	20	12	16	28	
	2	8	4	3	19	11	15	27	
	3	9	4	3	19	11	15	26	
	4	16	4	3	17	10	14	26	
	5	17	4	3	17	10	14	25	
	6	20	4	3	15	10	13	25	
	7	24	4	3	14	9	12	24	
	8	25	4	3	12	9	12	24	
	9	27	4	3	12	9	11	24	
26	1	1	3	3	25	27	17	25	
	2	6	3	2	20	25	15	23	
	3	9	3	2	19	23	15	22	
	4	15	3	2	18	23	14	20	
	5	19	3	2	14	22	14	16	
	6	20	3	2	14	20	13	14	
	7	21	3	2	10	20	12	12	
	8	29	3	2	8	19	12	11	
	9	30	3	2	8	18	11	10	
27	1	4	5	3	13	27	19	17	
	2	6	5	2	12	24	17	17	
	3	7	5	2	9	24	16	17	
	4	9	5	2	9	22	15	16	
	5	10	5	2	6	19	15	16	
	6	14	5	2	5	14	13	16	
	7	15	5	2	3	14	12	15	
	8	18	5	2	3	10	11	15	
	9	24	5	2	1	7	10	15	
28	1	1	5	5	17	21	30	24	
	2	3	4	4	14	20	28	23	
	3	4	4	3	14	17	27	23	
	4	7	3	3	11	16	26	22	
	5	17	3	3	11	14	26	22	
	6	18	3	2	9	12	26	22	
	7	20	3	2	7	8	25	21	
	8	21	2	1	5	7	23	21	
	9	22	2	1	5	5	23	21	
29	1	6	3	3	18	18	25	12	
	2	7	3	3	18	16	24	10	
	3	13	3	3	14	15	24	10	
	4	14	2	3	14	15	24	8	
	5	15	2	3	12	14	23	8	
	6	16	2	2	8	13	23	7	
	7	17	2	2	8	12	23	7	
	8	23	1	2	6	12	23	5	
	9	26	1	2	3	11	23	5	
30	1	6	4	4	22	5	19	6	
	2	14	4	3	21	5	18	5	
	3	16	4	3	21	5	17	5	
	4	17	4	3	20	4	16	5	
	5	18	3	2	20	4	16	3	
	6	25	3	2	19	4	15	3	
	7	28	3	1	19	4	15	3	
	8	29	3	1	18	3	15	1	
	9	30	3	1	17	3	14	1	
31	1	4	3	4	14	21	6	5	
	2	6	3	4	13	19	6	4	
	3	7	3	4	13	18	5	3	
	4	8	3	4	13	17	4	3	
	5	9	2	4	13	15	4	2	
	6	17	2	4	12	13	3	2	
	7	19	1	4	12	13	3	1	
	8	23	1	4	12	11	3	1	
	9	26	1	4	12	9	2	1	
32	1	8	4	1	9	29	23	7	
	2	10	3	1	9	25	23	6	
	3	12	3	1	8	22	22	6	
	4	14	2	1	8	19	22	6	
	5	15	2	1	7	19	22	5	
	6	20	2	1	6	14	21	5	
	7	22	2	1	6	12	21	5	
	8	28	1	1	6	11	20	5	
	9	30	1	1	5	7	20	5	
33	1	1	5	5	27	8	25	11	
	2	2	5	4	25	7	21	9	
	3	7	5	4	21	6	20	8	
	4	11	5	4	20	5	16	7	
	5	12	5	3	16	5	14	7	
	6	14	5	3	13	5	12	6	
	7	25	5	3	11	4	8	5	
	8	26	5	2	8	4	6	4	
	9	30	5	2	4	3	5	2	
34	1	2	2	2	21	17	27	28	
	2	3	2	1	20	15	27	25	
	3	6	2	1	17	15	27	25	
	4	8	2	1	17	13	26	23	
	5	9	2	1	13	11	26	23	
	6	14	2	1	13	9	25	22	
	7	18	2	1	10	9	24	21	
	8	22	2	1	9	5	24	20	
	9	28	2	1	8	4	24	18	
35	1	2	4	3	29	14	15	15	
	2	3	3	2	27	13	13	14	
	3	4	3	2	25	13	12	14	
	4	10	3	2	23	11	11	13	
	5	16	2	2	21	11	11	13	
	6	18	2	1	19	9	11	13	
	7	19	2	1	18	8	9	12	
	8	20	2	1	15	7	8	12	
	9	22	2	1	15	7	8	11	
36	1	3	2	4	29	13	19	20	
	2	7	2	3	24	12	19	19	
	3	9	2	3	23	11	19	19	
	4	16	2	2	21	10	19	19	
	5	19	2	2	15	7	19	18	
	6	23	2	2	13	6	18	18	
	7	25	2	2	12	6	18	17	
	8	26	2	1	8	4	18	17	
	9	27	2	1	5	2	18	17	
37	1	3	3	5	6	19	19	30	
	2	4	3	4	5	17	18	28	
	3	8	3	4	5	16	17	28	
	4	11	3	3	5	16	16	26	
	5	13	3	3	4	14	14	26	
	6	17	3	2	3	11	12	26	
	7	21	3	2	3	11	11	24	
	8	29	3	1	1	9	11	23	
	9	30	3	1	1	7	9	23	
38	1	7	4	3	2	29	20	20	
	2	8	4	3	1	29	20	20	
	3	19	4	3	1	29	18	20	
	4	20	4	2	1	29	18	20	
	5	24	4	2	1	28	17	20	
	6	27	3	2	1	28	15	20	
	7	28	3	1	1	28	14	20	
	8	29	3	1	1	28	14	19	
	9	30	3	1	1	28	13	20	
39	1	12	5	4	27	22	7	3	
	2	16	4	3	27	20	6	3	
	3	18	4	3	27	20	6	2	
	4	21	4	3	27	18	6	3	
	5	22	3	3	26	17	6	3	
	6	24	3	2	26	17	6	3	
	7	26	3	2	26	16	6	3	
	8	28	3	2	26	14	6	3	
	9	30	3	2	26	14	6	2	
40	1	5	4	1	12	15	12	20	
	2	6	4	1	11	13	11	20	
	3	8	4	1	10	12	11	20	
	4	9	4	1	9	11	11	20	
	5	10	4	1	9	9	10	20	
	6	12	4	1	8	9	10	20	
	7	13	4	1	8	6	9	20	
	8	14	4	1	7	5	8	20	
	9	17	4	1	6	5	8	20	
41	1	1	4	3	23	27	21	19	
	2	3	4	3	23	27	19	17	
	3	4	4	3	22	27	19	16	
	4	5	3	3	20	27	18	14	
	5	10	2	2	20	27	18	13	
	6	11	2	2	19	27	17	11	
	7	14	1	2	18	27	17	11	
	8	25	1	1	17	27	17	9	
	9	28	1	1	16	27	16	8	
42	1	2	3	4	19	28	28	11	
	2	3	2	4	15	27	28	11	
	3	6	2	4	13	27	28	10	
	4	15	2	4	12	27	27	10	
	5	19	2	4	11	27	27	10	
	6	20	2	4	8	26	26	9	
	7	21	2	4	7	26	26	9	
	8	23	2	4	4	26	25	8	
	9	26	2	4	4	26	25	7	
43	1	1	5	2	10	16	20	20	
	2	2	4	2	9	15	20	17	
	3	4	4	2	8	13	20	16	
	4	5	3	2	7	11	20	15	
	5	22	2	2	7	9	20	13	
	6	23	2	1	5	9	20	11	
	7	24	2	1	4	6	20	9	
	8	25	1	1	2	6	20	5	
	9	27	1	1	2	3	20	4	
44	1	8	3	4	18	22	22	30	
	2	9	3	4	17	22	22	29	
	3	10	3	4	17	22	21	29	
	4	16	3	3	17	21	20	29	
	5	19	3	2	17	21	18	29	
	6	23	2	2	16	21	17	28	
	7	24	2	2	16	21	16	28	
	8	25	2	1	16	20	15	28	
	9	26	2	1	16	20	15	27	
45	1	3	1	3	24	25	11	19	
	2	8	1	3	21	23	9	19	
	3	9	1	3	19	19	9	17	
	4	13	1	3	19	16	9	16	
	5	14	1	3	17	12	8	16	
	6	17	1	3	16	9	8	15	
	7	19	1	3	13	8	7	13	
	8	22	1	3	11	6	6	12	
	9	26	1	3	10	1	6	12	
46	1	1	4	2	18	7	29	14	
	2	8	4	2	15	7	22	14	
	3	9	4	2	13	7	19	14	
	4	22	4	2	11	7	18	14	
	5	24	4	2	9	7	15	14	
	6	27	4	2	8	7	12	13	
	7	28	4	2	5	7	7	14	
	8	29	4	2	5	7	7	13	
	9	30	4	2	1	7	2	13	
47	1	3	5	4	24	27	28	12	
	2	8	4	3	23	27	26	12	
	3	12	4	3	23	26	23	12	
	4	13	4	3	21	25	23	12	
	5	17	3	3	20	23	20	11	
	6	22	3	2	19	22	17	11	
	7	23	3	2	17	21	16	11	
	8	26	3	2	17	18	13	11	
	9	28	3	2	15	18	10	11	
48	1	5	4	3	14	18	23	3	
	2	6	4	3	12	17	22	3	
	3	8	4	3	12	14	22	3	
	4	14	4	3	11	13	21	3	
	5	18	4	2	10	11	19	3	
	6	25	4	2	10	9	17	3	
	7	28	4	2	10	6	16	3	
	8	29	4	1	8	6	16	3	
	9	30	4	1	8	4	15	3	
49	1	3	5	4	28	23	1	29	
	2	5	4	3	25	22	1	28	
	3	8	4	3	23	19	1	28	
	4	18	4	3	20	18	1	28	
	5	21	4	2	20	16	1	28	
	6	22	4	2	16	14	1	28	
	7	25	4	1	16	14	1	28	
	8	26	4	1	12	13	1	28	
	9	27	4	1	11	11	1	28	
50	1	5	4	1	22	23	9	22	
	2	6	4	1	21	22	9	21	
	3	7	3	1	17	21	8	19	
	4	9	3	1	16	19	8	17	
	5	15	3	1	14	17	8	16	
	6	16	2	1	11	15	7	14	
	7	18	2	1	11	13	6	14	
	8	29	1	1	7	13	6	12	
	9	30	1	1	7	12	6	11	
51	1	2	4	2	19	20	24	17	
	2	4	4	2	19	19	22	15	
	3	11	3	2	17	18	21	15	
	4	12	3	2	17	17	19	14	
	5	13	3	2	16	17	18	14	
	6	16	2	2	16	17	15	13	
	7	22	2	2	14	16	13	13	
	8	23	1	2	13	15	12	12	
	9	29	1	2	13	14	9	12	
52	1	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2	N 3	N 4
	22	25	625	612	652	668

************************************************************************
