import requests
from bs4 import BeautifulSoup

def is_valid_href(text):
    if not text: 
        return False
    return (text.endswith('.jpg') or text.endswith('.png')) and text.startswith('https://i.redd.it/')

def get_hyperlinks(html_data):
    soup = BeautifulSoup(html_data, 'html.parser')
    return soup.find_all('a')


def get_urls():
    base_url = 'https://www.reddit.com/'
    wallpapers_url = 'r/wallpapers'

    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

    print('parsing wallpapers..')
    r = requests.get(base_url + wallpapers_url, headers=headers)
    links = get_hyperlinks(r.content)

    seen = set()
    for link in links:
        href = link.get('href')
        if not href:
            continue
        if href.startswith('/r/wallpapers/comments/') and href not in seen:
            seen.add(href)

    background_urls = []

    count = 1
    for thread in seen:
        if count > 5:
            break
        print(f'parsing: #{count}', base_url, thread)
        r = requests.get(base_url + thread, headers=headers)
        if r.status_code != 200:
            print(f'request failed with error code {r.status_code}, skipping...')
            continue

        links = get_hyperlinks(r.content)

        links = set(link.get('href') for link in links if is_valid_href(link.get('href')))
        if len(links) != 1:
            print('bad link, skipping...')
            continue

        background_urls.append(links.pop())
        count += 1

    return background_urls
