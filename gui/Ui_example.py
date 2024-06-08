# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'example.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_example(object):
    def setupUi(self, example):
        if not example.objectName():
            example.setObjectName(u"example")
        example.resize(400, 300)
        self.gridLayout = QGridLayout(example)
        self.gridLayout.setObjectName(u"gridLayout")
        self.meanlab = QLabel(example)
        self.meanlab.setObjectName(u"meanlab")

        self.gridLayout.addWidget(self.meanlab, 0, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.numlab = QLabel(example)
        self.numlab.setObjectName(u"numlab")
        self.numlab.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.numlab)

        self.numedt = QLineEdit(example)
        self.numedt.setObjectName(u"numedt")

        self.verticalLayout.addWidget(self.numedt)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.timelab = QLabel(example)
        self.timelab.setObjectName(u"timelab")
        self.timelab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.timelab)

        self.timeedt = QLineEdit(example)
        self.timeedt.setObjectName(u"timeedt")

        self.verticalLayout_2.addWidget(self.timeedt)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.surebtn = QPushButton(example)
        self.surebtn.setObjectName(u"surebtn")

        self.gridLayout.addWidget(self.surebtn, 2, 0, 1, 2)

        self.openxlxsbtn = QPushButton(example)
        self.openxlxsbtn.setObjectName(u"openxlxsbtn")

        self.gridLayout.addWidget(self.openxlxsbtn, 3, 0, 1, 2)


        self.retranslateUi(example)

        QMetaObject.connectSlotsByName(example)
    # setupUi

    def retranslateUi(self, example):
        example.setWindowTitle(QCoreApplication.translate("example", u"example", None))
        self.meanlab.setText("")
        self.numlab.setText(QCoreApplication.translate("example", u"\u6837\u672c\u5bb9\u91cf", None))
        self.timelab.setText(QCoreApplication.translate("example", u"\u5b9e\u9a8c\u6b21\u6570", None))
        self.timeedt.setText(QCoreApplication.translate("example", u"1", None))
        self.surebtn.setText(QCoreApplication.translate("example", u"\u786e\u5b9a", None))
        self.openxlxsbtn.setText(QCoreApplication.translate("example", u"\u67e5\u770b\u7ed3\u679c\u8868", None))
    # retranslateUi

