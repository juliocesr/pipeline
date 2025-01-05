import requests
import json

def coletarDados():
    request = requests.get("https://api.nasa.gov/neo/rest/v1/feed?start_date=2024-12-31&end_date=2025-01-05&api_key=P7KEdXGBmocOHXDskhaM00nZPFAkLhzCLPixSlDx")
    dadosJson = json.loads(request.content)
    return dadosJson
