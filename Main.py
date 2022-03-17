from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5 import uic, QtGui, QtWidgets
from ui import Ui_MainWindow
import sys
from PIL import Image


class UI(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(UI, self).__init__()
                
        # Loading UI
        self.setupUi(self)
        # Button clicking
        self.input_images_button.clicked.connect(self.input_image)
        self.convert_button.clicked.connect(self.convert)
        self.light_mode_checkBox.stateChanged.connect(self.light_mode)
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


    def light_mode(self, checked):
        if checked:
            self.setStyleSheet("background-color: rgb(230, 235, 255);")
            self.light_mode_checkBox.setStyleSheet("color: rgb(34, 47, 62);")
            self.label.setStyleSheet("color: rgb(52, 31, 151);")
            self.input_images_button.setStyleSheet("QPushButton{\n"
            "    background-color: rgb(95, 39, 205);\n"
            "    background-color: rgb(255, 159, 67);\n"
            "}\n"
            "QPushButton:Pressed{\n"
            "    background-color: rgb(238, 82, 83);\n"
            "    color: rgb(254, 202, 87);\n"
            "}")
            self.convert_button.setStyleSheet("QPushButton{    \n"
            "    background-color: rgb(52, 31, 151);\n"
            "    color: rgb(254, 202, 87);\n"
            "}\n"
            "QPushButton:Pressed{\n"
            "    background-color: rgb(238, 82, 83);\n"
            "}")
            self.result_label.setStyleSheet("color: rgb(34, 47, 62);")
        else:
            self.setStyleSheet("background-color: rgb(34, 47, 62);")
            self.light_mode_checkBox.setStyleSheet("color: rgb(238, 82, 83);")
            self.label.setStyleSheet("color: rgb(254, 202, 87);")
            self.input_images_button.setStyleSheet("QPushButton{\n"
            "    background-color: rgb(84, 160, 255);\n"
            "}\n"
            "QPushButton:Pressed{\n"
            "    background-color: rgb(238, 82, 83);\n"
            "}")
            self.convert_button.setStyleSheet("QPushButton{\n"
            "    background-color: rgb(254, 202, 87);\n"
            "}\n"
            "QPushButton:Pressed{\n"
            "    background-color: rgb(238, 82, 83);\n"
            "}")
            self.result_label.setStyleSheet("color: rgb(29, 209, 161);")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = UI()
    ui.setWindowTitle("Images To PDF")
    ui.setWindowIcon(QtGui.QIcon("icon.png"))
    sys.exit(app.exec_())
