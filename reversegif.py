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

def reverseGif(gifUrl):
	request = requests.get(gifUrl)
	chunk_size = 1024
	with open('gif.gif', 'wb') as fd:
		for chunk in request.iter_content(chunk_size):
			fd.write(chunk)
	client = ImgurClient(imgur_client_id, imgur_client_secret)
	gifToBeReversed = "gif.gif" #can be either gif or url to a gif
	reversedGifFileName = 'reversed.gif'
	print('getting gif')
	clip = VideoFileClip(gifToBeReversed)
	# print(clip.fps)
	# print(clip.duration)
	# print(ffmpeg_parse_infos(gifToBeReversed, True, True))
	# clip.duration = 15
	# print(clip.duration)
	# i=0
	# for frame in clip.iter_frames():
	# 	print(i)
	# 	i+=1
	# pp = pprint.PrettyPrinter(indent=4)
	# pp.pprint(clip)
	print('reversing gif')
	clip = clip.fx(time_mirror)
	clip.write_gif(reversedGifFileName)
	imageURL = None
	try:
		print("Uploading image... ")
		imageURL = client.upload_from_path(reversedGifFileName, config=None, anon=False)
	except ImgurClientError as e:
	    print(e.error_message)
	    print(e.status_code)
	print("Done")
	print()
	print("Image was posted! Go check your images you sexy beast!")
	print("You can find it here: {0}".format(imageURL['link']))
	print("Deleting gifs")
	remove('gif.gif')
	remove(reversedGifFileName)
	print("gif deleted")
	return imageURL['link']

def main():
    r = praw.Reddit(user_agent='Reverse gif bot by /u/aldilaff')
    r.login(reddit_username, reddit_password)
	# r.send_message('aldilaff', 'Test1', 'You are awesome!')
    # print('calling reverseGif()')
    # reverseGif('hlN3NZZ.gif')
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
	    	msg.reply('reversed %s' % reversedGifUrl) #reply to comment
	    	print('Replied to message')
	    	time.sleep(2)
	    	msg.mark_as_read()
	    	print('Marked message as read')
	    #reverseGif('http://i.imgur.com/Z5mi7mI.gif')
	    print('Sleeping for 3 seconds...')
	    time.sleep(3)
if __name__ == "__main__":
    main()
