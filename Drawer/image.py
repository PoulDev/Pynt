import cv2
import numpy as np

from Drawer.shapes.shape import Shape

class Image:
    def __init__(self, width, height):
        self.img = np.ones((height, width, 3), dtype = np.uint8)
        self.background = (57, 57, 57)
        self.img *= int(''.join(hex(i)[2:] for i in self.background), 16)

    def draw(self, shape: Shape, size, color, thickness=None):
        shape.draw(self.img, size, color, thickness)
        return self.img

    def temp_draw(self, shape: Shape, size, color, thickness=None, old_img=None):
        if old_img is None:
            old_img = self.img
        temp_img = old_img.copy()
        shape.draw(temp_img, size, color, thickness)
        return temp_img

    def put_text(self, text, position, color, img=None):
        if img is None:
            img = self.img
        return cv2.putText(img, text, position, cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 1, cv2.LINE_AA)
