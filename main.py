import urllib
import requests
from bs4 import BeautifulSoup

def text_format(resp):
    #Success if Status code is 200
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        print(soup.prettify())
        #update here
        results = []
        for g in soup.find_all('div', class_='r'):
            anchors = g.find_all('a')
            if anchors:
                link = anchors[0]['href']
                title = g.find('h3').text
                item = {
                    "title": title,
                    "link": link
                }
                results.append(item)
        #print(results)

def main():
    query = 'Hoang Bui'.replace(' ', '+')

    #urls for search engines (can add more to list)
    goog = f'https://google.com/search?q={query}'
    #bing = f'https://www.bing.com/search?q={query}'
    #duck = f'https://duckduckgo.com/?q={query}'

    s_engines = [goog]

    #Google returns different search results for mobile vs. desktop https://hackernoon.com/how-to-scrape-google-with-python-bo7d2tal
    #desktop user-agent
    DESK_USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    #mobile user-agent
    MOBILE_USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

    #for URL in s_engines:
    headers = {"user-agent" : MOBILE_USER_AGENT}
    text_format(requests.get(goog, headers=headers))

if __name__ == "__main__":
    main()