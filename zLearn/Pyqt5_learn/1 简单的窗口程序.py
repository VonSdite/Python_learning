from PyQt5.QtWidgets import QWidget, QApplication, QMessageBox
import sys

app = QApplication(sys.argv)

w = QWidget()
w.setWindowTitle('1 简单的窗口程序.py')
q = QMessageBox(w)
# q.show()
w.resize(800, 500)
w.move(300, 300)
w.show()

sys.exit(app.exec_())
