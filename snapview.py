#! /usr/bin/python
# -*- coding: utf-8 -*-

import cv
import sys
import getopt
import os

def usage(param=''):
	if param:
		print param

	print 'Usage: '+sys.argv[0]+' [-t TIME] [-f] FILE'

def die(param=''):
	usage(param)
        sys.exit()

def clear_tmpfiles():
    filelist = glob.glob(imagefile + "*.jpg")
    for f in filelist:
        os.remove(f)	

        
if __name__ == '__main__':
	
	follow = False
	timelapse = 5
	title="snapview"

	try:
		opts, img_files = getopt.getopt(sys.argv[1:], "hft:", ["help", "follow", "time="])
	except getopt.GetoptError:
		die()
                sys.exit(2)

	for opt, arg in opts:
		if opt in ("-h", "--help"):
			die()
		elif opt in ( "-f", "--follow"):
			follow = True
		elif opt in ( "-t", "--time"):
			timelapse = int(arg)

	if not img_files:
		die()

#	img_file = img_files[0]
	(x, y) = (0, 0)
	cv.MoveWindow(title, x, y)
	runShow = True
	while runShow:
		for img_file in img_files:
			if runShow:
				if not os.path.isfile(img_file):
					usage(img_file+" not found")
				else:
		
					#print img_file

				        image_cv = cv.LoadImage(img_file)
					cv.ShowImage(title, image_cv)
					c = cv.WaitKey(timelapse*1000) % 256
					if c == 27:
						# ESC pressed. Finish the program
						follow = False
						runShow = False
	
		runShow = follow
		

	cv.DestroyWindow(title)

