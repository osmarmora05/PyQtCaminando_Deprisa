from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLineEdit, QTextEdit, QComboBox, QRadioButton, QLabel, QHBoxLayout, QButtonGroup
from PyQt5 import QtGui
from PyQt5.QtCore import Qt

"""
supported fields
- textbox
- radiobutton
- textarea
- combobox
"""

class CustomField(QWidget):
    def __init__(self, label, place_holder, options=None, data_type="text", field_type="textbox", text_boxes=None):
        super().__init__()

        self.text_boxes = text_boxes
        self.data_type = data_type
        self.field = field_type

        layout = QVBoxLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.setSpacing(5)
        layout.setAlignment(Qt.AlignTop)
        label_widget = QLabel(label)
        label_widget.setStyleSheet("color: #FAFAFA; font-size: 18")

        font = QtGui.QFont()
        font.setPointSize(14)
        label_widget.setFont(font)

        layout.addWidget(label_widget)

        if field_type == "textbox":
            self.widget = QLineEdit()
            self.widget.setPlaceholderText(place_holder)
            self.widget.setStyleSheet(
                """
                QLineEdit{
                    background-color: #09090B;
                    border-radius: 8px;
                    border: 1px solid #27272A;
                    color: #FAFAFA;
                    padding-top: 8px;
                    padding-bottom: 8px;
                    padding-right: 12px;
                    padding-left: 12px;
                }
                """
            )
            layout.addWidget(self.widget)

        elif field_type == "textarea":
            self.widget = QTextEdit()
            self.widget.setPlaceholderText(place_holder)
            self.widget.setStyleSheet(
                """
                QTextEdit{
                    background-color: #09090B;
                    border-radius: 8px;
                    border: 1px solid #27272A;
                    color: #FAFAFA;
                    padding-top: 8px;
                    padding-bottom: 8px;
                    padding-right: 12px;
                    padding-left: 12px;
                }
                """
            )
            self.widget.setMinimumHeight(140)
            layout.addWidget(self.widget)

        elif field_type == "combobox":
            self.widget = QComboBox()
            self.widget.setStyleSheet(
                """
                QComboBox{
                    background-color: #09090B;
                    border-radius: 8px;
                    border: 1px solid #27272A;
                    color: #FAFAFA;
                    padding-right: 12px;
                    padding-left: 12px;
                }
                """
            )
            self.widget.setMinimumHeight(40)
            self.widget.addItems(options)
            layout.addWidget(self.widget)

        elif field_type == "radiobutton":
            self.widget = QWidget()
            self.widget.setMaximumWidth(100)
            layout.addWidget(self.widget)

            radio_layout = QHBoxLayout()

            self.yes_radio = QRadioButton("Sí")
            self.yes_radio.setStyleSheet(
                """
                    QRadioButton {
                        color: #FAFAFA;                
                    }

                    QRadioButton::indicator:checked {
                        background-color: #27272A;
                    }

                    QRadioButton::indicator {
                        background-color: #FAFAFA;
                        border: 2px solid #FAFAFA;
                    }
                """
            )
            self.no_radio = QRadioButton("No")
            self.no_radio.setStyleSheet(
                """
                    QRadioButton {
                        color: #FAFAFA;                
                    }

                    QRadioButton::indicator:checked {
                        background-color: #27272A;
                    }

                    QRadioButton::indicator {
                        background-color: #FAFAFA;
                        border: 2px solid #FAFAFA;
                    }
                """
            )

            radio_layout.addWidget(self.yes_radio)
            radio_layout.addWidget(self.no_radio)

            self.widget.setLayout(radio_layout)


        self.setLayout(layout)