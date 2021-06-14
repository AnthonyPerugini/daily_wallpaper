# Daily wallpaper update from reddit.

One day project idea:

- download the top rated reddit/r/wallpapers image, and set it as my background.


steps:
1. connect to selenium controlled webbrowser OR use requests/bs4 to grab page info
2. get the src for the top rater comment picture
3. download the image to backgrounds folder (name format: Title-Date)
4. set image as desktop background


CODE NOTES:
import ctypes
SPI_SETDESKWALLPAPER = 20
img_path = r'C:\Users\Anthony\OneDrive\Pictures\Backgrounds\momo-by-ilya-kuvshinov-2560×1440.jpg'
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img_path , 0)

windows python path = C:\Python39\python.exe



import requests
from bs4 import BeautifulSoup

r = request.get('http://www.reddit.com/r/wallpapers')
soup = BeautifulSoup(r.text, 'html.parser')

for post in soup.find_all('img'):
...  print(post.get('src'))
