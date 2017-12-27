import cv2
import numpy as np

from math import floor, tan, sqrt
from util import plot_images, Image, show

def cylindrical_warp(img, f=20):
    """Performs a cylindrical warp on a given image"""

    # la implementacion viene de
    # https://stackoverflow.com/questions/12017790/warp-image-to-appear-in-cylindrical-projection

    def convert_coordinates(new_point, new_shape, f, r):
        height, width = new_shape
        
        y, x = centered_point = new_point[0] - height//2, new_point[1] - width//2
        
        omega = width / 2
        z0 = f - (r**2 - omega**2)**(1/2)

        zc = (2*z0 + sqrt(4 * z0**2 - 4 * (x**2 / f**2 + 1) * (z0**2 - r**2)))/(2 * (x**2/f**2 + 1))


        final_point = floor(y*zc/f + height//2), floor(x*zc/f + width//2)

        return final_point

    height, width = img.shape
    new_img = np.zeros(img.shape, dtype=np.uint8)

    for row_index in range(len(img)):
        for col_index in range(len(img[0])):
            y, x = convert_coordinates(
                (row_index, col_index),
                img.shape,
                f,
                f
            )

            if 0 <= x < width and 0 < y < height:
                new_img[row_index, col_index] = img[y, x]

    return new_img
                

def test_warp():
    """Computes and displays a cylindrical warp over a white image"""
    img = np.ones((600, 600))

    show(cylindrical_warp(img, f=600))
