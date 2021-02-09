'''
 # @ Author: Saeed Arabi
 # @ Create Time: 2021-01-30 22:15:26
 # @ Email: arabi@iastate.edu
 '''

import cv2
import glob
from helper import Phone_Detector, check_python_version


if __name__ == '__main__':

    check_python_version()
    phone_detector = Phone_Detector(
        save_image=True, debug=True)

    # downloding the deep model (if it's not already downloaded)
    MODEL_NAME = 'faster_rcnn_nas_coco_2018_01_28'
    phone_detector.PATH_TO_SAVED_MODEL = phone_detector.download_deep_learrning_model() + \
        "/saved_model"

    # loding the deep model
    phone_detector.load_deep_model()

    # setting the threshold for color filtering
    phone_detector.th = 59

    test_files = glob.glob("./find_phone/*.jpg")
    for test_file in test_files:
        test_image = cv2.imread(test_file)
        phone_detector.feed(test_image, test_file)

    phone_detector.summerize_result()
