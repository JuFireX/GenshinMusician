# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'musician.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QTextEdit, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 360)
        self.lineEdit_path = QLineEdit(Form)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setGeometry(QRect(30, 40, 181, 31))
        self.lineEdit_bpm = QLineEdit(Form)
        self.lineEdit_bpm.setObjectName(u"lineEdit_bpm")
        self.lineEdit_bpm.setGeometry(QRect(30, 110, 181, 31))
        self.textEdit_log = QTextEdit(Form)
        self.textEdit_log.setObjectName(u"textEdit_log")
        self.textEdit_log.setGeometry(QRect(30, 180, 181, 111))
        self.textEdit_log.setReadOnly(True)
        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setGeometry(QRect(130, 310, 21, 21))
        self.pushButton_pause = QPushButton(Form)
        self.pushButton_pause.setObjectName(u"pushButton_pause")
        self.pushButton_pause.setGeometry(QRect(160, 310, 21, 21))
        self.pushButton_stop = QPushButton(Form)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setGeometry(QRect(190, 310, 21, 21))
        self.label_path = QLabel(Form)
        self.label_path.setObjectName(u"label_path")
        self.label_path.setGeometry(QRect(30, 20, 61, 21))
        font = QFont()
        font.setPointSize(10)
        self.label_path.setFont(font)
        self.label_path.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_bpm = QLabel(Form)
        self.label_bpm.setObjectName(u"label_bpm")
        self.label_bpm.setGeometry(QRect(30, 90, 61, 21))
        self.label_bpm.setFont(font)
        self.label_bpm.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_log = QLabel(Form)
        self.label_log.setObjectName(u"label_log")
        self.label_log.setGeometry(QRect(30, 160, 61, 21))
        self.label_log.setFont(font)
        self.label_log.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u539f\u7434", None))
        self.lineEdit_path.setPlaceholderText(QCoreApplication.translate("Form", u"PATH", None))
        self.lineEdit_bpm.setPlaceholderText(QCoreApplication.translate("Form", u"BPM", None))
        self.pushButton_start.setText(QCoreApplication.translate("Form", u"0", None))
        self.pushButton_pause.setText(QCoreApplication.translate("Form", u"1", None))
        self.pushButton_stop.setText(QCoreApplication.translate("Form", u"2", None))
        self.label_path.setText(QCoreApplication.translate("Form", u"\u4e50\u8c31\u8def\u5f84", None))
        self.label_bpm.setText(QCoreApplication.translate("Form", u"\u64ad\u653e\u901f\u5ea6", None))
        self.label_log.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u65e5\u5fd7", None))
    # retranslateUi

