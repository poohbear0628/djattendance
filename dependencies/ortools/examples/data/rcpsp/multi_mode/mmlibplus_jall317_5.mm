jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 4 R
- nonrenewable              : 4 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	6		2 3 4 5 6 9 
2	9	7		18 15 13 12 11 8 7 
3	9	7		17 16 15 14 13 12 10 
4	9	7		18 17 16 15 14 12 10 
5	9	6		18 16 13 12 11 10 
6	9	6		25 18 17 12 10 8 
7	9	5		25 21 17 16 10 
8	9	4		20 19 16 14 
9	9	4		25 24 19 16 
10	9	4		24 22 20 19 
11	9	4		24 23 20 17 
12	9	3		24 22 21 
13	9	3		25 24 21 
14	9	2		24 21 
15	9	3		25 24 20 
16	9	2		23 22 
17	9	3		33 27 22 
18	9	4		33 32 27 24 
19	9	3		30 26 23 
20	9	5		33 32 30 29 26 
21	9	2		29 23 
22	9	4		32 30 29 26 
23	9	4		33 32 28 27 
24	9	2		30 26 
25	9	3		36 35 28 
26	9	2		36 28 
27	9	6		42 40 38 37 36 35 
28	9	3		40 34 31 
29	9	5		40 38 37 36 35 
30	9	4		42 39 38 36 
31	9	3		41 38 37 
32	9	3		41 38 37 
33	9	3		41 38 37 
34	9	5		51 43 42 41 39 
35	9	4		51 43 41 39 
36	9	5		51 49 44 43 41 
37	9	2		43 39 
38	9	5		51 49 48 47 46 
39	9	3		49 46 44 
40	9	3		48 46 43 
41	9	3		48 46 45 
42	9	3		47 46 45 
43	9	2		50 45 
44	9	2		47 45 
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
2	1	1	29	21	28	17	25	28	12	28	
	2	10	28	20	28	16	22	27	11	27	
	3	13	27	20	27	15	21	27	11	25	
	4	16	25	19	25	13	18	27	9	23	
	5	18	24	17	24	10	17	27	9	22	
	6	19	23	16	22	8	16	26	9	22	
	7	21	22	16	20	6	15	26	7	21	
	8	24	19	15	19	4	12	26	7	19	
	9	25	19	14	17	4	10	26	6	18	
3	1	4	19	16	12	30	15	20	17	29	
	2	13	19	16	10	28	14	18	14	28	
	3	14	19	15	8	24	12	18	12	27	
	4	15	19	15	8	22	11	17	12	25	
	5	20	19	14	5	20	10	16	10	25	
	6	21	18	14	5	18	9	16	9	24	
	7	22	18	13	4	17	8	16	6	23	
	8	27	18	13	3	14	8	15	5	22	
	9	29	18	13	2	13	6	14	4	21	
4	1	3	29	22	21	28	21	24	22	25	
	2	5	28	17	21	28	20	24	22	23	
	3	14	27	16	21	27	18	23	22	20	
	4	17	26	15	21	25	18	22	22	20	
	5	21	25	11	21	25	15	22	22	18	
	6	26	24	9	21	23	14	21	21	14	
	7	27	22	7	21	23	13	21	21	14	
	8	28	22	4	21	21	12	19	21	12	
	9	30	21	2	21	21	11	19	21	10	
5	1	5	5	28	20	3	27	18	27	15	
	2	9	4	26	19	3	26	18	24	14	
	3	11	4	25	19	3	26	18	22	14	
	4	15	4	22	19	3	24	18	21	13	
	5	16	3	21	18	3	24	17	16	13	
	6	18	3	21	17	3	24	17	16	13	
	7	19	3	19	17	3	23	17	13	12	
	8	21	2	18	16	3	22	16	9	12	
	9	22	2	16	15	3	21	16	8	12	
6	1	10	19	29	30	17	15	16	13	12	
	2	11	18	29	29	15	14	14	13	11	
	3	12	16	29	28	12	13	11	12	11	
	4	14	13	29	27	11	12	11	12	10	
	5	17	12	29	25	8	11	9	11	9	
	6	19	10	29	25	8	11	6	10	8	
	7	20	9	29	24	4	10	6	10	7	
	8	21	6	29	22	4	9	5	9	5	
	9	30	5	29	22	1	8	3	9	4	
