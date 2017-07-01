jobs  (incl. supersource/sink ):	102
RESOURCES
- renewable                 : 4 R
- nonrenewable              : 4 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	10		2 3 4 5 6 7 8 9 10 11 
2	9	11		30 27 25 22 21 19 18 17 16 15 14 
3	9	10		27 25 22 21 20 19 18 16 14 13 
4	9	7		21 20 19 16 15 14 12 
5	9	6		30 28 25 21 20 16 
6	9	6		29 28 22 21 16 13 
7	9	5		30 29 28 21 16 
8	9	2		20 16 
9	9	5		31 28 27 22 20 
10	9	5		34 30 26 23 20 
11	9	6		36 34 32 28 26 24 
12	9	7		38 34 33 31 30 29 28 
13	9	6		35 34 32 30 26 24 
14	9	7		38 37 34 33 31 29 28 
15	9	5		34 33 29 28 24 
16	9	4		35 34 26 24 
17	9	3		35 34 20 
18	9	5		41 37 35 33 29 
19	9	9		46 44 41 40 39 38 37 36 33 
20	9	3		43 32 29 
21	9	7		44 43 41 40 37 36 35 
22	9	5		44 37 36 34 33 
23	9	3		46 38 29 
24	9	7		49 44 42 41 39 38 37 
25	9	7		49 44 42 41 40 37 35 
26	9	4		44 40 33 31 
27	9	4		40 36 35 33 
28	9	5		43 42 41 40 35 
29	9	4		44 40 39 36 
30	9	6		50 49 44 41 40 37 
31	9	6		48 47 46 45 43 42 
32	9	6		58 50 48 47 46 41 
33	9	5		49 48 45 43 42 
34	9	5		49 48 47 41 40 
35	9	9		58 57 55 53 51 48 47 46 45 
36	9	4		52 49 45 42 
37	9	8		58 57 55 54 53 51 47 45 
38	9	5		57 55 54 45 43 
39	9	7		58 57 55 54 51 47 45 
40	9	7		60 58 54 53 52 51 45 
41	9	7		60 57 55 54 53 51 45 
42	9	9		69 63 60 58 57 55 54 51 50 
43	9	6		60 56 53 52 51 50 
44	9	6		69 63 58 57 51 48 
45	9	7		67 66 65 63 62 59 56 
46	9	9		71 69 66 65 64 63 62 61 59 
47	9	7		69 66 65 64 61 60 52 
48	9	5		74 71 66 64 54 
49	9	10		77 74 72 71 70 69 66 65 62 60 
50	9	7		74 71 70 66 65 61 59 
51	9	6		74 71 70 64 61 59 
52	9	8		78 77 74 73 72 71 70 62 
53	9	7		77 74 71 70 69 67 65 
54	9	4		70 65 62 59 
55	9	5		74 72 70 64 61 
56	9	4		74 71 64 61 
57	9	7		80 78 77 75 74 73 70 
58	9	4		77 76 68 67 
59	9	7		92 84 80 79 77 75 72 
60	9	6		80 79 78 76 73 68 
61	9	8		92 84 83 80 79 76 75 73 
62	9	5		84 82 79 76 68 
63	9	5		82 81 80 74 70 
64	9	5		84 82 79 78 68 
65	9	4		80 78 75 73 
66	9	3		80 79 68 
67	9	11		101 100 91 88 85 84 83 82 81 80 78 
68	9	6		100 92 90 85 83 75 
69	9	5		100 90 88 85 75 
70	9	9		101 97 92 91 90 87 85 84 79 
71	9	9		101 100 99 97 91 86 85 81 80 
72	9	7		101 100 99 96 87 82 76 
73	9	10		101 100 99 96 90 88 87 86 85 82 
74	9	4		96 87 84 76 
75	9	8		101 99 97 95 91 87 86 81 
76	9	5		98 90 88 86 85 
77	9	4		95 89 88 83 
78	9	6		98 97 96 95 90 89 
79	9	7		100 99 98 96 95 94 93 
80	9	5		96 95 94 90 87 
81	9	4		98 96 94 93 
82	9	4		97 95 94 93 
83	9	4		99 97 96 93 
84	9	3		95 93 89 
85	9	3		95 94 93 
86	9	2		93 89 
87	9	2		98 93 
88	9	2		97 94 
89	9	1		94 
90	9	1		93 
91	9	1		94 
92	9	1		96 
93	9	1		102 
94	9	1		102 
95	9	1		102 
96	9	1		102 
97	9	1		102 
98	9	1		102 
99	9	1		102 
100	9	1		102 
101	9	1		102 
102	1	0		
************************************************************************
REQUESTS/DURATIONS
jobnr.	mode	dur	R1	R2	R3	R4	N1	N2	N3	N4	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	0	0	
2	1	4	4	5	4	4	18	19	16	21	
	2	5	4	4	3	4	18	18	16	21	
	3	6	4	4	3	4	17	18	15	20	
	4	8	3	4	3	4	16	18	15	18	
	5	9	3	4	2	4	14	17	14	16	
	6	10	3	3	2	3	14	17	14	16	
	7	16	3	3	2	3	12	17	13	15	
	8	18	2	3	2	3	12	17	13	13	
	9	21	2	3	2	3	11	17	13	13	
3	1	2	4	4	3	4	19	23	27	19	
	2	5	4	3	3	3	18	21	24	19	
	3	9	4	3	3	3	18	21	22	17	
	4	10	4	3	3	3	18	19	19	14	
	5	12	4	2	2	2	17	17	17	11	
	6	13	4	2	2	2	17	17	12	11	
	7	14	4	2	1	2	17	15	11	8	
	8	15	4	2	1	1	16	14	8	7	
	9	29	4	2	1	1	16	13	5	5	
4	1	2	4	4	3	5	23	11	29	21	
	2	5	3	4	3	4	20	11	27	17	
	3	6	3	4	3	3	19	9	26	17	
	4	7	3	4	3	3	15	9	24	15	
	5	8	3	4	2	2	13	8	23	10	
	6	15	2	4	2	2	13	7	23	8	
	7	19	2	4	2	1	9	5	21	8	
	8	21	2	4	1	1	7	4	20	5	
	9	30	2	4	1	1	6	4	18	4	
5	1	6	4	5	3	3	22	25	27	26	
	2	14	4	4	3	2	21	24	25	25	
	3	18	4	3	3	2	20	23	24	21	
	4	19	3	3	2	2	20	22	22	19	
	5	21	3	2	2	2	18	21	19	16	
	6	22	2	2	2	2	18	20	18	12	
	7	23	1	1	2	2	16	19	16	10	
	8	27	1	1	1	2	15	18	15	9	
	9	28	1	1	1	2	15	18	14	5	
