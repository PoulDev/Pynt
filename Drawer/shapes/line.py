from Drawer.shapes.shape import Shape
import cv2

class Line(Shape):
    def draw(self, img, end_pos, color, thickness=None):
        if not thickness: thickness = 2
        cv2.line(img, (self.x, self.y), end_pos, color, thickness)
