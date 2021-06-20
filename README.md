# Daily wallpaper update from reddit.

One day project idea:

- download the top rated reddit/r/wallpapers images to OneDrive folder, sort by date downloaded.


steps:
1. Use requests/bs4 to grab page info
2. Get the href for the top rater comment pictures
3. Download the image to backgrounds/todays-date folder
4. Set image as desktop background


TODOs:
	* issues:
		** Step 4 doesn't seem to be able to be done through wsl.  I will need to use windows python for this step?
		** could have better naming convention for the filenames (use post title?)  Issue with this might be conflicts if two posts have the same name. 
