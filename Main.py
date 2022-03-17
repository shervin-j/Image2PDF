from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtGui, QtWidgets
import sys
from PIL import Image
from fpdf import FPDF
from numpy import save


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
        try:
            save_path = QtWidgets.QFileDialog.getSaveFileName(None, 'Save file', '','PDF files (*.pdf)')
            img1 = Image.open(self.input_path[0][0])
            img1.convert("RGB")
            width, height = img1.size
            pdf = FPDF(unit="pt", format=[width, height])
            # pdf = FPDF()
            for image in self.input_path[0]:
                print("HI")
                pdf.add_page()
                pdf.image(image)

            print(save_path)
            pdf.output(save_path[0], "F")
            # self.result_label.setText("PDF file has been saved")
        
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
