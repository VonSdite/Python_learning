import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Icon(QWidget):
    """docstring for Icon"""
    def __init__(self):
        super(Icon, self).__init__()
        
        self.initUI()

    def initUI(self):
        # setGeometry()做了两件事：将窗口在屏幕上显示，并设置了它的尺寸。setGeometry()方法的前两个参数定位了窗口的x轴和y轴位置。第三个参数是定义窗口的宽度，第四个参数是定义窗口的高度。
        self.setGeometry(300, 300, 800, 600)
        self.setWindowIcon(QIcon("gathering.jpg"))
        self.setWindowTitle('2 简单的应用图标.py')

        self.show()

if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    i = Icon()
    sys.exit(app.exec_())

