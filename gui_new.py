
import sys
from PyQt5.QtWidgets import * #QApplication, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtGui import *
from PyQt5.QtCore import *
class TriangleButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(60,60)
        self.setStyleSheet("border: none;")

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QRadialGradient(self.width() / 2, self.height() / 2, self.width() / 2)  # 定义渐变
        if self.isDown():  # 按钮被按下
            gradient.setColorAt(0, QColor(255,255,255))  # 开始颜色
            gradient.setColorAt(1, QColor("#90ee90"))  # 结束颜色
            painter.setBrush(gradient)  # 设置画刷
            painter.setPen(Qt.NoPen)  # 无边框
        else:
            gradient.setColorAt(0, QColor(255,255,255))  # 开始颜色
            gradient.setColorAt(1, QColor("#add8e6"))  # 结束颜色
            painter.setBrush(gradient)  # 设置画刷
            painter.setPen(Qt.NoPen)  # 无边框
        triangle = [QPoint(60, 30), QPoint(0, 0), QPoint(0, 60)]
        painter.drawPolygon(*triangle)

    def mousePressEvent(self, event):
        self.setGeometry(self.x() + 2, self.y() + 2, self.width() - 4, self.height() - 4)  # 按下时缩小
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setGeometry(self.x() - 2, self.y() - 2, self.width() + 4, self.height() + 4)  # 松开时恢复
        super().mouseReleaseEvent(event)
        
class RoundedRectButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(60, 60)
        self.setStyleSheet("border: none;")

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QRadialGradient(self.width() / 2, self.height() / 2, self.width() / 2)  # 定义渐变
        if self.isDown():  # 按钮被按下
            gradient.setColorAt(0, QColor(255,255,255))  # 开始颜色
            gradient.setColorAt(1, QColor("#ffb6c1"))  # 结束颜色
            painter.setBrush(gradient)  # 设置画刷
            painter.setPen(Qt.NoPen)  # 无边框
        else:
            gradient.setColorAt(0, QColor(255,255,255))  # 开始颜色
            gradient.setColorAt(1, QColor("#add8e6"))  # 结束颜色
            painter.setBrush(gradient)  # 设置画刷
            painter.setPen(Qt.NoPen)  # 无边框
        painter.setRenderHint(QPainter.Antialiasing)  # 反锯齿
        painter.drawRoundedRect(0, 0, self.width(), self.height(), 15, 15)  # 10 为圆角半径

    def mousePressEvent(self, event):
        self.setGeometry(self.x() + 2, self.y() + 2, self.width() - 4, self.height() - 4)  # 按下时缩小
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setGeometry(self.x() - 2, self.y() - 2, self.width() + 4, self.height() + 4)  # 松开时恢复
        super().mouseReleaseEvent(event)

class CircularButton(QPushButton):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(60, 60)  # 设置按钮的大小
        self.setStyleSheet("border: none;")

    def paintEvent(self, event):
        painter = QPainter(self)
        gradient = QRadialGradient(self.width() / 2, self.height() / 2, self.width() / 2)  # 定义渐变
        if self.isDown():  # 按钮被按下
            gradient.setColorAt(0, QColor(255,255,255))  # 开始颜色
            gradient.setColorAt(1, QColor("#ffa07a"))  # 结束颜色
            painter.setBrush(gradient)  # 设置画刷
            painter.setPen(Qt.NoPen)  # 无边框
        else:
            gradient.setColorAt(0, QColor(255,255,255))  # 开始颜色
            gradient.setColorAt(1, QColor("#add8e6"))  # 结束颜色
            painter.setBrush(gradient)  # 设置画刷
            painter.setPen(Qt.NoPen)  # 无边框
        # 使用不同颜色表示按钮的状态
        # if self.isDown():
        #     painter.setBrush(QColor("#0000CC"))  # 深蓝色
        # else:
        #     painter.setBrush(QColor("#0000FF"))  # 浅蓝色
        painter.setRenderHint(QPainter.Antialiasing)  # 开启抗锯齿
        painter.drawEllipse(0, 0, self.width(), self.height())  # 绘制圆形

    def mousePressEvent(self, event):
        self.setGeometry(self.x() + 2, self.y() + 2, self.width() - 4, self.height() - 4)  # 按下时缩小
        super().mousePressEvent(event)

    def mouseReleaseEvent(self, event):
        self.setGeometry(self.x() - 2, self.y() - 2, self.width() + 4, self.height() + 4)  # 松开时恢复
        super().mouseReleaseEvent(event)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Genshin Music")
        self.setWindowIcon(QIcon("icon.png"))
        self.setFixedSize(600, 800)
        self.setWindowOpacity(0.98)
        self.setStyleSheet("background-color: #f0f8ff;")
        central_widget = QWidget(self)
        self.setCentralWidget(central_widget)
        self.label = QLabel(central_widget)
        self.label.setText("乐谱的路径:")
        self.label.move(20, 20)
        self.label.resize(600, 50)
        self.label.setStyleSheet("font-size: 30px; font-weight: bold; color: #000000;")
        self.line_edit = QLineEdit(central_widget)
        self.line_edit.move(20, 100)
        self.line_edit.resize(560, 40)
        self.line_edit.setWindowOpacity(0.96)
        self.line_edit.setStyleSheet("font-size: 25px; font-weight: bold; color: #000000;background-color: #ffffff; border: none;")
        self.button = QPushButton(central_widget)
        self.button.setText("查找")
        self.button.move(20, 160)
        self.button.resize(560, 40)
        self.button.setStyleSheet("font-size: 25px; font-weight: bold; color: #000000; background-color: #ffffff;")
        self.label_bmp = QLabel(central_widget)
        self.label_bmp.setText("乐谱的节拍:")
        self.label_bmp.move(20, 260)
        self.label_bmp.resize(600, 50)
        self.label_bmp.setStyleSheet("font-size: 30px; font-weight: bold; color: #000000;")
        self.line_edit_bmp = QLineEdit(central_widget)
        self.line_edit_bmp.move(20, 340)
        self.line_edit_bmp.resize(560, 40)
        self.line_edit_bmp.setWindowOpacity(0.96)
        self.line_edit_bmp.setStyleSheet("font-size: 25px; font-weight: bold; color: #000000;background-color: #ffffff; border: none;")
        self.button_bmp = QPushButton(central_widget)
        self.button_bmp.setText("确认")
        self.button_bmp.move(20, 420)
        self.button_bmp.resize(560, 40)
        self.button_bmp.setStyleSheet("font-size: 25px; font-weight: bold; color: #000000; background-color: #ffffff;")
        
        self.triangle_button = TriangleButton(central_widget)
        self.triangle_button.move(270, 560)  # 设定三角形按钮的位置
        
        self.rounded_rect_button = RoundedRectButton(central_widget)
        self.rounded_rect_button.move(480,560)  # 设定圆角矩形按钮的位置

        self.circular_button = CircularButton(central_widget)
        self.circular_button.move(60, 560)  # 设定圆形按钮的位置
        
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())