#!/mnt/c/Python39/python.exe

import ctypes

SPI_SETDESKWALLPAPER = 20
directory = r'C:\Users\Anthony\OneDrive\Pictures\Backgrounds'
img_path = directory + r'\momo-by-ilya-kuvshinov-2560×1440.jpg' 

print(img_path)

ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, img_path , 0)
