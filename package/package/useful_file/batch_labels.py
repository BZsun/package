#coding=utf-8
import os
def generate(dir,label):
    files = os.listdir(dir)
    files.sort()
    print('****************')
    print('请输入图片路径 :',dir)
    print('start...')
    labelText = open(dir+'\\'+'label.txt','w')
    for file in files:
        fileType = os.path.split(file)
        if fileType[1] == '.txt':
            continue
        name = file + ' ' + str(int(label)) +'\n'
        labelText.write(name)
    labelText.close()
    print('down!')
    print('****************')

if __name__ == '__main__':
    generate('E:/yunxing/pythonCX/data_prepare/pic/validation/car/',0)