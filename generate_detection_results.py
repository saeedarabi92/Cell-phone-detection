'''
 # @ Author: Saeed Arabi
 # @ Create Time: 2021-01-30 22:15:26
 # @ Email: arabi@iastate.edu
 '''

import cv2
import glob
from helper import Phone_Detector, check_python_version


if __name__ == '__main__':
    test_files = ['./find_phone/60.jpg', './find_phone/61.jpg']
    #   './data/find_phone/125.jpg', './data/find_phone/5.jpg', './data/find_phone/47.jpg',
    #   './data/find_phone/48.jpg', './data/find_phone/109.jpg', './data/find_phone/41.jpg']
    # 33, 125, 5, 47
    #  60, 48, 109, 41
    check_python_version()
    phone_detector = Phone_Detector(
        save_image=True, debug=True, summerize_result=True)
    # test_files = glob.glob("./data/find_phone/*.jpg")
    for test_file in test_files:
        test_image = cv2.imread(test_file)
        phone_detector.feed(test_image, test_file)

    if phone_detector.summerize_result:
        print("phone_detector.correct_counts: ",
              phone_detector.correct_counts, "\n",
              "phone_detector.incorrect_counts: ",
              phone_detector.incorrect_counts, "\n",
              "phone_detector.accuracy: ", phone_detector.correct_counts * 100 / (phone_detector.correct_counts +
                                                                                  phone_detector.incorrect_counts), "%", "\n"
              "phone_detector.files_detected_by_deep_model: ",
              phone_detector.files_detected_by_deep_model, "\n",
              "phone_detector.files_detected_by_color_filtering: ",
              phone_detector.files_detected_by_color_filtering, "\n",
              "phone_detector.files_with_no_detection: ",
              phone_detector.files_with_no_detection, "\n")
