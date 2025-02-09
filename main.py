from PySide6.QtWidgets import QApplication, QWidget, QFileDialog
from PySide6.QtCore import QThread, Signal
from ui.Ui_musician_new import Ui_Form


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
        pass

    def pause_musician(self):
        pass

    def stop_musician(self):
        pass

class Musician(QThread):
    logSignal = Signal(str)

    def __init__(self, path, bpm):
        super().__init__()
        self.path = path
        self.bpm = bpm

    def run(self):
        pass

if __name__ == "__main__":
    app = QApplication()
    window = MainWindow()
    window.show()
    app.exec()
