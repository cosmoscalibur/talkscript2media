import shlex, subprocess
import re
import os 





def Image_Video():
	#Generating video from images and archive duration
	command_line ='ffmpeg -i Duration.txt  -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2"  Video0.mp4'
	args = shlex.split(command_line)	
	subprocess.Popen(args).communicate()
Image_Video()

def U_Audios(N,route_audio):
#Union of audios
	f= open('Aud.txt','w') 
	for i in range(N):
	    f.write('file '+route_audio+'/0%d.wav \n'%i)
	f.close()
	command_line ='ffmpeg -f concat -safe 0 -i Aud.txt -c copy '+route_audio+'/audio.wav'
	args = shlex.split(command_line)
	subprocess.Popen(args).communicate()



#Concatenate Video with Audio

def Video_U_Audio(route_audio,route_video,name_video):
	command_line ='ffmpeg -i Video0.mp4 -i '+route_audio+'/audio.wav -strict -2 '+route_video+'/'+name_video
	args = shlex.split(command_line)
	subprocess.Popen(args).communicate()





