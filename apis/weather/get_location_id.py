import pywapi
import pprint
from sys import argv

script, locale = argv
pp = pprint.PrettyPrinter(indent=4)

loc_id = pywapi.get_loc_id_from_weather_com(locale)

pp.pprint(loc_id)
