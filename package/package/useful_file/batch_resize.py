import os
from skimage import io,transform

# # for train
# img_dir = 'E:\\yunxing\\pythonCX\\useful_file\\face_data_1700\\train_original'
# save_dir='E:\\yunxing\\pythonCX\\useful_file\\face_data_1700\\train_180'
#
#
# if not os.path.exists(save_dir):
#     os.mkdir(save_dir)
#
# flist = os.listdir(img_dir)
# for name in flist:
#     img_path=img_dir+'/'+name
#     img=io.imread(img_path)
#     save_name = os.path.join(save_dir, name)
#     image=transform.resize(img,(180,180))
#     io.imsave(save_name, image)

# for val
img_dir = 'E:\yunxing\pythonCX\FaceDetect\multi-task face'
save_dir='E:\\yunxing\\pythonCX\\multi_task_face'


if not os.path.exists(save_dir):
    os.mkdir(save_dir)

flist = os.listdir(img_dir)
for name in flist:
    img_path=img_dir+'/'+name
    img=io.imread(img_path)
    save_name = os.path.join(save_dir, name)
    image=transform.resize(img,(160,160))
    io.imsave(save_name, image)