# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mcm.ui'
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
    QListView, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_mcm(object):
    def setupUi(self, mcm):
        if not mcm.objectName():
            mcm.setObjectName(u"mcm")
        mcm.resize(347, 383)
        self.gridLayout = QGridLayout(mcm)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lambdlab = QLabel(mcm)
        self.lambdlab.setObjectName(u"lambdlab")
        self.lambdlab.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lambdlab)

        self.lambdaedt = QLineEdit(mcm)
        self.lambdaedt.setObjectName(u"lambdaedt")

        self.verticalLayout.addWidget(self.lambdaedt)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.mlab = QLabel(mcm)
        self.mlab.setObjectName(u"mlab")
        self.mlab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.mlab)

        self.medt = QLineEdit(mcm)
        self.medt.setObjectName(u"medt")

        self.verticalLayout_2.addWidget(self.medt)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.x0lab = QLabel(mcm)
        self.x0lab.setObjectName(u"x0lab")
        self.x0lab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.x0lab)

        self.x0edt = QLineEdit(mcm)
        self.x0edt.setObjectName(u"x0edt")

        self.verticalLayout_4.addWidget(self.x0edt)


        self.gridLayout.addLayout(self.verticalLayout_4, 1, 2, 1, 1)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.clab = QLabel(mcm)
        self.clab.setObjectName(u"clab")
        self.clab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_3.addWidget(self.clab)

        self.cedt = QLineEdit(mcm)
        self.cedt.setObjectName(u"cedt")

        self.verticalLayout_3.addWidget(self.cedt)


        self.gridLayout.addLayout(self.verticalLayout_3, 1, 3, 1, 1)

        self.listView = QListView(mcm)
        self.listView.setObjectName(u"listView")
        font = QFont()
        font.setPointSize(15)
        self.listView.setFont(font)

        self.gridLayout.addWidget(self.listView, 0, 0, 1, 4)

        self.surebtn = QPushButton(mcm)
        self.surebtn.setObjectName(u"surebtn")

        self.gridLayout.addWidget(self.surebtn, 2, 0, 1, 4)

        self.sure2btn = QPushButton(mcm)
        self.sure2btn.setObjectName(u"sure2btn")

        self.gridLayout.addWidget(self.sure2btn, 3, 0, 1, 4)


        self.retranslateUi(mcm)

        QMetaObject.connectSlotsByName(mcm)
    # setupUi

    def retranslateUi(self, mcm):
        mcm.setWindowTitle(QCoreApplication.translate("mcm", u"\u4e58\u540c\u4f59\u6cd5/\u6df7\u5408\u540c\u4f59\u6cd5", None))
        self.lambdlab.setText(QCoreApplication.translate("mcm", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">lambda</p></body></html>", None))
        self.mlab.setText(QCoreApplication.translate("mcm", u"M", None))
        self.x0lab.setText(QCoreApplication.translate("mcm", u"x0", None))
        self.clab.setText(QCoreApplication.translate("mcm", u"c", None))
        self.surebtn.setText(QCoreApplication.translate("mcm", u"\u786e\u5b9a", None))
        self.sure2btn.setText(QCoreApplication.translate("mcm", u"\u9664\u4ee5M", None))
    # retranslateUi

