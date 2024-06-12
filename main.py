from PySide6.QtWidgets import QApplication, QWidget
from PySide6 import QtGui
from PySide6.QtCore import QThread, Signal
from PySide6.QtGui import QIcon


from PySide6.QtCore import QStringListModel
from PySide6.QtUiTools import QUiLoader
from qt_material import apply_stylesheet
import numpy as np
import os

from gui.Ui_Bernoulli import Ui_Bernoulli
from gui.Ui_Poisson import Ui_Poisson
from gui.Ui_Guide import Ui_Guide
from gui.Ui_mcm import Ui_mcm
from gui.Ui_example import Ui_example
from gui.Ui_example2 import Ui_Exp2
from src import draw
from mcm import getnum
from example import exa
import example2

def mygettext(self):
    self.p = self.pled.text()
    self.time = self.timeled.text()
    self.time = int(float(self.time))
    self.timeled.setText(str(self.time))
    print(self.p, self.time)

class WorkThread(QThread):
    signal = Signal(object)
    def __init__(self, num, meanlab, time):
        super().__init__()
        self.num = num
        self.meanlab = meanlab
        self.time = time
    def run(self):
        csvlist = np.array([])
        with open('1.csv', 'w', encoding='utf-8') as fp:
            for i in range(self.time):
                self.pfone = exa(self.num)
                csvlist = np.append(csvlist, self.pfone)
                # self.meanlab.setText(str(self.pfone))
                fp.write(str(self.pfone))
                fp.write('\n')
            print(csvlist)
            fp.write('pf,' + str(csvlist.mean()))
            fp.write('\n')
            fp.write('sigmapf,' + str(csvlist.std()))
            self.meanlab.setText(str('pf' + str(csvlist.mean()) + '\n' + 'sigma' + str(csvlist.std())))

class WorkThread1(QThread):
    def __init__(self, meanlab, time):
        super().__init__()
        self.meanlab = meanlab
        self.time = time
    def run(self):
        num = example2.exa(self.time)
        self.meanlab.setText('失效率：' + str(num))
            
class MainWindows(QWidget, Ui_Guide):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.showWindows()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)

    def showWindows(self):
        self.onewindows = PoissonWindows()
        self.onebtn.clicked.connect(lambda : self.onewindows.show())
        self.twowindows = BernoulliWindows()
        self.twobtn.clicked.connect(lambda : self.twowindows.show())
        self.threewindows = McmWindows()
        self.threebtn.clicked.connect(lambda : self.threewindows.show())
        self.fourwindows = ExampleWindows()
        self.fourbtn.clicked.connect(lambda : self.fourwindows.show())
        self.fivewindows = Example2Windows()
        self.fivebtn.clicked.connect(lambda : self.fivewindows.show())

class BernoulliWindows(QWidget, Ui_Bernoulli):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sure()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)

    def sure(self):
        self.subbtn.clicked.connect(lambda : self.gettext())

    def gettext(self):
        mygettext(self)
        draw('bernoulli', float(self.p), self.time)
        self.pix = QtGui.QPixmap('my_plot.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

class PoissonWindows(QWidget, Ui_Poisson):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sure()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)

    def sure(self):
        self.subbtn.clicked.connect(lambda : self.gettext())

    def gettext(self):
        mygettext(self)
        draw('poisson', float(self.p), self.time)
        self.pix = QtGui.QPixmap('my_plot.png')
        self.piclab.setScaledContents(True)
        self.piclab.setPixmap(self.pix)

class McmWindows(QWidget, Ui_mcm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.sure()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
    def setList(self):
        self.listView.setModel(self.listModel)
    def sure(self):
        self.surebtn.clicked.connect(lambda : self.getnumlist())
        self.sure2btn.clicked.connect(lambda : self.getm())
    def getnumlist(self):
        self.llambda = self.lambdaedt.text()
        self.M = self.medt.text()
        self.x0 = self.x0edt.text()
        if self.cedt.text() == '':
            self.list11 = getnum(eval(self.M), eval(self.llambda), eval(self.x0))
        else:
            self.list11 = getnum(eval(self.M), eval(self.llambda), eval(self.x0), eval(self.cedt.text()))
        self.list1 = [str(x) for x in self.list11]
        self.listModel = QStringListModel()
        self.listModel.setStringList(self.list1)
        self.setList()
    def getm(self):
        self.list11 = [x / eval(self.M) for x in self.list11]
        self.list1 = [str(x) for x in self.list11]
        self.listModel = QStringListModel()
        self.listModel.setStringList(self.list1)
        self.setList()

class ExampleWindows(QWidget, Ui_example):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.surebtnclk()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)

    def surebtnclk(self):
        
        self.surebtn.clicked.connect(lambda : self.star())
        self.openxlxsbtn.clicked.connect(lambda : os.popen('1.csv'))
    def star(self):
        self.num = int(float(self.numedt.text()))
        self.time = int(float(self.timeedt.text()))
        self.workThread = WorkThread(self.num, self.meanlab, self.time)
        self.pfone = self.workThread.start()
        self.workThread.finished.connect(lambda : self.overworkThread())
        self.meanlab.setText('计算中……')

    def overworkThread(self):
        self.workThread.deleteLater()


class Example2Windows(QWidget, Ui_Exp2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.surebtnclk()
        appIcon = QIcon('./icon/icon.ico')
        self.setWindowIcon(appIcon)
        self.band()

    def band(self):
        self.pix = QtGui.QPixmap('exp2.png')
        self.explab.setScaledContents(True)
        self.explab.setPixmap(self.pix)

    def surebtnclk(self):
        
        self.surebtn.clicked.connect(lambda : self.star())
    def star(self):
        self.time = int(float(self.lineEdit.text()))
        self.workThread = WorkThread1(self.finlab, self.time)
        self.workThread.start()
        self.workThread.finished.connect(lambda : self.overworkThread())
        self.finlab.setText('计算中……')

    def overworkThread(self):
        self.workThread.deleteLater()
    


if __name__ =="__main__":
    app = QApplication([])
    apply_stylesheet(app, theme='light_blue.xml', invert_secondary=True)
    window = MainWindows()
    window.show()
    app.exec()