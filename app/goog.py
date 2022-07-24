import http.client
import json

"""Class for obtaining and storing queries from google"""
class goog:

    def __init__(self, query):
        self.results = {}
        self.new_query(query)

    def get_results(self):
        return self.results
    
    def new_query(self, query):
        conn = http.client.HTTPSConnection('google-search3.p.rapidapi.com')
        headers = {
            'X-User-Agent': 'desktop',
            'X-Proxy-Location': 'CA',
            'X-RapidAPI-Key': '', #Keep personal key hidden
            'X-RapidAPI-Host': 'google-search3.p.rapidapi.com'
        }
        conn.request('GET', '/api/v1/search/q='+query+'&num=100', headers=headers)
        res = conn.getresponse()
        data = json.loads(res.read().decode('utf-8'))
        self.results = data.get('results')
