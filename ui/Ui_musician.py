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
        self.lineEdit_path = QLineEdit(Form)
        self.lineEdit_path.setObjectName(u"lineEdit_path")
        self.lineEdit_path.setGeometry(QRect(20, 40, 161, 31))
        self.lineEdit_bpm = QLineEdit(Form)
        self.lineEdit_bpm.setObjectName(u"lineEdit_bpm")
        self.lineEdit_bpm.setGeometry(QRect(20, 110, 201, 31))
        self.textEdit_log = QTextEdit(Form)
        self.textEdit_log.setObjectName(u"textEdit_log")
        self.textEdit_log.setGeometry(QRect(20, 180, 201, 111))
        self.textEdit_log.setReadOnly(True)
        self.pushButton_start = QPushButton(Form)
        self.pushButton_start.setObjectName(u"pushButton_start")
        self.pushButton_start.setGeometry(QRect(130, 310, 21, 21))
        self.pushButton_start.setStyleSheet(u"border: none")
        icon1 = QIcon()
        icon1.addFile(u":/icons/res/start_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_start.setIcon(icon1)
        self.pushButton_start.setIconSize(QSize(16, 16))
        self.pushButton_start.setCheckable(False)
        self.pushButton_start.setChecked(False)
        self.pushButton_pause = QPushButton(Form)
        self.pushButton_pause.setObjectName(u"pushButton_pause")
        self.pushButton_pause.setGeometry(QRect(160, 310, 21, 21))
        self.pushButton_pause.setStyleSheet(u"border: none")
        icon2 = QIcon()
        icon2.addFile(u":/icons/res/pause_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_pause.setIcon(icon2)
        self.pushButton_stop = QPushButton(Form)
        self.pushButton_stop.setObjectName(u"pushButton_stop")
        self.pushButton_stop.setGeometry(QRect(190, 310, 21, 21))
        self.pushButton_stop.setStyleSheet(u"border: none")
        icon3 = QIcon()
        icon3.addFile(u":/icons/res/stop_dark.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_stop.setIcon(icon3)
        self.label_path = QLabel(Form)
        self.label_path.setObjectName(u"label_path")
        self.label_path.setGeometry(QRect(20, 20, 61, 21))
        font = QFont()
        font.setPointSize(10)
        self.label_path.setFont(font)
        self.label_path.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_bpm = QLabel(Form)
        self.label_bpm.setObjectName(u"label_bpm")
        self.label_bpm.setGeometry(QRect(20, 90, 61, 21))
        self.label_bpm.setFont(font)
        self.label_bpm.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.label_log = QLabel(Form)
        self.label_log.setObjectName(u"label_log")
        self.label_log.setGeometry(QRect(20, 160, 61, 21))
        self.label_log.setFont(font)
        self.label_log.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.pushButton_select = QPushButton(Form)
        self.pushButton_select.setObjectName(u"pushButton_select")
        self.pushButton_select.setGeometry(QRect(190, 40, 31, 31))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_select.sizePolicy().hasHeightForWidth())
        self.pushButton_select.setSizePolicy(sizePolicy)
        icon4 = QIcon(QIcon.fromTheme(u"folder-open"))
        self.pushButton_select.setIcon(icon4)
        self.pushButton_select.setIconSize(QSize(14, 14))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"\u539f\u7434", None))
        self.lineEdit_path.setPlaceholderText(QCoreApplication.translate("Form", u"PATH", None))
        self.lineEdit_bpm.setPlaceholderText(QCoreApplication.translate("Form", u"BPM", None))
        self.pushButton_start.setText("")
        self.pushButton_pause.setText("")
        self.pushButton_stop.setText("")
        self.label_path.setText(QCoreApplication.translate("Form", u"\u4e50\u8c31\u8def\u5f84", None))
        self.label_bpm.setText(QCoreApplication.translate("Form", u"\u64ad\u653e\u901f\u5ea6", None))
        self.label_log.setText(QCoreApplication.translate("Form", u"\u8fd0\u884c\u65e5\u5fd7", None))
        self.pushButton_select.setText("")
    # retranslateUi

