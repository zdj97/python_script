# from moviepy.editor import VideoFileClip,concatenate_videoclips
#
# clip = VideoFileClip('hi小问电视背景音.wav')#获取视频1.mp4(视频需与程序置于同一文件夹)
#
# newclip = clip.volumex(5)#将音量调整为5倍
#
# newclip.write_videofile('out.mp4')#输出影片名为out.mp4

from pydub import AudioSegment

def match_target_amolitude(sound,target_dBFS):
    change_in_dBFS=target_dBFS-sound.dBFS
    print(change_in_dBFS)
    return sound.apply_gain(change_in_dBFS)

sound=AudioSegment.from_file('./hi小问电视背景音.wav','wav')
db=sound.dBFS
# print(db,db*0.5)
normalized_sound=match_target_amolitude(sound,db*0.5)
normalized_sound.export('./hi小问电视背景音0.5.wav','wav')