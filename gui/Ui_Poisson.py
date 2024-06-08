# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Poisson.ui'
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

class Ui_Poisson(object):
    def setupUi(self, Poisson):
        if not Poisson.objectName():
            Poisson.setObjectName(u"Poisson")
        Poisson.resize(412, 388)
        self.gridLayout = QGridLayout(Poisson)
        self.gridLayout.setObjectName(u"gridLayout")
        self.piclab = QLabel(Poisson)
        self.piclab.setObjectName(u"piclab")
        self.piclab.setMinimumSize(QSize(384, 288))

        self.gridLayout.addWidget(self.piclab, 0, 0, 1, 2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.plab = QLabel(Poisson)
        self.plab.setObjectName(u"plab")
        self.plab.setMinimumSize(QSize(192, 0))
        self.plab.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.plab)

        self.pled = QLineEdit(Poisson)
        self.pled.setObjectName(u"pled")
        self.pled.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.pled)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.timelab = QLabel(Poisson)
        self.timelab.setObjectName(u"timelab")
        self.timelab.setMinimumSize(QSize(192, 0))
        self.timelab.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.timelab)

        self.timeled = QLineEdit(Poisson)
        self.timeled.setObjectName(u"timeled")
        self.timeled.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.timeled)


        self.gridLayout.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.subbtn = QPushButton(Poisson)
        self.subbtn.setObjectName(u"subbtn")

        self.gridLayout.addWidget(self.subbtn, 2, 0, 1, 2)


        self.retranslateUi(Poisson)

        QMetaObject.connectSlotsByName(Poisson)
    # setupUi

    def retranslateUi(self, Poisson):
        Poisson.setWindowTitle(QCoreApplication.translate("Poisson", u"Poisson", None))
        self.piclab.setText("")
        self.plab.setText(QCoreApplication.translate("Poisson", u"\u5747\u503c\u65b9\u5dee", None))
        self.timelab.setText(QCoreApplication.translate("Poisson", u"\u5b9e\u9a8c\u6b21\u6570", None))
        self.subbtn.setText(QCoreApplication.translate("Poisson", u"\u786e\u5b9a", None))
    # retranslateUi

