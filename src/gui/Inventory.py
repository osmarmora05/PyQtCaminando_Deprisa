from PyQt5.QtWidgets import QWidget, QLineEdit, QTextEdit, QComboBox, QTableWidgetItem, QPushButton
from PyQt5 import QtGui
from src.utils.Form import Form
from src.helpers.datetime_helper import getDate, getTime
from .ui_Inventory import Ui_Inventory
from PyQt5.QtCore import QTimer
from .DoubleConfirmationInventory import DoubleConfirmationInventory

class Inventory(QWidget, Ui_Inventory):
    def __init__(self):
        super().__init__()
        self.fields = {
            "Generico": [
                Form(id="nombre", label="Nombre",
                     place_holder="Digita el nombre", field="textbox"),
                Form(id="modelo", label="Modelo",
                     place_holder="Digite el modelo", field="textbox"),
                Form(id="marca", label="Marca",
                     place_holder="Digite la marca", field="textbox"),
                Form(id="dimensiones", label="Dimensiones",
                     place_holder="Digite la dimension", field="textbox"),
                Form(id="descripcion", label="Descripción",
                     place_holder="Digite la descripción", field="textarea"),
                Form(id="cantidad", label="Cantidad",
                     place_holder="Digite la cantidad", field="textbox", data_type="int"),
                # Form(id="opcion", label="Opción",
                #      place_holder="", field="radiobutton", data_type="bool"),
            ],
            "Cuaderno": [
                Form(id="nombre", label="Nombre",
                     place_holder="Digita el nombre", field="textbox"),
                Form(id="modelo", label="Modelo",
                     place_holder="Digite el modelo", field="textbox"),
                Form(id="marca", label="Marca",
                     place_holder="Digite la marca", field="textbox"),
                Form(id="dimensiones", label="Dimensiones",
                     place_holder="Digite la descripción", field="textbox"),
                Form(id="descripcion", label="Descripción",
                     place_holder="Digite la descripción", field="textarea"),
                Form(id="formato", label="Formato",
                     place_holder="Digite el formato: cuadriculado, rayado ...", field="textarea"),
                Form(id="color", label="Color",
                     place_holder="Digite el color", field="textarea"),
                Form(id="tipo_papel", label="Tipo de papel",
                     place_holder="Digite el color", field="textarea"),
                Form(id="resorte", label="Resorte",
                     place_holder="Tipo de resorte", field="combobox", options=["Solo uno", "doble", "Triple"]),
                Form(id="cantidad", label="Cantidad",
                     place_holder="Digite la cantidad", field="textbox", data_type="int"),
                # Form(id="opcion", label="Opción",
                #      place_holder="", field="radiobutton", data_type="bool"),
            ],

            "Boligrafo": [
                Form(id="nombre", label="Nombre",
                     place_holder="Digita el nombre", field="textbox"),
                Form(id="modelo", label="Modelo",
                     place_holder="Digite el modelo", field="textbox"),
                Form(id="marca", label="Marca",
                     place_holder="Digite la marca", field="textbox"),
                Form(id="dimensiones", label="Dimensiones",
                     place_holder="Digite la descripción", field="textbox"),
                Form(id="descripcion", label="Descripción",
                     place_holder="Digite la descripción", field="textarea"),
                Form(id="formato", label="Formato",
                     place_holder="Digite el formato: cuadriculado, rayado ...", field="textarea"),
                Form(id="color", label="Color",
                     place_holder="Digite el color", field="textarea"),
                Form(id="tipo_papel", label="Tipo de papel",
                     place_holder="Digite el color", field="textarea"),
                Form(id="resorte", label="Resorte",
                     place_holder="Tipo de resorte", field="combobox", options=["Solo uno", "doble", "Triple"]),
                Form(id="cantidad", label="Cantidad",
                     place_holder="Digite la cantidad", field="textbox", data_type="int"),
                # Form(id="opcion", label="Opción",
                #      place_holder="", field="radiobutton", data_type="bool"),
            ],

        }

        self.double_confirmation_inventory = None
        self.setupUi(self)
        self.initComponents()
        self.initSignals()

    def initComponents(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_time)
        self.timer.start(1000)

    def update_time(self):
        self.date_label.setText(getDate())
        self.time_label.setText(getTime())

    def initSignals(self):
        self.acept_button.clicked.connect(
            self.enter_info_in_double_confirmation_inventory)
        self.cancel_button.clicked.connect(self.clean_fields)
        self.template_combobox.currentIndexChanged.connect(self.update_fields)
        self.item_confirmation_button.clicked.connect(
            self.show_double_confirmation_inventory)

     # EVENTS

    def test(self):
        print("----------------------------------")
        for field_id, custom_field in self.text_boxes.items():
            value = custom_field.widget.text() if isinstance(custom_field.widget, QLineEdit) else \
                custom_field.widget.currentText() if isinstance(custom_field.widget, QComboBox) else \
                custom_field.widget.toPlainText() if isinstance(custom_field.widget, QTextEdit) else \
                custom_field.yes_radio.isChecked() if isinstance(custom_field.widget, QWidget) and custom_field.field == "radiobutton" else \
                None

            if custom_field.data_type == "int":
                value = int(value) if value else None
            elif custom_field.data_type == "float":
                value = float(value) if value else None
            elif custom_field.data_type == "bool":
                value = bool(value) if value is not None else None

            print(f"{field_id}: {value}")

    def test2(self):
        for field_id, custom_field in self.text_boxes.items():
            if isinstance(custom_field.widget, QLineEdit):
                custom_field.widget.setText("")
            elif isinstance(custom_field.widget, QTextEdit):
                custom_field.widget.setText("")
            elif isinstance(custom_field.widget, QComboBox):
                custom_field.widget.setCurrentIndex(0)
            elif isinstance(custom_field.widget, QWidget) and custom_field.field == "radiobutton":
                self.radio_group.setExclusive(False)
                custom_field.yes_radio.setChecked(False)
                custom_field.no_radio.setChecked(False)
                self.radio_group.setExclusive(True)

    def show_double_confirmation_inventory(self):
        if self.double_confirmation_inventory is None:
            return
        if self.double_confirmation_inventory.isHidden():
            self.double_confirmation_inventory.show()

    def update_combobox_and_fields(self, table_name, data):
        self.template_combobox.setCurrentText(table_name)

        for field_id, value in data.items():
            if field_id in self.text_boxes:
                widget = self.text_boxes[field_id].widget
                if isinstance(widget, QLineEdit):
                    widget.setText(value)
                    # print(value)
                elif isinstance(widget, QTextEdit):
                    widget.setText(value)
                elif isinstance(widget, QComboBox):
                    index = widget.findText(value)
                    if index != -1:
                        widget.setCurrentIndex(index)
                elif isinstance(widget, QWidget) and self.text_boxes[field_id].field == "radiobutton":
                    # self.radio_group.setExclusive(False)
                    # custom_field.yes_radio.setChecked(False)
                    # custom_field.no_radio.setChecked(False)
                    # self.radio_group.setExclusive(True)
                    # print(value.lower())
                    pass

    def clean_fields(self):
        for field_id, custom_field in self.text_boxes.items():
            if isinstance(custom_field.widget, QLineEdit):
                custom_field.widget.setText("")
            elif isinstance(custom_field.widget, QTextEdit):
                custom_field.widget.setText("")
            elif isinstance(custom_field.widget, QComboBox):
                custom_field.widget.setCurrentIndex(0)
            elif isinstance(custom_field.widget, QWidget) and custom_field.field == "radiobutton":
                self.radio_group.setExclusive(False)
                custom_field.yes_radio.setChecked(False)
                custom_field.no_radio.setChecked(False)
                self.radio_group.setExclusive(True)

    def enter_info_in_double_confirmation_inventory(self):
        data = {}

        for field_id, custom_field in self.text_boxes.items():
            value = custom_field.widget.text() if isinstance(custom_field.widget, QLineEdit) else \
                custom_field.widget.currentText() if isinstance(custom_field.widget, QComboBox) else \
                custom_field.widget.toPlainText() if isinstance(custom_field.widget, QTextEdit) else \
                custom_field.yes_radio.isChecked() if isinstance(custom_field.widget, QWidget) and custom_field.field == "radiobutton" else \
                None

            if custom_field.data_type == "int":
                value = int(value) if value else None
            elif custom_field.data_type == "float":
                value = float(value) if value else None
            elif custom_field.data_type == "bool":
                value = bool(value) if value is not None else None

            data[field_id] = value

        table_name = self.template_combobox.currentText()

        if self.double_confirmation_inventory is None:
            self.double_confirmation_inventory = DoubleConfirmationInventory(
                {table_name: data}, parent=self)
            self.double_confirmation_inventory.row_selected.connect(
                self.update_combobox_and_fields)

            table = self.double_confirmation_inventory.create_table(
                table_name, data)
            self.double_confirmation_inventory.main_content_layout.addWidget(
                table)
            self.double_confirmation_inventory.tables[table_name] = table

        else:
            if table_name not in self.double_confirmation_inventory.tables:
                table = self.double_confirmation_inventory.create_table(
                    table_name, data)
                self.double_confirmation_inventory.main_content_layout.addWidget(
                    table)
                self.double_confirmation_inventory.tables[table_name] = table

            else:
                table_widget = self.double_confirmation_inventory.tables[table_name].layout(
                ).itemAt(1).widget()
                selected_row = table_widget.currentRow()

                if selected_row >= 0:
                    for col, (field_id, value) in enumerate(data.items()):
                        table_widget.setItem(
                            selected_row, col, QTableWidgetItem(str(value)))

                    date_item = QTableWidgetItem(getDate())
                    time_item = QTableWidgetItem(getTime())
                    table_widget.setItem(
                        selected_row, len(data) + 1, date_item)
                    table_widget.setItem(
                        selected_row, len(data) + 2, time_item)
                    table_widget.setCurrentCell(-1, -1)
                else:
                    # Agregar una nueva fila
                    self.double_confirmation_inventory.add_row(
                        table_name, data)

        self.clean_fields()
        self.double_confirmation_inventory.tables[table_name].layout().itemAt(
            1).widget().setCurrentCell(-1, -1)