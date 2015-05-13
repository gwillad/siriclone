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

app_id = 'Q59EW4-7K8AHE858R'
"App ID for testing this project. Please don't use for other apps."

answer_leads = ["The answer you are looking for is ", "I think you wanted ", "You were looking for "]

def test_basic():
	client = wolframalpha.Client(app_id)
	res = client.query('30 deg C in deg F')
        print res
	assert len(res.pods) > 0
	results = list(res.results)
	assert results[0].text == '86 °F  (degrees Fahrenheit)'
	print results[0].text

def test_invalid_app_id():
	client = wolframalpha.Client('abcdefg')
	with pytest.raises(Exception):
		client.query('30 deg C in deg F')


client = wolframalpha.Client(app_id)
query_wolf = raw_input()
res = client.query(query_wolf)
results = list(res.results)

if len(results) != 0:
    print random.choice(answer_leads) + results[0].text
else:
    print "I can't find anything on what you are looking for right now. Let me try and find some web pages that may help you"
