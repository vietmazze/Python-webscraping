#!/usr/bin/env python
# -*- coding: utf-8 -*-

#Our main module will be PRAW, you can search online for more info
import praw
import json
import csv
import itertools


#Reddit api requires login
reddit = praw.Reddit(client_id='#######',
                     client_secret='############',
                     user_agent='testscript by /u/yourname',
                     username='#########',
                     password='###############')

#This will confirm you are authenticated
print(reddit.user.me())

#This is one of the method in PRAW, using subreddit called Waltonchain
subreddit=reddit.subreddit('waltonchain')

# We are writing to csv file
with open('walton.csv','w',newline='') as f:
    writer=csv.writer(f)

# For loop allow us to limit what we want, in this case PRAW subbmission.title will give out title of the post and so on..    
    
    for submission in reddit.subreddit('waltonchain').hot(limit=10):
            title=submission.title
            url=submission.url
            author=submission.author
           
          #This will write out 3 columns that we wanted.  
           writer.writerow([title,url,author])