6	1	1	3	3	4	5	26	11	20	20	
	2	2	3	3	4	5	24	9	19	19	
	3	4	3	3	4	5	22	9	18	19	
	4	5	3	3	4	5	19	8	16	19	
	5	11	2	3	3	5	18	6	16	19	
	6	12	2	3	3	5	15	5	14	19	
	7	13	1	3	3	5	11	5	13	19	
	8	18	1	3	3	5	9	4	11	19	
	9	25	1	3	3	5	7	2	10	19	
7	1	9	4	1	2	2	25	29	7	24	
	2	10	4	1	2	2	22	29	5	23	
	3	12	4	1	2	2	21	29	5	22	
	4	22	3	1	2	2	19	29	5	19	
	5	23	3	1	2	2	18	29	4	18	
	6	25	3	1	1	1	16	29	3	18	
	7	26	3	1	1	1	15	29	3	15	
	8	28	2	1	1	1	13	29	2	13	
	9	29	2	1	1	1	13	29	2	12	
8	1	5	1	5	4	5	25	14	11	21	
	2	6	1	4	3	4	24	13	10	21	
	3	9	1	4	3	4	21	13	10	21	
	4	14	1	4	3	3	19	13	10	21	
	5	20	1	3	3	3	15	13	9	21	
	6	21	1	3	3	3	15	12	9	21	
	7	25	1	3	3	3	11	12	9	21	
	8	28	1	2	3	2	10	12	9	21	
	9	29	1	2	3	2	9	12	9	21	
9	1	1	5	5	3	4	13	21	29	10	
	2	9	4	5	2	3	12	19	28	9	
	3	16	4	5	2	3	12	19	27	9	
	4	17	3	5	2	2	11	17	27	9	
	5	20	3	5	1	2	11	17	26	9	
	6	21	2	5	1	2	10	16	25	9	
	7	23	1	5	1	1	9	16	25	9	
	8	29	1	5	1	1	9	14	24	9	
	9	30	1	5	1	1	8	14	24	9	
10	1	1	4	5	3	4	22	9	21	25	
	2	2	3	4	2	3	22	8	19	25	
	3	10	3	4	2	3	21	7	19	24	
	4	12	2	4	2	3	20	7	18	22	
	5	17	2	4	2	3	18	7	18	22	
	6	22	2	3	2	3	17	6	18	21	
	7	28	2	3	2	3	17	6	17	20	
	8	29	1	3	2	3	16	5	17	19	
	9	30	1	3	2	3	14	5	16	19	
11	1	3	4	3	3	3	7	15	23	9	
	2	4	4	3	3	3	7	14	20	8	
	3	5	4	3	3	3	7	14	17	8	
	4	11	3	3	3	3	7	13	17	7	
	5	18	3	3	2	3	7	13	13	6	
	6	19	3	3	2	3	6	12	12	5	
	7	20	2	3	2	3	6	12	11	3	
	8	22	2	3	2	3	6	11	9	3	
	9	26	2	3	2	3	6	11	6	1	
12	1	1	2	2	5	2	8	29	26	22	
	2	6	1	2	4	1	7	26	23	21	
	3	13	1	2	4	1	6	23	21	17	
	4	15	1	2	3	1	4	19	16	16	
	5	16	1	2	2	1	4	18	15	14	
	6	17	1	1	2	1	3	16	10	11	
	7	18	1	1	1	1	3	13	8	8	
	8	26	1	1	1	1	2	11	4	6	
	9	28	1	1	1	1	1	8	3	4	
13	1	2	3	4	5	5	26	16	11	27	
	2	6	3	4	4	4	24	14	10	26	
	3	7	3	4	4	4	22	13	9	25	
	4	8	3	4	4	4	22	11	8	24	
	5	9	3	3	3	4	19	10	8	23	
	6	17	3	3	3	4	19	9	7	22	
	7	18	3	2	3	4	16	6	6	21	
	8	23	3	2	2	4	16	3	5	20	
	9	26	3	2	2	4	15	2	5	19	
14	1	2	3	5	4	3	17	20	22	22	
	2	3	3	4	3	3	17	18	21	22	
	3	5	3	4	3	3	15	16	20	22	
	4	6	2	4	3	3	13	16	20	22	
	5	7	2	3	2	3	12	14	19	21	
	6	18	2	3	2	3	12	13	19	21	
	7	26	1	3	1	3	11	12	17	21	
	8	27	1	3	1	3	8	10	16	21	
	9	30	1	3	1	3	7	8	16	21	
15	1	4	4	1	1	2	9	21	17	12	
	2	5	3	1	1	2	9	20	17	12	
	3	6	3	1	1	2	7	20	15	12	
	4	8	3	1	1	2	7	20	14	12	
	5	16	3	1	1	2	5	19	13	12	
	6	21	3	1	1	2	4	19	12	12	
	7	22	3	1	1	2	3	19	10	12	
	8	27	3	1	1	2	2	19	9	12	
	9	29	3	1	1	2	1	19	8	12	
16	1	4	5	2	1	3	29	28	24	28	
	2	8	5	2	1	2	27	26	24	25	
	3	11	5	2	1	2	27	26	24	23	
	4	20	5	2	1	2	26	25	23	17	
	5	21	5	2	1	2	24	24	23	14	
	6	22	5	1	1	2	23	24	23	14	
	7	23	5	1	1	2	23	24	22	11	
	8	27	5	1	1	2	21	23	22	7	
	9	28	5	1	1	2	21	22	22	3	
17	1	6	3	4	4	3	28	29	23	25	
	2	8	2	3	4	3	24	26	22	23	
	3	11	2	3	3	3	23	26	22	22	
	4	14	2	3	3	3	19	23	21	21	
	5	21	1	3	2	3	15	23	21	21	
	6	22	1	3	2	3	13	20	20	21	
	7	23	1	3	2	3	11	18	19	19	
	8	26	1	3	1	3	10	16	19	19	
	9	27	1	3	1	3	7	16	19	18	
18	1	1	4	4	3	3	14	20	13	13	
	2	9	3	3	3	2	14	19	12	11	
	3	10	3	3	3	2	14	17	11	9	
	4	11	3	3	3	2	14	16	9	8	
	5	12	3	3	3	2	13	16	8	6	
	6	18	3	2	2	1	13	16	7	6	
	7	21	3	2	2	1	13	14	5	3	
	8	24	3	2	2	1	13	14	5	2	
	9	26	3	2	2	1	13	13	4	1	
19	1	4	3	4	4	3	4	19	9	17	
	2	7	3	3	3	3	3	17	8	16	
	3	12	3	3	3	3	3	15	8	13	
	4	13	3	2	3	3	2	14	8	11	
	5	18	3	2	3	3	2	12	7	9	
	6	20	3	2	3	3	2	9	7	8	
	7	25	3	2	3	3	1	9	7	6	
	8	27	3	1	3	3	1	5	6	5	
	9	30	3	1	3	3	1	5	6	3	
