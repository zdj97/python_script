import os

ori_path='./data_bk'
tar_path='./data'
for name in os.listdir(ori_path):
    ori_name=os.path.join(ori_path,name)
    tar_name=os.path.join(tar_path,name)
    command='ffmpeg -i {}  -ar 8000 -vn {} -y -loglevel quiet'.format(ori_name,tar_name)
    os.system(command)
    print(ori_name,tar_name)

