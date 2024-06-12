# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'guide.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QPushButton, QSizePolicy,
    QWidget)

class Ui_Guide(object):
    def setupUi(self, Guide):
        if not Guide.objectName():
            Guide.setObjectName(u"Guide")
        Guide.resize(400, 400)
        self.gridLayout = QGridLayout(Guide)
        self.gridLayout.setObjectName(u"gridLayout")
        self.onebtn = QPushButton(Guide)
        self.onebtn.setObjectName(u"onebtn")
        self.onebtn.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.onebtn, 0, 0, 1, 1)

        self.twobtn = QPushButton(Guide)
        self.twobtn.setObjectName(u"twobtn")
        self.twobtn.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.twobtn, 0, 1, 1, 1)

        self.fourbtn = QPushButton(Guide)
        self.fourbtn.setObjectName(u"fourbtn")
        self.fourbtn.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.fourbtn, 2, 0, 1, 1)

        self.fivebtn = QPushButton(Guide)
        self.fivebtn.setObjectName(u"fivebtn")
        self.fivebtn.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.fivebtn, 2, 1, 1, 1)

        self.threebtn = QPushButton(Guide)
        self.threebtn.setObjectName(u"threebtn")
        self.threebtn.setMinimumSize(QSize(0, 100))

        self.gridLayout.addWidget(self.threebtn, 1, 0, 1, 2)


        self.retranslateUi(Guide)

        QMetaObject.connectSlotsByName(Guide)
    # setupUi

    def retranslateUi(self, Guide):
        Guide.setWindowTitle(QCoreApplication.translate("Guide", u"\u6b22\u8fce", None))
        self.onebtn.setText(QCoreApplication.translate("Guide", u"\u7b97\u6570\u5747\u503c\u5927\u6570\u5b9a\u7406", None))
        self.twobtn.setText(QCoreApplication.translate("Guide", u"\u8d1d\u52aa\u5229\u5927\u6570\u5b9a\u7406", None))
        self.fourbtn.setText(QCoreApplication.translate("Guide", u"\u793a\u4f8b\u4e00", None))
        self.fivebtn.setText(QCoreApplication.translate("Guide", u"\u793a\u4f8b\u4e8c", None))
        self.threebtn.setText(QCoreApplication.translate("Guide", u"\u4e58\u540c\u4f59\u6cd5/\u6df7\u5408\u540c\u4f59\u6cd5", None))
    # retranslateUi

