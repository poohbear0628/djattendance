jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 4 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	14		2 3 5 6 7 8 9 10 12 14 15 16 18 20 
2	6	2		13 4 
3	6	6		31 25 22 19 17 11 
4	6	5		31 25 22 17 11 
5	6	5		31 26 25 17 11 
6	6	5		31 23 22 17 11 
7	6	5		28 25 22 17 13 
8	6	5		31 25 22 19 11 
9	6	8		35 31 29 28 25 22 19 17 
10	6	4		28 25 17 13 
11	6	10		40 39 35 32 30 29 28 27 24 21 
12	6	9		41 35 32 31 29 27 25 24 22 
13	6	7		40 35 29 27 24 21 19 
14	6	5		32 29 28 22 17 
15	6	5		34 32 29 25 17 
16	6	4		40 28 24 19 
17	6	8		41 40 39 38 37 30 27 24 
18	6	7		50 41 40 38 37 33 28 
19	6	10		51 50 48 45 39 37 36 34 32 30 
20	6	7		51 48 38 35 31 30 27 
21	6	10		51 50 49 47 41 38 37 36 34 33 
22	6	5		40 39 38 37 30 
23	6	9		51 50 49 48 47 46 44 43 42 
24	6	7		51 49 48 45 44 36 33 
25	6	7		51 48 46 45 43 39 37 
26	6	7		50 49 48 47 46 45 36 
27	6	6		50 49 47 45 44 33 
28	6	5		51 47 46 36 34 
29	6	7		50 49 48 46 44 43 42 
30	6	6		49 47 46 44 43 42 
31	6	5		46 45 44 43 42 
32	6	4		47 46 43 42 
33	6	2		43 42 
34	6	2		44 43 
35	6	2		45 43 
36	6	1		42 
37	6	1		42 
38	6	1		45 
39	6	1		44 
40	6	1		48 
41	6	1		44 
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
2	1	7	1	4	4	5	22	15	
	2	9	1	4	4	4	21	15	
	3	10	1	4	4	3	18	14	
	4	12	1	4	4	3	13	14	
	5	26	1	3	4	2	6	12	
	6	28	1	3	4	2	5	12	
3	1	1	3	4	4	5	29	18	
	2	10	2	4	4	4	25	15	
	3	12	2	4	3	3	21	10	
	4	22	1	4	3	3	20	9	
	5	24	1	4	1	3	18	6	
	6	25	1	4	1	2	13	1	
4	1	1	1	4	3	2	24	28	
	2	2	1	4	3	1	24	23	
	3	6	1	4	3	1	23	21	
	4	7	1	4	2	1	23	20	
	5	11	1	4	2	1	23	14	
	6	19	1	4	2	1	22	13	
5	1	3	4	4	3	4	16	22	
	2	5	4	3	2	3	13	22	
	3	7	4	2	2	3	9	18	
	4	15	4	2	2	3	7	15	
	5	24	4	1	2	3	7	10	
	6	27	4	1	2	3	3	8	
6	1	6	4	4	4	4	21	15	
	2	8	3	3	4	3	19	14	
	3	9	3	3	4	3	17	13	
	4	15	3	3	3	2	15	13	
	5	20	3	3	3	2	13	10	
	6	24	3	3	2	2	12	9	
7	1	3	4	5	5	4	19	26	
	2	4	4	4	4	3	15	23	
	3	17	3	4	4	2	14	17	
	4	18	2	4	4	2	12	17	
	5	19	2	3	3	2	8	13	
	6	23	1	3	3	1	5	7	
8	1	3	2	2	3	5	16	24	
	2	5	2	2	3	4	11	19	
	3	20	2	2	3	4	11	15	
	4	21	2	2	3	4	8	13	
	5	23	2	2	3	3	4	6	
	6	24	2	2	3	3	4	4	
