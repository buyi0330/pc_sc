# -*- coding: utf-8 -*-
"""
Created on Tue Jul  9 16:57:48 2019

@author: Yi Bu
"""

import os
import json
import io

targetEvent_list = ["PushEvent", "PullRequestEvent", "PullRequestReviewEvent", "PullRequestReviewCommentEvent", "PushEvent", "ForkEvent", "DownloadEvent", "CommitCommentEvent"]
directory_1 = "/kellogg/proj/ybo1623/github_raw"
directory_2 = "/kellogg/proj/ybo1623/github_processed"
#directory_1 = "C:/Users/Yi Bu/Desktop"
#directory_2 = "C:/Users/Yi Bu/Desktop/111"
for filename in os.listdir(directory_1):

    if filename.endswith(".json"):
        outFile = io.open(str(directory_2) + '/' + str(filename), "w", encoding = "utf8")
        with io.open(directory_1 + "/" + filename, "r", encoding = "utf8") as json_file:
            for line in json_file:
                line = line.strip()
                data = json.loads(line)
                if data["type"] in targetEvent_list:
                    outFile.write(line + "\n")