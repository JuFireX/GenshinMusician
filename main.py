from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtCore import QThread, Signal
from ui.Ui_musician_new import Ui_Form
import time


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.setWindowOpacity(0.95)

        self.path = ""
        self.bpm = 80
        self.condition = -1

        self.bind()

    def bind(self):
        self.pushButton_select.clicked.connect(self.select_path)
        self.pushButton_start.clicked.connect(self.start_musician)
        self.pushButton_pause.clicked.connect(self.pause_musician)
        self.pushButton_stop.clicked.connect(self.stop_musician)

    def select_path(self):
        self.path = QFileDialog.getOpenFileName(
            self, "选择谱面", "./songs/", "Text Files (*.txt)"
        )[0]
        self.lineEdit_path.setText(self.path)

    def start_musician(self):
        if self.condition != -1:
            if self.condition == 1:
                self.log_update(f"谱面 {self.path} 已在播放中")
                return
            else:
                self.log_update(f"继续播放")
                self.condition = 1
                return
        else:
            self.path = self.lineEdit_path.text()
            if self.path == "":
                self.log_update(f"请先选择谱面")
                return
            if self.lineEdit_bpm.text() != "":
                try:
                    self.bpm = int(self.lineEdit_bpm.text())
                except ValueError:
                    self.log_update(f"BPM 必须为整数")
                    return

            self.log_update(f"开始播放谱面 {self.path}\n 速度 {self.bpm}")
            self.condition = 1
            self.musician = Musician(self.path, self.bpm)
            self.musician.logSignal.connect(self.log_update)
            self.musician.start()
            self.musician.finished.connect(self.musician.deleteLater)

    def pause_musician(self):
        if self.condition != 1:
            self.log_update(f"没有谱面可以暂停")
            return
        else:
            self.log_update(f"暂停播放")
            self.condition = 0
            # self.musician.terminate()
            # self.musician.wait()

    def stop_musician(self):
        if self.condition == -1:
            self.log_update(f"没有谱面可以停止")
            return
        else:
            self.condition = -1
            self.musician.terminate()
            self.musician.wait()
            self.log_update(f"结束播放")

    def log_update(self, log):
        self.textEdit_log.append(log)


class Musician(QThread):
    logSignal = Signal(str)

    def __init__(self, path, bpm):
        super().__init__()
        self.path = path
        self.bpm = bpm

    def run(self):
        self.logSignal.emit(f"线程开始")
        # TODO: 开始播放音乐
        for i in range(3):
            time.sleep(1)
            self.logSignal.emit(f"播放进度 {i+1}/3")
        self.logSignal.emit(f"播放完成")
        self.logSignal.emit(f"线程结束")



if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