9	1	1	5	4	3	3	20	21	
	2	7	4	4	3	3	16	17	
	3	8	4	4	3	2	12	17	
	4	9	4	4	3	2	11	15	
	5	14	4	4	3	1	9	14	
	6	29	4	4	3	1	4	12	
10	1	1	3	3	1	4	14	22	
	2	5	2	2	1	4	14	18	
	3	16	2	2	1	4	14	13	
	4	18	1	2	1	4	13	9	
	5	20	1	2	1	3	13	8	
	6	27	1	2	1	3	13	5	
11	1	2	5	4	5	4	23	11	
	2	7	5	4	4	4	21	11	
	3	12	5	4	4	4	20	11	
	4	16	5	3	4	4	18	11	
	5	21	5	3	4	3	16	11	
	6	26	5	3	4	3	13	11	
12	1	5	4	3	4	3	1	25	
	2	9	3	2	3	2	1	21	
	3	10	2	2	3	2	1	20	
	4	15	2	1	3	2	1	18	
	5	16	2	1	2	1	1	14	
	6	18	1	1	2	1	1	14	
13	1	10	1	4	2	3	18	7	
	2	19	1	4	2	3	15	7	
	3	21	1	4	2	3	11	7	
	4	22	1	4	2	3	9	7	
	5	23	1	4	2	3	7	7	
	6	27	1	4	2	3	5	7	
14	1	5	3	2	2	4	27	27	
	2	6	3	1	2	3	25	23	
	3	10	3	1	2	3	24	19	
	4	20	2	1	2	3	20	13	
	5	22	2	1	1	2	17	13	
	6	26	2	1	1	2	16	5	
15	1	1	4	4	4	2	24	15	
	2	2	4	3	4	1	20	14	
	3	8	3	3	4	1	13	12	
	4	9	2	2	4	1	11	12	
	5	19	1	2	4	1	9	11	
	6	26	1	1	4	1	4	10	
16	1	1	4	2	4	3	23	18	
	2	4	4	1	3	3	22	16	
	3	7	4	1	3	3	19	12	
	4	8	3	1	3	3	18	10	
	5	24	2	1	2	3	16	9	
	6	25	2	1	2	3	15	8	
17	1	2	1	5	5	2	13	21	
	2	8	1	4	4	2	11	21	
	3	11	1	4	3	2	11	21	
	4	15	1	4	3	2	9	20	
	5	21	1	4	1	2	7	20	
	6	28	1	4	1	2	5	20	
18	1	6	1	4	5	2	9	25	
	2	12	1	4	4	2	8	23	
	3	15	1	4	4	2	8	20	
	4	18	1	4	4	1	7	19	
	5	23	1	3	4	1	7	17	
	6	24	1	3	4	1	7	15	
19	1	3	2	3	4	4	28	7	
	2	7	2	2	4	3	28	6	
	3	18	2	2	3	3	27	5	
	4	20	2	2	3	3	25	4	
	5	24	1	2	1	3	24	4	
	6	27	1	2	1	3	24	3	
20	1	2	3	4	2	5	24	18	
	2	6	2	3	1	4	20	15	
	3	9	2	3	1	4	15	15	
	4	15	2	2	1	4	13	13	
	5	20	1	1	1	4	8	10	
	6	27	1	1	1	4	4	10	
21	1	4	3	5	4	2	14	15	
	2	8	2	4	4	2	13	15	
	3	10	2	4	4	2	13	13	
	4	20	1	3	3	2	13	13	
	5	25	1	3	2	2	13	10	
	6	28	1	3	2	2	13	9	
22	1	6	2	4	5	4	13	24	
	2	12	2	4	4	3	11	19	
	3	13	2	3	4	2	8	13	
	4	18	2	3	4	2	5	9	
	5	20	2	2	4	1	4	9	
	6	29	2	1	4	1	1	5	
23	1	16	2	3	3	4	23	8	
	2	17	2	2	3	3	18	7	
	3	18	2	2	3	3	14	7	
	4	19	2	2	2	3	12	6	
	5	21	2	2	2	3	9	6	
	6	25	2	2	1	3	7	6	
