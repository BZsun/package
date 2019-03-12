from skimage import io,util,transform
import skimage
import os


# def add_noise(img,mode):
#     noise_image = skimage.util.random_noise(img, mode=mode, seed=None, clip=True)
# #mode=['gaussian','localvar','poisson','salt','pepper','s&p','speckle']

img_dir = 'E:\\yunxing\\pythonCX\\useful_file\\face_data_1700\\val_x4_LR'
save_dir='E:\\yunxing\\pythonCX\\useful_file\\face_data_1700\\val_x4_gaussian'

if not os.path.exists(save_dir):
    os.mkdir(save_dir)


flist = os.listdir(img_dir)
for name in flist:
    img_path=img_dir+'/'+name
    img=io.imread(img_path)
    save_name=os.path.join(save_dir,name)
    noise_image =skimage.util.random_noise(img, mode='gaussian', clip=True)
    io.imsave(save_name, noise_image)


