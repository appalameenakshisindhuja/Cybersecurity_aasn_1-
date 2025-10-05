import requests
from bs4 import BeautifulSoup

url = "http://127.0.0.1:5500/CS/index.html"
# Add headers to mimic a browser request
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) ' 
                  'AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/117.0.0.0 Safari/537.36'
}

response = requests.get(url, headers=headers)
html_content = response.content

soup = BeautifulSoup(html_content, 'html.parser')

dns_prefetch_links = soup.find_all('link', rel='dns-prefetch')

if dns_prefetch_links:
    for link in dns_prefetch_links:
        print(link.get('href'))
else:
    print('No dns-prefetch link tags found.')
