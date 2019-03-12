#coding=utf-8

import os
import os.path
from PIL import Image
import hashlib


def get_md5(filename):
    m = hashlib.md5()
    mfile = open(filename, "rb")
    m.update(mfile.read())
    mfile.close()
    md5_value = m.hexdigest()
    return md5_value


if __name__ == '__main__':
    ipath = "E:\\yunxing\\pythonCX\\FaceDetect\\human_face"

    for parent, dirnames, filenames in os.walk(ipath):
        md5_list = []
        # for dirname in dirnames:  # 输出文件夹信息
        # print "parent is:" + parent
        # print "dirname is: " + dirname
        for filename in filenames:
            # print "parent is :" + parent
            # print "filename is:" + filename
            # print "md5_list is : "

            if (get_md5(os.path.join(parent, filename)) in md5_list):
                os.remove(os.path.join(parent, filename))
            else:
                md5_list.append(get_md5(os.path.join(parent, filename)))
                # print md5_list
