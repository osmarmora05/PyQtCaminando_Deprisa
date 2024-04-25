import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, 
    QPushButton, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, 
    QLabel, QDialog, QRadioButton
)
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui

class InfoWindow(QDialog):
    row_selected = pyqtSignal(str, dict)
    
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Información")
        self.tables = {}
        self.init_ui(data)
    
    def init_ui(self, data):
        layout = QVBoxLayout()
        self.button = QPushButton("Seleccionar")
        self.button.clicked.connect(self.select_row)
        layout.addWidget(self.button)
        self.setLayout(layout)
    
    def create_table(self, table_name, initial_data):
        table = QTableWidget()
        table.setColumnCount(len(initial_data) + 3)
        header_labels = list(initial_data.keys()) + ["Acciones", "Fecha", "Hora"]
        table.setHorizontalHeaderLabels(header_labels)
        table.setRowCount(1)
        self.populate_table(table, initial_data)
        btn = self.create_remove_button(table_name)
        table.setCellWidget(0, len(initial_data), btn)
        return table

    def populate_table(self, table, data):
        for col, (field_id, value) in enumerate(data.items()):
            table.setItem(0, col, QTableWidgetItem(str(value)))
    
    def create_remove_button(self, table_name):
        btn = QPushButton("Eliminar")
        btn.clicked.connect(self.remove_row)
        btn.table_name = table_name
        return btn

    def select_row(self):
        for table_name, table in self.tables.items():
            selected_row = table.currentRow()
            if selected_row >= 0:
                data = self.get_table_data(table)
                self.row_selected.emit(table_name, data)
        self.hide()

    def get_table_data(self, table):
        return {table.horizontalHeaderItem(col).text(): table.item(table.currentRow(), col).text() 
                for col in range(table.columnCount() - 3)}

    def remove_row(self):
        btn = self.sender()
        table_name = btn.table_name
        index = self.tables[table_name].indexAt(btn.pos())
        if index.isValid():
            self.tables[table_name].removeRow(index.row())
            if self.tables[table_name].rowCount() == 0:
                self.layout().removeWidget(self.tables[table_name])
                self.tables[table_name].deleteLater()
                del self.tables[table_name] 

class Form:
    def __init__(self, id, label, place_holder, field, options=None, data_type="text"):
        self.id = id
        self.label = label
        self.place_holder = place_holder
        self.field = field
        self.options = options
        self.data_type = data_type

class CustomField(QWidget):
    def __init__(self, label, place_holder, options=None, data_type="text", field_type="textbox", text_boxes=None):
        super().__init__()
        self.text_boxes = text_boxes
        self.data_type = data_type  
        self.field = field_type  
        self.init_ui(label, place_holder, options)

    def init_ui(self, label, place_holder, options):
        layout = QVBoxLayout()
        label_widget = QLabel(label)
        self.set_label_style(label_widget)
        layout.addWidget(label_widget)
        self.widget = self.create_field_widget(place_holder, options)
        layout.addWidget(self.widget)
        self.setLayout(layout)

    def set_label_style(self, label_widget):
        label_widget.setStyleSheet("color: red; font-size: 18")
        font = QtGui.QFont()
        font.setPointSize(14)
        label_widget.setFont(font)

    def create_field_widget(self, place_holder, options):
        if self.field == "textbox":
            widget = QLineEdit()
        elif self.field == "textarea":
            widget = QTextEdit()
        elif self.field == "combobox":
            widget = QComboBox()
            widget.addItems(options)
        elif self.field == "radiobutton":
            widget = self.create_radio_button()
        widget.setPlaceholderText(place_holder)
        self.set_field_style(widget)
        return widget

    def create_radio_button(self):
        widget = QWidget()  
        radio_layout = QVBoxLayout()
        self.yes_radio = QRadioButton("Sí")
        self.no_radio = QRadioButton("No")
        radio_layout.addWidget(self.yes_radio)
        radio_layout.addWidget(self.no_radio)
        widget.setLayout(radio_layout)
        return widget

    def set_field_style(self, widget):
        widget.setStyleSheet(
            """
            background-color: #09090B;
            border-radius: 8px;
            border: 2px solid #71717A;
            color: #FAFAFA;
            padding: 8px 12px;
            """
        )

