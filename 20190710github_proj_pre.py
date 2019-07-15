# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:57:48 2019

@author: Yi Bu
"""

import os
import json

targetEvent_list = ["PushEvent", "PullRequestEvent", "PullRequestReviewEvent", "PullRequestReviewCommentEvent", "PushEvent", "ForkEvent", "DownloadEvent", "CommitCommentEvent"]
directory_1 = "/kellogg/proj/ybo1623/github_raw"
directory_2 = "/kellogg/proj/ybo1623/github_processed"
for filename in os.listdir(directory_1):
    if filename.endswith(".json"): 
        outFile = open(str(directory_2) + str(filename), "w")
        with open(filename, "r") as json_file:
            for line in json_file:
                line = line.strip()
                data = json.load(line)
                if data["type"] in targetEvent_list:
                    outFile.write(line)