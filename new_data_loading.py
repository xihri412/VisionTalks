# This file download extra untrained classes for YOLOv8 from Open Images Dataset V7
import fiftyone as fo
import fiftyone.zoo as foz


base_dir = '/Users/havx/Thesis Data'
open_images_dir = base_dir + '/open_images_data'  # Location to save the loaded datasets
export_base_dir = base_dir + '/yolo_open_images'  # Base directory for exported splits

new_classes = ["Tree", "Building", "Stairs", "Street light", "House", "Waste container"]


splits = ["train", "validation", "test"]
open_images_sample_sizes = [4200, 800, 800]


for i, split in enumerate(splits):
    open_images_dataset = foz.load_zoo_dataset(
      "open-images-v7",
      split=split,
      dataset_dir=f"{open_images_dir}/{split}",
      label_types=["detections"],
      classes=new_classes,
      max_samples=open_images_sample_sizes[i],
  )

    open_images_dataset.export(
      export_dir=f"{export_base_dir}/{split}",
      dataset_type=fo.types.YOLOv5Dataset,
      label_field="ground_truth",
      split=split,
      include_confidence=True,
      classes=new_classes
  )
