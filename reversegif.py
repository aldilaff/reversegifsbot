# help from: https://www.reddit.com/r/Python/comments/2angq5/ffmpeg_how_to_get_frames_from_gifvideo/

from moviepy.editor import VideoFileClip
from moviepy.video.fx.time_mirror import time_mirror
from numpy import fliplr
from config import *
from imgurpython import ImgurClient
from os import remove
import praw



def reverseGif(gifUrl):
	client = ImgurClient(imgur_client_id, imgur_client_secret)
	gifToBeReversed = gifUrl #can be either gif or url to a gif
	reversedGifFileName = 'reversed.gif'
	clip = VideoFileClip(gifToBeReversed)
	clip = clip.fx(time_mirror)
	clip.write_gif(reversedGifFileName)
	print("Uploading image... ")
	imageURL = client.upload_from_path(reversedGifFileName, config=None, anon=False)
	print("Done")
	print()
	print("Image was posted! Go check your images you sexy beast!")
	print(imageURL)
	print("You can find it here: {0}".format(imageURL['link']))
	print("Deleting gif")
	remove(reversedGifFileName)
	print("gif deleted")

def main():
    r = praw.Reddit(user_agent='Reverse gif bot by /u/aldilaff')
    r.login(reddit_username, reddit_password)
	# r.send_message('aldilaff', 'Test1', 'You are awesome!')
    reverseGif('http://i.imgur.com/Z5mi7mI.gif')
if __name__ == "__main__":
    main()