20	1	4	4	3	4	3	16	12	17	20	
	2	5	3	3	3	3	14	11	15	20	
	3	6	3	3	3	3	13	11	14	19	
	4	11	2	3	3	2	12	10	13	17	
	5	15	2	3	2	2	11	9	11	16	
	6	16	2	3	2	2	10	8	11	16	
	7	23	1	3	2	1	10	7	10	15	
	8	24	1	3	2	1	8	5	8	13	
	9	26	1	3	2	1	7	5	8	13	
21	1	1	3	4	4	3	26	8	19	18	
	2	2	3	4	3	3	24	7	16	16	
	3	7	3	4	3	3	22	7	14	16	
	4	14	3	4	2	3	22	6	11	16	
	5	15	3	4	2	2	19	5	10	15	
	6	16	3	4	2	2	15	5	8	14	
	7	17	3	4	1	2	13	4	8	14	
	8	19	3	4	1	1	11	3	5	12	
	9	26	3	4	1	1	10	2	3	12	
22	1	3	1	4	4	3	22	28	21	22	
	2	5	1	4	4	3	21	24	17	21	
	3	8	1	3	4	3	20	24	16	20	
	4	12	1	3	4	3	19	21	14	19	
	5	13	1	3	4	2	18	20	12	19	
	6	18	1	2	4	2	16	18	12	18	
	7	23	1	2	4	2	15	16	8	18	
	8	24	1	1	4	2	13	12	6	17	
	9	26	1	1	4	2	12	12	5	16	
23	1	3	4	5	3	5	14	24	27	24	
	2	4	4	4	2	4	14	22	27	23	
	3	6	4	4	2	3	12	18	27	24	
	4	7	4	4	2	3	12	18	27	23	
	5	10	4	3	2	3	11	14	27	23	
	6	15	4	3	1	2	10	13	26	22	
	7	16	4	3	1	2	9	12	26	22	
	8	26	4	3	1	1	7	10	26	22	
	9	30	4	3	1	1	7	6	26	22	
24	1	6	3	4	4	5	22	22	19	23	
	2	7	3	4	4	4	21	21	18	23	
	3	8	3	4	4	4	20	21	18	23	
	4	11	3	4	3	4	19	20	18	23	
	5	14	2	3	3	4	19	20	17	23	
	6	18	2	3	2	4	18	20	17	23	
	7	22	2	3	1	4	18	19	17	23	
	8	24	2	3	1	4	16	19	17	23	
	9	29	2	3	1	4	16	19	17	22	
25	1	1	3	3	4	4	13	10	28	21	
	2	3	3	3	4	3	12	9	27	21	
	3	5	3	3	4	3	12	9	25	19	
	4	10	3	3	4	2	11	7	23	19	
	5	11	2	3	4	2	9	7	19	18	
	6	12	2	3	4	2	9	5	18	16	
	7	22	2	3	4	1	7	5	15	14	
	8	26	2	3	4	1	7	3	11	13	
	9	30	2	3	4	1	6	3	11	12	
26	1	3	2	1	5	4	11	27	4	26	
	2	4	2	1	4	4	11	26	4	24	
	3	5	2	1	4	4	10	22	4	21	
	4	6	2	1	4	4	9	22	4	21	
	5	11	2	1	3	3	6	20	4	19	
	6	12	2	1	3	3	5	17	4	16	
	7	14	2	1	2	2	4	16	4	15	
	8	16	2	1	2	2	2	12	4	12	
	9	29	2	1	2	2	2	12	4	11	
27	1	7	1	2	4	4	28	22	19	25	
	2	8	1	2	4	4	26	18	17	25	
	3	13	1	2	4	4	26	16	17	24	
	4	14	1	2	4	4	25	16	17	22	
	5	15	1	1	4	4	24	13	16	21	
	6	19	1	1	3	4	24	10	16	20	
	7	20	1	1	3	4	24	9	15	19	
	8	21	1	1	3	4	23	8	15	19	
	9	30	1	1	3	4	22	6	14	18	
28	1	1	3	4	2	4	26	22	26	17	
	2	2	2	4	2	4	24	21	24	15	
	3	3	2	4	2	4	23	19	20	14	
	4	4	2	4	2	4	23	17	18	14	
	5	7	2	4	2	4	21	15	17	13	
	6	8	2	4	2	3	21	14	15	13	
	7	9	2	4	2	3	20	14	12	12	
	8	10	2	4	2	3	19	11	8	11	
	9	23	2	4	2	3	18	9	6	10	
29	1	3	4	2	2	5	13	24	9	27	
	2	4	4	1	2	4	13	22	8	27	
	3	5	3	1	2	4	12	19	7	25	
	4	10	3	1	2	3	11	17	7	24	
	5	11	3	1	1	3	11	17	5	22	
	6	15	2	1	1	2	11	15	5	21	
	7	16	2	1	1	1	10	12	4	20	
	8	17	1	1	1	1	9	11	2	20	
	9	21	1	1	1	1	9	9	2	18	
30	1	1	4	2	3	5	26	25	30	30	
	2	3	4	2	3	4	22	23	26	27	
	3	5	4	2	3	4	19	19	24	24	
	4	7	4	2	2	4	19	19	19	20	
	5	21	4	2	2	4	16	15	15	19	
	6	22	4	2	2	3	14	14	13	16	
	7	23	4	2	2	3	9	11	9	13	
	8	28	4	2	1	3	5	8	8	10	
	9	29	4	2	1	3	3	6	3	9	
31	1	1	5	4	3	3	10	25	26	13	
	2	3	4	4	3	2	10	22	25	13	
	3	5	4	4	3	2	9	21	23	11	
	4	6	3	4	3	2	8	18	21	10	
	5	7	3	4	3	1	7	18	18	9	
	6	8	3	4	2	1	5	17	17	9	
	7	14	3	4	2	1	4	15	16	8	
	8	15	2	4	2	1	3	12	14	7	
	9	22	2	4	2	1	3	10	10	6	
32	1	1	4	2	3	4	5	29	9	28	
	2	7	3	2	2	3	4	27	8	26	
	3	8	3	2	2	3	4	26	8	25	
	4	9	3	2	2	3	3	25	7	23	
	5	14	2	2	2	2	3	25	6	22	
	6	15	2	2	1	2	2	25	5	21	
	7	22	2	2	1	2	1	24	5	20	
	8	23	2	2	1	2	1	22	3	18	
	9	24	2	2	1	2	1	22	3	17	
33	1	2	2	5	3	3	18	15	10	27	
	2	3	2	4	2	3	16	15	10	27	
	3	4	2	3	2	3	16	15	10	27	
	4	6	2	3	2	3	14	14	10	27	
	5	8	2	3	2	3	13	14	10	27	
	6	9	2	2	1	3	11	13	10	27	
	7	19	2	1	1	3	11	12	10	27	
	8	25	2	1	1	3	9	12	10	27	
	9	27	2	1	1	3	9	12	10	26	
