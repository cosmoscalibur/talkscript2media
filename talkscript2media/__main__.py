import talkscript2media.storage as storage
import talkscript2media.text_to_audio as text_to_audio
import talkscript2media.to_video as to_video

file_name = 'file.txt'
route_output_video = 'tests'
name_output_video = 'Guardianes.mp4'

route_images = 'tests/img'
route_text = 'tests/text'
route_audio = 'tests/audio'



storage.Storage(route_images,route_text,route_audio,route_output_video )

storage.Existence(file_name,route_images,route_text)

text_to_audio.Audio_festival(route_images,route_text,route_audio,storage.Existence(file_name,route_images,route_text)[1],storage.Existence(file_name,route_images,route_text)[2])#text

                             #Audio_festival('tests/img','tests/text','tests/audio',['01.txt','02.txt','03.txt'],'en')

text_to_audio.Duration(route_images,route_audio,storage.Existence(file_name,route_images,route_text)[0])#img

to_video.Image_Video()

to_video.U_Audios(text_to_audio.Number_images(route_images),route_audio)

to_video.Video_U_Audio(route_audio,route_output_video ,name_output_video)
