1. Download new classes data from Open Images V7 dataset via `new_data_loading.py` to `/Users/havx/Documents/thesis_data/yolo_data(6000new 4000coco)/yolo_open_images`. After organizing, transfer new data to `/Users/havx/Desktop/UCLA Courses/Thesis Project/VisionTalks/data`.

2. Run `label_adjustment.py` to shift labels to maintain consistency with old classes. Also calculate the number of each class. ONLY RUN ONCE!

3. Download a subset of all old classes data from COCO dataset via `coco_data_loading.py` to `/Users/havx/Documents/thesis_data/yolo_data(6000new 4000coco)/yolo_coco`.

4. Run `coco_data_processing.py` to put coco subset data into train, test, and valid in `/Users/havx/Desktop/UCLA Courses/Thesis Project/VisionTalks/data`. ONLY RUN ONCE!
