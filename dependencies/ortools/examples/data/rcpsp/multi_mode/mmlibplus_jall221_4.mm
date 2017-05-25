jobs  (incl. supersource/sink ):	52
RESOURCES
- renewable                 : 2 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	19		2 3 4 5 6 7 8 9 10 12 14 15 16 18 19 23 24 28 33 
2	9	6		51 48 47 21 13 11 
3	9	9		51 49 46 32 30 29 26 25 11 
4	9	11		49 48 47 43 38 36 32 31 30 26 22 
5	9	11		50 48 47 46 38 36 32 31 30 25 22 
6	9	7		45 36 32 30 25 22 21 
7	9	12		49 46 42 39 38 37 36 31 30 29 26 25 
8	9	9		50 48 47 46 43 40 38 29 17 
9	9	11		48 47 45 42 41 38 37 36 31 25 20 
10	9	4		51 32 30 11 
11	9	11		45 44 43 41 40 39 38 37 36 34 27 
12	9	10		51 45 42 41 38 37 36 35 29 25 
13	9	10		50 49 41 39 38 37 36 35 34 26 
14	9	11		47 43 42 41 40 39 38 37 36 35 34 
15	9	10		49 48 47 41 40 37 36 35 34 29 
16	9	9		46 45 42 41 38 37 36 35 25 
17	9	7		42 41 39 37 36 34 31 
18	9	6		48 42 39 36 35 25 
19	9	7		50 45 40 38 37 35 34 
20	9	6		44 43 40 39 35 34 
21	9	5		46 38 35 34 29 
22	9	5		42 41 40 39 37 
23	9	5		39 38 37 36 35 
24	9	4		44 41 38 36 
25	9	2		43 34 
26	9	2		45 40 
27	9	2		42 35 
28	9	2		40 34 
29	9	1		44 
30	9	1		34 
31	9	1		35 
32	9	1		39 
33	9	1		34 
34	9	1		52 
35	9	1		52 
36	9	1		52 
37	9	1		52 
38	9	1		52 
39	9	1		52 
40	9	1		52 
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
jobnr.	mode	dur	R1	R2	N1	N2	
------------------------------------------------------------------------
1	1	0	0	0	0	0	
2	1	1	4	2	25	18	
	2	3	4	2	23	16	
	3	7	3	2	21	16	
	4	16	3	2	19	15	
	5	17	2	2	17	14	
	6	22	2	1	15	12	
	7	23	1	1	14	11	
	8	28	1	1	10	11	
	9	30	1	1	9	10	
3	1	1	3	2	19	14	
	2	2	3	1	18	12	
	3	5	3	1	17	12	
	4	11	3	1	15	10	
	5	14	3	1	15	9	
	6	16	3	1	12	10	
	7	17	3	1	12	9	
	8	21	3	1	9	8	
	9	25	3	1	8	7	
4	1	7	4	3	19	20	
	2	8	3	2	17	18	
	3	11	3	2	17	16	
	4	14	2	2	15	14	
	5	16	2	2	13	11	
	6	20	2	2	12	11	
	7	21	2	2	10	9	
	8	22	1	2	9	8	
	9	26	1	2	7	6	
5	1	1	2	5	29	19	
	2	2	2	4	27	19	
	3	6	2	4	24	18	
	4	7	2	3	23	18	
	5	8	2	3	21	18	
	6	9	2	2	20	17	
	7	13	2	1	16	16	
	8	19	2	1	16	15	
	9	28	2	1	14	16	
6	1	1	5	4	26	7	
	2	4	4	4	24	6	
	3	5	4	4	21	5	
	4	7	4	3	16	4	
	5	10	4	3	14	3	
	6	13	4	2	10	3	
	7	19	4	1	7	3	
	8	20	4	1	4	2	
	9	25	4	1	4	1	
7	1	3	2	4	26	28	
	2	4	1	4	25	25	
	3	5	1	4	23	24	
	4	6	1	3	22	21	
	5	13	1	2	18	21	
	6	17	1	2	17	18	
	7	24	1	2	15	17	
	8	25	1	1	14	14	
	9	27	1	1	13	12	
8	1	3	2	4	11	27	
	2	5	1	4	10	26	
	3	6	1	4	9	25	
	4	8	1	4	9	23	
	5	14	1	4	9	22	
	6	20	1	4	8	20	
	7	23	1	4	8	19	
	8	24	1	4	7	18	
	9	29	1	4	7	17	
