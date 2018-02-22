import praw
import config
import time
import urllib.request
import ctypes

def LoginToReddit():
	print ("Logging in...")
	r = praw.Reddit(username = config.username,
            password = config.password,
            client_id = config.client_id,
            client_secret = config.client_secret,
            user_agent = "my first reddit bot test v0.1")
	print ("Log in complete")

	return r

def GetWallpaperUrlFromReddit(r):
	global CommentsRepliedTo
	print ("looking at posts")
	for post in r.subreddit('wallpaper').top('day'):	
		return post.url

def SaveImageFromUrl(url, filePath):
	print ("saving an image")
	urllib.request.urlretrieve(url, filePath)

def SetWallpaper(filePath):
	print ("setting the image")
	ctypes.windll.user32.SystemParametersInfoW(20, 0, filePath , 0)


creds = LoginToReddit()
url = GetWallpaperUrlFromReddit(creds)
filePath = "C:\\Users\\Mark Paradiso\\Documents\\wallpapers\\MostRecentImage.jpg"
SaveImageFromUrl(url, filePath)
SetWallpaper(filePath)