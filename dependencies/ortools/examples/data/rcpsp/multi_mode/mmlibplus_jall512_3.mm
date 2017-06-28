jobs  (incl. supersource/sink ):	102
RESOURCES
- renewable                 : 4 R
- nonrenewable              : 2 N
- doubly constrained        : 0 D
************************************************************************
PRECEDENCE RELATIONS:
jobnr.    #modes  #successors   successors
1	1	12		2 3 4 5 6 8 10 11 12 13 14 15 
2	6	7		31 30 23 21 20 19 9 
3	6	5		30 23 17 16 7 
4	6	5		24 23 21 16 9 
5	6	4		24 21 18 9 
6	6	8		31 29 28 27 26 25 24 22 
7	6	6		45 33 28 26 24 21 
8	6	5		30 28 27 24 16 
9	6	7		45 33 29 28 27 26 25 
10	6	7		33 30 29 28 27 26 25 
11	6	7		45 38 33 31 29 28 27 
12	6	6		35 33 29 28 27 25 
13	6	4		34 30 26 20 
14	6	5		35 33 27 25 24 
15	6	3		33 24 21 
16	6	8		45 40 38 35 34 33 32 29 
17	6	4		47 27 26 24 
18	6	7		40 38 35 34 32 30 29 
19	6	5		45 38 35 33 27 
20	6	6		40 38 35 33 32 29 
21	6	2		29 27 
22	6	6		47 40 38 36 35 30 
23	6	7		46 41 40 37 36 34 33 
24	6	5		40 38 36 34 32 
25	6	7		47 46 42 41 38 37 34 
26	6	6		43 40 39 38 35 32 
27	6	4		41 40 34 32 
28	6	6		46 42 41 40 37 34 
29	6	5		47 43 41 37 36 
30	6	6		53 49 43 42 41 37 
31	6	5		56 51 47 40 37 
32	6	5		51 49 46 42 37 
33	6	7		56 53 52 49 48 47 44 
34	6	5		50 49 44 43 39 
35	6	5		56 51 49 46 37 
36	6	6		61 57 54 51 49 39 
37	6	4		52 50 48 44 
38	6	7		64 60 58 57 53 49 48 
39	6	8		64 60 59 58 56 55 53 52 
40	6	8		66 64 62 61 60 57 53 49 
41	6	8		67 65 64 62 61 60 58 51 
42	6	7		65 64 61 60 56 54 52 
43	6	6		61 60 59 58 56 54 
44	6	5		60 59 58 55 54 
45	6	8		67 66 65 62 61 60 59 57 
46	6	6		62 61 60 59 57 52 
47	6	6		67 66 65 64 61 50 
48	6	5		73 67 62 59 55 
49	6	4		73 72 65 59 
50	6	4		71 69 62 57 
51	6	4		72 68 66 59 
52	6	8		79 77 73 72 70 68 67 66 
53	6	8		93 77 76 72 71 68 67 63 
54	6	6		79 77 76 71 67 62 
55	6	5		77 72 66 65 63 
56	6	5		77 76 69 63 62 
57	6	8		93 80 77 76 73 72 68 63 
58	6	4		72 68 66 63 
59	6	6		93 77 76 71 69 63 
60	6	11		93 90 83 80 79 78 74 73 72 70 68 
61	6	10		93 90 80 79 78 76 74 73 72 70 
62	6	8		93 90 83 81 80 72 70 68 
63	6	7		90 83 82 79 78 74 70 
64	6	6		93 90 80 79 78 68 
65	6	5		93 83 80 74 68 
66	6	8		101 93 90 80 78 76 75 74 
67	6	5		89 83 80 74 69 
68	6	5		101 89 84 82 75 
69	6	5		101 90 87 84 75 
70	6	4		101 89 84 75 
71	6	4		89 86 84 78 
72	6	6		100 99 92 89 87 84 
73	6	8		101 100 99 97 92 91 88 85 
74	6	3		99 88 81 
75	6	7		100 99 97 92 91 88 85 
76	6	6		100 99 98 97 92 84 
77	6	5		101 99 92 86 84 
78	6	7		100 99 98 97 92 91 85 
79	6	5		100 99 88 87 85 
80	6	5		99 97 91 88 85 
81	6	4		100 91 87 86 
82	6	3		98 91 86 
83	6	4		101 98 96 92 
84	6	2		91 85 
85	6	3		96 95 94 
86	6	3		97 95 94 
87	6	3		97 96 95 
88	6	2		98 96 
89	6	2		98 94 
90	6	2		97 94 
91	6	1		94 
92	6	1		94 
93	6	1		95 
94	6	1		102 
95	6	1		102 
96	6	1		102 
97	6	1		102 
98	6	1		102 
99	6	1		102 
100	6	1		102 
101	6	1		102 
102	1	0		
************************************************************************
REQUESTS/DURATIONS
jobnr.	mode	dur	R1	R2	R3	R4	N1	N2	
------------------------------------------------------------------------
1	1	0	0	0	0	0	0	0	
2	1	8	3	2	4	2	15	19	
	2	12	3	2	4	2	14	15	
	3	14	3	2	3	2	14	13	
	4	19	3	2	2	2	14	11	
	5	20	3	2	2	2	13	6	
	6	21	3	2	1	2	13	3	
