# help from: https://www.reddit.com/r/Python/comments/2angq5/ffmpeg_how_to_get_frames_from_gifvideo/

from config import *
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
	print("You can find it here: {0}".format(imageURL))
	return imageURL["gfyName"]

def main():
    r = praw.Reddit(user_agent='Reverse gif bot by /u/aldilaff')
    r.login(reddit_username, reddit_password)

    while True:
	    for msg in r.get_unread(limit=None):
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
	    print('Sleeping for 3 seconds...')
	    time.sleep(3)
if __name__ == "__main__":
    main()
