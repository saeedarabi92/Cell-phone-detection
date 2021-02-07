import cv2
import glob
from helper import Phone_Detector, check_python_version


if __name__ == '__main__':

    l = []
    check_python_version()
    test_files = glob.glob("./find_phone/*.jpg")
    # test_files = ['./find_phone/60.jpg', './find_phone/40.jpg']
    phone_detector = Phone_Detector()
    for i in range(56, 65, 1):
        phone_detector.correct_counts = 0
        phone_detector.incorrect_counts = 0
        print("threshold: ", i)
        phone_detector.th = i
        for test_file in test_files:
            test_image = cv2.imread(test_file)
            phone_detector.feed(test_image, test_file)

        l.append([i, (phone_detector.correct_counts * 100 / (phone_detector.correct_counts + phone_detector.incorrect_counts))])
    print(l)