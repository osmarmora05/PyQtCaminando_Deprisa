from PyQt5.QtWidgets import QDialog, QVBoxLayout, QFrame, QLabel, QPushButton, QHBoxLayout, QScrollArea, QWidget
from PyQt5.QtCore import Qt
from PyQt5 import QtGui

class Ui_DoubleConfirmationInventory(object):

    def setupUI(self, DoubleConfirmationInventory):
        DoubleConfirmationInventory.setObjectName("DoubleConfirmationInventory")
        DoubleConfirmationInventory.resize(960, 700)
        DoubleConfirmationInventory.hide()
        DoubleConfirmationInventory.setWindowTitle("Doble confirmación")

        # Create the scroll area
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)  # Allows the scroll area to resize the widget

        # Create the main widget to hold the layout
        self.main_widget = QWidget()
        self.layout_widget = QVBoxLayout(self.main_widget)  # Set the QVBoxLayout on the main widget
        self.layout_widget.setContentsMargins(50, 50, 50, 50)
        self.layout_widget.setSpacing(10)
        self.layout_widget.setAlignment(Qt.AlignTop)

        # Header
        self.header_frame = QFrame()
        self.header_layout = QVBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setSpacing(0)
        self.header_layout.setAlignment(Qt.AlignTop)
        self.double_confirmation_label = QLabel("Doble confirmación")
        self.double_confirmation_label.setObjectName("double_confirmation_label")
        self.double_confirmation_label.setStyleSheet(
            """
                QLabel#double_confirmation_label{
                    color: #FAFAFA;
                }
            """
        )
        font = QtGui.QFont()
        font.setPointSize(18)
        self.double_confirmation_label.setFont(font)
        self.double_confirmation_description_label = QLabel(
            "En este apartado podra editar, eliminar productos para luego ingresar a la BD")
        self.double_confirmation_description_label.setObjectName(
            "double_confirmation_description_label")
        self.double_confirmation_description_label.setStyleSheet(
            """
                QLabel#double_confirmation_description_label{
                    color: #71717A;
                }
            """
        )
        font.setPointSize(14)
        self.double_confirmation_description_label.setFont(font)
        self.header_layout.addWidget(self.double_confirmation_label)
        self.header_layout.addWidget(self.double_confirmation_description_label)
        self.header_frame.setLayout(self.header_layout)

        # Main content
        self.main_content_frame = QFrame()
        self.main_content_layout = QVBoxLayout()
        self.main_content_layout.setContentsMargins(0, 0, 0, 0)
        self.main_content_layout.setSpacing(10)
        self.tables = {}

        # Footer
        # Footer (buttons)
        self.footer_frame = QFrame()
        self.footer_frame.setObjectName("footer_frame")
        self.footer_frame.setStyleSheet(
            """
                QFrame#footer_frame{
                    border: 0px solid transparent;
                }
            """
        )
        self.footer_layout = QHBoxLayout()
        self.footer_layout.setContentsMargins(0, 0, 0, 0)
        self.footer_layout.setAlignment(Qt.AlignCenter)
        self.footer_layout.setSpacing(24)
        self.acept_button = QPushButton("Aceptar")
        self.acept_button.setObjectName("acept_button")
        self.acept_button.setMaximumWidth(80)
        self.acept_button.setMaximumHeight(40)
        self.acept_button.setMinimumHeight(40)
        self.acept_button.setMinimumWidth(90)
        self.acept_button.setStyleSheet(
            """
                QPushButton#acept_button {
                    background-color: #FFFFFF;
                    color: #09090B;
                    border-radius: 4px;
                }
                QPushButton#acept_button:hover {
                    opacity: 0.9;
                }
            """
        )
        self.cancel_button = QPushButton("Cancelar")
        self.cancel_button.setObjectName("cancel_button")
        self.cancel_button.setMaximumWidth(80)
        self.cancel_button.setMaximumHeight(40)
        self.cancel_button.setMinimumHeight(40)
        self.cancel_button.setMinimumWidth(90)
        self.cancel_button.setStyleSheet(
            """
               QPushButton#cancel_button {
                    background-color: #09090B;
                    border: 1px solid #27272A;
                    border-radius: 4px;
                    color: #fff;
               }
               
               QPushButton#cancel_button:hover {
                    opacity: 0.9;
               }
            """
        )

        self.footer_layout.addWidget(self.cancel_button)
        self.footer_layout.addWidget(self.acept_button)
        self.footer_frame.setLayout(self.footer_layout)

        self.main_content_frame.setLayout(self.main_content_layout)

        self.layout_widget.addWidget(self.header_frame)
        self.layout_widget.addWidget(self.main_content_frame)
        self.layout_widget.addWidget(self.footer_frame)

        # Set the main widget as the widget of the scroll area
        self.scroll_area.setWidget(self.main_widget)
        
        # Set the scroll area as the main layout of the QDialog
        main_layout = QVBoxLayout(DoubleConfirmationInventory)
        main_layout.addWidget(self.scroll_area)