3	1	9	4	5	5	3	22	20	
	2	10	3	4	4	3	19	20	
	3	12	3	4	4	3	18	18	
	4	14	3	3	4	3	17	16	
	5	17	3	3	3	3	11	14	
	6	28	3	3	3	3	11	13	
4	1	13	4	3	5	2	28	19	
	2	26	4	3	4	2	24	18	
	3	27	4	2	4	2	23	18	
	4	28	4	2	4	2	20	18	
	5	29	4	2	4	1	17	16	
	6	30	4	1	4	1	17	16	
5	1	10	5	4	5	4	24	21	
	2	11	4	4	4	3	21	21	
	3	13	3	4	4	3	20	21	
	4	14	3	4	3	2	18	21	
	5	27	2	4	2	1	14	21	
	6	28	2	4	2	1	13	21	
6	1	3	5	4	5	5	12	13	
	2	4	4	3	3	3	12	13	
	3	6	3	3	3	3	8	13	
	4	9	3	2	2	3	6	13	
	5	11	3	1	1	1	4	12	
	6	12	2	1	1	1	3	12	
7	1	4	3	3	3	2	26	24	
	2	5	3	3	3	2	24	19	
	3	6	3	3	2	2	21	19	
	4	8	3	2	2	2	19	16	
	5	9	3	1	2	2	15	13	
	6	18	3	1	1	2	13	7	
8	1	5	1	5	2	4	17	17	
	2	8	1	3	2	3	15	16	
	3	10	1	3	2	3	12	15	
	4	16	1	3	1	2	10	14	
	5	17	1	1	1	1	5	13	
	6	27	1	1	1	1	3	13	
9	1	2	3	4	3	3	11	23	
	2	5	2	4	3	2	9	20	
	3	6	2	4	3	2	8	16	
	4	7	2	4	3	2	7	9	
	5	15	2	4	3	1	4	5	
	6	21	2	4	3	1	4	4	
10	1	3	1	5	4	3	11	11	
	2	6	1	3	4	2	10	9	
	3	10	1	3	4	2	10	8	
	4	14	1	2	3	1	9	7	
	5	21	1	2	2	1	9	5	
	6	23	1	1	2	1	8	2	
11	1	8	4	2	1	1	19	9	
	2	11	4	2	1	1	18	8	
	3	15	4	2	1	1	14	6	
	4	18	4	2	1	1	11	6	
	5	21	4	2	1	1	8	5	
	6	22	4	2	1	1	5	3	
12	1	6	5	3	3	4	3	16	
	2	11	4	2	3	3	3	16	
	3	12	3	2	3	2	3	14	
	4	14	3	2	3	2	2	11	
	5	24	1	2	3	2	2	7	
	6	25	1	2	3	1	1	4	
13	1	1	3	2	5	4	20	27	
	2	3	3	2	4	3	20	25	
	3	12	3	2	4	3	20	24	
	4	19	2	2	4	3	19	22	
	5	20	2	2	4	3	19	21	
	6	22	2	2	4	3	18	17	
