from moviepy.editor import *
import os
from natsort import natsorted
import json

import psutil

def killProcess():
    try:
        pids=psutil.pids()
        for pid in pids:
            p=psutil.Process(pid)
            if p.name() == 'ffmpeg-win64-v4.1.exe':
                cmd = 'taskkill /f /im ffmpeg-win64-v4.1.exe 2>nul 1>null'
                os.system(cmd)
    except:
        pass

if __name__ =="__main__":
    for i in range(30):
        myjsondirs = 'D:/13260183/{}/entry.json'.format(i+1)
        vdtitle = ''
        with open(myjsondirs,'r',encoding='utf-8') as load_f:
            load_dict = json.load(load_f)
        vdtitle=load_dict['page_data']['part']

        videodirs='D:/13260183/{}/lua.flv720.bili2api.64'.format(i+1)
        L=[]

        for root,dirs,files in os.walk(videodirs):
            files=natsorted(files)
            for file in files:
                if os.path.splitext(file)[1]=='.blv':
                    filepath=os.path.join(root,file)
                    myvideo=VideoFileClip(filepath)
                    L.append(myvideo)

        final_clip=concatenate_videoclips(L)
        targetdir='D:/target/{}.mp4'.format(vdtitle)
        final_clip.write_videofile(targetdir,fps=24,remove_temp=True)
        print("{}----{}----拼接成功！".format(i+1,vdtitle))
    killProcess()


