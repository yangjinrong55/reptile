import os

path = r"C:/动物"
root = path + "//"
file = os.listdir(path)
for i in file:
    dir = root + i
    with open(dir,"rb") as f:
        data = f.read()

    # #根据 读取的字符长度进行删除
    # if len(data)<20000:
    #     os.remove(dir)
    #根据读取的内容进行删除
    if "</html>"  in str(data):
        os.remove(dir)
