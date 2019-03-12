#coding=utf-8
import os
import cv2

img_dir = 'E:\\yunxing\\pythonCX\\image_add_noise\\gaussian_noise'
save_dir='E:\\yunxing\\pythonCX\\image_add_noise\\gaussian_blur25_noise'
kernel_size=(5,5)
sigma=25
if not os.path.exists(save_dir):
    os.mkdir(save_dir)

flist = os.listdir(img_dir)
for name in flist:
    img_path=img_dir+'/'+name
    img=cv2.imread(img_path)
    save_name=os.path.join(save_dir,name)
    image = cv2.GaussianBlur(img, kernel_size, sigma)
    cv2.imwrite(save_name, image)