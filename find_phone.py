'''
 # @ Author: Saeed Arabi
 # @ Create Time: 2021-02-03 15:54:06
 # @ Email: arabi@iastate.edu
 '''

from helper import Phone_Detector, check_python_version
import sys
import cv2

if __name__ == '__main__':
    check_python_version()
    img_path = sys.argv[1]
    phone_detector = Phone_Detector(
        save_image=False, debug=False, summerize_result=False)
    img = cv2.imread(img_path)
    x, y = phone_detector.feed(img, img_path)
    print(round(x, 4), " ", round(y, 4))
