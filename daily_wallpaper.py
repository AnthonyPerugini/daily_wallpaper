from url_scraping import get_urls, is_valid_url
import os
import wget
from datetime import datetime

# urls = get_urls()
urls = ['https://i.redd.it/6se14k41od671.png', 'https://i.redd.it/gk2bi6yvre671.jpg', 'https://i.redd.it/7pbcxhep3g671.png', 'https://i.redd.it/qzwl491dza671.jpg', 'https://i.redd.it/2y0u9067hg671.png']

backgrounds_path = '/mnt/c/Users/Anthony/OneDrive/Pictures/Backgrounds/'

existing_files = set()
existing_dirs = set()

for _, dirs, files in os.walk(backgrounds_path):
    for fi in files:
       existing_files.add(fi) 
    for directory in dirs:
        existing_dirs.add(directory)

print(existing_dirs)
print(existing_files)

date = datetime.now().strftime('%Y.%m.%d')
if date not in existing_dirs:
    print('creating todays date folder')
    os.mkdir(backgrounds_path + date)
else:
    print('todays date already made, adding')


os.chdir(backgrounds_path + date)
print(os.getcwd())

failed = 0
for url in urls:
    filename = url.split('/')[-1]
    print(f'{filename=}')
    if filename not in existing_files:
        wget.download(url, out=os.getcwd())
        print()
    else:
        print('file already found in existing_files, skippping...')
        failed += 1


print(f'Successfully downloaded {len(urls) - failed}/{len(urls)} images ({(len(urls) - failed) / len(urls) * 100}%)')