34	1	1	4	2	2	4	15	17	22	15	
	2	4	3	1	2	4	14	14	21	15	
	3	5	3	1	2	4	13	12	21	15	
	4	7	3	1	2	3	11	11	20	14	
	5	12	3	1	2	3	9	9	20	14	
	6	21	3	1	2	2	9	8	19	14	
	7	27	3	1	2	1	7	7	19	14	
	8	28	3	1	2	1	6	5	17	13	
	9	29	3	1	2	1	4	4	17	13	
35	1	9	1	2	5	4	18	15	21	22	
	2	10	1	2	4	4	15	15	20	18	
	3	20	1	2	4	4	13	12	19	17	
	4	25	1	2	4	4	12	12	18	16	
	5	26	1	2	4	4	12	9	18	15	
	6	27	1	2	4	3	10	7	16	13	
	7	28	1	2	4	3	9	6	16	10	
	8	29	1	2	4	3	6	5	15	10	
	9	30	1	2	4	3	5	4	13	8	
36	1	1	5	5	2	4	16	22	14	22	
	2	2	4	4	2	4	15	21	14	21	
	3	3	4	3	2	4	14	20	14	18	
	4	10	4	3	2	4	12	19	14	16	
	5	12	4	2	2	3	12	17	14	16	
	6	15	4	2	2	3	11	16	14	15	
	7	17	4	1	2	3	11	15	14	12	
	8	18	4	1	2	3	9	14	14	11	
	9	30	4	1	2	3	9	13	14	9	
37	1	1	2	4	5	4	14	12	18	13	
	2	5	2	4	4	4	13	11	17	11	
	3	12	2	4	3	4	11	10	16	10	
	4	16	2	4	3	3	11	10	16	10	
	5	23	2	4	2	3	10	8	14	9	
	6	27	2	3	2	2	9	6	13	8	
	7	28	2	3	1	1	8	4	12	7	
	8	29	2	3	1	1	7	3	11	6	
	9	30	2	3	1	1	7	2	11	5	
38	1	1	2	3	4	2	26	26	20	8	
	2	2	2	3	3	2	26	25	19	8	
	3	6	2	3	3	2	25	23	19	8	
	4	9	2	3	3	2	24	23	17	8	
	5	10	2	3	2	2	23	21	17	8	
	6	17	2	3	2	2	22	20	17	8	
	7	20	2	3	2	2	20	18	16	8	
	8	26	2	3	2	2	20	15	15	8	
	9	29	2	3	2	2	18	14	14	8	
39	1	1	2	2	5	3	12	19	18	27	
	2	7	1	2	4	2	11	17	17	21	
	3	10	1	2	4	2	10	15	14	20	
	4	13	1	2	4	2	8	13	14	17	
	5	16	1	2	3	2	7	12	11	15	
	6	20	1	2	3	1	6	12	10	11	
	7	24	1	2	3	1	4	11	9	11	
	8	28	1	2	2	1	3	9	7	8	
	9	30	1	2	2	1	3	7	5	5	
40	1	4	4	2	4	2	26	4	16	26	
	2	14	4	2	4	2	25	4	13	23	
	3	16	4	2	4	2	25	4	12	22	
	4	17	4	2	4	2	25	3	9	20	
	5	18	4	2	3	2	25	3	9	20	
	6	19	4	2	3	1	24	2	7	19	
	7	21	4	2	3	1	24	1	4	16	
	8	26	4	2	3	1	24	1	4	15	
	9	29	4	2	3	1	24	1	2	15	
41	1	2	3	3	5	5	27	24	22	26	
	2	13	3	3	5	4	24	22	22	24	
	3	14	3	3	5	4	23	19	22	23	
	4	15	3	3	5	4	20	16	22	22	
	5	16	2	2	5	4	17	15	22	22	
	6	17	2	2	5	4	16	11	22	22	
	7	20	2	2	5	4	13	10	22	21	
	8	26	2	1	5	4	11	7	22	19	
	9	30	2	1	5	4	11	4	22	19	
42	1	2	5	3	4	5	26	20	27	29	
	2	4	4	3	4	4	25	20	25	28	
	3	5	4	3	4	4	24	20	21	27	
	4	10	4	3	3	4	23	20	19	26	
	5	14	4	3	3	3	20	20	17	26	
	6	16	3	3	2	3	19	20	13	26	
	7	17	3	3	2	3	18	20	11	25	
	8	24	3	3	1	3	17	20	10	24	
	9	26	3	3	1	3	16	20	8	24	
43	1	9	5	2	3	4	9	28	24	27	
	2	10	4	2	3	4	8	26	24	26	
	3	12	4	2	3	4	8	23	23	26	
	4	17	4	2	3	4	7	19	21	26	
	5	21	3	2	2	4	6	18	21	25	
	6	25	3	1	2	4	6	17	21	25	
	7	26	3	1	1	4	5	13	19	24	
	8	28	2	1	1	4	5	10	19	24	
	9	29	2	1	1	4	5	7	18	24	
44	1	3	2	5	4	3	27	9	22	8	
	2	8	2	5	4	3	25	9	20	8	
	3	9	2	5	4	3	25	8	17	8	
	4	10	2	5	4	3	25	7	15	7	
	5	20	2	5	3	3	23	5	13	6	
	6	24	2	5	3	3	23	4	12	6	
	7	26	2	5	3	3	23	4	9	5	
	8	28	2	5	3	3	21	3	7	5	
	9	30	2	5	3	3	21	2	4	5	
45	1	2	4	4	4	4	26	25	23	27	
	2	3	4	4	3	3	26	21	21	26	
	3	15	4	4	3	3	25	17	20	25	
	4	17	4	3	2	3	24	16	20	24	
	5	18	4	3	2	2	22	14	19	21	
	6	19	4	2	2	2	22	10	17	21	
	7	22	4	2	1	2	21	10	16	18	
	8	23	4	1	1	2	19	5	14	18	
	9	25	4	1	1	2	18	5	14	17	
46	1	2	5	5	2	4	15	11	28	25	
	2	7	4	5	1	3	15	10	27	24	
	3	8	4	5	1	3	15	10	26	22	
	4	10	4	5	1	3	15	8	23	22	
	5	20	4	5	1	3	15	8	22	18	
	6	22	3	5	1	3	15	7	20	17	
	7	24	3	5	1	3	15	6	19	16	
	8	25	3	5	1	3	15	5	18	14	
	9	26	3	5	1	3	15	4	15	13	
