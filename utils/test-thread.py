import time
from PySide6.QtCore import QThread, Signal, QMutex
from PySide6.QtWidgets import QApplication, QPushButton, QVBoxLayout, QLabel, QWidget


# 创建一个主窗口
class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QThread Example")
        self.setGeometry(500, 200, 240, 240)
        self.setFixedSize(self.size())

        self.status_label = QLabel("Thread status: Not running", self)
        self.count_label = QLabel("Counter: 0", self)
        self.start_btn = QPushButton("Start", self)
        self.pause_btn = QPushButton("Pause", self)
        self.resume_btn = QPushButton("Resume", self)
        self.stop_btn = QPushButton("Stop", self)

        self.thread = MyThread()

        # 信号与槽函数连接
        self.thread.count_changed.connect(lambda count: self.count_label.setText(f"Counter: {count}"))
        self.thread.status_changed.connect(lambda status: self.status_label.setText(f"Thread status: {status}"))

        self.start_btn.clicked.connect(self.thread.start)
        self.pause_btn.clicked.connect(self.thread.pause)
        self.resume_btn.clicked.connect(self.thread.resume)
        self.stop_btn.clicked.connect(self.thread.stop)

        # 布局设置
        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.count_label)
        layout.addWidget(self.start_btn)
        layout.addWidget(self.pause_btn)
        layout.addWidget(self.resume_btn)
        layout.addWidget(self.stop_btn)
        self.setLayout(layout)

class MyThread(QThread):
    count_changed = Signal(int)  # 信号，用于通知计数器值变化
    status_changed = Signal(str)  # 信号，用于通知线程状态变化

    def __init__(self):
        super().__init__()
        self.is_running = False  # 线程运行标志
        self.is_paused = False   # 线程暂停标志
        self.lock = QMutex()     # 线程同步锁

    def run(self):
        self.status_changed.emit("Thread started")
        self.is_running = True
        self.count = 0

        while self.is_running:
            self.lock.lock()  # 获取锁，防止并发问题
            if not self.is_paused:
                self.count += 1
                self.count_changed.emit(self.count)
                time.sleep(0.1)  # 模拟任务延迟
            self.lock.unlock()  # 释放锁

    def pause(self):
        self.is_paused = True
        self.status_changed.emit("Thread paused")

    def resume(self):
        self.is_paused = False
        self.status_changed.emit("Thread resumed")

    def stop(self):
        self.is_running = False
        self.status_changed.emit("Thread stopped")
        self.quit()  # 退出线程事件循环
        self.wait()  # 等待线程完成

# 主程序
if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()