24	1	8	4	2	4	4	12	25	
	2	13	3	2	4	3	10	23	
	3	17	3	2	4	3	9	19	
	4	19	3	2	4	3	7	18	
	5	26	3	1	4	3	7	15	
	6	27	3	1	4	3	6	14	
25	1	9	4	4	5	5	27	21	
	2	21	4	4	5	3	25	20	
	3	22	3	3	5	3	23	17	
	4	27	3	2	5	3	20	17	
	5	29	1	1	5	1	18	16	
	6	30	1	1	5	1	18	14	
26	1	2	4	3	5	2	20	12	
	2	8	4	3	4	2	19	10	
	3	9	4	3	4	2	17	8	
	4	12	4	2	4	2	15	8	
	5	13	4	2	3	2	13	7	
	6	23	4	2	3	2	10	5	
27	1	2	3	1	2	2	27	19	
	2	4	3	1	2	2	25	16	
	3	12	3	1	2	2	22	15	
	4	21	3	1	2	2	21	12	
	5	26	3	1	2	2	18	10	
	6	27	3	1	2	2	18	7	
28	1	4	4	3	4	5	18	7	
	2	5	4	2	3	4	14	6	
	3	14	4	2	3	3	11	6	
	4	19	4	2	2	3	8	6	
	5	26	4	1	2	3	7	6	
	6	30	4	1	2	2	3	6	
29	1	9	3	5	4	2	23	12	
	2	13	3	4	4	2	22	12	
	3	20	3	4	4	2	16	11	
	4	23	3	3	4	2	13	9	
	5	27	3	2	3	2	12	7	
	6	28	3	2	3	2	8	6	
30	1	3	2	4	5	4	29	27	
	2	6	2	4	4	4	28	22	
	3	11	2	3	4	4	28	20	
	4	20	2	2	4	4	27	19	
	5	21	1	2	3	4	27	14	
	6	24	1	1	3	4	27	10	
31	1	3	2	3	3	4	20	12	
	2	7	2	3	3	4	19	9	
	3	10	2	3	2	4	19	9	
	4	17	2	3	2	4	18	6	
	5	21	2	3	2	4	18	5	
	6	22	2	3	1	4	17	5	
32	1	3	4	3	4	5	22	27	
	2	7	4	2	3	4	18	25	
	3	14	4	2	3	3	18	25	
	4	15	4	2	3	2	17	24	
	5	18	4	2	2	2	15	22	
	6	19	4	2	2	1	13	21	
33	1	5	4	3	4	3	11	26	
	2	14	3	2	4	3	11	23	
	3	19	3	2	4	3	11	19	
	4	20	3	2	4	2	11	16	
	5	21	2	1	4	1	10	13	
	6	28	2	1	4	1	10	12	
34	1	7	4	4	5	1	21	9	
	2	8	3	4	4	1	17	7	
	3	9	3	4	3	1	17	7	
	4	16	3	3	3	1	14	5	
	5	26	2	3	2	1	13	5	
	6	27	1	2	2	1	9	4	
35	1	6	2	2	5	3	17	9	
	2	8	2	2	5	3	14	8	
	3	9	2	2	5	3	12	7	
	4	15	2	2	5	3	8	5	
	5	20	2	1	5	3	5	5	
	6	29	2	1	5	3	1	4	
36	1	3	3	5	2	3	18	26	
	2	7	2	4	2	2	14	25	
	3	16	2	3	2	2	12	25	
	4	23	1	3	1	2	10	25	
	5	24	1	2	1	2	8	25	
	6	27	1	2	1	2	6	25	
37	1	4	1	5	1	4	20	13	
	2	5	1	4	1	4	19	10	
	3	8	1	4	1	4	16	9	
	4	10	1	4	1	3	16	9	
	5	14	1	4	1	2	13	6	
	6	15	1	4	1	2	12	4	
