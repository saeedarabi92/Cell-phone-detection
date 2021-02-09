'''
 # @ Author: Saeed Arabi
 # @ Create Time: 2021-02-06 23:23:02
 # @ Email: arabi@iastate.edu
 '''

import cv2
import glob
from helper import Phone_Detector, check_python_version


if __name__ == '__main__':

    accuraces = []
    check_python_version()
    test_files = glob.glob("./find_phone/*.jpg")
    phone_detector = Phone_Detector()
    for i in range(56, 65, 1):
        phone_detector.correct_counts = 0
        phone_detector.incorrect_counts = 0
        print("threshold: ", i)
        phone_detector.th = i
        for test_file in test_files:
            test_image = cv2.imread(test_file)
            phone_detector.feed(test_image, test_file)

        accuraces.append([i, (phone_detector.correct_counts * 100 /
                              (phone_detector.correct_counts + phone_detector.incorrect_counts))])
    print("Accuraces: ", accuraces)