class Inventario(QWidget):
    def __init__(self):
        super().__init__()
        self.campos = {
            "generico": [
                Form(id="nombre", label="Nombre", place_holder="Digita el nombre", field="textbox"),
                Form(id="modelo", label="Modelo", place_holder="Digite el modelo", field="textbox"),
                Form(id="marca", label="Marca", place_holder="Digite la marca", field="textbox"),
                Form(id="dimensiones", label="Dimensiones", place_holder="Digite la descripción", field="textbox"),
                Form(id="resorte", label="Resorte", place_holder="Tipo de resorte", field="combobox", options=["Solo uno", "doble", "Triple"]),
            ],
            "cuaderno": [
                Form(id="nombre", label="Nombre", place_holder="Digita el nombre", field="textbox"),
                Form(id="modelo", label="Modelo", place_holder="Digite el modelo", field="textbox"),
                Form(id="marca", label="Marca", place_holder="Digite la marca", field="textbox"),
                Form(id="dimensiones", label="Dimensiones", place_holder="Digite la descripción", field="textbox"),
                Form(id="descripcion", label="Descripción", place_holder="Digite la descripción", field="textarea"),
                Form(id="formato", label="Formato", place_holder="Digite el formato: cuadriculado, rayado ...", field="textarea"),
                Form(id="color", label="Color", place_holder="Digite el color", field="textarea"),
                Form(id="tipo_papel", label="Tipo de papel", place_holder="Digite el tipo de papel", field="textarea")
            ]
        }
        self.init_ui()

    def init_ui(self):
        self.layout = QVBoxLayout()
        self.fields_layout = QVBoxLayout()
        self.control_layout = QHBoxLayout()
        self.comboBox = QComboBox()
        self.comboBox.currentIndexChanged.connect(self.update_fields)
        self.control_layout.addWidget(self.comboBox)
        self.button = QPushButton("Agregar")
        self.button.clicked.connect(self.on_button_clicked)
        self.control_layout.addWidget(self.button)
        self.fields_layout.addLayout(self.control_layout)
        self.text_boxes = {}
        self.widgets = []
        self.info_window = None  
        self.comboBox.addItems(list(self.campos.keys()))
        self.update_fields()
        self.layout.addLayout(self.fields_layout)
        self.setLayout(self.layout)

    def update_fields(self):
        current_selection = self.comboBox.currentText()
        self.clear_layout(self.fields_layout)
        self.text_boxes.clear()
        self.fields_layout.addLayout(self.control_layout)
        for x in self.campos[current_selection]:
            field = CustomField(label=x.label, place_holder=x.place_holder, options=x.options,
                                data_type=x.data_type, field_type=x.field, text_boxes=self.text_boxes)
            self.text_boxes[x.id] = field
            self.fields_layout.addWidget(field)
            self.widgets.append(field)

    def clear_layout(self, layout):
        while layout.count() > 0:
            widget = layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

    def on_button_clicked(self):
        data = self.get_form_data()
        table_name = self.comboBox.currentText()
        self.update_info_window(data, table_name)
        self.clear_form_data()

    def get_form_data(self):
        return {field_id: self.get_field_value(custom_field) for field_id, custom_field in self.text_boxes.items()}

    def get_field_value(self, custom_field):
        if isinstance(custom_field.widget, QLineEdit):
            return custom_field.widget.text()
        elif isinstance(custom_field.widget, QTextEdit):
            return custom_field.widget.toPlainText()
        elif isinstance(custom_field.widget, QComboBox):
            return custom_field.widget.currentText()
        elif custom_field.field == "radiobutton":
            return "Sí" if custom_field.yes_radio.isChecked() else "No"

    def update_info_window(self, data, table_name):
        if self.info_window is None:
            self.create_new_info_window(data, table_name)
        else:
            self.update_existing_info_window(data, table_name)

    def create_new_info_window(self, data, table_name):
        self.info_window = InfoWindow({table_name: data}, parent=self)
        self.info_window.row_selected.connect(self.update_combobox_and_fields)
        table = self.info_window.create_table(table_name, data)
        self.info_window.layout().addWidget(table)
        self.info_window.tables[table_name] = table

    def update_existing_info_window(self, data, table_name):
        if table_name not in self.info_window.tables:
            table = self.info_window.create_table(table_name, data)
            self.info_window.layout().addWidget(table)
            self.info_window.tables[table_name] = table
        else:
            self.update_table_data(data, table_name)

    def update_table_data(self, data, table_name):
        selected_row = self.info_window.tables[table_name].currentRow()
        if selected_row >= 0:
            for col, (field_id, value) in enumerate(data.items()):
                self.info_window.tables[table_name].setItem(selected_row, col, QTableWidgetItem(str(value)))
            self.update_timestamp(selected_row, table_name)
            self.info_window.tables[table_name].setCurrentCell(-1, -1)
        else:
            self.add_new_row(data, table_name)

    def update_timestamp(self, row, table_name):
        current_date = QTableWidgetItem(datetime.datetime.now().strftime("%Y-%m-%d"))
        current_time = QTableWidgetItem(datetime.datetime.now().strftime("%H:%M:%S"))
        self.info_window.tables[table_name].setItem(row, len(self.text_boxes) + 1, current_date)
        self.info_window.tables[table_name].setItem(row, len(self.text_boxes) + 2, current_time)

    def add_new_row(self, data, table_name):
        self.info_window.tables[table_name].setRowCount(self.info_window.tables[table_name].rowCount() + 1)
        for col, (field_id, value) in enumerate(data.items()):
            self.info_window.tables[table_name].setItem(self.info_window.tables[table_name].rowCount() - 1, col, QTableWidgetItem(str(value)))
        btn = QPushButton("Eliminar")
        btn.clicked.connect(self.info_window.remove_row)
        btn.table_name = table_name
        self.info_window.tables[table_name].setCellWidget(self.info_window.tables[table_name].rowCount() - 1, len(self.text_boxes), btn)
        self.update_timestamp(self.info_window.tables[table_name].rowCount() - 1, table_name)

    def clear_form_data(self):
        for custom_field in self.text_boxes.values():
            if isinstance(custom_field.widget, QLineEdit) or isinstance(custom_field.widget, QTextEdit):
                custom_field.widget.clear()
            elif isinstance(custom_field.widget, QComboBox):
                custom_field.widget.setCurrentIndex(0)
            elif custom_field.field == "radiobutton":
                custom_field.yes_radio.setChecked(False)
                custom_field.no_radio.setChecked(False)
        
        self.info_window.show()

    def update_combobox_and_fields(self, table_name, data):
        self.comboBox.setCurrentText(table_name)
        for field_id, value in data.items():
            if field_id in self.text_boxes:
                widget = self.text_boxes[field_id].widget
                if isinstance(widget, QLineEdit) or isinstance(widget, QTextEdit):
                    widget.setText(value)
                elif isinstance(widget, QComboBox):
                    index = widget.findText(value)
                    if index != -1:
                        widget.setCurrentIndex(index)
                elif isinstance(widget, QWidget) and self.text_boxes[field_id].field == "radiobutton":
                    if value.lower() == "sí":
                        widget.yes_radio.setChecked(True)
                        widget.no_radio.setChecked(False)
                    elif value.lower() == "no":
                        widget.yes_radio.setChecked(False)
                        widget.no_radio.setChecked(True)

app = QApplication([])
window = Inventario()
window.show()
app.exec()
