#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""
from __future__ import division
import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print "dataset size %d" % len(enron_data)

pers_count = 0
poi_count = 0

with_salary = 0
with_valid_email = 0
with_no_payments = 0
poi_with_no_payments = 0

max_salary = 0
max_id = ''

for key in enron_data.keys():
    features = enron_data[key]
    print "%3d %20s feature size %d salary %s" % (pers_count, key, len(features), features["salary"])
    pers_count += 1

    if features["salary"] != "NaN":
        salary = int(features["salary"])
        if salary > max_salary:
            max_salary = salary
            max_id = key

    if features["poi"] == 1:
        poi_count += 1
        if features["total_payments"] == "NaN":
            poi_with_no_payments += 1

    if features["email_address"] != "NaN":
        with_valid_email += 1

    if features["salary"] != "NaN":
        with_salary += 1

    if features["total_payments"] == "NaN":
        with_no_payments += 1

print "\n"
print " max salary [%s] %d" % (max_id, max_salary)

print "\n"
print "poi count %d " % poi_count

print "with salary %d" % with_salary
print "with valid email %d" % with_valid_email

print "with no payments %d total %d percentage %.3f" % (with_no_payments, pers_count, with_no_payments/pers_count * 100)
print "poi with no payments %d total %d percentage %.3f" % (poi_with_no_payments, pers_count, poi_with_no_payments/pers_count * 100)

print "\n"

person_id = "PRENTICE JAMES"
person_data = enron_data[person_id]

for key in person_data.keys():
    print "feature key: %30s     value: %30s" % (key, person_data[key])

print "\n"
print "total stock value: %s" % person_data["total_stock_value"]


person_id = "COLWELL WESLEY"
person_data = enron_data[person_id]

print "to_messages: %s" % person_data["to_messages"]
print "from_messages: %s" % person_data["from_messages"]
print "total_messages: %d" % (person_data["from_messages"] + person_data["to_messages"])

print "from_this_person_to_poi: %s" % person_data["from_this_person_to_poi"]


person_id = "SKILLING JEFFREY K"
person_data = enron_data[person_id]

print "exercised_stock_options: %s" % person_data["exercised_stock_options"]


print "total payments of %20s is %d " % ("SKILLING JEFFREY K", enron_data["SKILLING JEFFREY K"]["total_payments"])
print "total payments of %20s is %d " % ("FASTOW ANDREW S", enron_data["FASTOW ANDREW S"]["total_payments"])
print "total payments of %20s is %d " % ("LAY KENNETH L", enron_data["LAY KENNETH L"]["total_payments"])






