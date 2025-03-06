from PySide6.QtWidgets import QApplication, QWidget, QFileDialog, QMessageBox
from ui.Ui_transfer import Ui_Form
import os
import sys


class MainWindow(QWidget, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.path1 = ""
        self.path2 = ""

        self.bind()

    def bind(self):
        self.pushButton_1.clicked.connect(self.openFileBef)
        self.pushButton_2.clicked.connect(self.openFileAft)
        self.pushButton_trans.clicked.connect(self.transfer)

    def openFileBef(self):
        self.path = QFileDialog.getOpenFileName(
            self, "选择谱面", "./Gmidi/songs/", "Text Files (*.txt);;Midi Files (*.mid)"
        )[0]
        self.lineEdit_1.setText(self.path)
        self.path1 = self.path

    def openFileAft(self):
        self.path = QFileDialog.getSaveFileName(
            self, "保存谱面", "./Gmidi/songs/", "Gmidi Files (*.gmid)"
        )[0]
        self.lineEdit_2.setText(self.path)
        self.path2 = self.path

    def transfer(self):
        if self.path1 == "":
            QMessageBox.information(self, "注意", "请选择谱面！")
            return
        if self.path2 == "":
            QMessageBox.information(self, "注意", "请选择保存路径！")
            return
        transfer(self.path1, self.path2)
        QMessageBox.information(self, "提示", "转换成功！")

def transfer(path1, path2):
    with open(path1, "r") as f:
        content = f.read()
    with open(path2, "w") as f:
        f.write(content)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    sys.exit(app.exec())