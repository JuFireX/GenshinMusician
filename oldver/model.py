import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
import pyautogui
import threading
import time
import numpy as np
import pyautogui
import cv2


template_path = "data\\matchpicture.png"
target_size = (1854, 632)

gui_condition = -1  # 0: 暂停， 1: 运行， -1: 结束
get_path = ""
get_bpm = 120

click = None
scores = []
tik = 0

dark_stylesheet = """
    QMainWindow {
        background-color: #191919;
    }

    QLabel {
        font-size: 28px;
        font-family: microsoft yahei ui;
        border: none;
        padding: 5px;
    }

    QLineEdit {
        font-size: 24px; 
        font-family: microsoft yahei ui;
        border-radius: 8px;
        padding: 5px;
        background-color: #2d2d2d;
        color: #7b7b7b;
        border: 2px solid #4e4e4e;
    }

    QLineEdit:hover {
        border: 2px solid #5e5e5e;
    }

    QLineEdit:focus {
        border: 2px solid #7e7e7e;
    }

    QLabel {
        color: #fcfcfc;
    }

    QScrollArea {
        font-size: 24px;
        padding: 5px;
        background-color: #2d2d2d;
        border: 2px solid #4e4e4e;
        border-radius: 8px;
    }

    QScrollArea QWidget QWidget {
        background-color: #2d2d2d;
    }

    QPushButton {
        border: none;
        border-radius: 8px;
        background-color: #191919;
    }

    QPushButton:hover {
        background-color: #292929;
    }

    QPushButton:pressed {
        background-color: #494949;
    }
"""

light_stylesheet = """
    QMainWindow {
        background-color: #f2f2f2;
    }

    QLabel {
        font-size: 28px;
        font-family: microsoft yahei ui;
        border: none;
        padding: 5px;
    }

    QLineEdit {
        font-size: 24px; 
        font-family: microsoft yahei ui;
        border-radius: 8px;
        padding: 5px;
        background-color: #fffef9;
        color: #2d2d2d;
        border: 2px solid #cecece; 
    }

    QLineEdit:hover {
        border: 2px solid #bebebe;
    }

    QLineEdit:focus {
        border: 2px solid #9e9e9e;
    }


    QLabel {
        color: #070707;
    }

    QScrollArea {
        font-size: 24px;
        padding: 5px;
        background-color: #fffef9;
        border: 2px solid #cecece;
        border-radius: 8px;
    }

    QScrollArea QWidget QWidget {
        background-color: #fffef9;
    }

    QPushButton {
        border: none;
        border-radius: 8px;
        background-color: #f2f2f2;
    }

    QPushButton:hover {
        background-color: #e2e2e2;
    }

    QPushButton:pressed {
        background-color: #c2c2c2;
    }
"""


# 检测系统主题
def is_system_light_mode():
    return 1  # 这里暂时返回True，以便调试，真实环境下应该调用系统API获取系统主题


def load_musical_score(filename):
    musical_score = []
    try:
        with open(filename, "r", encoding="utf-8") as file:
            for line in file:
                line = line.strip()
                musical_score.append(tuple(line))
            print(f"乐谱文件 '{filename}' 加载成功")
    except FileNotFoundError:
        print(f"乐谱文件 '{filename}' 路径错误")
    except Exception as e:
        print(f"乐谱文件 '{filename}' 加载失败: {e}")

    return musical_score


