_future__ import print_function
from __future__ import division
from builtins import input

from PIL import Image
import sys
import math
import pprint
import read_colors
from io import BytesIO
from subprocess import call
from time import sleep
from picamera import PiCamera

idealsize = (400,400)

def getrbg(channel):
	rgb=[]
	avgrgb=[] #average rgb
	for i in range(3):
		rgb.append(list(channel[i].getdata()))
		avgrgb.append(sum(rgb[i])/len(rgb[i]))
		print ("avg rgb:{}".format(avgrgb[i]))
	return (avgrgb[0],avgrgb[1],avgrgb[2])


def get_colors_from_file():
	global im
	im = Image.open("./{}.jpg".format(imagename))

def extract_color(im):
	# make image smaller to avoid noise
	# also makes it faster to study
	# local_im = im.resize(idealsize)

	local_im = im
	# print("Image size is {}".format(im.size))

	# take the central part which avoids lots of noise
	local_im = local_im.crop((im.size[0]//4,
				im.size[1]//4,
				im.size[0]*3//4,
				im.size[1]*3//4))
	# print("local_im size is {}".format(local_im.size))

	local_im.save("small.jpg")
	channel = local_im.split()

	

def identify_color(im):

	extractedrgb= extract_color(im)

	
	rgb_color = read_colors.identifycolor(extractedrgb)
	print("Color as identified by RGB is {}".format(rgb_color))
	


if __name__ == '__main__':


	tmp_img_name = "tmp.jpg"
	stream = BytesIO()
	camera = PiCamera()
	camera.resolution=(1280,720)
	camera.start_preview()
	sleep(2)

	cmd_beg= 'espeak -ven+f1 '
	#cmd_end= ' | aplay /home/pi/Desktop/Text.wav  2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
	cmd_end= ' 2>/dev/null' # To play back the stored .wav file and to dump the std errors to /dev/null
	last_color = ""

	i = 0
	if len(sys.argv) == 2 and sys.argv[1].upper() == "LEARN":
		while True:
			camera.capture(tmp_img_name)	
			im = Image.open(tmp_img_name)
			im_name = learn_color(im)
			im.save(im_name)
	elif len(sys.argv)==1:	
		while i==0:
			i+=1
			camera.capture(tmp_img_name)	
			im = Image.open(tmp_img_name)
			im.save("test.jpg")

			read_colors.read_colors_def()
			rgbstr = identify_color(im)
			print(rgbstr)
			
	
	camera.close()

