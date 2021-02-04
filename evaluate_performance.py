'''
 # @ Author: Saeed Arabi
 # @ Create Time: 2021-02-03 18:04:46
 # @ Email: arabi@iastate.edu
 '''

from helper import Phone_Detector, check_python_version
import time
import cv2


check_python_version()

if __name__ == "__main__":
    phone_detector = Phone_Detector()
    img_path = './find_phone/61.jpg'
    img = cv2.imread(img_path)
    phone_detector.evaluate_detection_speed_performance(img, img_path)
