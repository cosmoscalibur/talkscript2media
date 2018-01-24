import talkscript2media.storage as storage
import talkscript2media.text_to_audio as text_to_audio
import talkscript2media.to_video as to_video

# Exist[0] Name images, Exist[1] Name texts, Exist[2] language,Exist[3] routes.
Exist = storage.Existence('tests/file.txt')



file_name = Exist[3][0]
route_output_video = Exist[3][1]
name_output_video = Exist[3][2]

route_images = Exist[3][3]
route_text = Exist[3][4]
route_audio = Exist[3][5]

N = text_to_audio.Number_images(route_images)

storage.Storage(route_images, route_text, route_audio, route_output_video)




text_to_audio.Audio_festival(route_text, route_audio, Exist[1], Exist[2], N)
text_to_audio.Duration(N, route_images, route_audio, Exist[0])

to_video.Image_Video()
to_video.U_Audios(text_to_audio.Number_images(route_images), route_audio)
to_video.Video_U_Audio(route_audio, route_output_video, name_output_video)
