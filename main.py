import sys
from PyQt6 import uic
# from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QFileDialog



class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.orginal_pixmap = QPixmap()
        # self.sign_pixmap = QPixmap()
        #
        # self.path_2_img = str()
        # self.sign = str()
        uic.loadUi('./simple.ui', self)
        #
        # self.pushButton.clicked.connect(self.btn_on_click)
        # self.pushButton_2.clicked.connect(qApp.quit)
    def btn_on_click(self):
        print("dffd")
if __name__ == '__main__':
    app = QApplication(sys.argv)
    app.setStyle("plastique")

    window = MainWindow()
    window.show()
    app.exec()
    # sys.exit(app.exec_())