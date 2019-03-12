import cv2
import os.path
from glob import glob

# Get user supplied values
imagePath = 'E:\\yunxing\\pythonCX\\useful_file\\new\\'
cascPath = "haarcascade_frontalface_default.xml"
def detect(filename, cascadePath="haarcascade_frontalface_default.xml"):
    if not os.path.isfile(cascadePath):
        raise RuntimeError("%s: not found" % cascadePath)

    faceCascade = cv2.CascadeClassifier(cascPath)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    image = cv2.imread(filename, cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Detect faces in the image
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(160, 160))

    print("Found {0} faces!".format(len(faces)))

    # Draw a rectangle around the faces
    for i, (x, y, w, h) in enumerate(faces):
        face = image[y: y + h, x:x + w, :]
        save_filename = '%s-%d.jpg' % (os.path.basename(filename).split('.')[0], i)
        cv2.imwrite("faces/" + save_filename, face)

if __name__ == '__main__':
    if os.path.exists('faces') is False:
        os.makedirs('faces')
    file_list = glob('E:\\yunxing\\pythonCX\\useful_file\\new\\*.jpg')
    for filename in file_list:
        detect(filename)
