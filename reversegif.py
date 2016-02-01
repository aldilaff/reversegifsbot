# help from: https://www.reddit.com/r/Python/comments/2angq5/ffmpeg_how_to_get_frames_from_gifvideo/

from moviepy.editor import VideoFileClip
from moviepy.video.fx.time_mirror import time_mirror
from numpy import fliplr
from config import *
from imgurpython import ImgurClient
from imgurpython.helpers.error import ImgurClientError
from os import remove
import praw
import time
import requests
import json
import pprint
from gfycat.client import GfycatClient
from gfycat.error import GfycatClientError


def reverseGif(gifUrl):
	imageURL = None
	client = GfycatClient()
	try:
		imageURL= client.upload_from_url(gifUrl)
	except GfycatClientError as e:
	    print(e.error_message)
	    print(e.status_code)
	print("Done")
	print()
	print("Image was posted! Go check your images you sexy beast!")
	# print("You can find it here: {0}".format(imageURL['link']))
	print("You can find it here: {0}".format(imageURL))
	return imageURL["gfyName"]

def main():
    r = praw.Reddit(user_agent='Reverse gif bot by /u/aldilaff')
    r.login(reddit_username, reddit_password)
	# r.send_message('aldilaff', 'Test1', 'You are awesome!')

    while True:
	    for msg in r.get_unread(limit=None):
	    	# if msg.is_root:
	    	# 	print('comment is a root')
	    	time.sleep(2)
	    	print('Message: %s' % msg)
	    	print('Message link: %s' % msg.permalink)
	    	time.sleep(2)
	    	submission = r.get_submission(msg.permalink)
	    	print(submission.url)
	    	reversedGifUrl = reverseGif(submission.url)
	    	time.sleep(2)
	    	print('reversed https://gfycat.com/%s#?direction=reverse' % reversedGifUrl)
	    	msg.reply('reversed https://gfycat.com/%s#?direction=reverse' % reversedGifUrl) #reply to comment
	    	print('Replied to message')
	    	time.sleep(2)
	    	msg.mark_as_read()
	    	print('Marked message as read')
	    #reverseGif('http://i.imgur.com/Z5mi7mI.gif')
	    print('Sleeping for 3 seconds...')
	    time.sleep(3)
if __name__ == "__main__":
    main()
