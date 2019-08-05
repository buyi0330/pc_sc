# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:55:21 2019

@author: Yi Bu
"""
import json
import matplotlib.pyplot as plt
import ast
from collections import Counter

# Given a dictionary, return x_list as its key list, and y_list as its value list (correspondingly)
def dic_plot (dic):
    x_list = []
    y_list = []
    for item in dic.keys():
        x_list.append(item)
        y_list.append(dic[item])
    return x_list, y_list


inFile = open("/kellogg/proj/ybo1623/temp_descriptive.txt", "r")
inFile.readline()
inFile.readline()

date_pushCount = {}
date_pullCount = {}
date_forkCount = {}
repo_pushCount = []
repo_pullCount = []
repo_forkCount = []
repo_userCount = []

count = 3
for line in inFile:
    print count
    if count == 3:
        line.replace("'", "\"")
        date_pushCount = ast.literal_eval(line)
    elif count == 4:
        line.replace("'", "\"")
        date_pullCount = ast.literal_eval(line)
    elif count == 5:
        line.replace("'", "\"")
        date_forkCount = ast.literal_eval(line)
    elif count == 7:
        line = line.strip().split(",")
        for index in range(len(line) - 1):
            repo_pushCount.append(int(line[index]))
        for index in range(100):
            print repo_pushCount[index]
    '''
    elif count == 8:
        line = line.strip().split(",")
        for index in range(len(line) - 1):
            repo_pullCount.append(int(line[index]))
    elif count == 9:
        line = line.strip().split(",")
        for index in range(len(line) - 1):
            repo_forkCount.append(int(line[index]))
    elif count == 10:
        line = line.strip().split(",")
        for index in range(len(line) - 1):
            repo_userCount.append(int(line[index]))
    '''
    count += 1


    
print "Plotting 1st..."
push_dist = Counter(repo_pushCount)
plt.plot(push_dist, "r+", markersize = 1)
plt.title("Distribution: Number of pushes in a repo")
plt.xlabel("number of pushes")
plt.ylabel("number of repos with the corresponding number of pushes")
plt.xscale("log")
plt.yscale("log")
plt.savefig("/kellogg/proj/ybo1623/push distribution.jpg", dpi = 600)