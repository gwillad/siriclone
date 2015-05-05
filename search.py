import urllib
import simplejson
import sys

def format_lisp_query(lst):
  result = ""
  for string in lst:
    result += string + " "
  result.strip()
  return result

#query = raw_input("Please enter you query: ")
query = sys.argv[1:]
query = format_lisp_query(query)
query = urllib.urlencode({'q':query})
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % (query)
search_results = urllib.urlopen(url)

json = simplejson.loads(search_results.read())
results = json['responseData']['results']
for item in results:
  print item['title'] + ": " + item['url']
