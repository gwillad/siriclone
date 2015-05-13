#-*- coding: utf-8 -*-
###################################################################
# Casey Collins, Adam Gwilliam, Zach Arnold
# wolfram_alpha_api.py
# This will call and search the wolfram alpha api
###################################################################



from __future__ import unicode_literals

import pytest
import random
import wolframalpha
from sys import argv



app_id = 'Q59EW4-7K8AHE858R'
"App ID for testing this project. Please don't use for other apps."

answer_leads = ["The answer you are looking for is ", "I think you wanted ", "Hi, I'm pretty sure you were looking for "]

arithmetic_leads = ["The answer to problem you asked is ", "The solution to your arithmetic query is "]

client = wolframalpha.Client(app_id)

def arithmetic_query(query):
    res = client.query(query_wolf)
    results = list(res.results)
    if len(res.pods) > 0:
        print random.choice(arithmetic_leads) + results[0].text
    else:
        print "I can't find anything on what you are looking for right now. Let me try and find some web pages that may help you"

def normal_query(query):
    res = client.query(query_wolf)
    results = list(res.results)
    if len(res.pods) > 0:
        print random.choice(answer_leads) + results[0].text
    else:
        print "I can't find anything on what you are looking for right now. Let me try and find some web pages that may help you"
    
query_wolf = " ".join(argv[1:])

if any((c in "=-/*^") for c in query_wolf):
    arithmetic_query(query_wolf)
else:
    normal_query(query_wolf)