7	1	2	27	19	14	15	26	26	20	16	
	2	4	24	19	14	13	26	23	19	13	
	3	7	24	17	12	12	26	22	16	12	
	4	15	19	14	12	11	26	21	15	12	
	5	16	16	13	10	10	26	18	11	10	
	6	17	16	9	10	8	25	18	9	8	
	7	23	12	7	9	5	25	16	7	8	
	8	28	9	6	7	3	25	14	7	6	
	9	29	7	2	7	2	25	12	5	5	
8	1	5	8	18	27	7	19	23	10	8	
	2	10	6	18	26	7	18	22	9	8	
	3	11	5	16	23	7	18	20	8	7	
	4	12	5	15	20	7	17	20	7	6	
	5	16	4	15	18	6	16	16	6	6	
	6	17	4	15	16	6	15	16	6	6	
	7	20	2	13	14	6	14	13	5	5	
	8	21	2	12	12	6	14	12	4	5	
	9	29	1	12	11	6	13	10	3	4	
9	1	1	28	26	19	8	25	17	22	28	
	2	2	27	22	18	6	25	14	19	28	
	3	3	23	20	14	6	24	13	18	25	
	4	9	22	18	14	5	22	13	15	24	
	5	16	18	15	11	4	21	11	14	20	
	6	17	18	15	8	4	19	10	12	18	
	7	25	15	11	6	3	18	8	10	16	
	8	26	12	9	3	2	18	7	10	16	
	9	30	10	7	2	2	16	7	8	14	
10	1	3	21	24	24	7	21	6	5	25	
	2	7	21	24	23	7	19	5	4	25	
	3	19	16	24	22	7	18	5	4	21	
	4	20	14	24	19	6	16	5	4	20	
	5	21	12	24	17	6	16	5	3	14	
	6	23	10	24	17	6	14	4	3	12	
	7	25	6	24	15	5	13	4	2	9	
	8	26	4	24	13	5	12	4	2	7	
	9	27	2	24	11	5	11	4	2	6	
11	1	2	16	13	9	27	18	13	26	15	
	2	5	14	12	8	26	17	13	22	15	
	3	6	13	10	7	26	16	13	20	15	
	4	7	9	9	5	24	15	13	18	14	
	5	14	8	9	5	23	15	13	15	13	
	6	19	6	8	4	22	14	13	14	13	
	7	23	4	7	3	20	13	13	11	13	
	8	28	2	5	2	19	11	13	8	12	
	9	29	1	5	2	19	10	13	6	12	
12	1	7	16	16	15	12	27	17	27	28	
	2	14	16	15	15	10	24	16	27	27	
	3	19	15	15	15	10	23	15	26	27	
	4	20	15	15	15	10	21	14	25	27	
	5	21	14	15	14	9	19	12	24	26	
	6	23	13	15	14	8	18	12	23	26	
	7	24	13	15	14	8	14	11	21	26	
	8	26	13	15	14	7	14	10	21	25	
	9	27	12	15	14	6	10	9	20	25	
13	1	3	25	27	12	21	10	24	6	25	
	2	7	22	24	12	20	10	23	6	23	
	3	8	21	19	12	20	9	20	6	22	
	4	10	21	16	11	20	7	17	5	22	
	5	11	20	15	10	20	7	15	5	21	
	6	12	18	10	10	19	6	13	5	20	
	7	14	16	10	10	19	5	11	5	19	
	8	16	16	4	9	19	5	9	4	18	
	9	27	14	2	9	19	4	8	4	17	
14	1	1	12	20	14	3	7	18	29	30	
	2	3	11	19	14	2	6	18	29	29	
	3	11	10	17	13	2	6	17	29	28	
	4	17	9	15	13	2	6	17	29	28	
	5	18	8	12	12	1	5	17	29	27	
	6	22	8	10	12	1	5	16	29	27	
	7	23	8	8	12	1	5	15	29	27	
	8	24	7	5	11	1	5	15	29	26	
	9	30	6	3	11	1	5	15	29	26	
15	1	2	16	20	22	24	29	22	20	25	
	2	3	13	19	21	22	24	21	17	22	
	3	4	12	18	20	22	20	19	17	20	
	4	5	11	18	19	22	17	19	16	16	
	5	6	11	17	18	21	15	16	14	15	
	6	9	9	17	17	20	13	15	13	14	
	7	12	7	17	16	20	10	14	12	10	
	8	14	6	16	14	18	7	13	11	10	
	9	25	6	16	14	18	5	11	9	6	
