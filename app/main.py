import http.client
import json

#Function to obtain query
def obtain_query():
    name = input('Input your full name\n')
    country = input('Input your country (leave blank if not needed)\n')
    extra = input("Input other query params that you like to add (put space in between)\n")

    return name.replace(' ', '+') + "+" + country.replace(' ', '+') + "+" + extra.replace(' ', '+')


#Function to query google
def goog_search(query):
    conn = http.client.HTTPSConnection('google-search3.p.rapidapi.com')

    headers = {
        'X-User-Agent': 'desktop',
        'X-Proxy-Location': 'CA',
        'X-RapidAPI-Key': '{insert key}',
        'X-RapidAPI-Host': 'google-search3.p.rapidapi.com'
        }

    conn.request('GET', '/api/v1/search/q='+query+'&num=100', headers=headers)

    res = conn.getresponse()
    data = json.loads(res.read().decode('utf-8'))
    #print(data)
    return data.get('results')

def main():
    query = obtain_query()

    #query results
    goog = goog_search(query)
    #more to be added in the future

    results = [goog]

    for result in results:
        for item in result:
            print(item)
            print('\n')

if __name__ == "__main__":
    main()