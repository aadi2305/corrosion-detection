import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

path_cor = r"Corroded"
path_non_cor = r"Non-Corroded"
training_data = []
IMG_SIZE = 200


def create_training_data(path, class_num):
    print(class_num)
    for img in os.listdir(path):
        img_array = cv2.imread(os.path.join(path,img), 1)
        new_array = cv2.resize(img_array , (IMG_SIZE,IMG_SIZE))
        training_data.append([new_array, class_num])
create_training_data(path_cor, 1)   
create_training_data(path_non_cor, 0) 