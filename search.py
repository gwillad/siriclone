import urllib
import simplejson
import sys
from subprocess import call
from HTMLParser import HTMLParser

enumeration_strings = ["first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eigth", "ninth", "tenth"]

class MLStripper(HTMLParser):
    def __init__(self):
        self.reset()
        self.fed = []
    def handle_data(self, d):
        self.fed.append(d)
    def get_data(self):
        return ''.join(self.fed)

def strip_tags(html):
    s = MLStripper()
    s.feed(html)
    return s.get_data()

def format_lisp_query(lst):
  result = ""
  for string in lst:
    result += string + " "
  result.strip()
  return result

#query = raw_input("Please enter you query: ")

query = sys.argv[2:] # eliminate "google"
query = format_lisp_query(query)
query = urllib.urlencode({'q':query})
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % (query)
search_results = urllib.urlopen(url)

json = simplejson.loads(search_results.read())
#print json


#exit(0)

results = json['responseData']['results']

i=0
for result in results:
  print "The " + enumeration_strings[i] + " result I have gathered for you is:"
  i = i+1
  print strip_tags(result['title']) + " : " + result['url']
  answer = raw_input("If you would like to visit this URL please type 'yes' (any other entry for no or none to quit): ")
  if answer == "yes":
    call(["firefox", result['url']])
  elif answer == "none":
    exit(0)
  