9	1	1	4	2	23	27	
	2	2	4	2	21	26	
	3	8	4	2	19	24	
	4	13	4	2	14	24	
	5	14	4	2	14	23	
	6	16	4	2	11	21	
	7	22	4	2	6	20	
	8	25	4	2	5	20	
	9	27	4	2	2	19	
10	1	6	3	1	23	25	
	2	11	3	1	21	24	
	3	12	3	1	20	24	
	4	14	3	1	18	24	
	5	17	2	1	17	23	
	6	23	2	1	13	23	
	7	24	2	1	10	22	
	8	25	1	1	8	22	
	9	26	1	1	8	21	
11	1	3	5	4	19	23	
	2	5	4	4	18	21	
	3	7	4	4	17	20	
	4	16	4	4	15	18	
	5	19	3	4	14	18	
	6	24	3	4	13	16	
	7	27	2	4	12	14	
	8	28	2	4	11	13	
	9	29	2	4	10	13	
12	1	1	4	5	22	22	
	2	6	4	4	22	19	
	3	8	4	4	21	16	
	4	12	4	4	19	16	
	5	17	3	4	19	14	
	6	20	3	4	18	13	
	7	23	3	4	16	10	
	8	28	2	4	15	8	
	9	29	2	4	15	6	
13	1	2	4	2	7	24	
	2	4	4	2	7	23	
	3	8	4	2	7	22	
	4	9	4	2	7	21	
	5	10	4	1	7	22	
	6	14	3	1	7	22	
	7	16	3	1	7	21	
	8	19	3	1	7	20	
	9	30	3	1	7	19	
14	1	1	3	5	26	15	
	2	2	3	4	25	13	
	3	3	3	4	24	11	
	4	13	3	4	22	11	
	5	14	3	4	20	10	
	6	15	3	3	17	9	
	7	19	3	3	16	7	
	8	21	3	3	14	7	
	9	24	3	3	10	6	
15	1	3	2	3	27	18	
	2	4	2	2	26	16	
	3	5	2	2	25	15	
	4	6	2	2	24	11	
	5	7	1	2	23	9	
	6	16	1	2	23	7	
	7	23	1	2	21	7	
	8	25	1	2	20	5	
	9	29	1	2	20	2	
16	1	1	4	4	25	7	
	2	1	4	4	22	8	
	3	2	4	4	22	7	
	4	4	4	4	20	7	
	5	9	3	4	18	6	
	6	17	3	4	16	6	
	7	21	3	4	15	5	
	8	24	2	4	14	5	
	9	26	2	4	12	5	
17	1	1	4	4	13	27	
	2	2	3	4	12	26	
	3	3	3	4	11	26	
	4	4	3	3	9	26	
	5	6	2	3	8	25	
	6	8	2	2	6	24	
	7	10	2	2	6	23	
	8	13	2	1	4	22	
	9	22	2	1	3	22	
18	1	1	2	4	8	26	
	2	10	2	3	8	24	
	3	11	2	3	8	23	
	4	18	2	3	8	20	
	5	19	2	2	8	19	
	6	20	1	2	7	17	
	7	23	1	2	7	14	
	8	25	1	2	7	12	
	9	30	1	2	7	11	
19	1	3	4	2	24	12	
	2	8	3	1	23	12	
	3	9	3	1	23	11	
	4	10	3	1	22	12	
	5	12	3	1	22	11	
	6	13	2	1	21	12	
	7	18	2	1	21	11	
	8	19	2	1	20	12	
	9	27	2	1	19	12	
20	1	2	5	5	29	22	
	2	3	4	4	27	22	
	3	6	4	4	25	22	
	4	10	3	4	25	22	
	5	13	3	3	23	21	
	6	17	3	3	22	21	
	7	18	3	3	19	21	
	8	19	2	3	19	21	
	9	29	2	3	17	21	
21	1	1	1	3	21	7	
	2	2	1	3	21	5	
	3	4	1	3	19	5	
	4	10	1	3	17	5	
	5	11	1	3	13	4	
	6	14	1	2	13	3	
	7	21	1	2	11	3	
	8	22	1	2	7	1	
	9	23	1	2	6	1	
22	1	7	3	5	30	25	
	2	8	3	5	27	24	
	3	16	3	5	24	24	
	4	21	3	5	24	22	
	5	22	3	5	22	21	
	6	23	3	5	18	21	
	7	26	3	5	18	20	
	8	28	3	5	15	19	
	9	29	3	5	13	18	
23	1	1	4	2	19	21	
	2	3	4	2	19	19	
	3	7	4	2	19	17	
	4	8	4	2	19	15	
	5	11	4	1	19	12	
	6	13	4	1	19	11	
	7	14	4	1	19	10	
	8	15	4	1	19	7	
	9	19	4	1	19	6	
