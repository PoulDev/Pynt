from PySide6.QtGui import QFont, QIcon, QImage, QPixmap
from PySide6.QtWidgets import *
from PySide6.QtCore import Qt
import os
import sys
import logging

from UI.ui_main import Ui_MainWindow as MainUI
from utils import points_distance, convert_cv_qt 
from Drawer.image import Image
from Drawer.shapes.square import Square
from Drawer.shapes.circle import Circle
from Drawer.shapes.line   import Line
from Drawer.drawer        import drawer, drawers

logging.basicConfig(level=logging.DEBUG)


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self) 
        self.ui = MainUI()
        self.ui.setupUi(self)
        self.pressing = False
        self.current_tool = None
        self.last_press_pos = None
        self.last_brush_point = None
        self.color = (0,0,0)

        self.iter_tools(lambda item: item.setIcon(QIcon(f'Icons/{item.text().lower()}.png')))
        self.ui.tools.itemClicked.connect(self.change_tool)

        self.ui.thickness_slider.valueChanged.connect(lambda: self.ui.thickness_spinbox.setValue(self.ui.thickness_slider.value()))

        self.show()
        self.setFixedSize(self.width(), self.height())

        self.ui.select_brush_color.clicked.connect(self.update_color)
        self.img = Image(self.ui.image.width(), self.ui.image.height())
        self.ui.image.setPixmap(convert_cv_qt(self.img.img, self.ui.image.width(), self.ui.image.height()))

    @drawer('RECT')
    def rect_drawer(self, x, y, thickness, temp):
        self.final_image = temp = self.img.temp_draw(Square(*self.last_press_pos), (x,y), self.color, thickness, old_img=temp) 
        if self.ui.show_infos.isChecked():
            temp = self.img.put_text(
                    f' w:{round(abs(x-self.last_press_pos[0]), 2)},h:{round(abs(y-self.last_press_pos[1]), 2)}',
                        (x, y), (255, 255, 255), temp.copy())
        return temp

    @drawer('CIRCLE')
    def circle_drawer(self, x, y, thickness, temp):
        radius = points_distance(*self.last_press_pos, x, y)
        self.final_image = temp = self.img.temp_draw(Circle(*self.last_press_pos), radius, self.color, thickness, old_img=temp)
        if self.ui.show_infos.isChecked():
            temp = self.img.temp_draw(Line(*self.last_press_pos), (x, y), (255, 255, 255), old_img=temp)
            temp = self.img.put_text(f' r:{round(radius, 2)}', (x, y), (255, 255, 255), temp)
        return temp

    @drawer('LINE')
    def line_drawer(self, x, y, thickness, temp):
        self.final_image = temp = self.img.temp_draw(Line(*self.last_press_pos), (x, y), self.color, self.ui.thickness_spinbox.value(), old_img=temp)
        return temp

    @drawer('BRUSH')
    def brush_drawer(self, x, y, thickness, temp):
        thickness = self.ui.thickness_spinbox.value()
        if not self.last_brush_point: self.last_brush_point = (x, y)
        if (d := points_distance(*self.last_brush_point, x, y)) > (thickness + thickness/2):
            self.final_image = self.img.draw(Line(*self.last_brush_point), (x,y), self.color, thickness*2)
        else:
            self.final_image = self.img.draw(Circle(x, y), thickness, self.color, -1)

        self.last_brush_point = (x, y)
        return temp

    @drawer('ERASER')
    def eraser_drawer(self, x, y, thickness, temp):
        self.final_image = temp = self.img.draw(Circle(x, y), thickness*2, self.img.background, -1)
        return temp

    def update_color(self):
        color = QColorDialog.getColor()
        self.ui.select_brush_color.setStyleSheet(f'background: rgb({color.red()}, {color.green()}, {color.blue()});')
        self.color = (color.red(), color.green(), color.blue())
    def change_tool(self, item): 
        self.iter_tools(lambda i: i.setText(i.text().capitalize()))
        item.setText(item.text().upper())
        self.current_tool = item.text()

    def iter_tools(self, func):
        for index in range(self.ui.tools.count()):
            item = self.ui.tools.item(index)
            func(item)


    def is_in_drawing_zone(self, x, y):
        if x < 0 or y < 0:
            return False
        if x > self.ui.image.width() or y > self.ui.image.height():
            return False
        return True

    def mouseMoveEvent(self, event):
        if self.pressing and self.last_press_pos:
            x, y = (event.position().x(), event.position().y())
            x, y = (int(x - self.ui.image.x()), int(y - self.ui.image.y())) 
            thickness = self.ui.thickness_spinbox.value() if not self.ui.fill.isChecked() else -1 
            if self.is_in_drawing_zone(x, y):
                temp = self.img.img.copy()  
                temp = drawers[self.current_tool](self, x, y, thickness, temp)
                if self.ui.show_red_dots.isChecked():
                    temp = self.img.temp_draw(Circle(*self.last_press_pos), 1, (255,0,0), old_img=temp)
                    temp = self.img.temp_draw(Circle(x, y), 1, (255, 0, 0), old_img=temp)
                self.ui.image.setPixmap(convert_cv_qt(temp, self.ui.image.width(), self.ui.image.height()))

        return super().mouseMoveEvent(event)
    
    def mousePressEvent(self, event):
        self.pressing = True
        self.last_press_pos = (int(event.position().x() - self.ui.image.x()), int(event.position().y() - self.ui.image.y())) 
        return super().mousePressEvent(event)
    
    def mouseReleaseEvent(self, event):
        self.pressing = False
        self.last_press_pos = None
        self.last_brush_point = None
        self.img.img = self.final_image
        self.ui.image.setPixmap(convert_cv_qt(self.img.img, self.ui.image.width(), self.ui.image.height()))
        return super().mouseReleaseEvent(event)

os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

os.environ["QT_ENABLE_HIGHDPI_SCALING"] = "1"
os.environ["QT_SCALE_FACTOR"] = "1.5"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    font = QFont()
    font.setFamilies([u"Poppins"])
    font.setPointSize(9)
    font.setBold(False)

    app.setFont(font)
    app.setWindowIcon(QIcon('Icons/logo.png'))
    window = MainWindow()
    app.exec()
