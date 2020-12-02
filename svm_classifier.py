import cv2
from projectFiles import StackedImages as si
import numpy as np
import argparse
import imutils
import glob
from projectFiles import dataset_trainer as dt
from Resources import au_images

# define the svm classifier for each of the image sets leaving the last 10 images as validation sets