# 截取屏幕并匹配模板
def capture_and_match_template():
    """
    截取屏幕、加载并调整模板图片，然后匹配模板位置。用以定位原神窗口。

    参数:
        template_path (str): 模板图片的路径。
        target_size (tuple): 模板图片的目标大小 (width, height)。

    返回:
        min_loc (tuple): 模板在截图中的左上角位置 (x, y)。

    """
    screenshot = np.array(pyautogui.screenshot())
    template = cv2.imread(template_path)
    if template is None:
        print(f"定位模板 '{template_path}' 路径错误")

    resized_template = cv2.resize(template, target_size)
    result = cv2.matchTemplate(screenshot, resized_template, cv2.TM_SQDIFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    print(f"窗口定位 '{min_loc}' 已加载")

    return min_loc


class MainLogicWorker(QThread):
    log = Signal(str)

    def __init__(self):
        super().__init__()

    def active(self):
        global click, scores, tik
        self.click = capture_and_match_template()
        click = self.click
        self.scores = load_musical_score(get_path)
        scores = self.scores
        self.tik = 12 / get_bpm
        try:
            pyautogui.click(self.click)
        except pyautogui.FailSafeException:
            self.log.emit(f"窗口激活失败")
            return 0
        except Exception as e:
            self.log.emit(f"窗口激活失败 {e}")
            return 0
        self.log.emit(f"窗口激活成功")
        return 1

    def work(self):
        global gui_condition
        self.log.emit("主逻辑开始")

        if not self.active():
            gui_condition = -1
            self.log.emit("主逻辑异常结束")
            return

        index = 0
        while index < len(self.scores):
            if gui_condition == -1:
                break

            if gui_condition == 0:
                continue

            chord = self.scores[index]
            pyautogui.hotkey(*chord)
            time.sleep(self.tik)
            index += 1

        gui_condition = -1
        self.log.emit("主逻辑结束")
        time.sleep(0.5)


class RunButton(QPushButton):
    clicked_button_run = Signal(str)

    def __init__(self, parent=None, path_in=None, bpm_in=None):
        super().__init__(parent)
        self.setFixedSize(36, 36)
        self.clicked.connect(self.run_clicked)
        self.path_in = path_in
        self.bpm_in = bpm_in
        self.update_icon()

    def update_icon(self):
        if is_system_light_mode():
            self.setIcon(QIcon("data\\run light mode.svg"))
        else:
            self.setIcon(QIcon("data\\run dark mode.svg"))

    def run_clicked(self):
        global gui_condition, get_path, get_bpm
        if gui_condition == 1:
            self.clicked_button_run.emit(f'歌曲 "{get_path}" 正在运行！')
            return
        if gui_condition == 0:
            self.clicked_button_run.emit(f'歌曲 "{get_path}" 继续')
            pyautogui.click(click)
            time.sleep(0.5)
            gui_condition = 1
            return
        try:
            get_path = str(self.path_in.text())
            get_bpm = int(self.bpm_in.text())
            gui_condition = 1
            self.clicked_button_run.emit(f'乐谱路径 "{get_path}"\n预定速度 {get_bpm}')
            self.clicked_button_run.emit(f"等待主逻辑响应···")
        except:
            self.clicked_button_run.emit(f"获取路径或速度失败！")
            return


class PauseButton(QPushButton):
    clicked_button_pause = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(36, 36)
        self.clicked.connect(self.pause_clicked)
        self.update_icon()

    def update_icon(self):
        if is_system_light_mode():
            self.setIcon(QIcon("data\\pause light mode.svg"))
        else:
            self.setIcon(QIcon("data\\pause dark mode.svg"))

    def pause_clicked(self):
        global gui_condition, get_path, get_bpm
        if gui_condition == -1:
            self.clicked_button_pause.emit(f"没有歌曲正在运行！")
            return
        if gui_condition == 1:
            gui_condition = 0
            self.clicked_button_pause.emit(f'歌曲 "{get_path}" 暂停')
            time.sleep(0.5)
        if gui_condition == 0:
            gui_condition = 1
            self.clicked_button_pause.emit(f'歌曲 "{get_path}" 继续')
            pyautogui.click(click)
            time.sleep(0.5)


class StopButton(QPushButton):
    clicked_button_stop = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setFixedSize(36, 36)
        self.clicked.connect(self.stop_clicked)
        self.update_icon()

    def update_icon(self):
        if is_system_light_mode():
            self.setIcon(QIcon("data\\stop light mode.svg"))
        else:
            self.setIcon(QIcon("data\\stop dark mode.svg"))

    def stop_clicked(self):
        global gui_condition, get_path, get_bpm
        if gui_condition == -1:
            self.clicked_button_stop.emit("没有歌曲正在运行！")
            return
        gui_condition = -1
        self.clicked_button_stop.emit(f'歌曲 "{get_path}" 停止运行')
        time.sleep(0.5)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.condition = 0
        self.setWindowTitle("Genshin Musician")
        self.setFixedSize(600, 800)
        self.setWindowOpacity(0.95)
        if is_system_light_mode():
            self.setWindowIcon(QIcon("data\\icon light mode.svg"))
        else:
            self.setWindowIcon(QIcon("data\\icon dark mode.svg"))
        self.initUI()

    def initUI(self):  # 创建主界面
        widget = QWidget(self)
        self.setCentralWidget(widget)
        if is_system_light_mode():
            self.setStyleSheet(light_stylesheet)  # 设置浅色主题
        else:
            self.setStyleSheet(dark_stylesheet)  # 设置暗色主题

        # 乐谱路径
        self.label_path = QLabel(widget)
        self.label_path.move(25, 20)
        self.label_path.setText("乐谱路径")

        self.line_edit_path = QLineEdit(widget)
        self.line_edit_path.move(40, 70)
        self.line_edit_path.resize(520, 60)
        self.line_edit_path.setPlaceholderText("Path")

        # 歌曲速度
        self.label_bpm = QLabel(widget)
        self.label_bpm.move(25, 150)
        self.label_bpm.setText("歌曲速度")

        self.line_edit_bpm = QLineEdit(widget)
        self.line_edit_bpm.move(40, 200)
        self.line_edit_bpm.resize(520, 60)
        self.line_edit_bpm.setPlaceholderText("BPM")

        # 运行日志
        self.label_log = QLabel(widget)
        self.label_log.move(25, 280)
        self.label_log.setText("运行日志")

        self.scroll_area = QScrollArea(widget)
        self.scroll_area.setGeometry(40, 330, 520, 360)
        self.scroll_area.setWidgetResizable(True)

        self.log_content = QWidget()
        self.scroll_area.setWidget(self.log_content)

        self.layout = QVBoxLayout(self.log_content)
        # self.layout.setAlignment(Qt.AlignTop)
        # self.layout.setSpacing(0)

        self.add_log(f"等待开始···")

        # 创建按钮
        self.run_button = RunButton(widget, self.line_edit_path, self.line_edit_bpm)
        self.run_button.move(350, 730)  # run按钮的位置
        self.run_button.clicked_button_run.connect(self.handle_run_button)

        self.pause_button = PauseButton(widget)
        self.pause_button.move(430, 730)  # pause按钮的位置
        self.pause_button.clicked_button_pause.connect(self.handle_pause_button)

        self.stop_button = StopButton(widget)
        self.stop_button.move(510, 730)  # stop按钮的位置
        self.stop_button.clicked_button_stop.connect(self.handle_stop_button)

    def handle_run_button(self, msg):
        self.add_log(f"{msg}")

    def handle_pause_button(self, msg):
        self.add_log(f"{msg}")

    def handle_stop_button(self, msg):
        self.add_log(f"{msg}")

    def add_log(self, log):
        log_label = QLabel(log, alignment=Qt.AlignLeft)
        self.layout.addWidget(log_label)
        self.scroll_area.verticalScrollBar().setValue(
            self.scroll_area.verticalScrollBar().maximum()
        )
        self.scroll_area.update()


def gui_main(app, window):
    window.show()
    sys.exit(app.exec_())


def worker_thread(worker: MainLogicWorker):
    global gui_condition
    while True:
        if gui_condition == 1:
            worker.work()
            gui_condition = -1
            time.sleep(0.5)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    worker = MainLogicWorker()
    worker.log.connect(window.add_log)
    worker_loop = threading.Thread(target=worker_thread, args=(worker,))
    worker_loop.daemon = True
    worker_loop.start()
    gui_main(app, window)
