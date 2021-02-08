'''
 # @ Author: Saeed Arabi
 # @ Create Time: 2021-02-03 15:46:05
 # @ Email: arabi@iastate.edu
 '''

from helper import check_python_version, Phone_Detector

if __name__ == "__main__":
    check_python_version()
    phone_detector = Phone_Detector()
    print("""
    
    This program downloads the faster rcnn nas model trained on COCO dataset. The results will be in "~/.keras/datasets".

    """)
    phone_detector.download_deep_learrning_model()
