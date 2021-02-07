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
    phone_detector.th = 59
    test_files = glob.glob("./find_phone/*.jpg")
    for test_file in test_files:
        test_image = cv2.imread(test_file)
        phone_detector.feed(test_image, test_file)

    phone_detector.summerize_result()