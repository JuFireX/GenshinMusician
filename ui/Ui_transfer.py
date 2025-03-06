# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'transfer.ui'
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
    QSizePolicy, QWidget)
import icons_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(240, 360)
        Form.setMinimumSize(QSize(240, 360))
        Form.setMaximumSize(QSize(240, 360))
        icon = QIcon()
        icon.addFile(u":/icons/res/icon.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Form.setWindowIcon(icon)
        self.lineEdit_1 = QLineEdit(Form)
        self.lineEdit_1.setObjectName(u"lineEdit_1")
        self.lineEdit_1.setGeometry(QRect(20, 40, 161, 31))
        self.lineEdit_2 = QLineEdit(Form)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 120, 161, 31))
        self.pushButton_trans = QPushButton(Form)
        self.pushButton_trans.setObjectName(u"pushButton_trans")
        self.pushButton_trans.setGeometry(QRect(80, 280, 81, 31))
        self.pushButton_2 = QPushButton(Form)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(190, 120, 31, 31))
        icon1 = QIcon(QIcon.fromTheme(u"folder"))
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(14, 14))
        self.pushButton_1 = QPushButton(Form)
        self.pushButton_1.setObjectName(u"pushButton_1")
        self.pushButton_1.setGeometry(QRect(190, 40, 31, 31))
        icon2 = QIcon(QIcon.fromTheme(u"folder-open"))
        self.pushButton_1.setIcon(icon2)
        self.pushButton_1.setIconSize(QSize(14, 14))
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 61, 21))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 100, 61, 21))
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 200, 201, 31))
        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 180, 61, 21))
        self.label_3.setFont(font)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u539f\u7434", None))
        self.lineEdit_1.setPlaceholderText(QCoreApplication.translate("Form", u".txt / .mid", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("Form", u".gmid", None))
        self.pushButton_trans.setText(QCoreApplication.translate("Form", u"\u8f6c\u6362", None))
        self.pushButton_2.setText("")
        self.pushButton_1.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u6e90\u6587\u4ef6", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u76ee\u6807\u6587\u4ef6", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u9ed8\u8ba4BPM", None))
    # retranslateUi