16	1	5	22	21	17	17	25	12	28	25	
	2	7	22	18	15	16	23	12	28	24	
	3	8	22	15	15	16	23	12	27	22	
	4	9	22	13	14	16	22	11	27	18	
	5	11	21	12	13	15	21	10	27	18	
	6	14	21	10	12	15	21	10	26	16	
	7	21	21	7	11	14	20	9	25	13	
	8	24	21	4	10	14	19	9	25	12	
	9	29	21	4	9	13	19	9	25	10	
17	1	2	17	14	22	7	22	30	24	25	
	2	3	16	12	20	6	19	25	22	25	
	3	4	15	11	17	6	19	22	21	21	
	4	12	14	11	17	4	16	19	20	20	
	5	17	13	8	14	4	14	17	20	18	
	6	18	10	7	12	3	11	12	19	16	
	7	19	9	5	7	3	9	12	17	15	
	8	20	9	4	4	2	7	7	16	12	
	9	22	8	4	4	1	6	5	16	10	
18	1	6	27	18	3	15	16	17	17	23	
	2	9	26	16	2	14	15	15	15	20	
	3	15	25	15	2	14	14	15	15	19	
	4	18	25	11	2	14	13	15	13	15	
	5	21	24	10	2	13	13	14	13	14	
	6	22	24	7	2	13	12	14	11	13	
	7	24	24	6	2	13	11	13	11	11	
	8	25	23	4	2	13	11	12	10	7	
	9	26	23	1	2	13	10	12	9	6	
19	1	1	17	24	20	18	19	12	12	3	
	2	7	16	23	19	17	17	11	12	2	
	3	9	16	23	19	16	16	11	11	2	
	4	10	15	22	18	16	15	10	9	2	
	5	16	14	21	18	16	14	10	8	2	
	6	17	14	21	18	15	13	10	8	2	
	7	19	14	21	17	15	11	9	7	2	
	8	20	12	20	17	14	11	8	6	2	
	9	21	12	20	17	14	10	8	5	2	
20	1	1	24	23	30	7	27	24	27	20	
	2	2	24	21	27	6	26	23	27	17	
	3	4	20	21	26	5	24	22	27	16	
	4	6	18	21	24	5	22	22	27	15	
	5	13	14	20	23	5	21	22	26	13	
	6	18	14	19	22	4	19	21	26	12	
	7	20	9	18	20	4	18	20	26	11	
	8	21	8	18	19	3	16	20	26	9	
	9	29	6	17	18	3	15	20	26	8	
21	1	5	27	26	6	25	28	23	15	19	
	2	7	27	25	6	22	24	22	13	15	
	3	8	27	25	5	22	23	21	12	14	
	4	13	27	25	5	21	21	20	12	14	
	5	16	27	24	4	20	20	18	10	10	
	6	24	27	24	3	18	18	18	10	9	
	7	25	27	24	3	17	16	17	9	9	
	8	28	27	24	3	16	12	15	8	6	
	9	30	27	24	2	14	12	15	7	5	
22	1	1	29	29	22	27	8	28	8	15	
	2	4	27	26	22	23	7	27	7	15	
	3	6	27	24	22	22	7	24	6	15	
	4	9	25	24	22	18	7	22	5	15	
	5	10	24	22	22	17	6	22	4	15	
	6	11	23	21	21	14	5	20	4	15	
	7	15	23	18	21	12	5	19	3	15	
	8	17	22	18	21	9	4	16	1	15	
	9	26	21	17	21	6	4	15	1	15	
23	1	2	14	28	29	14	14	26	22	23	
	2	5	14	28	28	12	14	24	19	18	
	3	12	14	28	27	11	14	23	19	18	
	4	13	14	28	26	10	14	22	17	15	
	5	16	13	28	26	10	14	22	15	14	
	6	18	13	28	26	9	13	20	13	11	
	7	19	13	28	25	8	13	19	12	8	
	8	22	12	28	24	8	13	19	10	7	
	9	24	12	28	24	7	13	18	9	5	
24	1	2	23	22	26	7	18	17	9	19	
	2	5	22	21	23	7	16	15	9	17	
	3	6	19	20	21	6	15	15	9	16	
	4	16	18	17	20	6	14	14	8	15	
	5	17	15	13	19	5	13	13	8	14	
	6	23	12	13	17	4	11	13	8	13	
	7	24	12	11	15	4	11	12	8	12	
	8	28	10	8	14	4	9	11	7	9	
	9	29	8	6	14	3	8	11	7	9	
