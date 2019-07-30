# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 18:37:21 2019

@author: Yi Bu
"""

import os
import json
import re
from collections import defaultdict
#import matplotlob.pyplot as plt

path = "/kellogg/proj/ybo1623/github_processed/"
files = []

date_push = {} # key: date, value: number of pushes in this date
date_pull = {}
date_fork = {}

repo_user = defaultdict(list) #key: repo id, value: the list of users contributing to it (and related events)

# read data
# r=root, d=directories, f = files
for r, d, f in os.walk(path):
    for file in f:
        curr_file = open(str(path) + str(file), "r")
        date = re.sub('.json', '', file)
        
        # initiliazation
        date_push[date] = 0
        date_pull[date] = 0
        date_fork[date] = 0
        
        for line in curr_file:
            line = line.strip()
            json_data = json.loads(line)
            
            # quantify number of different events in each date
            if json_data['type'] == "PushEvent":
                date_push[date] += 1
            elif json_data['type'] == "PullRequestEvent":
                date_pull[date] += 1
            elif json_data['type'] == "ForkEvent":
                date_fork[date] += 1
            
            # extract repo, push, pull, and user information
            temp = []
            temp.append(json_data['actor']['id'])
            temp.append(json_data['type'])
            repo_user[json_data['repo']['id']].append(temp) 

#process data
repo_push_count = []
repo_pull_count = []
repo_fork_count = []
repo_user_count = []

for repo in repo_user.keys():
    push_temp = 0
    pull_temp = 0
    fork_temp = 0
    for event in repo_user[repo]:
        if event[1] == "PushEvent":
            push_temp += 1
        elif event[1] == "PullRequestEvent":
            pull_temp += 1
        elif event[1] == "ForkEvent":
            fork_temp += 1
    repo_push_count.append(push_temp)
    repo_pull_count.append(pull_temp)
    repo_fork_count.append(fork_temp)
    repo_user_count.append(len(repo_user[repo]))

outFile = open("temp_descriptive.txt", "w")
outFile.write("\nnumber of events in different dates\n")
outFile.write(str(date_push) + "\n")
outFile.write(str(date_pull) + "\n")
outFile.write(str(date_fork) + "\n")
outFile.write("repo_push_count:\n")
outFile.write(",".join(item for item in repo_push_count))
outFile.write("\nrepo_pull_count:\n")
outFile.write(",".join(item for item in repo_pull_count))
outFile.write("\nrepo_fork_count:\n")
outFile.write(",".join(item for item in repo_fork_count))
outFile.write("\nrepo_user_count:\n")
outFile.write(",".join(item for item in repo_user_count))

# visualize data
# 2. distribution of number of pushes (pulls, forks) in a repo