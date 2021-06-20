from url_scraping import get_urls, is_valid_url
import os
import wget
from datetime import datetime

# urls = get_urls()

urls = ['https://i.redd.it/6se14k41od671.png', 'https://i.redd.it/gk2bi6yvre671.jpg', 'https://i.redd.it/7pbcxhep3g671.png', 'https://i.redd.it/qzwl491dza671.jpg', 'https://i.redd.it/2y0u9067hg671.png']

path = '/mnt/c/Users/Anthony/OneDrive/Pictures/Backgrounds/'
os.chdir(path)

existing_files = set()
existing_dirs = set()

for _, dirs, files in os.walk(os.curdir):
    for fi in files:
       existing_files.add(fi) 
    for directory in dirs:
        existing_dirs.add(directory)


print(existing_dirs)
print(existing_files)

date = datetime.now().strftime('%Y.%m.%d')

if date not in existing_dirs:
    print('todays date not made')
    os.mkdir(path + date)
else:
    print('todays date already made')


os.chdir(path + date)
print(os.getcwd())
exit()


for url in urls:
    filename, extension = url.split('/')[-1].split('.')
    print(f'{filename=}{extension=}')


# wget.download(url, out='filenametest.png')


