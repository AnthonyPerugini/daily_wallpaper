from wallpaper_scraper import get_urls
import os
import wget
from datetime import datetime

urls = get_urls()
backgrounds_path = '/mnt/c/Users/Anthony/OneDrive/Pictures/Backgrounds/'

existing_files = set()
existing_dirs = set()

for _, dirs, files in os.walk(backgrounds_path):
    for fi in files:
       existing_files.add(fi) 
    for directory in dirs:
        existing_dirs.add(directory)

date = datetime.now().strftime('%Y.%m.%d')

if date not in existing_dirs:
    print('creating todays date folder...')
    os.mkdir(backgrounds_path + date)

os.chdir(backgrounds_path + date)

failed = 0
for url in urls:
    filename = url.split('/')[-1]
    print(f'{filename=}')
    if filename not in existing_files:
        wget.download(url, out=os.getcwd())
        print('\n')
    else:
        print('file already found in existing_files, skippping...')
        failed += 1


print(f'Successfully downloaded {len(urls) - failed}/{len(urls)} images ({(len(urls) - failed) / len(urls) * 100}%)')
