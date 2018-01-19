import shlex, subprocess
import re
import os 
#import text_to_audio


def Image_Video():
	#Generating video from images and archive duration
	command_line ='ffmpeg -i Duration.txt  -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2"  Video0.mp4'
	args = shlex.split(command_line)	
	subprocess.Popen(args).communicate()


Image_Video()

#N
def U_Audios():
#Union of audios
	f= open('Aud.txt','w') 
	path, dirs, files = os.walk("tests/img").__next__()
	N = len(files)
	for i in range(1,N+1):
	    f.write('file tests/audio/0%d.wav \n'%i)
	f.close()
	command_line ='ffmpeg -f concat -safe 0 -i Aud.txt -c copy tests/audio/audio.wav'
	args = shlex.split(command_line)
	subprocess.Popen(args).communicate()

U_Audios()

#Concatenate Video with Audio

def Video_U_Audio():
	command_line ='ffmpeg -i Video0.mp4 -i tests/audio/audio.wav -strict -2 Video00.mp4'
	args = shlex.split(command_line)
	subprocess.Popen(args).communicate()

Video_U_Audio()