47	1	1	5	1	4	3	25	14	11	19	
	2	3	5	1	4	3	25	13	11	17	
	3	4	5	1	4	3	24	13	11	17	
	4	5	5	1	3	2	22	13	10	15	
	5	11	5	1	2	2	21	13	10	15	
	6	12	5	1	2	2	19	13	9	15	
	7	13	5	1	2	1	16	13	8	14	
	8	21	5	1	1	1	15	13	8	12	
	9	24	5	1	1	1	15	13	8	11	
48	1	14	3	3	4	3	21	12	28	8	
	2	16	3	3	4	2	19	11	27	7	
	3	18	3	3	4	2	16	10	27	6	
	4	19	3	3	4	2	16	9	25	6	
	5	23	3	2	4	2	13	9	25	5	
	6	24	3	2	3	2	12	9	24	4	
	7	25	3	1	3	2	10	7	23	4	
	8	29	3	1	3	2	9	7	22	3	
	9	30	3	1	3	2	6	6	22	3	
49	1	3	3	4	3	3	22	14	11	30	
	2	4	2	3	3	3	20	14	11	24	
	3	7	2	3	3	3	18	14	10	24	
	4	13	2	3	3	3	18	14	9	20	
	5	17	2	3	3	3	16	13	9	18	
	6	19	2	3	3	3	15	13	9	16	
	7	20	2	3	3	3	15	13	8	13	
	8	23	2	3	3	3	14	13	7	11	
	9	29	2	3	3	3	12	13	7	7	
50	1	2	5	1	4	4	13	29	10	19	
	2	4	4	1	4	4	13	27	9	19	
	3	5	4	1	4	4	12	24	9	18	
	4	9	4	1	3	3	12	22	8	17	
	5	10	4	1	3	3	11	21	8	17	
	6	12	4	1	3	2	11	18	8	16	
	7	14	4	1	3	2	10	17	7	16	
	8	22	4	1	2	1	10	15	7	14	
	9	23	4	1	2	1	10	14	7	14	
51	1	4	5	5	3	4	27	2	24	19	
	2	9	4	4	3	4	26	2	22	19	
	3	14	4	3	3	4	25	2	22	19	
	4	18	3	3	2	4	25	2	22	19	
	5	21	3	2	2	4	23	2	21	19	
	6	22	3	2	2	4	21	2	20	19	
	7	23	3	1	1	4	19	2	20	19	
	8	24	2	1	1	4	18	2	19	19	
	9	25	2	1	1	4	18	2	19	18	
52	1	2	5	1	3	2	11	22	13	26	
	2	5	4	1	3	2	9	21	13	24	
	3	9	3	1	3	2	9	21	13	23	
	4	10	3	1	3	2	7	19	13	22	
	5	12	2	1	3	2	7	19	12	18	
	6	13	2	1	2	2	7	18	12	17	
	7	15	1	1	2	2	5	17	12	14	
	8	26	1	1	2	2	5	16	12	12	
	9	27	1	1	2	2	4	16	12	10	
53	1	7	2	3	1	5	11	26	17	15	
	2	9	2	2	1	4	11	26	17	15	
	3	11	2	2	1	4	10	25	13	14	
	4	12	2	2	1	4	9	24	11	12	
	5	16	2	1	1	4	9	23	9	11	
	6	19	2	1	1	4	8	23	9	9	
	7	20	2	1	1	4	7	21	5	9	
	8	25	2	1	1	4	7	20	4	8	
	9	30	2	1	1	4	6	20	2	7	
54	1	1	5	5	4	3	21	18	8	14	
	2	2	5	4	4	2	21	16	6	13	
	3	6	5	3	3	2	21	14	6	12	
	4	7	5	3	3	2	21	12	5	12	
	5	8	5	2	3	2	21	12	5	11	
	6	12	5	2	2	2	21	10	4	10	
	7	16	5	2	1	2	21	8	4	10	
	8	20	5	1	1	2	21	6	4	9	
	9	29	5	1	1	2	21	5	3	8	
55	1	1	5	5	5	2	11	25	8	24	
	2	3	4	4	4	2	11	23	7	18	
	3	11	4	4	4	2	10	23	7	18	
	4	12	4	4	4	2	9	22	7	15	
	5	22	4	4	3	2	8	22	7	13	
	6	26	4	4	3	1	7	21	7	8	
	7	27	4	4	3	1	7	20	7	7	
	8	28	4	4	2	1	5	19	7	5	
	9	30	4	4	2	1	5	19	7	1	
56	1	5	4	5	4	5	7	15	9	21	
	2	6	3	5	4	4	7	14	9	19	
	3	8	3	5	4	4	7	14	9	18	
	4	9	3	5	4	3	7	14	9	18	
	5	17	3	5	3	2	7	13	9	17	
	6	21	3	5	3	2	6	13	8	15	
	7	22	3	5	2	1	6	12	8	14	
	8	24	3	5	2	1	6	12	8	12	
	9	30	3	5	2	1	6	12	8	11	
57	1	1	4	2	3	3	13	21	27	26	
	2	8	4	2	2	3	11	19	25	25	
	3	9	4	2	2	3	11	19	25	24	
	4	17	4	2	2	3	10	18	23	24	
	5	18	3	2	2	3	7	17	20	24	
	6	23	3	1	1	3	7	17	20	23	
	7	25	3	1	1	3	5	17	17	23	
	8	26	3	1	1	3	4	15	16	22	
	9	29	3	1	1	3	3	15	13	22	
58	1	1	2	3	5	5	29	26	21	7	
	2	6	2	3	4	4	29	23	21	7	
	3	7	2	3	4	4	29	21	18	6	
	4	9	2	2	3	3	29	20	17	6	
	5	15	1	2	3	3	29	19	14	5	
	6	17	1	2	3	3	29	17	10	5	
	7	20	1	2	2	3	29	13	9	4	
	8	21	1	1	2	2	29	13	6	3	
	9	24	1	1	2	2	29	11	5	3	
59	1	1	3	5	2	4	23	29	19	12	
	2	2	3	4	2	3	21	28	17	11	
	3	5	3	4	2	3	20	28	17	9	
	4	9	3	4	2	3	18	28	17	8	
	5	15	3	4	2	2	17	27	16	8	
	6	17	3	4	2	2	17	27	15	6	
	7	18	3	4	2	1	15	26	15	6	
	8	25	3	4	2	1	14	25	15	4	
	9	26	3	4	2	1	13	25	14	4	
60	1	9	3	2	3	4	21	16	18	27	
	2	12	3	2	3	3	20	13	17	25	
	3	16	3	2	3	3	18	12	17	25	
	4	17	3	2	3	3	18	10	16	25	
	5	18	3	1	2	3	15	9	16	24	
	6	19	3	1	2	2	14	6	16	23	
	7	21	3	1	2	2	12	4	15	23	
	8	23	3	1	1	2	12	4	14	23	
	9	26	3	1	1	2	10	1	14	22	
