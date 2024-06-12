# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'example2.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Exp2(object):
    def setupUi(self, Exp2):
        if not Exp2.objectName():
            Exp2.setObjectName(u"Exp2")
        Exp2.resize(491, 467)
        self.gridLayout = QGridLayout(Exp2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.explab = QLabel(Exp2)
        self.explab.setObjectName(u"explab")
        self.explab.setMinimumSize(QSize(0, 300))

        self.gridLayout.addWidget(self.explab, 0, 0, 1, 1)

        self.surebtn = QPushButton(Exp2)
        self.surebtn.setObjectName(u"surebtn")

        self.gridLayout.addWidget(self.surebtn, 5, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_2 = QLabel(Exp2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(16777215, 20))
        self.label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_2)

        self.label_3 = QLabel(Exp2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(16777215, 20))
        self.label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.label_3)


        self.gridLayout.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(Exp2)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.lineEdit = QLineEdit(Exp2)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lineEdit)


        self.gridLayout.addLayout(self.verticalLayout, 3, 0, 1, 1)

        self.finlab = QLabel(Exp2)
        self.finlab.setObjectName(u"finlab")
        self.finlab.setAlignment(Qt.AlignCenter)

        self.gridLayout.addWidget(self.finlab, 4, 0, 1, 1)


        self.retranslateUi(Exp2)

        QMetaObject.connectSlotsByName(Exp2)
    # setupUi

    def retranslateUi(self, Exp2):
        Exp2.setWindowTitle(QCoreApplication.translate("Exp2", u"example2", None))
        self.explab.setText("")
        self.surebtn.setText(QCoreApplication.translate("Exp2", u"\u786e\u5b9a", None))
        self.label_2.setText(QCoreApplication.translate("Exp2", u"\u4e2d\u5fc3\u70b9\u6cd5\uff1a0.0962", None))
        self.label_3.setText(QCoreApplication.translate("Exp2", u"\u9a8c\u7b97\u70b9\u6cd5\uff1a0.184", None))
        self.label.setText(QCoreApplication.translate("Exp2", u"\u8bd5\u9a8c\u6b21\u6570", None))
        self.finlab.setText("")
    # retranslateUi

