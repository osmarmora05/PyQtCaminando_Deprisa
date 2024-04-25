from PyQt5.QtWidgets import QWidget, QLabel, QVBoxLayout, QHBoxLayout, QComboBox, QFrame, QPushButton, QGridLayout, QScrollArea, QButtonGroup
from PyQt5 import QtGui, QtCore
from PyQt5.QtCore import Qt
from src.utils.CustomField import CustomField

"""
widget structure you can see it here

./.backup/Inventory
"""

class Ui_Inventory(object):
    def setupUi(self, Inventory):
        Inventory.setObjectName("Inventory")
        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)

        self.scroll_widget = QWidget()
        self.layout_widget = QVBoxLayout(self.scroll_widget)
        self.layout_widget.setContentsMargins(50, 50, 50, 50)
        self.layout_widget.setSpacing(18)
        self.layout_widget.setAlignment(Qt.AlignTop)
        self.radio_group = QButtonGroup()

        # Header
        self.header_layout = QHBoxLayout()
        self.header_layout.setContentsMargins(0, 0, 0, 0)
        self.header_layout.setAlignment(Qt.AlignTop)
        self.header_frame = QFrame()
        self.template_layout = QVBoxLayout()
        self.template_layout.setContentsMargins(0, 0, 0, 0)
        self.template_layout.setSpacing(8)
        self.datetime_layout = QVBoxLayout()
        self.datetime_layout.setContentsMargins(0, 0, 0, 0)
        self.datetime_layout.setSpacing(0)

        # Header: select combobox template (left)
        self.select_template_label = QLabel(
            "Seleccione el producto a ingresar ....")
        self.select_template_label.setAlignment(Qt.AlignLeft)
        self.select_template_label.setObjectName("select_template_label")
        self.select_template_label.setStyleSheet(
            """
               QLabel#select_template_label {
                    color: #FAFAFA;
                    padding-left: 0
               }
            """
        )
        font = QtGui.QFont()
        font.setPointSize(14)
        self.select_template_label.setFont(font)

        self.template_combobox = QComboBox()
        self.template_combobox.addItems(list(self.fields.keys()))
        self.template_combobox.setObjectName("template_combobox")
        self.template_combobox.setMinimumHeight(40)
        self.template_combobox.setStyleSheet(
            """
            QComboBox#template_combobox{
                    background-color: #09090B;
                    border-radius: 8px;
                    border: 1px solid #27272A;
                    color: #FAFAFA;
                    padding-right: 12px;
                    padding-left: 12px;
            }

            QComboBox#template_combobox QAbstractItemView {
               background-color: #09090B;
               border-radius: 8px;
               border: 1px solid #27272A;
            }

            QComboBox#template_combobox QListView::item:hover{
               background-color: magenta;
               border: 1px solid #27272A;
            }
            """
        )

        self.template_layout.addWidget(self.select_template_label)
        self.template_layout.addWidget(self.template_combobox)

        # Header: datetime (right)
        self.date_label = QLabel("")
        self.date_label.setFont(font)
        self.date_label.setObjectName("date_label")
        self.date_label.setAlignment(Qt.AlignRight)
        self.date_label.setStyleSheet(
            """
               QLabel#date_label{
                    color: #71717A;
               }
            """
        )
        self.date_label.setFont(font)
        self.time_label = QLabel("")
        self.time_label.setFont(font)
        self.time_label.setObjectName("time_label")
        self.time_label.setAlignment(Qt.AlignRight)
        self.time_label.setStyleSheet(
            """
               QLabel#time_label{
                    color: #71717A;
               }
            """
        )
        self.time_label.setFont(font)

        self.datetime_layout.addWidget(self.date_label)
        self.datetime_layout.addWidget(self.time_label)
        self.header_layout.addLayout(self.template_layout)
        self.header_layout.addLayout(self.datetime_layout)
        self.header_frame.setLayout(self.header_layout)

        # Main Content
        self.main_content_frame = QFrame()
        self.main_content_frame.setObjectName("main_content_frame")
        self.main_content_frame.setStyleSheet(
            """
               QFrame#main_content_frame{
                    border-radius: 8px;
                    border: 1px solid #27272A;
                    background-color: #09090B;
                    padding: 40px 60px 40px 60px;
               }
            """
        )
        self.main_content_frame_layout = QVBoxLayout()
        self.main_content_frame_layout.setAlignment(Qt.AlignTop)
        self.main_content_frame_layout.setSpacing(24)
        self.main_content_frame_layout.setContentsMargins(0, 0, 0, 0)

        # Main Content: Confirm article (left)
        self.confirm_articles_layout = QHBoxLayout()
        self.confirm_articles_layout.setContentsMargins(0, 0, 0, 0)
        self.enter_data_label = QLabel(
            "Digite los datos \nnecesarios para procesar su solicitud")
        self.enter_data_label.setObjectName("enter_data_label")
        self.enter_data_label.setStyleSheet(
            """
            QLabel#enter_data_label {
               color: #FAFAFA
            }

            """
        )
        font.setPointSize(18)
        self.enter_data_label.setFont(font)

        # Main Content: Confirm article (right)
        self.item_confirmation_button = QPushButton(
            "Confirmación de artículos")
        item_confirmation_icon = QtGui.QIcon()
        item_confirmation_icon.addPixmap(QtGui.QPixmap(
            "assets/icons/history.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.item_confirmation_button.setIcon(item_confirmation_icon)
        self.item_confirmation_button.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.item_confirmation_button.setObjectName("item_confirmation_button")
        self.item_confirmation_button.setMinimumHeight(40)
        self.item_confirmation_button.setMaximumWidth(220)
        self.item_confirmation_button.setStyleSheet(
            """
               QPushButton#item_confirmation_button{
                    text-align: left;
                    color: #FAFAFA;
                    border: none;
                    border-radius: 7;
                    background-color: #27272A;
                    padding-left: 9;
               }

               QPushButton#item_confirmation_button:hover {
                    background-color: #46464B;
               }

            """
        )
        self.confirm_articles_layout.addWidget(self.enter_data_label)
        self.confirm_articles_layout.addWidget(self.item_confirmation_button)
        self.main_content_frame_layout.addLayout(self.confirm_articles_layout)

        # Main Content: Fields
        self.fields_layout = QGridLayout()
        self.fields_layout.setContentsMargins(0, 0, 0, 0)
        self.fields_layout.setAlignment(Qt.AlignTop)
        self.fields_layout.setVerticalSpacing(24)
        self.fields_layout.setHorizontalSpacing(32)
        self.text_boxes = {}
        self.widgets = []
        self.update_fields()
        self.main_content_frame_layout.addLayout(self.fields_layout)
        self.main_content_frame.setLayout(self.main_content_frame_layout)

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

        self.layout_widget.addWidget(self.header_frame)
        self.layout_widget.addWidget(self.main_content_frame)
        self.layout_widget.addWidget(self.footer_frame)
        self.scroll_area.setWidget(self.scroll_widget)
        self.layout = QVBoxLayout(Inventory)
        self.layout.addWidget(self.scroll_area)
        Inventory.setLayout(self.layout)

    def update_fields(self):
        current_selection = self.template_combobox.currentText()
        col = 0
        row = 0
        counter = 0

        while self.fields_layout.count() > 0:
            widget = self.fields_layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        self.text_boxes.clear()

        for x in self.fields[current_selection]:
            field = CustomField(label=x.label, place_holder=x.place_holder, options=x.options,
                                data_type=x.data_type, field_type=x.field, text_boxes=self.text_boxes)

            self.text_boxes[x.id] = field
            self.fields_layout.addWidget(field, row, col)

            if x.field == "radiobutton":  # Asegúrate de utilizar el nombre correcto del atributo
                self.radio_group.addButton(field.yes_radio)
                self.radio_group.addButton(field.no_radio)

            counter += 1
            col += 1

            if counter % 2 == 0:
                col = 0
                row += 1

            self.widgets.append(field)