14	1	3	4	4	2	1	16	18	
	2	7	3	3	1	1	15	13	
	3	12	3	2	1	1	15	12	
	4	14	2	2	1	1	14	7	
	5	18	2	1	1	1	11	4	
	6	29	2	1	1	1	10	1	
15	1	4	4	4	2	5	23	11	
	2	16	3	4	1	4	17	11	
	3	23	3	4	1	3	16	10	
	4	24	2	3	1	3	11	10	
	5	25	1	3	1	2	9	8	
	6	27	1	3	1	2	3	8	
16	1	3	5	5	5	2	28	24	
	2	12	5	3	5	2	27	20	
	3	14	5	3	5	2	27	18	
	4	16	5	3	5	2	26	13	
	5	25	5	1	5	2	26	6	
	6	26	5	1	5	2	25	3	
17	1	3	1	5	5	3	27	14	
	2	15	1	4	4	2	26	12	
	3	17	1	4	3	2	25	11	
	4	21	1	3	3	2	23	9	
	5	22	1	3	1	2	22	8	
	6	25	1	3	1	2	20	8	
18	1	10	3	4	4	4	22	5	
	2	11	3	4	4	4	20	5	
	3	12	3	4	3	4	19	4	
	4	21	2	4	3	4	16	2	
	5	25	1	4	2	4	14	1	
	6	26	1	4	2	4	13	1	
19	1	4	2	3	3	3	28	16	
	2	13	2	2	3	2	23	13	
	3	14	2	2	2	2	20	11	
	4	15	2	2	2	2	12	10	
	5	19	2	2	1	2	10	8	
	6	28	2	2	1	2	3	7	
20	1	11	4	2	3	1	23	26	
	2	20	3	2	3	1	20	22	
	3	25	3	2	3	1	16	19	
	4	26	3	2	2	1	14	16	
	5	28	1	1	1	1	6	16	
	6	29	1	1	1	1	3	12	
21	1	7	4	4	4	5	21	23	
	2	8	4	4	4	5	20	19	
	3	10	3	4	3	5	18	15	
	4	12	2	4	2	5	16	15	
	5	14	2	4	2	5	16	10	
	6	15	1	4	1	5	14	9	
22	1	8	3	4	2	2	12	16	
	2	9	2	3	2	1	11	14	
	3	13	2	2	2	1	11	10	
	4	16	2	2	2	1	8	9	
	5	22	2	2	1	1	7	6	
	6	28	2	1	1	1	6	4	
23	1	1	4	5	2	4	20	29	
	2	7	4	4	1	4	19	29	
	3	14	4	4	1	3	18	27	
	4	21	4	4	1	3	18	26	
	5	27	3	4	1	2	17	25	
	6	28	3	4	1	2	16	25	
24	1	2	3	4	4	5	27	24	
	2	5	3	4	3	4	25	20	
	3	12	3	4	2	3	22	19	
	4	14	3	3	2	3	14	14	
	5	26	3	3	2	1	14	13	
	6	28	3	2	1	1	7	10	
25	1	4	5	4	4	3	23	19	
	2	5	4	4	4	2	19	19	
	3	8	4	4	4	2	14	18	
	4	26	4	4	4	1	13	17	
	5	27	3	3	3	1	7	16	
	6	29	3	3	3	1	7	15	
26	1	1	5	4	3	5	26	13	
	2	6	4	4	3	5	23	12	
	3	9	3	4	3	5	18	9	
	4	12	3	3	2	5	14	9	
	5	20	2	3	2	5	11	7	
	6	23	2	2	1	5	9	5	
27	1	1	3	3	3	4	29	25	
	2	2	3	3	3	3	29	25	
	3	3	3	3	3	3	29	24	
	4	8	3	3	3	3	29	23	
	5	9	3	2	2	3	29	22	
	6	12	3	2	2	3	29	21	
