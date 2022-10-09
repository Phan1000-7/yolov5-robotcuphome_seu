# encoding=utf-8
# divide train and valid data
import os
from shutil import copy2

image_original_path = r"E:\Study\Machine Learning\Pytorch\ComputerVision\img"
label_original_path = r"E:\Study\Machine Learning\Pytorch\ComputerVision\labs"

train_image_path = r"E:\Study\Machine Learning\Pytorch\ComputerVision\data\train\images"
train_label_path = r"E:\Study\Machine Learning\Pytorch\ComputerVision\data\train\labels"

valid_image_path = r"E:\Study\Machine Learning\Pytorch\ComputerVision\data\valid\images"
valid_label_path = r"E:\Study\Machine Learning\Pytorch\ComputerVision\data\valid\labels"


def mkdir():
    if not os.path.exists(train_image_path):
        os.makedirs(train_image_path)
    if not os.path.exists(train_label_path):
        os.makedirs(train_label_path)

    if not os.path.exists(valid_image_path):
        os.makedirs(valid_image_path)
    if not os.path.exists(valid_label_path):
        os.makedirs(valid_label_path)


def main():
   # mkdir()

    all_image = os.listdir(image_original_path)
    for i in range(len(all_image)):
        if i % 10 != 0:
            copy2(os.path.join(image_original_path, all_image[i]), train_image_path)
        else:
            copy2(os.path.join(image_original_path, all_image[i]), valid_image_path)

    all_label = os.listdir(label_original_path)
    for i in range(len(all_label)):
        if i % 10 != 0:
            copy2(os.path.join(label_original_path, all_label[i]), train_label_path)
        else:
            copy2(os.path.join(label_original_path, all_label[i]), valid_label_path)


if __name__ == '__main__':
    main()
