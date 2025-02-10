from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtCore import QThread, Signal, QMutex
from ui.Ui_musician_new import Ui_Form
import time


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # self.setWindowOpacity(0.95)   # 设置窗口透明度

        self.path = ""
        self.name = ""
        self.bpm = 80
        self.status = -1

        self.bind()

    def bind(self):
        self.pushButton_select.clicked.connect(self.select_path)
        self.pushButton_start.clicked.connect(self.start)
        self.pushButton_pause.clicked.connect(self.pause)
        self.pushButton_stop.clicked.connect(self.stop)

    def select_path(self):
        self.path = QFileDialog.getOpenFileName(
            self, "选择谱面", "./songs/", "Text Files (*.txt)"
        )[0]
        self.lineEdit_path.setText(self.path)

    def start(self):
        if self.status != -1:
            if self.status == 1:
                self.log_update(f"谱面 {self.name} 已在播放中")
                return
            else:
                self.log_update(f"继续播放")
                self.status = 1
                self.musician.resume()
                return
        else:
            self.path = self.lineEdit_path.text()
            self.name = self.path.split("/")[-1].split(".")[0]
            # 检查谱面文件是否存在
            if self.path == "":
                self.log_update(f"请先选择谱面")
                return
            try:
                with open(self.path, "r", encoding="utf-8") as f:
                    f.close()
            except FileNotFoundError:
                self.log_update(f"谱面 {self.path} 不存在")
                return
            except UnicodeDecodeError:
                self.log_update(f"谱面 {self.path} 编码错误")
                return
            except:
                self.log_update(f"未知错误")
                return
            # 读取 BPM
            if self.lineEdit_bpm.text() != "":
                try:
                    self.bpm = int(self.lineEdit_bpm.text())
                except ValueError:
                    self.log_update(f"BPM 必须为整数")
                    return
            # 参数校验完成
            self.musician = Musician(self)
            self.musician.logSignal.connect(self.log_update)
            self.musician.finished.connect(self.musician.deleteLater)
            self.status = 1
            self.musician.start()
            return

    def pause(self):
        if self.status == -1:
            self.log_update(f"没有谱面可以暂停")
            return
        else:
            if self.status == 0:
                self.log_update(f"继续播放")
                self.status = 1
                self.musician.resume()
                return
            if self.status == 1:
                self.log_update(f"暂停播放")
                self.status = 0
                self.musician.pause()
                return

    def stop(self):
        if self.status == -1:
            self.log_update(f"没有谱面可以结束")
            return
        else:
            self.status = -1
            self.musician.stop()
            return

    def log_update(self, log):
        self.textEdit_log.append(log)


class Musician(QThread):
    logSignal = Signal(str)

    def __init__(self, _parent):
        super().__init__()
        self._parent = _parent
        self.path = str(self._parent.path)
        self.bpm = int(self._parent.bpm)
        self.name = self.path.split("/")[-1].split(".")[0]
        self.is_running = False  # 线程运行标志
        self.is_paused = False  # 线程暂停标志
        self.lock = QMutex()  # 线程同步锁

    def run(self):
        self.logSignal.emit(f"开始播放")
        self.logSignal.emit(f"谱面 {self.name} 速度 {self.bpm}")
        self.is_running = True
        # TODO: 读取谱面文件
        # TODO: 解析谱面文件
        # TODO: 打开原神窗口
        self.mainloop()  # 主循环

    def pause(self):
        self.is_paused = True

    def resume(self):
        # TODO: 恢复音乐播放
        self.is_paused = False

    def stop(self):
        self.logSignal.emit(f"结束播放")
        self.is_running = False
        self.quit()  # 退出线程事件循环
        self.wait()  # 等待线程完成

    def mainloop(self):
        while self.is_running:
            self.lock.lock()  # 获取锁，防止并发问题
            # TODO: 音乐播放
            if not self.is_paused:
                self.logSignal.emit(f"播放中......")
                time.sleep(1)
            self.lock.unlock()  # 释放锁


if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