28	1	1	3	5	3	4	22	29	
	2	11	3	4	3	4	22	27	
	3	16	3	4	3	3	21	24	
	4	25	2	4	3	3	19	24	
	5	27	1	4	3	3	18	23	
	6	29	1	4	3	2	18	20	
29	1	10	5	3	4	5	25	13	
	2	13	4	3	3	4	19	13	
	3	15	4	3	3	4	15	11	
	4	18	3	3	3	3	10	11	
	5	23	3	3	2	3	6	10	
	6	28	2	3	2	3	3	9	
30	1	15	1	4	3	4	8	23	
	2	16	1	4	3	4	7	18	
	3	17	1	4	3	3	7	16	
	4	18	1	4	3	2	6	14	
	5	25	1	4	2	2	5	12	
	6	27	1	4	2	1	5	9	
31	1	1	4	4	2	2	8	14	
	2	9	4	3	2	2	8	13	
	3	11	3	3	2	2	8	12	
	4	14	2	2	2	2	8	11	
	5	16	2	1	2	2	8	9	
	6	19	1	1	2	2	8	9	
32	1	1	4	5	3	1	21	23	
	2	3	4	3	3	1	19	23	
	3	5	4	3	2	1	14	23	
	4	8	3	3	2	1	14	23	
	5	11	3	2	1	1	7	22	
	6	24	3	1	1	1	4	22	
33	1	12	2	5	4	5	13	20	
	2	13	2	4	4	4	13	19	
	3	14	2	4	4	4	12	18	
	4	21	2	4	4	3	12	16	
	5	26	2	3	4	3	12	14	
	6	27	2	3	4	3	11	11	
34	1	4	3	5	3	5	28	29	
	2	13	3	4	3	4	27	24	
	3	14	3	4	3	4	23	23	
	4	28	3	3	3	4	21	21	
	5	29	3	3	3	4	18	17	
	6	30	3	3	3	4	16	17	
35	1	1	4	3	4	5	20	18	
	2	13	3	3	3	4	20	17	
	3	17	3	3	3	4	19	13	
	4	21	3	3	3	4	18	12	
	5	22	2	2	2	4	16	11	
	6	24	1	2	2	4	15	7	
36	1	14	4	4	1	4	21	20	
	2	15	4	3	1	3	19	18	
	3	17	4	2	1	3	15	14	
	4	21	4	2	1	3	13	12	
	5	23	4	1	1	3	9	8	
	6	24	4	1	1	3	8	8	
37	1	2	5	3	3	4	8	29	
	2	9	4	2	3	4	5	24	
	3	13	4	2	3	4	4	20	
	4	19	4	2	3	4	4	11	
	5	23	3	2	3	4	2	9	
	6	29	3	2	3	4	2	5	
38	1	5	4	3	3	4	20	24	
	2	6	4	3	2	4	19	17	
	3	10	4	3	2	3	15	16	
	4	13	4	2	1	3	15	12	
	5	15	3	2	1	2	11	10	
	6	22	3	2	1	1	10	6	
39	1	2	5	2	4	5	15	26	
	2	4	4	2	3	5	13	26	
	3	6	3	2	3	5	12	22	
	4	9	3	2	2	5	11	19	
	5	15	1	2	2	5	8	16	
	6	25	1	2	1	5	6	12	
40	1	3	5	1	4	5	18	25	
	2	11	3	1	4	4	18	23	
	3	12	3	1	4	4	16	22	
	4	21	3	1	4	4	14	21	
	5	27	2	1	4	4	13	21	
	6	28	1	1	4	4	12	20	
41	1	8	3	4	4	3	19	30	
	2	18	3	3	3	2	17	25	
	3	23	2	3	3	2	16	18	
	4	25	2	3	3	1	14	14	
	5	26	1	2	3	1	12	6	
	6	27	1	1	3	1	11	6	
42	1	14	1	2	4	2	23	18	
	2	16	1	2	3	2	22	16	
	3	20	1	2	3	2	18	15	
	4	24	1	2	3	2	13	14	
	5	29	1	2	2	2	8	11	
	6	30	1	2	2	2	8	9	
