# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 13:55:21 2019

@author: Yi Bu
"""
import json
import matplotlib.pyplot as plt


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
        data = json.load(line)
        date_pushCount = json.loads(data)
    elif count == 4:
        data = json.load(line)
        date_pullCount = json.loads(data)
    elif count == 5:
        data = json.load(line)
        date_forkCount = json.loads(data)
    '''
    elif count == 7:
        line = line.strip().split(",")
        for index in range(len(line) - 1):
            repo_pushCount.append(int(line[index]))
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
    else:
        pass
    count += 1

print "Plotting 1st..."

x1, y1 = dic_plot(date_pushCount)
x2, y2 = dic_plot(date_pullCount)
x3, y3 = dic_plot(date_forkCount)
plt.plot(x1, y1, "r+", markersize = 1, label = "pushEvent")
plt.plot(x2, y2, "y+", markersize = 1, label = "pullRequestEvent")
plt.plot(x3, y3, "b+", markersize = 1, label = "forkEvent")
plt.title("Number of events over time")
plt.xlabel("date")
plt.ylabel("number of events")
plt.savefig("date_EventCount.jpg", dpi = 600)