25	1	10	18	20	26	29	26	28	24	20	
	2	16	17	16	25	28	25	24	22	20	
	3	17	16	14	25	28	23	24	22	18	
	4	20	14	14	24	28	22	22	21	16	
	5	21	13	12	22	28	22	21	20	16	
	6	24	13	9	22	27	20	18	20	13	
	7	27	12	7	20	27	20	17	18	13	
	8	28	10	5	19	27	18	16	18	11	
	9	29	9	4	19	27	18	15	17	10	
26	1	2	29	16	15	25	22	20	25	25	
	2	4	27	16	14	25	21	18	24	25	
	3	8	23	14	13	24	19	15	24	23	
	4	16	19	14	12	22	16	13	22	19	
	5	21	17	13	11	21	15	13	22	16	
	6	22	16	11	10	19	12	10	19	16	
	7	25	11	10	9	17	10	7	19	14	
	8	27	10	10	7	17	8	7	17	9	
	9	28	6	8	6	15	8	5	17	9	
27	1	1	16	18	30	22	20	13	6	6	
	2	2	13	18	29	20	18	12	5	6	
	3	5	12	18	27	20	18	11	4	5	
	4	11	12	18	27	18	16	10	4	5	
	5	12	9	18	26	18	16	10	4	4	
	6	20	8	18	25	17	13	10	3	4	
	7	22	7	18	25	16	12	9	2	3	
	8	24	4	18	23	16	11	8	2	3	
	9	26	3	18	23	15	11	8	2	3	
28	1	1	17	13	6	23	24	23	22	23	
	2	5	16	12	5	23	23	23	18	22	
	3	6	15	12	5	23	21	23	17	22	
	4	11	15	10	5	23	15	23	16	22	
	5	15	15	9	5	23	14	23	12	21	
	6	17	14	8	5	22	11	23	10	21	
	7	19	14	8	5	22	9	23	6	21	
	8	20	13	6	5	22	4	23	6	21	
	9	24	13	5	5	22	3	23	3	21	
29	1	3	11	25	12	24	14	29	17	24	
	2	7	11	23	11	24	13	24	16	21	
	3	14	11	19	10	20	13	21	15	19	
	4	18	11	18	9	17	13	18	13	17	
	5	21	11	15	8	16	13	17	10	15	
	6	24	11	15	7	15	12	11	9	12	
	7	25	11	12	5	13	12	11	8	12	
	8	26	11	11	4	8	12	7	7	8	
	9	27	11	8	3	6	12	3	5	7	
30	1	9	8	19	16	8	2	22	23	9	
	2	11	7	18	15	8	2	21	23	8	
	3	12	7	18	14	8	2	21	22	8	
	4	15	6	17	12	7	2	20	22	8	
	5	19	6	16	12	7	2	20	22	8	
	6	20	5	16	11	7	1	20	21	7	
	7	21	5	15	8	6	1	20	20	7	
	8	22	3	15	8	6	1	19	20	7	
	9	30	3	15	6	6	1	19	20	7	
31	1	5	25	26	23	4	18	23	20	19	
	2	6	24	24	23	4	18	22	20	19	
	3	7	21	22	23	3	18	18	18	19	
	4	8	15	20	23	3	18	16	18	18	
	5	9	14	15	23	3	18	16	17	18	
	6	11	11	15	22	2	18	11	16	17	
	7	14	10	13	22	2	18	11	14	17	
	8	15	7	10	22	1	18	7	13	16	
	9	17	2	5	22	1	18	5	13	16	
32	1	5	28	28	27	23	25	14	2	18	
	2	6	26	26	27	20	25	11	1	17	
	3	12	25	26	26	19	25	10	1	15	
	4	22	23	24	25	16	25	10	1	11	
	5	24	21	23	24	15	25	9	1	9	
	6	26	21	20	23	12	25	8	1	8	
	7	27	18	19	23	12	25	7	1	7	
	8	28	16	17	21	10	25	5	1	4	
	9	30	15	16	21	8	25	4	1	3	
33	1	4	18	27	19	18	24	7	30	23	
	2	5	18	23	18	17	21	7	27	20	
	3	6	17	21	18	16	18	6	24	16	
	4	7	17	18	18	16	15	5	23	14	
	5	11	15	17	18	14	13	5	20	13	
	6	18	15	15	17	12	11	4	18	10	
	7	22	14	11	17	12	9	4	15	9	
	8	27	13	11	17	11	5	3	15	6	
	9	30	13	8	17	9	2	3	11	6	