43	1	2	4	1	3	3	18	10	
	2	6	3	1	2	2	16	8	
	3	18	3	1	2	2	14	8	
	4	19	3	1	2	1	12	7	
	5	20	3	1	2	1	9	7	
	6	27	3	1	2	1	6	6	
44	1	1	5	2	2	4	21	26	
	2	14	5	1	2	4	21	24	
	3	16	5	1	2	4	20	21	
	4	21	5	1	2	4	19	14	
	5	25	5	1	2	4	18	11	
	6	29	5	1	2	4	17	11	
45	1	3	1	4	5	4	14	21	
	2	5	1	3	3	3	14	19	
	3	12	1	2	3	3	12	17	
	4	21	1	2	3	3	11	9	
	5	26	1	1	2	3	9	9	
	6	30	1	1	1	3	7	2	
46	1	9	4	1	4	4	30	19	
	2	10	4	1	4	4	28	18	
	3	13	4	1	4	4	27	17	
	4	14	4	1	4	4	26	17	
	5	16	4	1	4	4	25	15	
	6	18	4	1	4	4	25	14	
47	1	6	2	4	4	5	14	26	
	2	8	2	3	4	4	14	24	
	3	9	2	3	4	4	13	24	
	4	13	2	3	4	4	13	23	
	5	14	2	2	4	3	13	19	
	6	29	2	2	4	3	12	18	
48	1	6	3	3	1	5	25	8	
	2	7	2	2	1	4	21	7	
	3	8	2	2	1	3	17	7	
	4	16	2	2	1	2	11	7	
	5	24	2	2	1	1	10	6	
	6	29	2	2	1	1	3	6	
49	1	2	4	5	2	3	16	23	
	2	3	3	3	2	3	16	22	
	3	5	3	3	2	3	13	22	
	4	20	2	3	2	3	11	20	
	5	28	1	1	2	3	11	17	
	6	29	1	1	2	3	8	16	
50	1	2	5	2	3	2	5	25	
	2	7	4	2	3	2	4	24	
	3	8	4	2	3	2	4	23	
	4	21	3	2	3	2	3	23	
	5	22	3	2	3	2	3	22	
	6	28	2	2	3	2	3	21	
51	1	11	5	3	2	3	17	20	
	2	12	5	3	2	3	15	16	
	3	13	5	2	2	3	12	13	
	4	17	5	2	2	3	11	13	
	5	22	5	2	2	3	5	10	
	6	25	5	1	2	3	2	6	
52	1	5	2	3	4	4	9	9	
	2	6	2	2	4	4	9	9	
	3	12	2	2	4	4	7	9	
	4	15	2	2	3	4	6	9	
	5	19	2	2	3	4	2	8	
	6	29	2	2	3	4	2	7	
53	1	9	4	1	2	3	16	11	
	2	17	4	1	1	3	13	9	
	3	18	4	1	1	3	11	6	
	4	19	4	1	1	2	8	5	
	5	20	3	1	1	2	3	2	
	6	29	3	1	1	2	2	2	
54	1	1	5	3	4	5	19	11	
	2	3	4	3	3	4	17	10	
	3	6	3	3	3	4	14	8	
	4	7	3	3	2	4	13	6	
	5	9	3	3	2	3	11	6	
	6	26	2	3	1	3	9	5	
55	1	3	5	4	5	3	28	28	
	2	4	5	3	4	2	25	21	
	3	5	5	2	4	2	21	17	
	4	13	5	2	4	2	18	13	
	5	28	5	1	4	1	17	6	
	6	29	5	1	4	1	13	2	
56	1	12	5	5	5	3	26	15	
	2	13	4	5	5	2	25	14	
	3	14	4	5	5	2	24	11	
	4	16	3	5	5	1	23	9	
	5	23	3	5	5	1	22	6	
	6	26	3	5	5	1	21	5	
57	1	2	4	5	3	2	24	26	
	2	5	3	4	3	2	21	26	
	3	8	3	3	3	2	20	26	
	4	12	3	3	3	1	18	25	
	5	13	3	2	3	1	16	24	
	6	18	3	2	3	1	14	24	
