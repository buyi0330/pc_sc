# -*- coding: utf-8 -*-
"""
Created on Fri Jul 26 14:10:53 2019

@author: Yi Bu
"""
from collections import defaultdict

keyword_list = ["causal inference", "propensity score", "potential outcome", "potential outcomes", "causality"
                ,"counterfactual", "counterfactuals", "causation", "causal effect", "causal effects"]

print "1. paper"
paper_file = open("/home/buyi/Desktop/wos/wos_paper.txt", "r")
paper_file.readline()
str_int = {}
int_str = {}
for line in paper_file:
    line = line.strip().split("======")
    str_int[line[0]] = int(line[1])
    int_str[int(line[1])] = line[0]

print "2. year"
year_file = open("/home/buyi/Desktop/wos/wos_year.txt", "r")
year_file.readline()
int_year = {}
for line in year_file:
    line = line.strip().split("======")
    int_year[int(line[0])] = int(line[1])

print "3. citing"
citing_file = open("/home/buyi/Desktop/wos/wos_citing.txt", "r")
citing_file.readline()
citing_cited = defaultdict(list)
cited_citing = defaultdict(list)
for line in citing_file:
    line = line.strip().split("======")
    citing_cited[int(line[1])].append(int(line[0]))
    cited_citing[int(line[0])].append(int(line[1]))

print "4. journal"
journal_file = open("/home/buyi/Desktop/wos/wos_journal.txt", "r")
journal_file.readline()
int_journal = {}
for line in journal_file:
    line = line.strip().split("======")
    if line[1] == "1":
        int_journal[int(line[0])] = line[2]

print "5. author"
author_file = open("/home/buyi/Desktop/wos/wos_author.txt", "r")
author_file.readline()
int_author = defaultdict(list)
for line in author_file:
    line = line.strip().split("======")
    int_author[int(line[0])].append(line[2])

print "6. doctype"
doctype_file = open("/home/buyi/Desktop/wos/wos_doctype.txt", "r")
doctype_file.readline()
int_doctype = {}
for line in doctype_file:
    line = line.strip().split("======")
    int_doctype[int(line[0])] = line[1]
    
print "7. title"
title_file = open("/home/buyi/Desktop/wos/wos_title.txt", "r")
title_file.readline()
int_title = {}
for line in title_file:
    line = line.strip().split("======")
    int_title[int(line[0])] = line[1]
    
print "8. subject"
subject_file = open("/home/buyi/Desktop/wos/wos_subject.txt", "r")
subject_file.readline()
int_subject = defaultdict(list)
for line in subject_file:
    line = line.strip().split("======")
    int_subject[int(line[0])].append(line[2])
    
print "9. keywords"
keywords_file = open("/home/buyi/Desktop/wos/wos_keywords.txt", "r")
keywords_file.readline()
int_keywords = {}
temp = []
for line in keywords_file:
    line = line.strip().split("======")
    if int(line[1]) == 1:
        temp.append(line[2])
        int_keywords[int(line[0])] = temp
        temp = []
    else:
        temp.append(line[2])

print "10. output_1"
outFile_1 = open("/home/buyi/Desktop/causal_pre.txt", "w")
outFile_1.write("int_id, wos_id, year, subject, doctype, journal, title, keywords\n")
for paper in int_str.keys():
    flag = 0
    for keyword in keyword_list:
        if keyword in int_keywords[paper]:
            flag = 1
    if flag == 1:
        temp = []
        temp.append(paper)
        temp.append(int_str[paper])
        temp.append(int_year[paper])
        temp.append(int_subject[paper])
        temp.append(int_doctype[paper])
        temp.append(int_journal[paper])
        temp.append(int_title[paper])
        temp.append(int_keywords[paper])
        outFile.write("======".join(temp) + "\n")

print "11. output_2"
outFile_2 = open("/home/buyi/Desktop/causal_pre_citation.txt", "w")
outFile_2.write("int_id_target, int_id_citation\n")
for paper in int_str.keys():
    flag = 0
    for keyword in keyword_list:
        if keyword in int_keywords[paper]:
            flag = 1
    if flag == 1:
        temp = []
        if len(citing_cited[paper]) > 0:
            for item in citing_cited[paper]:
                outFile_2.write(str(paper) + "======" + str(item) + "\n")

print "12. output_3"
outFile_3 = open("/home/buyi/Desktop/causal_pre_ref.txt", "w")
outFile_3.write("int_id_target, int_id_ref\n")
for paper in int_str.keys():
    flag = 0
    for keyword in keyword_list:
        if keyword in int_keywords[paper]:
            flag = 1
    if flag == 1:
        temp = []
        if len(cited_citing[paper]) > 0:
            for item in cited_citing[paper]:
                outFile_3.write(str(paper) + "======" + str(item) + "\n")