34	1	3	13	18	30	4	25	30	23	29	
	2	4	12	16	27	4	23	30	23	25	
	3	11	10	15	22	4	22	30	22	22	
	4	12	9	14	22	4	21	30	22	19	
	5	17	8	13	17	4	18	30	21	19	
	6	24	8	12	17	4	18	30	21	17	
	7	25	6	10	14	4	16	30	20	13	
	8	26	5	9	9	4	16	30	20	10	
	9	27	5	9	9	4	15	30	20	9	
35	1	2	23	25	23	19	12	21	19	10	
	2	3	23	24	23	16	12	19	19	9	
	3	4	21	20	23	15	11	19	18	8	
	4	7	20	16	22	13	9	17	16	8	
	5	9	20	16	22	12	7	17	16	6	
	6	10	19	11	22	11	7	15	16	6	
	7	14	18	9	21	9	5	14	14	5	
	8	15	16	6	21	7	5	14	14	4	
	9	22	15	4	21	6	4	13	13	4	
36	1	1	19	23	21	14	21	26	23	29	
	2	6	19	21	19	14	21	23	23	27	
	3	9	19	20	15	14	19	22	22	25	
	4	12	19	18	15	14	17	20	22	25	
	5	13	18	17	12	14	17	17	21	22	
	6	18	18	15	11	14	15	16	20	21	
	7	20	18	11	9	14	13	13	20	20	
	8	26	18	11	8	14	13	11	19	19	
	9	27	18	8	5	14	12	10	19	17	
37	1	4	25	30	26	26	19	13	21	12	
	2	9	22	24	21	24	18	13	21	10	
	3	10	19	24	21	23	15	13	21	9	
	4	15	14	19	17	22	14	13	21	7	
	5	16	11	17	17	20	10	13	21	5	
	6	17	11	15	12	19	8	13	21	5	
	7	18	7	12	11	16	8	13	21	3	
	8	20	5	12	8	15	6	13	21	3	
	9	27	2	7	8	14	3	13	21	1	
38	1	1	9	23	22	25	5	29	13	27	
	2	3	9	21	21	24	5	27	10	22	
	3	7	9	18	19	22	5	24	10	20	
	4	11	9	16	18	22	5	22	9	20	
	5	19	9	16	18	21	5	22	6	15	
	6	20	8	13	16	21	4	18	6	15	
	7	24	8	12	15	20	4	17	5	13	
	8	27	8	11	14	19	4	14	4	10	
	9	29	8	9	14	18	4	12	2	7	
39	1	3	8	16	11	15	18	23	27	21	
	2	6	6	14	10	15	17	22	22	21	
	3	8	6	14	10	15	16	20	20	20	
	4	9	6	12	8	14	16	18	18	19	
	5	15	5	11	8	14	15	17	16	18	
	6	16	4	9	6	14	14	15	12	18	
	7	21	4	9	5	13	14	14	8	16	
	8	25	2	8	4	13	13	13	8	16	
	9	27	2	7	3	13	12	10	3	15	
40	1	5	11	21	11	28	17	21	12	14	
	2	6	10	20	10	27	16	17	11	14	
	3	7	9	19	10	26	15	17	11	13	
	4	8	8	18	9	25	15	16	10	13	
	5	15	6	15	8	24	14	12	10	12	
	6	19	5	15	8	23	13	12	9	12	
	7	23	4	13	7	22	12	9	9	11	
	8	24	2	12	6	22	10	8	8	11	
	9	25	1	11	6	21	10	6	8	11	
41	1	1	15	20	19	19	14	22	18	28	
	2	3	13	20	17	19	12	21	18	27	
	3	4	12	17	17	17	12	18	17	27	
	4	6	11	13	16	13	10	18	17	27	
	5	9	9	12	15	11	9	15	16	27	
	6	13	8	10	15	9	9	12	16	26	
	7	21	5	6	15	8	7	9	15	26	
	8	25	5	4	13	7	7	7	15	26	
	9	28	3	1	13	5	6	5	15	26	
42	1	3	28	23	10	14	9	26	28	29	
	2	6	26	21	10	13	8	23	28	28	
	3	9	25	19	10	13	8	20	25	28	
	4	14	22	18	9	11	8	15	23	27	
	5	17	21	14	9	10	7	14	22	27	
	6	21	21	10	8	10	7	11	21	27	
	7	24	19	9	7	9	6	9	18	27	
	8	26	18	8	7	8	5	6	15	26	
	9	29	17	3	7	7	5	2	15	26	
