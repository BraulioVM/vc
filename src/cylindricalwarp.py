import cv2
import numpy as np
from matplotlib.pyplot import imread

from math import floor, tan, sqrt
from util import plot_images, Image, show

def cylindrical_warp(img, f=20):
    """Performs a cylindrical warp on a given image"""

    # la implementacion viene de
    # https://stackoverflow.com/questions/12017790/warp-image-to-appear-in-cylindrical-projection

    def convert_coordinates(new_point, new_shape, f, r):

        y, x = (
            new_point[0] - new_shape[0]//2,
            new_point[1] - new_shape[1]//2
        )

        new_y = y * sqrt(1 + tan(x / f) ** 2)
        new_x = f * tan(x / f)

        return (
            floor(new_y) + new_shape[0]//2,
            floor(new_x) + new_shape[1]//2
        )

    height, width = img.shape[:2]
    new_img = np.zeros(img.shape, dtype=np.uint8)

    for row_index in range(len(img)):
        for col_index in range(len(img[0])):
            y, x = convert_coordinates(
                (row_index, col_index),
                img.shape[:2],
                f,
                f
            )

            if 0 <= x < width and 0 < y < height:
                new_img[row_index, col_index] = img[y, x]

    return new_img
                

def test_warp():
    """Computes and displays a cylindrical warp over a white image"""
    img = np.ones((600, 600))
    mondrian = imread('../images/mondrian.jpg')

    show(cylindrical_warp(img, f=600))
    show(cylindrical_warp(mondrian, f=100))
