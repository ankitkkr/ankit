from PIL import ImageGrab
import numpy as np
import cv2
from win32api import GetSystemMetrics
import datetime


#generate the dimensions of system
width = GetSystemMetrics(0)
height = GetSystemMetrics(1)

#recording time_stamp
time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
#specifying filename as the time its recording
file_name = f'output_{time_stamp}.mp4'
#export file format (mp4)
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
capture_video = cv2.VideoWriter(file_name,fourcc,20.0,(width,height))

#capture everything until the loop breaks
while True:
	#record the screen as per the dimention provided
    img = ImageGrab.grab(bbox = (0,0,width,height))
    img_np = np.array(img)
    #colour correction
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    #savefile
    capture_video.write(img_final)
    #showing what is being recorded
    cv2.imshow('screen_recording', img_final)
    #stops recording when pressed "="
    if cv2.waitKey(10) == ord('='):
    	break