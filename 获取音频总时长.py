import wave
import os
file_path='./testing_list_mix_mia.txt'
total_time=0
nonwaketime=waketime=0
hiwake=nihaowake=0
f=open(file_path,'r')
for line in f:
    label,file_name=line.split()
    #print(label)
    with wave.open (file_name, 'rb') as f:
        frames = f.getnframes ()
        rate = f.getframerate ()
        #print(frames,rate)
        wav_length = frames / float (rate)
        if label=='-1':
            nonwaketime+=wav_length
        elif label=='0':
            hiwake+=wav_length
            waketime+=wav_length
        else:
            nihaowake+=wav_length
            waketime+=wav_length
        total_time+=wav_length
print('非唤醒词测试总时长为{},唤醒词测试总时长为{},测试总时长为{},hixiaowen唤醒词时长为{},你好问问时长为{}'.format(nonwaketime,waketime,total_time,hiwake,nihaowake))
def dd():
    pass