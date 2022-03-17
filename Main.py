from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtWidgets
import sys
from PIL import Image


class UI(QMainWindow):
    def __init__(self):
        super(UI, self).__init__()
        
        # Loading UI
        uic.loadUi("ui.ui", self)
        # Button clicking
        self.input_images_button.clicked.connect(self.input_image)
        self.convert_button.clicked.connect(self.convert)
        self.show()
        

    def input_image(self):
        try:
            self.input_path = QtWidgets.QFileDialog.getOpenFileNames(None, 'Open a file', '','All Files (*.*)')
        
        except:
            image_message = QtWidgets.QMessageBox()
            image_message.warning(self, "Try Again", "Something went wrong, Please try again.", QtWidgets.QMessageBox.Ok)


    def convert(self):
        images = []
        try:
            save_path = QtWidgets.QFileDialog.getSaveFileName(None, 'Save file', '','PDF files (*.pdf)')
            
            for image in self.input_path[0]:
                images.append(Image.open(image))
            
            images[0].save(save_path[0], save_all=True, append_images=images[1:])
            self.result_label.setText("PDF file has been saved")
        
        except:
            image_message = QtWidgets.QMessageBox()
            image_message.warning(self, "Try Again", "Something went wrong, Please try again.", QtWidgets.QMessageBox.Ok)


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ui = UI()
    ui.setWindowTitle("Images To PDF")
    # ui.setWindowIcon(QtGui.QIcon("icon.png"))
    sys.exit(app.exec_())