61	1	1	3	3	4	1	11	24	28	16	
	2	2	3	3	3	1	9	21	25	16	
	3	4	3	3	3	1	7	21	20	16	
	4	10	3	3	3	1	7	15	16	16	
	5	18	3	3	2	1	6	13	14	16	
	6	19	2	2	2	1	5	12	11	16	
	7	22	2	2	2	1	3	6	10	16	
	8	28	2	2	1	1	2	3	4	16	
	9	29	2	2	1	1	2	1	2	16	
62	1	3	4	4	5	5	12	26	11	22	
	2	4	4	4	4	4	10	25	9	20	
	3	5	4	4	4	4	9	23	9	20	
	4	6	4	4	4	3	7	23	7	19	
	5	7	4	4	3	3	7	22	7	18	
	6	9	4	4	3	3	6	20	7	18	
	7	10	4	4	3	3	5	20	5	17	
	8	15	4	4	3	2	4	18	4	15	
	9	16	4	4	3	2	3	18	4	15	
63	1	5	4	3	2	5	26	2	29	23	
	2	9	3	3	2	4	21	2	24	22	
	3	17	3	3	2	4	20	2	22	19	
	4	18	3	2	2	4	18	2	21	18	
	5	22	3	2	2	3	13	2	19	18	
	6	23	2	2	2	3	10	1	17	15	
	7	24	2	2	2	3	8	1	16	15	
	8	25	2	1	2	3	4	1	14	12	
	9	30	2	1	2	3	4	1	10	11	
64	1	2	2	1	4	1	15	10	13	20	
	2	9	2	1	4	1	13	8	13	19	
	3	10	2	1	4	1	12	8	13	17	
	4	14	2	1	4	1	10	8	13	14	
	5	19	2	1	4	1	10	6	13	12	
	6	20	2	1	3	1	8	6	13	12	
	7	21	2	1	3	1	6	5	13	10	
	8	24	2	1	3	1	5	5	13	6	
	9	30	2	1	3	1	3	4	13	4	
65	1	7	4	4	4	3	8	27	19	27	
	2	9	3	4	3	3	7	26	17	26	
	3	12	3	4	3	3	6	25	16	25	
	4	18	2	4	3	2	5	23	16	24	
	5	21	2	3	3	2	4	21	14	24	
	6	24	2	3	3	2	4	19	12	23	
	7	25	2	3	3	1	3	17	10	23	
	8	26	1	3	3	1	2	14	8	23	
	9	27	1	3	3	1	1	14	7	22	
66	1	5	1	4	4	5	13	22	19	20	
	2	6	1	4	4	4	12	19	18	19	
	3	7	1	4	4	4	10	17	17	18	
	4	10	1	4	3	3	10	17	17	17	
	5	11	1	4	2	2	9	13	17	17	
	6	12	1	4	2	2	9	13	16	16	
	7	21	1	4	2	1	7	11	15	15	
	8	22	1	4	1	1	7	9	15	14	
	9	30	1	4	1	1	6	8	15	14	
67	1	7	5	3	4	3	14	28	23	5	
	2	8	5	3	4	3	14	26	22	4	
	3	9	5	3	4	3	12	26	22	4	
	4	15	5	3	4	3	9	25	21	4	
	5	19	5	3	4	2	7	23	20	4	
	6	21	5	3	4	2	7	22	18	3	
	7	22	5	3	4	2	5	22	16	3	
	8	23	5	3	4	2	3	21	15	3	
	9	27	5	3	4	2	2	20	15	3	
68	1	2	2	5	5	4	20	23	19	29	
	2	4	1	4	4	3	17	22	18	27	
	3	7	1	4	4	3	16	21	18	27	
	4	8	1	4	4	3	15	20	18	25	
	5	13	1	4	4	3	13	19	18	25	
	6	14	1	4	4	3	12	19	18	23	
	7	27	1	4	4	3	11	18	18	22	
	8	29	1	4	4	3	9	16	18	22	
	9	30	1	4	4	3	7	16	18	21	
69	1	6	2	4	5	3	21	22	13	19	
	2	7	2	3	4	3	19	22	12	17	
	3	8	2	3	4	3	18	22	11	14	
	4	9	2	3	4	3	17	21	11	12	
	5	10	2	2	3	3	13	21	9	10	
	6	11	2	2	3	2	11	21	8	10	
	7	12	2	2	2	2	7	21	8	7	
	8	16	2	2	2	2	6	20	7	5	
	9	17	2	2	2	2	3	20	6	4	
70	1	2	3	4	2	3	17	28	11	19	
	2	3	3	3	2	3	16	24	10	17	
	3	4	3	3	2	3	15	24	9	17	
	4	7	3	3	2	3	14	20	9	14	
	5	12	3	2	2	2	13	18	8	14	
	6	13	3	2	2	2	11	16	8	12	
	7	14	3	2	2	2	11	16	8	11	
	8	21	3	2	2	1	9	14	7	9	
	9	22	3	2	2	1	9	12	7	9	
71	1	8	4	3	4	5	27	5	25	23	
	2	9	4	3	4	4	25	5	21	22	
	3	10	3	3	4	4	24	4	19	22	
	4	11	3	3	4	4	23	4	17	21	
	5	12	3	2	4	3	23	4	14	21	
	6	13	2	2	3	3	21	3	10	20	
	7	14	1	1	3	2	20	3	7	20	
	8	23	1	1	3	2	19	2	7	19	
	9	30	1	1	3	2	19	2	2	19	
72	1	2	4	1	2	3	14	15	14	10	
	2	14	3	1	1	3	12	14	14	8	
	3	20	3	1	1	3	12	14	13	8	
	4	22	3	1	1	2	10	14	10	7	
	5	23	3	1	1	2	10	13	9	5	
	6	24	3	1	1	2	9	12	9	5	
	7	25	3	1	1	1	9	11	8	3	
	8	26	3	1	1	1	7	11	6	2	
	9	27	3	1	1	1	7	10	5	2	
73	1	3	4	3	4	2	13	12	18	11	
	2	6	3	3	4	2	11	11	17	11	
	3	7	3	3	4	2	10	10	16	11	
	4	9	3	2	4	2	9	9	15	10	
	5	18	2	2	4	2	7	8	15	10	
	6	19	2	2	4	2	6	6	14	9	
	7	21	2	2	4	2	3	5	12	8	
	8	25	1	1	4	2	2	5	12	8	
	9	29	1	1	4	2	1	4	10	8	
74	1	3	3	4	3	1	25	24	21	24	
	2	5	3	3	3	1	22	23	18	22	
	3	8	3	3	3	1	21	23	17	21	
	4	9	3	3	3	1	17	21	14	20	
	5	15	3	3	3	1	16	21	13	20	
	6	19	2	3	3	1	13	20	12	19	
	7	20	2	3	3	1	9	20	8	19	
	8	26	2	3	3	1	6	19	7	18	
	9	27	2	3	3	1	6	18	4	17	
