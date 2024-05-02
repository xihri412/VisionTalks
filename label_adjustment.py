# Shift labels (ONLY do this process on new data before merging with old data)
import os

path = 'data/'

# Shift the label to maintain consistency with pre-trained model classes
train_annotation = path + 'train/labels'
test_annotation = path + 'test/labels'
valid_annotation = path + 'valid/labels'

class_count = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0}  # calculate the number of each class


def adjust_labels(annotation_path, label_shift=80):
    for filename in os.listdir(annotation_path):
        file_path = os.path.join(annotation_path, filename)
        if file_path.endswith('.txt'):  # Check if it's an annotation file
            with open(file_path, 'r') as file:
                lines = file.readlines()
                for line in lines:
                    parts = line.strip().split()
                    class_id = int(parts[0])

                    class_count[class_id] += 1

            with open(file_path, 'w') as file: # This step will creat a folder 'label 2'
                for line in lines:
                    parts = line.strip().split()
                    class_id = int(parts[0])
                    # Apply the label shift only to new class labels (0 to 5)
                    if 0 <= class_id <= 5:
                        class_id += label_shift
                    # Write the modified line back to the file
                    parts[0] = str(class_id)
                    file.write(' '.join(parts) + '\n')
    return class_count

# ONLY run once

# print(adjust_labels(train_annotation))
# print(adjust_labels(test_annotation))
# print(adjust_labels(valid_annotation))
