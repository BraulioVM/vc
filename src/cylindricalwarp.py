import cv2
import numpy as np

from math import floor, tan
from util import plot_images, Image, show

def cylindrical_warp(img, f=20):
    """Performs a cylindrical warp on a given image"""

    height, width = img.shape
    new_img = np.zeros(img.shape, dtype=np.uint8)

    for row_index in range(len(img)):
        for col_index in range(len(img[0])):
            c_row_index = floor(row_index - height*0.5) + 1
            c_col_index = floor(col_index - width*0.5) + 1

            img_col = f * tan(c_col_index / f)
            
            img_row = img_col * (1 + tan(c_row_index/f)**2) ** 0.5

            img_col = floor(img_col + width*0.5) - 1
            img_row = floor(img_row + height*0.5) - 1

            if 0 <= img_col < width and 0 < img_row < height:
                new_img[img_row][img_col] = img[row_index][col_index]

    return new_img
                

def test_warp():
    """Computes and displays a cylindrical warp over a white image"""
    img = np.ones((300, 300))

    show(cylindrical_warp(img, f=600))