75	1	1	4	4	4	5	29	21	23	29	
	2	4	3	4	4	5	24	19	22	27	
	3	12	3	4	4	5	22	19	18	26	
	4	14	3	3	4	5	19	14	17	23	
	5	20	3	2	3	5	17	13	16	21	
	6	21	3	2	3	5	15	11	14	20	
	7	22	3	2	2	5	13	7	10	19	
	8	23	3	1	2	5	9	7	10	17	
	9	27	3	1	2	5	7	4	6	17	
76	1	7	4	5	1	4	21	30	8	19	
	2	9	4	4	1	3	18	28	7	18	
	3	14	4	4	1	3	17	27	7	18	
	4	15	4	4	1	3	15	26	6	18	
	5	16	4	4	1	2	14	23	6	18	
	6	17	4	3	1	2	13	22	5	17	
	7	18	4	3	1	2	12	21	5	17	
	8	22	4	3	1	1	9	20	5	17	
	9	26	4	3	1	1	8	18	4	17	
77	1	4	4	5	3	3	21	18	29	27	
	2	8	4	5	2	2	19	16	27	26	
	3	9	3	5	2	2	19	16	26	24	
	4	10	3	5	2	2	17	14	24	21	
	5	13	2	5	1	2	17	11	21	21	
	6	14	2	5	1	2	15	11	20	19	
	7	15	2	5	1	2	15	10	16	18	
	8	17	1	5	1	2	13	7	16	15	
	9	20	1	5	1	2	13	6	12	14	
78	1	2	3	2	3	5	28	14	23	29	
	2	3	3	2	3	4	28	12	23	29	
	3	4	3	2	3	4	27	12	22	28	
	4	5	3	2	3	4	27	10	22	26	
	5	15	3	2	3	4	26	8	22	26	
	6	17	3	1	2	4	26	7	21	25	
	7	19	3	1	2	4	25	7	21	25	
	8	27	3	1	2	4	25	4	20	24	
	9	29	3	1	2	4	24	4	20	23	
79	1	4	3	5	4	5	12	30	25	10	
	2	6	3	4	3	4	12	25	21	10	
	3	10	3	4	3	4	11	25	20	9	
	4	12	3	4	3	4	11	22	20	9	
	5	20	3	4	3	3	10	19	18	9	
	6	21	2	4	2	3	10	16	17	8	
	7	24	2	4	2	3	9	12	14	8	
	8	28	2	4	2	3	8	11	12	7	
	9	29	2	4	2	3	8	10	11	7	
80	1	3	1	4	3	1	30	16	7	4	
	2	11	1	3	2	1	29	14	6	3	
	3	13	1	3	2	1	28	13	6	3	
	4	15	1	3	2	1	26	13	5	3	
	5	16	1	3	1	1	26	12	4	3	
	6	20	1	3	1	1	25	11	4	2	
	7	23	1	3	1	1	23	10	3	2	
	8	24	1	3	1	1	23	9	3	2	
	9	28	1	3	1	1	21	9	3	2	
81	1	7	3	5	3	4	23	24	15	22	
	2	10	3	4	2	3	22	22	14	22	
	3	12	3	4	2	3	21	18	13	19	
	4	13	3	4	2	2	20	17	12	17	
	5	22	3	4	2	2	17	12	10	12	
	6	25	3	4	2	2	17	9	9	10	
	7	26	3	4	2	2	16	9	8	9	
	8	28	3	4	2	1	14	4	7	6	
	9	30	3	4	2	1	13	3	7	4	
82	1	6	3	2	1	3	16	29	16	20	
	2	16	2	2	1	3	14	29	15	19	
	3	17	2	2	1	3	13	29	13	18	
	4	18	2	2	1	3	12	29	11	18	
	5	19	2	2	1	3	11	29	9	17	
	6	20	1	2	1	3	10	29	7	17	
	7	21	1	2	1	3	9	29	7	16	
	8	22	1	2	1	3	8	29	5	16	
	9	29	1	2	1	3	8	29	3	15	
83	1	3	4	4	1	2	10	10	28	23	
	2	11	4	4	1	2	9	10	28	23	
	3	14	4	4	1	2	9	10	27	21	
	4	15	3	4	1	2	8	10	25	20	
	5	18	3	4	1	2	8	9	24	18	
	6	19	2	4	1	2	8	9	24	18	
	7	23	2	4	1	2	7	9	23	17	
	8	25	1	4	1	2	7	8	21	14	
	9	26	1	4	1	2	6	8	21	13	
84	1	1	3	5	4	4	22	9	22	1	
	2	2	3	4	4	3	22	8	19	1	
	3	6	3	4	4	3	21	7	16	1	
	4	9	2	4	4	3	21	6	15	1	
	5	15	2	3	4	2	20	6	13	1	
	6	16	2	3	4	2	20	5	10	1	
	7	18	1	2	4	2	20	4	5	1	
	8	19	1	2	4	1	19	3	4	1	
	9	23	1	2	4	1	19	3	1	1	
85	1	1	4	5	5	5	17	18	18	25	
	2	4	3	4	4	5	16	17	15	24	
	3	5	3	4	4	5	15	16	13	24	
	4	6	3	3	4	5	14	14	13	23	
	5	8	3	2	3	5	11	14	11	23	
	6	14	2	2	3	5	11	11	9	23	
	7	19	2	2	3	5	10	9	7	22	
	8	23	2	1	3	5	8	8	7	22	
	9	29	2	1	3	5	8	7	5	22	
86	1	3	4	4	2	2	22	22	27	26	
	2	8	4	3	2	2	21	19	27	25	
	3	10	4	3	2	2	17	18	27	24	
	4	11	3	3	2	2	14	17	26	24	
	5	14	3	2	2	1	11	14	26	22	
	6	16	3	2	1	1	11	12	25	22	
	7	17	3	2	1	1	7	11	25	22	
	8	29	2	2	1	1	6	10	24	21	
	9	30	2	2	1	1	4	8	24	20	
87	1	3	4	5	4	3	24	25	30	23	
	2	6	3	4	4	3	20	22	27	20	
	3	8	3	4	4	3	17	20	23	20	
	4	9	3	3	4	2	16	19	22	19	
	5	16	2	3	4	2	13	16	20	16	
	6	17	2	2	4	2	9	16	17	14	
	7	21	2	1	4	1	9	13	15	12	
	8	24	2	1	4	1	5	10	13	12	
	9	30	2	1	4	1	3	10	10	10	
88	1	1	5	5	4	3	22	1	21	16	
	2	5	5	4	3	3	21	1	17	13	
	3	10	5	4	3	3	21	1	15	12	
	4	15	5	4	2	3	21	1	14	9	
	5	18	5	4	2	3	21	1	9	9	
	6	20	5	4	2	3	21	1	8	8	
	7	21	5	4	1	3	21	1	6	5	
	8	22	5	4	1	3	21	1	5	2	
	9	29	5	4	1	3	21	1	2	2	
