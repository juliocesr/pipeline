import requests
import json

def coletarDados():
    request = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2015-09-07&end_date=2015-09-08&api_key=P7KEdXGBmocOHXDskhaM00nZPFAkLhzCLPixSlDx")
    dadosJson = json.loads(request.content)
    print(dadosJson)