24	1	6	5	3	21	20	
	2	9	4	2	21	16	
	3	10	4	2	20	15	
	4	11	3	2	18	13	
	5	16	3	2	17	12	
	6	21	3	2	15	8	
	7	22	3	2	12	6	
	8	25	2	2	11	4	
	9	28	2	2	10	4	
25	1	1	3	4	26	27	
	2	4	2	4	26	25	
	3	7	2	4	26	19	
	4	9	2	4	26	16	
	5	12	1	4	25	16	
	6	14	1	4	25	10	
	7	18	1	4	25	9	
	8	23	1	4	25	4	
	9	26	1	4	25	2	
26	1	5	1	1	27	4	
	2	10	1	1	26	3	
	3	13	1	1	24	3	
	4	16	1	1	24	2	
	5	17	1	1	20	3	
	6	21	1	1	20	2	
	7	24	1	1	17	3	
	8	27	1	1	16	3	
	9	30	1	1	15	3	
27	1	1	5	3	26	24	
	2	4	5	3	24	23	
	3	6	5	3	23	23	
	4	9	5	3	18	23	
	5	14	5	2	15	23	
	6	15	5	2	13	23	
	7	16	5	2	12	23	
	8	23	5	1	7	23	
	9	29	5	1	6	23	
28	1	1	4	2	25	24	
	2	3	4	2	22	24	
	3	6	4	2	20	23	
	4	8	3	2	16	21	
	5	11	2	2	13	20	
	6	12	2	1	12	20	
	7	14	1	1	11	19	
	8	23	1	1	6	17	
	9	28	1	1	6	16	
29	1	4	2	5	13	10	
	2	7	2	4	13	9	
	3	8	2	4	13	8	
	4	22	2	4	13	7	
	5	23	2	3	13	9	
	6	25	1	3	13	9	
	7	27	1	2	13	10	
	8	28	1	2	13	9	
	9	30	1	2	13	8	
30	1	2	3	5	23	22	
	2	5	3	4	20	21	
	3	8	3	4	17	21	
	4	10	3	4	16	21	
	5	11	3	3	14	21	
	6	15	3	3	10	21	
	7	18	3	2	10	21	
	8	28	3	2	7	21	
	9	29	3	2	3	21	
31	1	1	3	4	18	27	
	2	6	3	3	15	25	
	3	7	3	3	14	22	
	4	11	3	3	12	20	
	5	14	2	3	12	17	
	6	21	2	2	9	14	
	7	24	2	2	7	13	
	8	26	2	2	6	9	
	9	28	2	2	5	6	
32	1	5	5	3	18	22	
	2	9	4	3	18	21	
	3	10	4	3	17	20	
	4	15	4	3	17	19	
	5	16	3	2	16	17	
	6	17	3	2	16	15	
	7	22	3	2	15	14	
	8	23	3	2	15	13	
	9	27	3	2	15	12	
33	1	7	1	5	26	22	
	2	8	1	4	26	19	
	3	9	1	4	26	18	
	4	15	1	4	26	16	
	5	16	1	4	25	13	
	6	17	1	3	25	11	
	7	23	1	3	25	7	
	8	28	1	3	25	5	
	9	29	1	3	25	3	
34	1	4	4	4	29	26	
	2	5	3	4	28	23	
	3	6	3	4	27	22	
	4	7	3	4	26	22	
	5	10	2	4	24	20	
	6	13	2	4	23	18	
	7	14	2	4	22	15	
	8	27	2	4	19	13	
	9	30	2	4	19	12	
35	1	1	1	3	20	23	
	2	6	1	3	19	20	
	3	17	1	3	18	19	
	4	18	1	3	17	18	
	5	19	1	3	16	18	
	6	24	1	3	16	16	
	7	25	1	3	16	15	
	8	28	1	3	14	15	
	9	29	1	3	14	14	
36	1	10	3	4	30	22	
	2	11	3	4	29	20	
	3	14	3	4	28	19	
	4	19	3	4	26	18	
	5	22	3	4	26	16	
	6	24	2	4	24	15	
	7	25	2	4	23	12	
	8	27	2	4	22	11	
	9	28	2	4	22	9	
37	1	2	1	3	20	18	
	2	4	1	2	19	19	
	3	5	1	2	19	18	
	4	6	1	2	18	17	
	5	7	1	2	18	16	
	6	10	1	2	18	15	
	7	15	1	2	18	14	
	8	16	1	2	17	15	
	9	25	1	2	17	14	