58	1	3	4	2	4	3	20	21	
	2	7	3	2	3	3	19	20	
	3	10	3	2	3	3	19	18	
	4	27	2	1	3	3	18	16	
	5	28	2	1	3	3	16	12	
	6	29	2	1	3	3	15	11	
59	1	1	4	4	4	2	17	19	
	2	4	4	3	4	1	15	18	
	3	5	3	3	4	1	13	18	
	4	10	3	2	4	1	12	18	
	5	13	1	2	4	1	11	18	
	6	16	1	1	4	1	11	18	
60	1	8	4	5	2	5	22	28	
	2	10	4	4	2	4	19	26	
	3	12	4	4	2	3	13	24	
	4	22	4	3	2	3	9	19	
	5	26	3	3	2	2	8	17	
	6	27	3	3	2	2	3	17	
61	1	3	4	2	5	4	15	24	
	2	13	4	1	4	4	12	22	
	3	14	4	1	3	4	12	22	
	4	15	4	1	3	3	11	19	
	5	16	4	1	2	3	9	18	
	6	20	4	1	2	3	8	17	
62	1	8	5	1	3	2	30	18	
	2	12	5	1	2	2	30	17	
	3	13	5	1	2	2	30	16	
	4	15	5	1	2	2	30	15	
	5	24	5	1	2	1	30	16	
	6	30	5	1	2	1	30	15	
63	1	2	3	1	3	5	19	28	
	2	3	3	1	2	5	17	23	
	3	11	2	1	2	5	16	17	
	4	13	2	1	2	5	16	15	
	5	14	2	1	2	5	15	11	
	6	27	1	1	2	5	14	7	
64	1	10	4	4	3	4	21	27	
	2	12	4	4	3	4	20	27	
	3	13	4	4	3	4	17	26	
	4	15	3	4	3	4	16	26	
	5	26	3	4	2	4	14	26	
	6	28	2	4	2	4	11	25	
65	1	5	2	4	4	4	22	17	
	2	24	1	3	3	4	21	17	
	3	25	1	3	3	4	20	17	
	4	26	1	2	2	3	18	17	
	5	27	1	1	2	3	18	17	
	6	30	1	1	1	3	17	17	
66	1	5	3	5	2	1	9	21	
	2	8	2	4	2	1	8	16	
	3	11	2	3	2	1	6	15	
	4	12	1	2	2	1	5	11	
	5	13	1	2	2	1	4	11	
	6	25	1	1	2	1	4	6	
67	1	3	1	5	4	5	28	26	
	2	6	1	4	4	4	28	24	
	3	17	1	3	4	3	27	25	
	4	18	1	3	4	3	27	24	
	5	27	1	1	4	3	25	22	
	6	30	1	1	4	2	25	22	
68	1	8	2	3	2	4	9	19	
	2	14	2	3	2	3	7	19	
	3	18	2	3	2	3	6	19	
	4	21	2	2	2	2	6	19	
	5	25	2	2	2	1	3	18	
	6	28	2	2	2	1	3	17	
69	1	10	4	5	5	5	28	20	
	2	17	3	3	4	4	26	19	
	3	23	3	3	4	3	25	19	
	4	24	3	3	4	3	24	19	
	5	28	3	2	4	2	22	19	
	6	30	3	1	4	2	20	19	
70	1	5	2	4	3	4	16	29	
	2	6	2	4	3	3	13	29	
	3	8	2	4	3	3	11	29	
	4	18	2	4	2	3	11	29	
	5	25	2	4	2	2	8	29	
	6	30	2	4	1	1	5	29	
71	1	6	4	3	2	3	3	25	
	2	8	4	2	2	2	2	22	
	3	17	4	2	2	2	2	18	
	4	20	4	2	2	2	2	15	
	5	21	4	2	2	2	2	12	
	6	27	4	2	2	2	2	9	
72	1	2	4	2	3	4	11	11	
	2	3	4	2	3	3	10	9	
	3	5	4	2	2	3	10	7	
	4	6	4	2	2	2	9	6	
	5	27	4	1	1	2	9	4	
	6	30	4	1	1	1	9	4	
