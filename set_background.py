#!/mnt/c/Users/anthony/AppData/Local/Programs/Python/Python39/python.exe
# Laptop

#!/mnt/c/Python39/python.exe
# Desktop

# from Browser import Browser
import ctypes


SPI_SETDESKWALLPAPER = 20
directory = r'C:\Users\Anthony\OneDrive\Pictures\Backgrounds'
img_path = directory + r'\momo-by-ilya-kuvshinov-2560×1440.jpg' 

print(img_path)

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img_path , 0)

url = 'http://www.reddit.com/r/wallpapers'


# browser = Browser()
# browser.open(url)
# browser.tearDown()



