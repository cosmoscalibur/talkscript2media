import talkscript2media.storage as storage
import talkscript2media.text_to_audio as text_to_audio
import talkscript2media.to_video as to_video

file_name = 'tests/file.txt'
route_output_video = 'tests'
name_output_video = 'Guardianes.mp4'

route_images = 'tests/img'
route_text = 'tests/text'
route_audio = 'tests/audio'

N = text_to_audio.Number_images(route_images)

storage.Storage(route_images, route_text, route_audio, route_output_video)

# Exist[0] Name images, Exist[1] Name texts, Exist[2] language
Exist = storage.Existence(file_name, route_images, route_text)


text_to_audio.Audio_festival(route_text, route_audio, Exist[1], Exist[2], N)
text_to_audio.Duration(N, route_images, route_audio, Exist[0])

to_video.Image_Video()
to_video.U_Audios(text_to_audio.Number_images(route_images), route_audio)
to_video.Video_U_Audio(route_audio, route_output_video, name_output_video)
