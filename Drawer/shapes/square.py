from Drawer.shapes.shape import Shape
import cv2

class Square(Shape):
    def draw(self, img, size, color, thickness=None):
        if not thickness: thickness = 2
        cv2.rectangle(img, (int(self.x), int(self.y)), (int(size[0]), int(size[1])), color, thickness)

