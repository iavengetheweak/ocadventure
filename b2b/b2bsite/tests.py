from django.test import TestCase
import requests

import sys
sys.path.append('/Users/preston/Documents/Programs/teamproject/checkmate_library')
sys.path.append('../checkmate_library/parsers.json')

from Checkmate import *

name = "Jacob"
pword = "!password"
query = site_book_data(None)
query.book_dictionary["book_title"] = "Harry Potter"
query.book_dictionary["ready_for_sale"] = True

response = requests.post("http://127.0.0.1:8000/b2b/search/request/", {"query":query, "name": name, "pword": pword})
print("\n\nResults: "+str(response.content))