43	1	11	29	26	17	15	24	11	11	18	
	2	15	29	24	15	14	23	11	9	18	
	3	17	29	24	13	14	23	11	8	14	
	4	20	29	24	12	14	22	10	6	13	
	5	21	29	23	10	14	22	10	5	12	
	6	25	28	22	8	14	21	10	4	8	
	7	27	28	22	6	14	20	9	3	6	
	8	28	28	21	5	14	20	9	3	6	
	9	29	28	21	3	14	20	9	1	3	
44	1	3	17	30	29	14	15	8	29	27	
	2	4	15	27	28	12	15	7	28	27	
	3	6	14	25	28	12	14	7	24	22	
	4	7	14	24	28	11	13	7	24	21	
	5	19	12	20	28	10	13	6	21	17	
	6	20	11	20	28	8	12	6	18	14	
	7	24	11	18	28	7	12	6	18	14	
	8	25	9	15	28	5	11	6	16	10	
	9	28	9	14	28	5	11	6	13	8	
45	1	4	6	12	14	29	13	27	21	23	
	2	6	6	12	14	28	12	26	19	22	
	3	10	6	12	13	28	12	26	16	21	
	4	21	6	12	11	27	12	25	16	21	
	5	22	6	12	11	26	12	24	14	21	
	6	23	5	12	10	26	12	24	12	20	
	7	24	5	12	8	26	12	24	9	19	
	8	25	5	12	8	25	12	23	9	19	
	9	26	5	12	7	25	12	23	6	19	
46	1	3	18	17	21	21	10	8	21	22	
	2	12	15	16	18	21	9	7	20	21	
	3	13	14	14	17	21	8	7	18	21	
	4	18	14	13	17	21	7	6	16	20	
	5	19	13	12	14	21	6	6	16	19	
	6	20	12	11	13	21	6	6	14	19	
	7	23	10	10	13	21	6	6	13	17	
	8	24	9	9	12	21	5	5	11	17	
	9	30	8	9	11	21	4	5	9	16	
47	1	1	26	16	28	29	9	23	16	27	
	2	2	26	14	27	27	9	22	13	24	
	3	3	23	13	26	26	9	18	12	22	
	4	6	20	12	24	26	9	16	12	22	
	5	8	17	12	23	24	8	15	9	19	
	6	11	14	9	21	23	8	14	9	19	
	7	21	13	8	20	23	7	11	7	17	
	8	22	9	7	20	22	7	9	6	16	
	9	30	6	6	18	21	7	9	4	15	
48	1	4	9	30	28	18	23	27	28	20	
	2	16	8	28	25	16	23	27	25	19	
	3	17	8	28	23	16	23	27	23	18	
	4	18	7	27	21	15	23	27	19	16	
	5	19	6	27	21	14	23	27	14	16	
	6	21	6	27	19	14	23	26	13	14	
	7	25	6	26	17	12	23	26	10	13	
	8	26	5	25	14	11	23	26	5	13	
	9	28	5	25	14	11	23	26	1	12	
49	1	5	30	24	11	19	18	16	18	27	
	2	6	29	23	10	18	17	15	18	27	
	3	7	28	22	9	18	17	14	18	24	
	4	9	27	22	8	18	17	13	17	22	
	5	10	27	21	7	18	16	10	17	21	
	6	16	26	19	7	18	15	10	16	18	
	7	17	25	19	7	18	14	9	15	16	
	8	18	24	18	5	18	13	7	15	15	
	9	22	24	16	5	18	13	5	15	13	
50	1	2	9	26	23	30	28	25	18	20	
	2	6	9	25	21	27	26	23	16	17	
	3	7	8	25	18	27	23	22	15	17	
	4	8	8	24	18	26	18	19	13	15	
	5	9	7	23	14	25	17	18	9	12	
	6	13	7	23	12	24	12	18	7	9	
	7	21	7	23	9	23	9	15	5	7	
	8	26	6	22	7	21	5	15	3	6	
	9	30	6	22	2	20	3	13	3	4	
51	1	4	28	28	12	23	28	24	3	28	
	2	12	26	26	11	23	27	22	2	28	
	3	13	24	26	10	20	27	21	2	28	
	4	16	22	25	9	16	26	18	2	28	
	5	21	22	25	8	13	26	16	1	28	
	6	22	20	25	6	12	25	16	1	28	
	7	27	20	24	6	8	24	13	1	28	
	8	28	17	24	5	8	24	12	1	28	
	9	29	16	23	3	6	24	10	1	28	
52	1	0	0	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	R 3	R 4	N 1	N 2	N 3	N 4
	56	63	59	52	741	796	716	812

************************************************************************
