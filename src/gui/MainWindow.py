from PyQt5.QtWidgets import QWidget
from .ui_MainWindow import Ui_MainWindow
from .Inventory import Inventory

class MainWindow(QWidget,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.ui_inventary = Inventory()
        self.initComponents()
        

    def initComponents(self):
        self.stackedWidget.addWidget(self.ui_inventary)
        self.inventario_button.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.ui_inventary))