import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import Qt
from ctypes import windll, Structure, c_int, c_uint, POINTER, byref

# 定义DWM_BLURBEHIND结构体
class DWM_BLURBEHIND(Structure):
    _fields_ = [
        ("dwFlags", c_uint),
        ("fEnable", c_int),
        ("hRgnBlur", c_int),  # 如果需要特定区域模糊，可以设置此字段
        ("fTransitionOnMaximized", c_int),
    ]

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        # 设置窗口无边框
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        # 设置窗口透明度
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        # 设置窗口尺寸
        self.resize(400, 300)
        # 调用Win32 API启用模糊效果
        self.setup_blur()

    def setup_blur(self):
        hwnd = self.winId().__int__()
        # 定义常量
        DWM_BB_ENABLE = 0x00000001
        DWM_BB_BLURREGION = 0x00000002  # 如果需要特定区域模糊，可以设置此字段
        DWM_BB_TRANSITIONONMAXIMIZED = 0x00000004

        # 创建DWM_BLURBEHIND实例
        bb = DWM_BLURBEHIND()
        # 设置模糊效果的标志
        bb.dwFlags = DWM_BB_ENABLE
        bb.fEnable = 1  # 启用模糊效果
        bb.fTransitionOnMaximized = 0  # 0: false, 1: true

        # 使用pywin32调用DwmEnableBlurBehindWindow设置模糊效果
        result = windll.dwmapi.DwmEnableBlurBehindWindow(hwnd, byref(bb))
        if result != 0:
            print(f"启用模糊效果失败，错误码: {result}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