'''

0 METTS MARK feature size 21
1 BAXTER JOHN C feature size 21
2 ELLIOTT STEVEN feature size 21
3 CORDES WILLIAM R feature size 21
4 HANNON KEVIN P feature size 21
5 MORDAUNT KRISTINA M feature size 21
6 MEYER ROCKFORD G feature size 21
7 MCMAHON JEFFREY feature size 21
8 HORTON STANLEY C feature size 21
9 PIPER GREGORY F feature size 21
10 HUMPHREY GENE E feature size 21
11 UMANOFF ADAM S feature size 21
12 BLACHMAN JEREMY M feature size 21
13 SUNDE MARTIN feature size 21
14 GIBBS DANA R feature size 21
15 LOWRY CHARLES P feature size 21
16 COLWELL WESLEY feature size 21
17 MULLER MARK S feature size 21
18 JACKSON CHARLENE R feature size 21
19 WESTFAHL RICHARD K feature size 21
20 WALTERS GARETH W feature size 21
21 WALLS JR ROBERT H feature size 21
22 KITCHEN LOUISE feature size 21
23 CHAN RONNIE feature size 21
24 BELFER ROBERT feature size 21
25 SHANKMAN JEFFREY A feature size 21
26 WODRASKA JOHN feature size 21
27 BERGSIEKER RICHARD P feature size 21
28 URQUHART JOHN A feature size 21
29 BIBI PHILIPPE A feature size 21
30 RIEKER PAULA H feature size 21
31 WHALEY DAVID A feature size 21
32 BECK SALLY W feature size 21
33 HAUG DAVID L feature size 21
34 ECHOLS JOHN B feature size 21
35 MENDELSOHN JOHN feature size 21
36 HICKERSON GARY J feature size 21
37 CLINE KENNETH W feature size 21
38 LEWIS RICHARD feature size 21
39 HAYES ROBERT E feature size 21
40 MCCARTY DANNY J feature size 21
41 KOPPER MICHAEL J feature size 21
42 LEFF DANIEL P feature size 21
43 LAVORATO JOHN J feature size 21
44 BERBERIAN DAVID feature size 21
45 DETMERING TIMOTHY J feature size 21
46 WAKEHAM JOHN feature size 21
47 POWERS WILLIAM feature size 21
48 GOLD JOSEPH feature size 21
49 BANNANTINE JAMES M feature size 21
50 DUNCAN JOHN H feature size 21
51 SHAPIRO RICHARD S feature size 21
52 SHERRIFF JOHN R feature size 21
53 SHELBY REX feature size 21
54 LEMAISTRE CHARLES feature size 21
55 DEFFNER JOSEPH M feature size 21
56 KISHKILL JOSEPH G feature size 21
57 WHALLEY LAWRENCE G feature size 21
58 MCCONNELL MICHAEL S feature size 21
59 PIRO JIM feature size 21
60 DELAINEY DAVID W feature size 21
61 SULLIVAN-SHAKLOVITZ COLLEEN feature size 21
62 WROBEL BRUCE feature size 21
63 LINDHOLM TOD A feature size 21
64 MEYER JEROME J feature size 21
65 LAY KENNETH L feature size 21
66 BUTTS ROBERT H feature size 21
67 OLSON CINDY K feature size 21
68 MCDONALD REBECCA feature size 21
69 CUMBERLAND MICHAEL S feature size 21
70 GAHN ROBERT S feature size 21
71 MCCLELLAN GEORGE feature size 21
72 HERMANN ROBERT J feature size 21
73 SCRIMSHAW MATTHEW feature size 21
74 GATHMANN WILLIAM D feature size 21
75 HAEDICKE MARK E feature size 21
76 BOWEN JR RAYMOND M feature size 21
77 GILLIS JOHN feature size 21
78 FITZGERALD JAY L feature size 21
79 MORAN MICHAEL P feature size 21
80 REDMOND BRIAN L feature size 21
81 BAZELIDES PHILIP J feature size 21
82 BELDEN TIMOTHY N feature size 21
83 DURAN WILLIAM D feature size 21
84 THORN TERENCE H feature size 21
85 FASTOW ANDREW S feature size 21
86 FOY JOE feature size 21
87 CALGER CHRISTOPHER F feature size 21
88 RICE KENNETH D feature size 21
89 KAMINSKI WINCENTY J feature size 21
90 LOCKHART EUGENE E feature size 21
91 COX DAVID feature size 21
92 OVERDYKE JR JERE C feature size 21
93 PEREIRA PAULO V. FERRAZ feature size 21
94 STABLER FRANK feature size 21
95 SKILLING JEFFREY K feature size 21
96 BLAKE JR. NORMAN P feature size 21
97 SHERRICK JEFFREY B feature size 21
98 PRENTICE JAMES feature size 21
99 GRAY RODNEY feature size 21
100 PICKERING MARK R feature size 21
101 THE TRAVEL AGENCY IN THE PARK feature size 21
102 NOLES JAMES L feature size 21
103 KEAN STEVEN J feature size 21
104 TOTAL feature size 21
105 FOWLER PEGGY feature size 21
106 WASAFF GEORGE feature size 21
107 WHITE JR THOMAS E feature size 21
108 CHRISTODOULOU DIOMEDES feature size 21
109 ALLEN PHILLIP K feature size 21
110 SHARP VICTORIA T feature size 21
111 JAEDICKE ROBERT feature size 21
112 WINOKUR JR. HERBERT S feature size 21
113 BROWN MICHAEL feature size 21
114 BADUM JAMES P feature size 21
115 HUGHES JAMES A feature size 21
116 REYNOLDS LAWRENCE feature size 21
117 DIMICHELE RICHARD G feature size 21
118 BHATNAGAR SANJAY feature size 21
119 CARTER REBECCA C feature size 21
120 BUCHANAN HAROLD G feature size 21
121 YEAP SOON feature size 21
122 MURRAY JULIA H feature size 21
123 GARLAND C KEVIN feature size 21
124 DODSON KEITH feature size 21
125 YEAGER F SCOTT feature size 21
126 HIRKO JOSEPH feature size 21
127 DIETRICH JANET R feature size 21
128 DERRICK JR. JAMES V feature size 21
129 FREVERT MARK A feature size 21
130 PAI LOU L feature size 21
131 BAY FRANKLIN R feature size 21
132 HAYSLETT RODERICK J feature size 21
133 FUGH JOHN L feature size 21
134 FALLON JAMES B feature size 21
135 KOENIG MARK E feature size 21
136 SAVAGE FRANK feature size 21
137 IZZO LAWRENCE L feature size 21
138 TILNEY ELIZABETH A feature size 21
139 MARTIN AMANDA K feature size 21
140 BUY RICHARD B feature size 21
141 GRAMM WENDY L feature size 21
142 CAUSEY RICHARD A feature size 21
143 TAYLOR MITCHELL S feature size 21
144 DONAHUE JR JEFFREY M feature size 21
145 GLISAN JR BEN F feature size 21

'''