38	1	2	3	5	15	25	
	2	3	2	5	12	22	
	3	5	2	5	11	22	
	4	14	2	5	9	21	
	5	18	2	5	8	19	
	6	20	1	5	6	18	
	7	24	1	5	4	15	
	8	26	1	5	4	13	
	9	27	1	5	1	12	
39	1	6	4	4	13	24	
	2	7	3	3	12	23	
	3	8	3	3	11	22	
	4	10	3	3	10	22	
	5	12	3	2	10	21	
	6	13	2	2	9	21	
	7	14	2	2	8	21	
	8	16	2	1	6	20	
	9	29	2	1	6	19	
40	1	11	5	5	28	27	
	2	14	4	4	27	25	
	3	21	4	4	26	24	
	4	22	3	4	23	23	
	5	23	3	3	21	22	
	6	24	3	3	20	22	
	7	25	3	3	20	21	
	8	28	2	3	17	19	
	9	30	2	3	17	18	
41	1	2	5	1	21	5	
	2	6	4	1	19	4	
	3	7	4	1	19	3	
	4	9	3	1	17	3	
	5	12	3	1	16	2	
	6	20	2	1	13	2	
	7	21	1	1	12	1	
	8	26	1	1	10	1	
	9	28	1	1	9	1	
42	1	12	4	1	15	29	
	2	17	4	1	15	28	
	3	18	4	1	15	26	
	4	19	3	1	15	25	
	5	22	3	1	15	24	
	6	24	3	1	15	23	
	7	25	3	1	15	22	
	8	27	2	1	15	21	
	9	30	2	1	15	20	
43	1	2	5	3	8	13	
	2	4	5	2	7	13	
	3	5	5	2	7	12	
	4	6	5	2	7	11	
	5	7	5	2	7	9	
	6	10	5	1	7	9	
	7	17	5	1	7	8	
	8	21	5	1	7	7	
	9	27	5	1	7	6	
44	1	3	4	5	25	18	
	2	5	3	4	25	16	
	3	7	3	4	22	14	
	4	9	2	3	20	13	
	5	20	2	2	18	11	
	6	22	2	2	17	9	
	7	23	1	1	14	8	
	8	26	1	1	11	7	
	9	29	1	1	10	6	
45	1	3	3	1	25	27	
	2	5	3	1	24	26	
	3	6	3	1	24	25	
	4	12	3	1	23	24	
	5	23	3	1	22	24	
	6	24	3	1	22	23	
	7	26	3	1	21	22	
	8	27	3	1	21	20	
	9	29	3	1	21	19	
46	1	1	4	2	23	26	
	2	4	3	1	21	25	
	3	8	3	1	20	22	
	4	11	3	1	19	20	
	5	14	3	1	18	20	
	6	17	3	1	15	18	
	7	22	3	1	14	15	
	8	28	3	1	12	12	
	9	30	3	1	12	11	
47	1	2	5	5	18	6	
	2	3	4	4	17	5	
	3	4	4	4	16	5	
	4	6	4	4	15	5	
	5	7	4	3	14	5	
	6	8	4	3	14	4	
	7	9	4	3	13	4	
	8	13	4	3	13	3	
	9	17	4	3	12	4	
48	1	2	4	4	16	11	
	2	10	4	3	15	10	
	3	16	4	3	15	9	
	4	17	4	3	13	8	
	5	19	3	3	13	8	
	6	20	3	3	12	7	
	7	22	3	3	10	7	
	8	24	3	3	9	6	
	9	29	3	3	9	5	
49	1	5	3	1	26	20	
	2	8	3	1	22	20	
	3	11	3	1	19	20	
	4	17	3	1	17	19	
	5	21	2	1	14	19	
	6	24	2	1	13	18	
	7	25	1	1	11	18	
	8	26	1	1	8	17	
	9	27	1	1	6	17	
50	1	2	1	4	11	11	
	2	5	1	3	9	11	
	3	7	1	3	9	10	
	4	12	1	3	8	10	
	5	15	1	2	7	10	
	6	23	1	2	7	9	
	7	25	1	2	6	9	
	8	27	1	1	6	9	
	9	28	1	1	5	9	
51	1	2	2	5	23	8	
	2	3	1	4	21	7	
	3	6	1	4	19	6	
	4	7	1	4	18	4	
	5	8	1	3	15	4	
	6	11	1	3	15	3	
	7	15	1	2	13	3	
	8	27	1	2	12	2	
	9	28	1	2	11	1	
52	1	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	N 1	N 2
	33	33	813	765

************************************************************************