89	1	1	4	5	5	4	18	29	20	26	
	2	2	4	5	5	4	17	26	19	24	
	3	3	4	5	5	4	16	26	17	24	
	4	4	4	5	5	4	16	25	16	21	
	5	7	4	5	5	3	14	22	14	20	
	6	18	4	5	5	3	13	22	14	20	
	7	23	4	5	5	3	13	19	13	17	
	8	24	4	5	5	3	12	17	10	17	
	9	29	4	5	5	3	10	17	10	15	
90	1	9	5	5	4	4	23	16	9	10	
	2	12	4	5	4	4	22	15	8	9	
	3	16	4	5	4	4	18	14	6	9	
	4	21	4	5	4	3	17	12	6	9	
	5	22	4	5	4	2	13	11	5	9	
	6	25	3	5	4	2	11	10	5	9	
	7	26	3	5	4	1	8	8	4	9	
	8	27	3	5	4	1	7	7	2	9	
	9	28	3	5	4	1	5	5	2	9	
91	1	1	4	3	3	2	22	14	19	11	
	2	9	4	2	3	1	18	14	18	10	
	3	10	4	2	3	1	17	14	18	9	
	4	13	4	2	3	1	15	14	16	8	
	5	16	4	1	3	1	12	14	14	7	
	6	21	4	1	3	1	10	14	14	7	
	7	28	4	1	3	1	8	14	11	6	
	8	29	4	1	3	1	6	14	10	5	
	9	30	4	1	3	1	5	14	9	4	
92	1	2	5	5	5	5	25	29	24	25	
	2	3	4	5	4	4	25	28	24	22	
	3	5	4	5	4	3	23	28	22	21	
	4	9	3	5	4	3	19	26	18	19	
	5	18	2	5	4	2	18	26	16	17	
	6	22	2	5	3	2	17	25	15	14	
	7	24	2	5	3	2	14	24	13	13	
	8	27	1	5	3	1	13	22	8	10	
	9	28	1	5	3	1	9	22	8	10	
93	1	3	3	2	4	5	28	12	21	18	
	2	5	3	2	4	5	25	10	19	15	
	3	7	3	2	4	5	23	10	15	15	
	4	14	3	2	4	5	19	9	13	13	
	5	18	2	2	3	5	16	8	11	10	
	6	26	2	2	3	5	15	8	10	10	
	7	27	2	2	3	5	13	7	6	6	
	8	28	1	2	3	5	11	7	5	5	
	9	29	1	2	3	5	10	6	4	3	
94	1	2	5	3	2	3	23	19	21	24	
	2	6	4	3	1	3	21	18	21	21	
	3	7	4	3	1	3	21	16	20	19	
	4	8	4	3	1	3	20	15	19	19	
	5	9	4	3	1	2	19	14	18	17	
	6	10	4	3	1	2	18	12	18	12	
	7	17	4	3	1	2	18	12	18	10	
	8	18	4	3	1	1	16	10	16	8	
	9	22	4	3	1	1	16	8	16	6	
95	1	2	4	5	5	3	16	30	6	25	
	2	5	3	4	4	2	13	27	6	24	
	3	6	3	4	4	2	11	25	6	22	
	4	16	3	4	4	2	10	25	6	19	
	5	17	3	3	4	2	8	22	6	17	
	6	18	3	3	4	2	6	21	6	15	
	7	19	3	2	4	2	5	20	6	15	
	8	20	3	2	4	2	5	17	6	13	
	9	21	3	2	4	2	3	17	6	10	
96	1	1	2	2	4	4	27	23	8	5	
	2	3	1	2	4	4	26	23	7	4	
	3	10	1	2	4	4	24	22	6	4	
	4	15	1	2	4	3	24	19	5	4	
	5	17	1	2	4	3	23	18	4	4	
	6	20	1	1	3	3	21	18	4	4	
	7	25	1	1	3	3	21	16	2	4	
	8	28	1	1	3	2	20	14	2	4	
	9	30	1	1	3	2	19	14	1	4	
97	1	3	5	5	3	5	3	8	6	19	
	2	11	4	4	2	4	2	8	6	19	
	3	13	4	4	2	4	2	8	5	15	
	4	16	4	4	2	4	2	7	4	14	
	5	19	3	4	2	4	2	7	4	13	
	6	21	3	4	2	4	2	7	3	9	
	7	22	3	4	2	4	2	6	2	7	
	8	23	3	4	2	4	2	6	1	6	
	9	27	3	4	2	4	2	6	1	4	
98	1	10	3	5	1	3	7	21	13	8	
	2	11	2	5	1	2	6	21	12	7	
	3	12	2	5	1	2	5	21	11	7	
	4	13	2	5	1	2	5	21	10	7	
	5	21	2	5	1	1	4	21	9	6	
	6	22	2	5	1	1	4	21	7	6	
	7	25	2	5	1	1	3	21	7	6	
	8	26	2	5	1	1	2	21	5	5	
	9	30	2	5	1	1	2	21	5	4	
99	1	8	5	5	3	2	19	30	29	6	
	2	9	4	5	3	1	18	29	29	6	
	3	10	4	5	3	1	17	28	28	6	
	4	14	3	5	3	1	16	28	28	5	
	5	18	3	5	2	1	15	27	26	5	
	6	19	3	5	2	1	13	27	26	5	
	7	21	3	5	2	1	11	27	25	4	
	8	23	2	5	1	1	10	26	25	4	
	9	24	2	5	1	1	8	26	24	4	
100	1	1	1	5	2	1	21	24	27	24	
	2	3	1	4	1	1	21	24	25	23	
	3	5	1	4	1	1	18	21	23	23	
	4	13	1	4	1	1	15	17	20	22	
	5	14	1	3	1	1	14	16	18	22	
	6	15	1	3	1	1	13	13	14	22	
	7	19	1	3	1	1	12	11	12	21	
	8	24	1	3	1	1	9	9	7	21	
	9	30	1	3	1	1	7	6	4	21	
101	1	3	2	4	3	3	16	28	18	8	
	2	6	2	4	2	3	14	24	17	8	
	3	9	2	3	2	3	13	23	16	8	
	4	17	2	3	2	3	12	21	15	8	
	5	25	2	2	1	3	11	19	13	8	
	6	27	2	2	1	3	11	17	12	7	
	7	28	2	2	1	3	10	14	12	7	
	8	29	2	1	1	3	9	11	11	7	
	9	30	2	1	1	3	7	9	9	7	
102	1	0	0	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	R 3	R 4	N 1	N 2	N 3	N 4
	29	31	30	30	1181	1279	1198	1353

************************************************************************
