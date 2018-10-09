from PIL import Image
import os
path = r'C:\images2\gif'
for url in os.listdir(path):
    path1 = path + '\\' + url
    for gif in os.listdir(path1):
        gif_url = path1 + '\\' + gif
        try:
            im =  Image.open(gif_url)
            #jpg_dir = gif_url[:-4]
            while True:
                #保存当前的一帧图片
                name = im.tell()
                im.save(path1+'\\'+str(name)+'.png')
                im.seek(name+1)
        except Exception as e:
            print(e)