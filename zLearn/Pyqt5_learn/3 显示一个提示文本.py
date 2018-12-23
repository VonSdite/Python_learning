from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication
from PyQt5.QtGui import QFont, QIcon
import sys

class Tip(QWidget):
    """docstring for Tip"""
    def __init__(self):
        super(Tip, self).__init__()

        self.initUI()

    def initUI(self):

        QToolTip.setFont(QFont('SansSerif', 10))

        self.setToolTip('This is a <b>QWidget</b> widget')

        btn = QPushButton('Button', self)
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        self.setGeometry(300, 300, 800, 500)
        self.setWindowTitle('3 显示一个提示文本.py')
        self.setWindowIcon(QIcon('gathering.jpg'))
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    t = Tip()
    sys.exit(app.exec_())

