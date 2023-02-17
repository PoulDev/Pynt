from Drawer.shapes.shape import Shape
import cv2

class Circle(Shape):
    def draw(self, img, radius, color, thickness=None):
        if not thickness:
            thickness = 2
        cv2.circle(img, (int(self.x), int(self.y)), int(radius), color, thickness)
