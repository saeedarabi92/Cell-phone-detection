'''
 # @ Author: Saeed Arabi
 # @ Create Time: 2021-01-30 22:15:26
 # @ Email: arabi@iastate.edu
 '''

import numpy as np
import cv2
import glob
import sys
import tensorflow as tf
import os
import time

# Preventing tensorflow warnings to print in terminal
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'


def check_python_version(debug=False):

    # Check if the script is running by python 3

    if sys.version_info[0] < 3:
        print("""


                ***ATTENTION***


        """)
        print("This program were tested on Python 3 or a more recent version. Please use Python 3 or a more recent version.")
        sys.exit()
    else:
        if debug:
            print("Python version is 3 or above!")


class Phone_Detector():

    def __init__(self, save_image=False, debug=False):
        self.save_image = save_image
        self.debug = debug
        self.detect_fn = None
        self.annotation_list = None
        self.detected = False
        self.display_image = False
        self.model_name = "faster_rcnn_nas_coco_2018_01_28"
        self.box_normalized_area_mean = 0.008565091
        self.box_normalized_area_std = 0.0033687195
        self.image_width = 490
        self.image_height = 326
        self.incorrect_counts = 0
        self.correct_counts = 0
        self.files_detected_by_deep_model = []
        self.files_detected_by_color_filtering = []
        self.files_with_no_detection = []
        self.load_annotation_file()
        self.th = None
        if self.debug:
            print("Instance of Phone detector were initiated")

    def feed(self, img, img_name):
        detections = self.detect_with_deep_model(img)
        detection = self.filter_deep_model_detection(detections)
        if self.if_deep_model_detect(detection, img_name):
            self.detected = True
            x, y = self.get_deep_model_normalized_bbox_center(detections)
            detection_is_corect = self.if_detection_is_correct(
                x, y, img_name)
            if detection_is_corect:
                self.correct_counts += 1
                self.files_detected_by_deep_model.append(img_name)
            else:
                self.detected = False
                self.incorrect_counts += 1
                self.files_with_no_detection.append(img_name)
        else:
            bboxs = self.detection_by_color_filtering(img)
            bbox = self.filter_detection_by_color(bboxs)
            # print('bbox: ', bbox)

            if self.if_color_filtering_detect(bbox, img_name):
                x, y = self.get_color_filtering_normalized_bbox_center(bbox)
                detection_is_corect = self.if_detection_is_correct(
                    x, y, img_name)
                if detection_is_corect:
                    self.detected = True
                    self.correct_counts += 1
                    self.files_detected_by_color_filtering.append(img_name)
                else:
                    self.detected = False
                    self.incorrect_counts += 1
                    self.files_with_no_detection.append(img_name)
            else:
                self.detected = False
                self.incorrect_counts += 1
                self.files_with_no_detection.append(img_name)

        if self.save_image and self.detected:
            img = self.draw_bbox_centered(x, y, img)
            img_name = "./find_phone_detection/" + img_name.split('/')[-1]
            cv2.imwrite(img_name, img)
        if self.detected:
            return y, x
        else:
            if self.debug:
                print("Detector could not detect any cell phone!")

    def if_color_filtering_detect(self, bbox, img_path):
        if bbox == None:
            if self.debug:
                print("Color filtering could not detect any cell phone on ",
                      img_path.split('/')[-1])
            return False
        else:
            return True

    def if_deep_model_detect(self, det, img_path):
        if len(det['detection_boxes']) == 0:
            if self.debug:
                print("Deep model could not detect any cell phone on ",
                      img_path.split('/')[-1])
            return False
        else:
            return True

    def detection_by_color_filtering(self, img):

        # converting to gray scale
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        # removing the light reflection
        mask = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)[1]
        result = cv2.inpaint(gray, mask, 50, cv2.INPAINT_TELEA)

        # removing noise in image
        blur_r = cv2.GaussianBlur(result, (5, 5), 0)
        th_g, threshed_r = cv2.threshold(
            blur_r, self.th, 255, cv2.THRESH_BINARY_INV)

        # finding bounding boxes in the image
        cnts = cv2.findContours(
            threshed_r, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)[-2]
        bboxes = []
        for cnt in cnts:
            x, y, w, h = cv2.boundingRect(cnt)
            if self.display_image:
                cv2.rectangle(img, (x, y), (x + w, y + h),
                              (0, 0, 255), thickness=2)
            bboxes.append([x, y, w, h])

        if self.display_image:
            cv2.imshow('org_img', img)
            # cv2.imshow('blur', blur_r)
            # cv2.imshow('mask', mask)
            # cv2.imshow('result', result)
            # cv2.imshow('threshed_r', threshed_r)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
        return bboxes

    def get_bbox_normalized_area(self, box):
        x, y, w, h = box
        return (w/self.image_width) * (h/self.image_height)

    def if_detection_is_cell_phone(self, box):
        area = self.get_bbox_normalized_area(box)

        # check if  mean - 2*sigma < bounding_box < mean + 2*sigma
        if area < self.box_normalized_area_mean + 2*self.box_normalized_area_std and area > self.box_normalized_area_mean - 2*self.box_normalized_area_std:
            return True
        else:
            return False

    def filter_detection_by_color(self, bboxes):
        for box in bboxes:
            if self.if_detection_is_cell_phone(box):
                return box
            return None

    def load_deep_model(self):
        if self.debug:
            print("Loading deep model...")
        model = tf.saved_model.load(self.PATH_TO_SAVED_MODEL)
        self.detect_fn = model.signatures['serving_default']
        if self.debug:
            print("Deep model loaded successfully")

    def detect_with_deep_model(self, img):

        # converting image ot tensor
        input_tensor = tf.convert_to_tensor(img)

        # adding an axis to make a batch
        input_tensor = input_tensor[tf.newaxis, ...]
        detections = self.detect_fn(input_tensor)

        # All outputs are batches tensors.
        # Convert to numpy arrays, and take index [0] to remove the batch dimension.
        # We're only interested in the first num_detections.
        num_detections = int(detections.pop('num_detections'))
        detections = {key: value[0, :num_detections].numpy()
                      for key, value in detections.items()}
        detections['num_detections'] = num_detections

        # detection_classes should be ints.
        detections['detection_classes'] = detections['detection_classes'].astype(
            np.int64)
        return detections

    def get_color_filtering_normalized_bbox_center(self, box):
        x, y, w, h = box
        return y/self.image_height + h/self.image_height/2, x/self.image_width + w/self.image_width/2

    def filter_deep_model_detection(self, detections):

        # Cell phone ID is 77 in COCO dataset label
        i,  = np.where(detections['detection_classes'] == 77)
        detections['detection_boxes'] = detections['detection_boxes'][i]
        detections['detection_classes'] = detections['detection_classes'][i]
        detections['detection_scores'] = detections['detection_scores'][i]
        return detections

    def load_annotation_file(self):
        f = open("./find_phone/labels.txt", 'r')
        annotation_list = f.readlines()
        annotation_list = [i[:-2] for i in annotation_list]
        self.annotation_list = [i.split() for i in annotation_list]

    def get_deep_model_normalized_bbox_center(self, detections):
        x1 = detections['detection_boxes'][0][0]
        y1 = detections['detection_boxes'][0][1]
        x2 = detections['detection_boxes'][0][2]
        y2 = detections['detection_boxes'][0][3]
        return x1+(x2-x1)/2, y1+(y2-y1)/2

    def if_detection_is_correct(self, y_d, x_d, img_name):
        img_name = img_name.split('/')[-1]
        x_g = float([i[1]
                     for i in self.annotation_list if i[0] == img_name][0])
        y_g = float([i[2]
                     for i in self.annotation_list if i[0] == img_name][0])
        dist = np.sqrt((x_g - x_d)**2 + (y_g - y_d)**2)
        if dist < .05:
            return True
        else:
            return False

    def draw_bbox_centered(self, x, y, np_img):
        x = x*self.image_height
        y = y*self.image_width
        np_img = cv2.circle(np_img, (int(round(y)), int(round(x))),
                            radius=5, color=(0, 0, 225), thickness=-1)
        return np_img

    def evaluate_detection_speed_performance(self, img, img_path):
        then = time.time()
        for i in range(0, 50):
            self.feed(img, img_path)
        now = time.time()
        print("Detection performance is {} FPS".format(50 / round(now - then, 2)))

    def download_deep_learrning_model(self):

        base_url = 'http://download.tensorflow.org/models/object_detection/'
        model_file = self.model_name + '.tar.gz'
        model_dir = tf.keras.utils.get_file(fname=self.model_name,
                                            origin=base_url + model_file,
                                            untar=True)
        return str(model_dir)


def summerize_result(self):
    print("correct_counts: ",
          self.correct_counts, "\n",
          "incorrect_counts: ",
          self.incorrect_counts, "\n",
          "accuracy: ", self.correct_counts * 100 /
          (self.correct_counts + self.incorrect_counts), "%", "\n"
          "files_detected_by_deep_model: ",
          self.files_detected_by_deep_model, "\n",
          "files_detected_by_color_filtering: ",
          self.files_detected_by_color_filtering, "\n",
          "files_with_no_detection: ",
          self.files_with_no_detection, "\n")
