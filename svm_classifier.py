import cv2
import StackedImages as si
import numpy as np
import argparse
import imutils
import time
import glob
import dataset_trainer as dt
# import tensorflow as tf
import contours as con
import copy_path_names as cpath
# define the svm classifier for each of the image sets leaving the last 10 images as validation sets
# what features does the character have? a boundary shape and a color
# need to define the boundary lines of the character
# we then import the boundary line of each image as a data field of labels
# along with the color as a feature to make a labels matrix of size
images_path = "C:/Users/Nathan Gillespie/PycharmProjects/machine_learning_final_project/Resources/au_images/"
path_names = cpath.get_filepaths(images_path)
path = "C:/Users/Nathan Gillespie/PycharmProjects/machine_learning_final_project/projectFiles/path_names.txt"
with open(path, "w") as output:
    for columns in path_names:
        output.write(str(columns).join(("\"", "\"")) + '\n')
with open(path, "r") as file:
    replaced_data = file.read()
    replaced_data = replaced_data.replace('\\', '/')
with open(path, "w") as output:
    output.write(replaced_data)

# this needs to be applied over all images in the au_images file
# create a list of all of the paths inside of au_images that then gets set as the current path with a for loop that
# sets a new exported file containing all of the label data and
#print(replaced_data)
#for columns in replaced_data:
f = open(path, 'r+')
lines = [line for line in f.readlines()]
f.close()
pathname: str = lines[1]
img = cv2.imread(pathname)
cv2.imshow("images", img)
cv2.waitKey(0)
#imgContour = img.copy()
#imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 1)
#imgCanny = cv2.Canny(imgBlur, 50, 50)
#imgBlank = np.zeros_like(img)
#imgStack = si.stackImages(0.6, ([img, imgGray, imgBlur],
#                               [imgCanny, imgBlank, imgBlank]))
#given that we only have one set of features we can easily make a naive bayes classifier that can predict
# the label of the character, this will be cross-correlated with that character being an imposter or not
# to devise a true false scheme for the labels k=2 such that
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required=True, help="path to input image")
ap.add_argument("-p", "--prototxt", required=False,	help="path to Caffe 'deploy' prototxt file")
ap.add_argument("-m", "--model", required=True,	help="path to Caffe pre-trained model")
ap.add_argument("-l", "--labels", required=True, help="path to labels (i.e., syn-sets)")
args = vars(ap.parse_args())