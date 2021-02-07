# Cell phone detection using shallow and deep models



# Initial results:
phone_detector.correct_counts:  110 
 phone_detector.incorrect_counts:  19 
 phone_detector.accuracy:  85.27131782945736 % 
phone_detector.files_detected_by_deep_model:  ['./find_phone/128.jpg', './find_phone/3.jpg', './find_phone/106.jpg', './find_phone/102.jpg', './find_phone/36.jpg', './find_phone/6.jpg', './find_phone/52.jpg', './find_phone/11.jpg', './find_phone/74.jpg', './find_phone/31.jpg', './find_phone/12.jpg', './find_phone/111.jpg', './find_phone/110.jpg', './find_phone/44.jpg', './find_phone/73.jpg', './find_phone/132.jpg', './find_phone/69.jpg', './find_phone/94.jpg', './find_phone/113.jpg', './find_phone/107.jpg', './find_phone/101.jpg', './find_phone/76.jpg', './find_phone/71.jpg', './find_phone/67.jpg', './find_phone/57.jpg', './find_phone/20.jpg', './find_phone/25.jpg', './find_phone/79.jpg', './find_phone/68.jpg', './find_phone/0.jpg', './find_phone/130.jpg', './find_phone/22.jpg', './find_phone/92.jpg', './find_phone/117.jpg', './find_phone/98.jpg', './find_phone/122.jpg', './find_phone/126.jpg', './find_phone/75.jpg', './find_phone/50.jpg', './find_phone/84.jpg', './find_phone/45.jpg', './find_phone/129.jpg', './find_phone/62.jpg', './find_phone/15.jpg', './find_phone/23.jpg', './find_phone/87.jpg', './find_phone/99.jpg', './find_phone/37.jpg', './find_phone/86.jpg', './find_phone/105.jpg', './find_phone/26.jpg', './find_phone/7.jpg', './find_phone/78.jpg', './find_phone/35.jpg', './find_phone/119.jpg', './find_phone/127.jpg', './find_phone/88.jpg', './find_phone/96.jpg', './find_phone/121.jpg', './find_phone/123.jpg', './find_phone/125.jpg'] 
 phone_detector.files_detected_by_color_filtering:  ['./find_phone/24.jpg', './find_phone/5.jpg', './find_phone/17.jpg', './find_phone/39.jpg', './find_phone/49.jpg', './find_phone/1.jpg', './find_phone/47.jpg', './find_phone/61.jpg', './find_phone/91.jpg', './find_phone/51.jpg', './find_phone/63.jpg', './find_phone/53.jpg', './find_phone/131.jpg', './find_phone/16.jpg', './find_phone/30.jpg', './find_phone/33.jpg', './find_phone/134.jpg', './find_phone/70.jpg', './find_phone/38.jpg', './find_phone/32.jpg', './find_phone/120.jpg', './find_phone/80.jpg', './find_phone/124.jpg', './find_phone/27.jpg', './find_phone/83.jpg', './find_phone/104.jpg', './find_phone/72.jpg', './find_phone/77.jpg', './find_phone/115.jpg', './find_phone/43.jpg', './find_phone/55.jpg', './find_phone/114.jpg', './find_phone/64.jpg', './find_phone/90.jpg', './find_phone/100.jpg', './find_phone/42.jpg', './find_phone/93.jpg', './find_phone/85.jpg', './find_phone/95.jpg', './find_phone/81.jpg', './find_phone/54.jpg', './find_phone/112.jpg', './find_phone/89.jpg', './find_phone/108.jpg', './find_phone/10.jpg', './find_phone/116.jpg', './find_phone/66.jpg', './find_phone/82.jpg', './find_phone/133.jpg'] 
 phone_detector.files_with_no_detection:  ['./find_phone/4.jpg', './find_phone/46.jpg', './find_phone/29.jpg', './find_phone/59.jpg', './find_phone/40.jpg', './find_phone/109.jpg', './find_phone/9.jpg', './find_phone/18.jpg', './find_phone/48.jpg', './find_phone/118.jpg', './find_phone/13.jpg', './find_phone/58.jpg', './find_phone/14.jpg', './find_phone/34.jpg', './find_phone/60.jpg', './find_phone/41.jpg', './find_phone/103.jpg', './find_phone/97.jpg', './find_phone/8.jpg'] 






 60:

correct_counts:  8 
 incorrect_counts:  11 
 accuracy:  42.10526315789474 % 
