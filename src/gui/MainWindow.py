from PyQt5.QtWidgets import QWidget
from .ui_MainWindow import Ui_MainWindow

class MainWindow(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        