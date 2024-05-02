# This file split the subset COCO into train, valid, and test
import os
import shutil
import random

# Define your base directory
base_dir = '/Users/havx/Thesis Data/training_data(6000new 4000coco)/yolo_coco/'
export_base_dir = '/Users/havx/Desktop/UCLA Courses/Thesis Project/VisionTalks/data'

# Setup directories for train, validation, and test sets
train_dir = os.path.join(export_base_dir, 'train')
val_dir = os.path.join(export_base_dir, 'valid')
test_dir = os.path.join(export_base_dir, 'test')

# Gather all image files that have corresponding label files
files = [f for f in os.listdir(base_dir+'images/train') if f.endswith('.jpg') and os.path.exists(os.path.join(base_dir, 'labels/train', f.replace('.jpg', '.txt')))]
random.shuffle(files)  # Shuffle the list randomly

# Split the data
train_samples = 2800
val_samples = 600

# Assign files to splits
train_files = files[:train_samples]
val_files = files[train_samples:train_samples + val_samples]
test_files = files[train_samples + val_samples: 4000]


# Function to copy files to respective directories
def copy_files(files, image_dir, label_dir):
    for f in files:
        shutil.copy(os.path.join(base_dir, 'images/train', f), os.path.join(image_dir, f))
        label_file = f.replace('.jpg', '.txt')
        shutil.copy(os.path.join(base_dir, 'labels/train', label_file), os.path.join(label_dir, label_file))


# Copy files to their respective directories
# copy_files(train_files, os.path.join(train_dir, 'images'), os.path.join(train_dir, 'labels'))
# copy_files(val_files, os.path.join(val_dir, 'images'), os.path.join(val_dir, 'labels'))
# copy_files(test_files, os.path.join(test_dir, 'images'), os.path.join(test_dir, 'labels'))

