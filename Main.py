from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtGui, QtWidgets
import sys


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        # Loading UI
        uic.loadUi("ui.ui", self)
        # Button clicking
        self.input_images_button.clicked.connect(self.input_image)
        self.convert_button.clicked.connect(self.input_image)


        self.show()
        

    def input_image(self):
        try:
            path = QtWidgets.QFileDialog.getOpenFileNames(None, 'Open a file', '','All Files (*.*)')
            print(path)
        except:
            image_message = QtWidgets.QMessageBox()
            image_message.warning(self, "Choosing image", "Please choose an image", QtWidgets.QMessageBox.Ok)
        return None


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = UI()
    ui.setWindowTitle("Images To PDF")
    # ui.setWindowIcon(QtGui.QIcon("icon.png"))
    sys.exit(app.exec_())
