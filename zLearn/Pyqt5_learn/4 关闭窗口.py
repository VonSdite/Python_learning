import sys
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QMessageBox, QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication

class Quit(QWidget):
    """docstring for Quit"""
    def __init__(self):
        super(Quit, self).__init__()
        
        self.initUI()

    def initUI(self):

        # QPushButton(string text, QWidget parent = None)
        # text参数是将显示在按钮中的内容。
        # parent参数是一个用来放置我们按钮的组件。在我们的例子中将会是QWidget组件。
        # 一个应用的组件是分层结构的。在这个分层内，大多数组件都有父类。没有父类的组件是顶级窗口。
        qbtn = QPushButton('退出按钮', self)
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        qbtn.resize(qbtn.sizeHint())
        qbtn.move(30, 30)

        self.setWindowTitle('4 关闭窗口.py')
        self.setWindowIcon(QIcon('gathering.jpg'))
        self.resize(800, 500)
        self.center()
        self.show()

    def closeEvent(self, event):
         
        reply = QMessageBox.question(self, 'Message',
            "Are you sure to quit?", QMessageBox.Yes |
            QMessageBox.No, QMessageBox.No)
 
        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()    

    def center(self):
         
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())   
         

if __name__ == '__main__':
    app = QApplication(sys.argv)
    q = Quit()
    sys.exit(app.exec_())