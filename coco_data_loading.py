# This file download trained classes for YOLOv8 from COCO
import fiftyone as fo
import fiftyone.zoo as foz

base_dir = '/Users/havx/Thesis Data'
coco_dir = base_dir + '/coco_data'
export_base_dir = base_dir + '/yolo_coco'  # Base directory for exported splits

classes = ['person', 'bicycle', 'car', 'motorcycle', 'airplane', 'bus', 'train', 'truck', 'boat', 'traffic light',
           'fire hydrant', 'stop sign', 'parking meter', 'bench', 'bird', 'cat', 'dog', 'horse', 'sheep', 'cow',
           'elephant', 'bear', 'zebra', 'giraffe', 'backpack', 'umbrella', 'handbag', 'tie', 'suitcase', 'frisbee',
           'skis', 'snowboard', 'sports ball', 'kite', 'baseball bat', 'baseball glove', 'skateboard', 'surfboard',
           'tennis racket', 'bottle', 'wine glass', 'cup', 'fork', 'knife', 'spoon', 'bowl', 'banana', 'apple',
           'sandwich', 'orange', 'broccoli', 'carrot', 'hot dog', 'pizza', 'donut', 'cake', 'chair', 'couch',
           'potted plant', 'bed', 'dining table', 'toilet', 'tv', 'laptop', 'mouse', 'remote', 'keyboard', 'cell phone',
           'microwave', 'oven', 'toaster', 'sink', 'refrigerator', 'book', 'clock', 'vase', 'scissors', 'teddy bear',
           'hair drier', 'toothbrush']


coco_dataset = foz.load_zoo_dataset(
      "coco-2017",
      split='train',
      dataset_dir=coco_dir,
      label_types=["detections"],
      classes=classes,
      max_samples=4200 # only use the 4000 to split in case of mismatching
  )

coco_dataset.export(
      export_dir=export_base_dir,
      dataset_type=fo.types.YOLOv5Dataset,
      label_field="ground_truth",
      split='train',
      classes=classes
  )