73	1	8	3	4	5	3	25	19	
	2	10	3	4	4	3	23	15	
	3	12	3	4	4	3	23	12	
	4	13	3	4	3	3	18	8	
	5	18	3	4	3	3	17	6	
	6	26	3	4	2	3	14	4	
74	1	4	2	5	4	3	13	12	
	2	5	2	5	4	3	12	9	
	3	14	2	5	4	3	12	8	
	4	19	2	5	3	2	10	7	
	5	22	2	5	3	2	8	6	
	6	26	2	5	2	1	7	5	
75	1	15	3	4	3	2	21	22	
	2	19	3	4	2	2	21	20	
	3	20	3	4	2	2	19	16	
	4	24	2	4	2	2	18	11	
	5	25	1	4	1	2	17	11	
	6	26	1	4	1	2	17	8	
76	1	4	3	2	4	5	10	24	
	2	10	3	2	3	4	9	23	
	3	20	3	2	3	4	8	23	
	4	21	2	2	3	4	8	22	
	5	22	2	2	3	4	6	22	
	6	24	1	2	3	4	6	21	
77	1	5	2	4	5	1	30	20	
	2	8	2	3	5	1	29	19	
	3	11	2	3	5	1	29	16	
	4	15	2	3	5	1	29	13	
	5	16	2	3	5	1	29	8	
	6	24	2	3	5	1	29	6	
78	1	11	5	4	4	4	18	26	
	2	15	3	3	3	4	17	22	
	3	18	3	3	3	4	16	20	
	4	21	3	3	3	4	15	18	
	5	23	1	3	1	3	13	18	
	6	28	1	3	1	3	13	14	
79	1	6	5	3	4	3	27	5	
	2	7	4	3	3	3	22	4	
	3	18	3	3	3	3	16	4	
	4	19	3	3	3	3	13	4	
	5	24	3	3	3	3	10	3	
	6	30	2	3	3	3	5	3	
80	1	7	3	4	4	2	25	21	
	2	11	2	4	3	2	21	19	
	3	18	2	4	3	2	19	17	
	4	24	1	4	2	2	14	16	
	5	27	1	4	1	2	13	15	
	6	30	1	4	1	2	9	14	
81	1	4	4	5	3	5	20	15	
	2	6	4	4	3	4	19	14	
	3	12	4	4	3	4	18	13	
	4	16	3	4	3	4	18	13	
	5	19	2	4	3	4	16	13	
	6	27	2	4	3	4	16	12	
82	1	5	5	5	4	4	25	22	
	2	6	5	4	4	3	23	18	
	3	13	5	4	4	3	22	15	
	4	21	5	3	4	2	19	11	
	5	26	5	3	4	1	19	7	
	6	30	5	3	4	1	17	6	
83	1	4	4	3	4	5	5	8	
	2	5	3	3	3	5	5	7	
	3	6	3	3	3	5	5	6	
	4	7	2	3	3	5	5	6	
	5	8	2	3	1	5	4	6	
	6	29	1	3	1	5	4	5	
84	1	1	3	4	5	2	11	25	
	2	5	2	4	5	2	11	22	
	3	6	2	4	5	2	11	17	
	4	8	2	4	5	1	11	17	
	5	12	1	4	5	1	11	14	
	6	19	1	4	5	1	11	10	
85	1	6	4	5	3	3	23	10	
	2	7	4	4	3	2	18	10	
	3	9	4	3	3	2	13	8	
	4	10	4	3	3	2	13	7	
	5	11	4	3	3	2	10	6	
	6	17	4	2	3	2	4	3	
86	1	10	4	4	5	1	24	28	
	2	15	4	4	3	1	21	23	
	3	16	4	4	3	1	19	15	
	4	19	3	4	3	1	14	10	
	5	25	3	4	2	1	12	8	
	6	30	2	4	1	1	10	5	
87	1	5	1	2	3	4	19	22	
	2	6	1	1	3	4	19	19	
	3	19	1	1	3	4	14	15	
	4	20	1	1	3	4	13	13	
	5	24	1	1	3	4	10	13	
	6	27	1	1	3	4	8	9	
