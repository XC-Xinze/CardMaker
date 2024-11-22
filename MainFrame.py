# Copyright (c) 2024 [XC-Xinze]
# Licensed under the Custom License. 
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QSplitter, QTreeView, QFileSystemModel, QTextBrowser
from PySide6.QtCore import Qt
#Create main window 
#Inherite from QMainWindow as the children class
class  CardMakerMain(QMainWindow):
    def __init__(self):
        super().__init__()#Construct this class
        self.setWindowTitle('CardMaker')#title
        self.resize(400, 300) #size

if __name__=='__main__':
    app=QApplication(sys.argv)# need QApplication for starting using any GUI
                              # sys.argv is for transfer parameters of booting into program
    window=CardMakerMain()
    window.show()  # 显示窗口
    sys.exit(app.exec())  # 

