import shlex, subprocess
import re
import os

def Number_images(route_images):
	
	path, dirs, files = os.walk(route_images).__next__()
	N = len(files)

	return N




def Audio_festival(route_text,route_audio,text,language,N):
  
 	#from text generating audio files with festival 
	for i in range(N):
		command_line = 'text2wave '+route_text+'/'+text[i]+' -o '+route_audio+'/0%d.wav'%i #language !!
         
		args = shlex.split(command_line)
		subprocess.Popen(args).communicate()





def Duration(N,route_images,route_audio,img):
    
    #generates a file with the duration of each audio, with the format specified by ffmpeg

	f= open('Duration.txt','w')
	f.write('ffconcat version 1.0\n')
        for i in range(N):
    		f.write('file '+route_images+'/'+img[i]+' \n')
    		process = subprocess.Popen(['ffmpeg',  '-i',route_audio+'/0%d.wav'%i], stdout=subprocess.PIPE, 			stderr=subprocess.STDOUT)
    		out,_ = process.communicate()
    		result = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),",out.decode	('utf-8'), re.DOTALL).groupdict()
    		f.write('duration  '+result['seconds']+'\n')
	f.close()



