from xpinyin import Pinyin
import os

p = Pinyin()
path = r'C:\Users\ADMIN\Desktop\第三批'

#更改二级文件夹名
for root,dirs,files in os.walk(path):
    for dir in dirs:
        old_name = os.path.join(root,dir)
        new_name =  os.path.join(root,p.get_pinyin(dir,''))
        os.rename(old_name,new_name)

#更改文件名
for root,dirs,files in os.walk(path):
    for file in files:
        old_name = os.path.join(root,file)
        new_name =  os.path.join(root,p.get_pinyin(file,''))
        os.rename(old_name,new_name)





