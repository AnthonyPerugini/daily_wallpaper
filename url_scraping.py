import requests
from bs4 import BeautifulSoup

def is_valid_url(text):
    if not text: return False
    return (text.endswith('.jpg') or text.endswith('.png')) and text.startswith('https://i.redd.it/')

def get_urls():
    url = 'https://www.reddit.com/r/wallpapers'
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
    print('parsing wallpapers..')

    r = requests.get(url, headers=headers)
    soup = BeautifulSoup(r.content, 'html.parser')

    links = soup.find_all('a')
    seen = set()

    for link in links:
        href = link.get('href')
        if not href:
            continue
        if href.startswith('/r/wallpapers/comments/') and href not in seen:
            seen.add(href)

    base_url = 'https://www.reddit.com'
    background_urls = []

    count = 1
    for thread in seen:
        if count > 5:
            break
        print(f'parsing: #{count}', base_url, thread)
        r = requests.get(base_url + thread, headers=headers)
        print(r.status_code)

        soup = BeautifulSoup(r.content, 'html.parser')
        links = soup.find_all('a')
        links = set(link.get('href') for link in links if is_valid_url(link.get('href')))
        if len(links) != 1:
            print('bad link, skipping...')
            continue

        background_urls.append(links.pop())
        count += 1

    return background_urls
