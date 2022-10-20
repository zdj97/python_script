# -*- coding: utf-8 -*-
"""
# @Time : 2022/9/15 10:19
# @Author : WangYK
# @Site : 
# @File : add_noise.py
# @Software: PyCharm
# @Desc:    choose one random noise add to the wav

"""
import os
import soundfile as sf
import numpy as np
import math
from tqdm import tqdm

def file_name(file_dir):
    L = []
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == '.wav':
                filename=os.path.join(root, file)
                # print(get_label(filename))
                L.append(filename)
    return L

def add_noise(clean_data, noise_data,noised_filename, SNR, sr=16000):

    # data align
    if(len(clean_data)>len(noise_data)):
        times=math.ceil(len(clean_data)/len(noise_data)) #向上取整
        noise_data=list(noise_data)*times
        noise_data=np.array(noise_data)

    noise_data=noise_data[:len(clean_data)]

    #计算语音信号功率Ps和噪声功率Pn1
    Ps = np.sum(clean_data ** 2) / len(clean_data)
    Pn1 = np.sum(noise_data ** 2) / len(noise_data)

    # 计算k值
    k=math.sqrt(Ps/(10**(SNR/10)*Pn1))
    #将噪声数据乘以k,
    random_values_we_need=noise_data*k

    #将噪声数据叠加到纯净音频上去
    outdata=clean_data+random_values_we_need
    # 将叠加噪声的数据写入文件
    sf.write(noised_filename, outdata, sr)

if __name__ == '__main__':

    clean_dir='./release_dev_final_1_after_drc/wav'
    noise_dir='./split_noise'
    output_dir='./noised/'
    SNR_list = [30, 27, 25, 23, 20, 17, 15]

    clean_files=file_name(clean_dir)
    noise_files=file_name(noise_dir)

    for clean_filename in tqdm(clean_files):
        # create one random SNR
        SNR_index = np.random.randint(0, len(SNR_list))
        SNR = SNR_list[SNR_index]

        # choose one random noise type
        random_index=np.random.randint(0,len(noise_files))
        noise_filename=noise_files[random_index]
        noise_type=(noise_filename.split('\\')[1]).split('.wav')[0]
        clean_type=(clean_filename.split('\\')[-1]).split('.wav')[0]
        noised_filename=output_dir+clean_type+'_'+noise_type+'_'+str(SNR)+'dB.wav'

        #读取音频
        clean_data,fs=sf.read(clean_filename)
        noise_data,fs=sf.read(noise_filename)

        # add noise
        add_noise(clean_data,noise_data,noised_filename,SNR,fs)

