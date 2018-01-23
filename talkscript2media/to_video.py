import shlex
import subprocess


def Image_Video():
    #Generating video from images and archive duration with ffmpeg
    #Each image appears the determined seconds
    command_line = 'ffmpeg -i Duration.txt -vf "scale=trunc(iw/2)*2:trunc(ih/2)*2" Video0.mp4'
    args = shlex.split(command_line)
    subprocess.Popen(args).communicate()


def U_Audios(N, route_audio):
    #Union of audios generated with Audio_festival()
    #Necessary file for input to ffmpeg for audio union
    f = open('Aud.txt', 'w')
    for i in range(N):
        f.write('file '+route_audio+'/0%d.wav \n'%i)
    f.close()
    command_line = 'ffmpeg -f concat -safe 0 -i Aud.txt -c copy ' + route_audio \
        + '/audio.wav'
    args = shlex.split(command_line)
    subprocess.Popen(args).communicate()


def Video_U_Audio(route_audio, route_video, name_video):
    #Concatenate video obtained in Image_Video() and audio obtained in  U_Audios().
    command_line = 'ffmpeg -i Video0.mp4 -i '+route_audio+'/audio.wav -strict -2 '+route_video+'/'+name_video
    args = shlex.split(command_line)
    subprocess.Popen(args).communicate()
