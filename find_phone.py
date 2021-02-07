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
        save_image=False, debug=False)

    # setting the threshold for color filtering (This value found using a grid-based search approach. Forr more information checkout grid_search.py)
    phone_detector.th = 59

    # loading the image to numpy array
    img = cv2.imread(img_path)
    try:
        x, y = phone_detector.feed(img, img_path)
        print(round(x, 4), " ", round(y, 4))
    except:
        print("No detection resutl found for {}".format(img_path))