88	1	7	2	5	4	2	28	17	
	2	9	2	4	4	1	27	15	
	3	15	2	4	4	1	27	13	
	4	17	2	4	4	1	25	8	
	5	20	2	4	4	1	24	7	
	6	21	2	4	4	1	24	5	
89	1	5	3	4	4	3	11	22	
	2	6	3	3	4	3	9	21	
	3	12	3	3	4	3	8	16	
	4	18	3	3	4	2	5	11	
	5	28	3	3	4	2	4	8	
	6	30	3	3	4	1	3	4	
90	1	7	5	5	1	4	5	27	
	2	8	4	4	1	4	5	25	
	3	11	4	4	1	4	5	21	
	4	12	4	4	1	4	4	16	
	5	13	3	4	1	4	4	11	
	6	21	3	4	1	4	4	6	
91	1	6	2	1	4	4	17	14	
	2	7	2	1	3	4	16	14	
	3	16	2	1	3	4	16	12	
	4	23	2	1	3	3	16	12	
	5	24	2	1	3	2	16	11	
	6	25	2	1	3	2	16	10	
92	1	3	5	3	2	2	26	12	
	2	5	4	2	2	2	24	9	
	3	6	3	2	2	2	18	9	
	4	15	3	1	2	1	14	8	
	5	24	2	1	1	1	11	6	
	6	28	1	1	1	1	8	6	
93	1	1	3	2	3	3	17	19	
	2	3	3	1	2	3	15	14	
	3	8	3	1	2	2	13	13	
	4	22	3	1	2	2	12	9	
	5	26	3	1	1	1	8	5	
	6	30	3	1	1	1	6	3	
94	1	1	4	2	4	1	22	26	
	2	11	3	1	3	1	21	19	
	3	12	3	1	2	1	21	15	
	4	15	2	1	2	1	20	12	
	5	25	1	1	1	1	20	8	
	6	28	1	1	1	1	20	7	
95	1	6	4	4	4	4	17	6	
	2	7	4	3	4	3	15	6	
	3	8	4	2	4	3	14	5	
	4	19	4	2	4	2	14	4	
	5	20	4	1	4	1	13	2	
	6	23	4	1	4	1	12	1	
96	1	1	3	4	5	4	26	25	
	2	2	2	3	3	4	23	24	
	3	17	2	3	3	4	19	22	
	4	22	2	3	2	4	19	22	
	5	28	2	2	1	4	16	20	
	6	29	2	2	1	4	13	19	
97	1	2	2	5	3	3	25	26	
	2	3	2	4	3	2	24	26	
	3	5	2	4	3	2	16	25	
	4	16	1	3	3	2	12	25	
	5	20	1	2	3	2	12	24	
	6	24	1	2	3	2	6	24	
98	1	6	2	2	4	3	16	4	
	2	8	2	2	4	3	16	3	
	3	12	2	2	4	3	16	2	
	4	18	1	2	4	3	16	4	
	5	20	1	2	4	2	16	4	
	6	27	1	2	4	2	16	3	
99	1	8	4	5	1	3	17	22	
	2	13	3	4	1	2	16	21	
	3	15	3	4	1	2	13	20	
	4	19	3	4	1	2	8	20	
	5	26	3	3	1	2	6	18	
	6	27	3	3	1	2	3	18	
100	1	1	2	2	2	4	12	22	
	2	7	2	1	2	3	10	21	
	3	20	2	1	2	3	10	17	
	4	21	1	1	2	2	8	14	
	5	22	1	1	2	2	8	11	
	6	26	1	1	2	2	7	11	
101	1	2	4	4	2	4	18	24	
	2	3	3	4	2	4	15	24	
	3	4	3	4	2	4	14	24	
	4	10	2	4	2	4	9	23	
	5	16	2	3	2	4	5	23	
	6	20	1	3	2	4	3	22	
102	1	0	0	0	0	0	0	0	
************************************************************************

 RESOURCE AVAILABILITIES 
	R 1	R 2	R 3	R 4	N 1	N 2
	33	33	33	29	1475	1521

************************************************************************
