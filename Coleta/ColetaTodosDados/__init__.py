import requests
import json

def coletarDados():
    request = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2025-01-01&end_date=2025-01-02&api_key=P7KEdXGBmocOHXDskhaM00nZPFAkLhzCLPixSlDx")
    dadosJson = json.loads(request.content)
    return dadosJson
