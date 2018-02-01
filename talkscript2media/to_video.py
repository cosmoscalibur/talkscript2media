import shlex
import subprocess
import time


def Image_Video(r_video):
    
    # Generating video from images and archive duration with ffmpeg
    
    
    log = open('process.log', 'a')
    log.write('Image_Video\n')
    log.flush()  
    print('Image to video...')
    command_line = 'ffmpeg -i Duration.txt -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2"  '+r_video+'/Video0.mp4'
    args = shlex.split(command_line)
    c = subprocess.Popen(args, stdout=log, stderr=log)


def U_Audios(N,route_audio):
    
    log = open('process.log', 'a')
    log.write('U_Audios\n')
    log.flush()
    print('Concatenating audios')
    
    # Union of audios generated with Audio_festival()
    # Necessary file for input to ffmpeg for audio union
    
    f = open('Aud.txt', 'w')
    for i in range(N):
        f.write('file '+route_audio+'/0%d.wav \n'%i)
    f.close()
    command_line = 'ffmpeg -f concat -safe 0 -i Aud.txt -c copy ' + route_audio \
        + '/audio.wav'
    args = shlex.split(command_line)
    #file_log=subprocess.Popen(args).communicate()
    c = subprocess.Popen(args, stdout=log, stderr=log)


def Video_U_Audio(route_audio, route_video, name_video):
    
    #Concatenate video obtained in Image_Video() and audio obtained in  U_Audios().
   
    log = open('process.log', 'a')
    log.write('Video_U_Audio\n')
    log.flush() 
    print('Video.............')
    
    command_line = 'ffmpeg -i '+route_video+'/Video0.mp4 -i '+route_audio+'/audio.wav -strict -2 '+route_video+'/'+name_video
    args = shlex.split(command_line)
    c = subprocess.Popen(args,stdout=log, stderr=log).communicate()
    




