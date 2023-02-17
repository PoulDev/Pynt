from PySide6.QtGui  import QImage, QPixmap
from PySide6.QtCore import Qt
import math

def convert_cv_qt(cv_img, width, height):
    h, w, ch = cv_img.shape
    bytes_per_line = ch * w
    convert_to_Qt_format = QImage(cv_img.data, w, h, bytes_per_line, QImage.Format_RGB888)
    p = convert_to_Qt_format.scaled(width, height, Qt.KeepAspectRatio)
    return QPixmap.fromImage(p)

def points_distance(x1, y1, x2, y2):
    return math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