38	1	3	5	4	5	4	20	25	
	2	6	4	3	5	3	20	24	
	3	9	4	3	5	3	19	19	
	4	12	3	3	5	3	19	18	
	5	23	3	3	5	3	19	15	
	6	26	2	3	5	3	18	12	
39	1	2	3	4	3	3	25	20	
	2	3	2	3	2	2	23	15	
	3	6	2	2	2	2	22	14	
	4	25	2	2	2	2	22	10	
	5	26	2	2	1	2	19	10	
	6	27	2	1	1	2	19	6	
40	1	3	3	3	5	4	29	26	
	2	4	3	3	4	4	27	23	
	3	6	3	3	4	4	24	19	
	4	7	3	2	4	4	21	16	
	5	10	3	2	4	4	16	10	
	6	26	3	2	4	4	15	8	
41	1	3	3	4	1	5	22	15	
	2	10	3	4	1	4	18	12	
	3	15	2	4	1	4	17	12	
	4	18	2	4	1	4	15	10	
	5	21	1	4	1	3	13	8	
	6	22	1	4	1	3	12	8	
42	1	2	5	3	5	3	10	28	
	2	3	4	3	4	2	10	27	
	3	12	4	3	4	2	10	26	
	4	13	3	3	4	2	9	27	
	5	19	3	3	4	1	9	27	
	6	23	3	3	4	1	8	27	
43	1	6	3	3	1	3	2	28	
	2	11	3	3	1	3	2	23	
	3	21	3	3	1	2	2	19	
	4	24	3	3	1	2	2	16	
	5	29	3	2	1	1	2	14	
	6	30	3	2	1	1	2	10	
44	1	4	3	3	3	2	8	15	
	2	5	3	3	3	2	8	14	
	3	8	3	3	3	2	8	12	
	4	9	3	2	3	2	8	11	
	5	23	3	1	3	1	8	11	
	6	26	3	1	3	1	8	9	
45	1	1	3	4	3	1	25	17	
	2	5	2	4	3	1	20	16	
	3	10	2	4	2	1	18	16	
	4	16	1	4	2	1	15	15	
	5	17	1	3	1	1	13	15	
	6	24	1	3	1	1	12	14	
46	1	3	3	4	3	2	16	20	
	2	4	3	4	3	2	16	17	
	3	6	3	3	3	2	16	15	
	4	17	3	3	3	2	16	14	
	5	29	3	2	3	2	16	12	
	6	30	3	2	3	2	16	11	
47	1	10	4	2	5	3	14	5	
	2	13	3	1	5	3	12	4	
	3	19	3	1	5	3	11	4	
	4	20	2	1	5	3	9	3	
	5	22	1	1	5	3	5	2	
	6	23	1	1	5	3	4	2	
48	1	5	5	3	3	3	22	22	
	2	6	4	3	2	3	21	17	
	3	7	4	3	2	3	20	15	
	4	9	4	3	2	3	20	13	
	5	15	4	2	1	2	18	9	
	6	20	4	2	1	2	17	3	
49	1	3	1	4	4	5	22	24	
	2	25	1	4	3	4	19	24	
	3	26	1	4	2	4	16	23	
	4	28	1	4	2	4	16	22	
	5	29	1	4	2	4	11	20	
	6	30	1	4	1	4	10	19	
50	1	2	4	2	4	4	2	25	
	2	15	4	2	3	4	2	21	
	3	17	4	2	3	4	2	20	
	4	27	4	1	2	3	2	19	
	5	29	4	1	2	2	2	18	
	6	30	4	1	2	2	2	16	
51	1	6	4	3	1	3	14	12	
	2	8	3	3	1	3	13	8	
	3	10	2	3	1	3	13	7	
	4	23	2	3	1	2	11	5	
	5	24	2	3	1	2	10	4	
	6	30	1	3	1	2	10	1	
52	1	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	R 3	R 4	N 1	N 2
	35	38	37	41	829	823

************************************************************************
