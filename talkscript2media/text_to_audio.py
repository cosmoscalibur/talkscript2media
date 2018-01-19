import shlex, subprocess
import re
import os

def Number_images():
	
	path, dirs, files = os.walk("tests/img").__next__()
	N = len(files)

	return N



def Audio_festival():
 	#from text generating audio files with festival 
	for i in range(1,Number_images()+1):
		command_line = 'text2wave tests/text/0%d.txt'%i + ' -o tests/audio/0%d.wav'%i
		args = shlex.split(command_line)
		subprocess.Popen(args).communicate()


Audio_festival()

def Duration():

	f= open('Duration.txt','w')
	f.write('ffconcat version 1.0\n')
	for i in range(1,Number_images()+1):
    		f.write('file  tests/img/0%d.jpg \n'%i)
    		process = subprocess.Popen(['ffmpeg',  '-i','tests/audio/0%d.wav'%i], stdout=subprocess.PIPE, 			stderr=subprocess.STDOUT)
    		out,_ = process.communicate()
    		result = re.search(r"Duration:\s{1}(?P<hours>\d+?):(?P<minutes>\d+?):(?P<seconds>\d+\.\d+?),",out.decode	('utf-8'), re.DOTALL).groupdict()
    		f.write('duration  '+result['seconds']+'\n')
	f.close()

Duration()

Duration()

