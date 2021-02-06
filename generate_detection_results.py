'''
 # @ Author: Saeed Arabi
 # @ Create Time: 2021-01-30 22:15:26
 # @ Email: arabi@iastate.edu
 '''

import cv2
import glob
from helper import Phone_Detector, check_python_version


if __name__ == '__main__':
    test_files = ['./find_phone/1.jpg']
    # ['./find_phone/1.jpg', './find_phone/59.jpg', './find_phone/40.jpg', './find_phone/47.jpg', './find_phone/18.jpg', './find_phone/48.jpg', './find_phone/118.jpg', './find_phone/58.jpg', './find_phone/75.jpg', './find_phone/34.jpg', './find_phone/43.jpg', './find_phone/60.jpg', './find_phone/41.jpg', './find_phone/103.jpg', './find_phone/97.jpg'] 
    
    # 
    check_python_version()
    phone_detector = Phone_Detector(
        save_image=True, debug=True)
    phone_detector.th = 59
    # test_files = glob.glob("./find_phone/*.jpg")
    for test_file in test_files:
        test_image = cv2.imread(test_file)
        phone_detector.feed(test_image, test_file)

    phone_detector.summerize_result()


#  1, 47, 58, 75, 43, 103,