files_detected_by_deep_model:  [] 
 files_detected_by_color_filtering:  ['./find_phone/4.jpg', './find_phone/46.jpg', './find_phone/29.jpg', './find_phone/109.jpg', './find_phone/9.jpg', './find_phone/13.jpg', './find_phone/14.jpg', './find_phone/8.jpg'] 
 files_with_no_detection:  ['./find_phone/59.jpg', './find_phone/40.jpg', './find_phone/18.jpg', './find_phone/48.jpg', './find_phone/118.jpg', './find_phone/58.jpg', './find_phone/34.jpg', './find_phone/60.jpg', './find_phone/41.jpg', './find_phone/103.jpg', './find_phone/97.jpg'] 


40

75:
correct_counts:  7 
 incorrect_counts:  12 
 accuracy:  36.8421052631579 % 
files_detected_by_deep_model:  [] 
 files_detected_by_color_filtering:  ['./find_phone/4.jpg', './find_phone/29.jpg', './find_phone/109.jpg', './find_phone/13.jpg', './find_phone/58.jpg', './find_phone/14.jpg', './find_phone/103.jpg'] 
 files_with_no_detection:  ['./find_phone/46.jpg', './find_phone/59.jpg', './find_phone/40.jpg', './find_phone/9.jpg', './find_phone/18.jpg', './find_phone/48.jpg', './find_phone/118.jpg', './find_phone/34.jpg', './find_phone/60.jpg', './find_phone/41.jpg', './find_phone/97.jpg', './find_phone/8.jpg'] 


grid search:
[[56, 86.82170542635659], [57, 87.59689922480621], [58, 88.37209302325581], [59, 88.37209302325581], [60, 87.59689922480621], [61, 86.82170542635659], [62, 86.82170542635659], [63, 85.27131782945736], [64, 83.72093023255815]]
[[30, 83.72093023255815], [35, 84.49612403100775], [40, 85.27131782945736], [45, 85.27131782945736], [50, 84.49612403100775], [55, 86.82170542635659], [60, 87.59689922480621], [65, 84.49612403100775], [70, 84.49612403100775], [75, 82.94573643410853], [80, 85.27131782945736], [85, 83.72093023255815], [90, 80.62015503875969], [95, 79.84496124031008], [100, 80.62015503875969], [105, 79.06976744186046], [110, 79.84496124031008], [115, 72.86821705426357], [120, 65.11627906976744], [125, 68.9922480620155], [130, 60.46511627906977], [135, 59.689922480620154], [140, 53.48837209302326], [145, 52.713178294573645], [150, 52.713178294573645], [155, 50.3875968992248], [160, 48.06201550387597], [165, 47.286821705426355], [170, 48.06201550387597], [175, 46.51162790697674]]



 files_detected_by_color_filtering:  ['./find_phone/24.jpg', './find_phone/17.jpg', './find_phone/4.jpg', './find_phone/1.jpg', './find_phone/40.jpg', './find_phone/91.jpg', './find_phone/51.jpg', './find_phone/131.jpg', './find_phone/109.jpg', './find_phone/48.jpg', './find_phone/134.jpg', './find_phone/70.jpg', './find_phone/38.jpg', './find_phone/32.jpg', './find_phone/80.jpg', './find_phone/124.jpg', './find_phone/27.jpg', './find_phone/83.jpg', './find_phone/104.jpg', './find_phone/72.jpg', './find_phone/13.jpg', './find_phone/77.jpg', './find_phone/115.jpg', './find_phone/55.jpg', './find_phone/64.jpg', './find_phone/90.jpg', './find_phone/42.jpg', './find_phone/93.jpg', './find_phone/81.jpg', './find_phone/41.jpg', './find_phone/112.jpg', './find_phone/89.jpg', './find_phone/108.jpg', './find_phone/116.jpg', './find_phone/66.jpg', './find_phone/82.jpg', './find_phone/133.jpg'] 
 files_with_no_detection:  ['./find_phone/5.jpg', './find_phone/39.jpg', './find_phone/46.jpg', './find_phone/29.jpg', './find_phone/49.jpg', './find_phone/59.jpg', './find_phone/47.jpg', './find_phone/61.jpg', './find_phone/63.jpg', './find_phone/53.jpg', './find_phone/9.jpg', './find_phone/16.jpg', './find_phone/18.jpg', './find_phone/30.jpg', './find_phone/33.jpg', './find_phone/120.jpg', './find_phone/118.jpg', './find_phone/58.jpg', './find_phone/14.jpg', './find_phone/75.jpg', './find_phone/34.jpg', './find_phone/43.jpg', './find_phone/114.jpg', './find_phone/45.jpg', './find_phone/100.jpg', './find_phone/95.jpg', './find_phone/60.jpg', './find_phone/54.jpg', './find_phone/103.jpg', './find_phone/10.jpg', './find_phone/97.jpg', './find_phone/8.jpg'] 