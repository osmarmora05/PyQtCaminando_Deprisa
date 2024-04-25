import datetime
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton,
    QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QLabel, QRadioButton
)
from PyQt5.QtCore import pyqtSignal

class InfoWindow(QWidget):
    row_selected = pyqtSignal(str, dict)
    
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Información")
        self.tables = {}
        layout = QVBoxLayout()

        for table_name, table_data in data.items():
            table = self.create_table(table_name, table_data)
            layout.addWidget(table)
            self.tables[table_name] = table

        self.button = QPushButton("Seleccionar")
        self.button.clicked.connect(self.select_row)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
    
    def create_table(self, table_name, initial_data):
        table = QTableWidget()
        table.setColumnCount(len(initial_data) + 3)
        header_labels = list(initial_data.keys()) + ["Acciones", "Fecha", "Hora"]
        table.setHorizontalHeaderLabels(header_labels)
        self.add_table_row(table, initial_data)
        return table
    
    def add_table_row(self, table, data):
        row_position = table.rowCount()
        table.setRowCount(row_position + 1)
        
        for col, (field_id, value) in enumerate(data.items()):
            table.setItem(row_position, col, QTableWidgetItem(str(value)))
        
        btn = QPushButton("Eliminar")
        btn.clicked.connect(self.remove_row)
        btn.table_name = table.objectName()
        table.setCellWidget(row_position, len(data), btn)
        
    def select_row(self):
        for table_name, table in self.tables.items():
            selected_row = table.currentRow()
            if selected_row >= 0:
                data = {}
                for col in range(table.columnCount() - 3):
                    field_id = table.horizontalHeaderItem(col).text()
                    value_item = table.item(selected_row, col)
                    if value_item:
                        data[field_id] = value_item.text()
                self.row_selected.emit(table_name, data)
        self.hide()
    
    def remove_row(self):
        btn = self.sender()
        table_name = btn.table_name
        index = self.tables[table_name].indexAt(btn.pos())
        if index.isValid():
            self.tables[table_name].removeRow(index.row())


class CustomField(QWidget):
    def __init__(self, label, place_holder, options=None, data_type="text", field_type="textbox"):
        super().__init__()
        self.data_type = data_type  
        self.field = field_type  
        self.widget = self.create_widget(field_type, options)
        
        layout = QVBoxLayout()
        label_widget = QLabel(label)
        label_widget.setStyleSheet("color: red; font-size: 18")
        layout.addWidget(label_widget)
        layout.addWidget(self.widget)
        self.setLayout(layout)
        self.widget.setPlaceholderText(place_holder)
        self.set_styles()

    def create_widget(self, field_type, options):
        if field_type == "textbox":
            return QLineEdit()
        elif field_type == "textarea":
            return QTextEdit()
        elif field_type == "combobox":
            widget = QComboBox()
            if options:
                widget.addItems(options)
            return widget
        elif field_type == "radiobutton":
            widget = QWidget()
            radio_layout = QVBoxLayout()
            self.yes_radio = QRadioButton("Sí")
            self.no_radio = QRadioButton("No")
            radio_layout.addWidget(self.yes_radio)
            radio_layout.addWidget(self.no_radio)
            widget.setLayout(radio_layout)
            return widget

    def set_styles(self):
        self.widget.setStyleSheet(
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
                Form("nombre", "Nombre", "Digita el nombre", "textbox"),
                Form("modelo", "Modelo", "Digite el modelo", "textbox"),
                Form("marca", "Marca", "Digite la marca", "textbox"),
                Form("dimensiones", "Dimensiones", "Digite la descripción", "textbox"),
                Form("resorte", "Resorte", "Tipo de resorte", "combobox", ["Solo uno", "doble", "Triple"]),
            ],
            "cuaderno": [
                Form("nombre", "Nombre", "Digita el nombre", "textbox"),
                Form("modelo", "Modelo", "Digite el modelo", "textbox"),
                Form("marca", "Marca", "Digite la marca", "textbox"),
                Form("dimensiones", "Dimensiones", "Digite la descripción", "textbox"),
                Form("descripcion", "Descripción", "Digite la descripción", "textarea"),
                Form("formato", "Formato", "Digite el formato: cuadriculado, rayado ...", "textarea"),
                Form("color", "Color", "Digite el color", "textarea"),
                Form("tipo_papel", "Tipo de papel", "Digite el tipo de papel", "textarea")
            ]
        }

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
        
        for x in self.campos[current_selection]:
            field = CustomField(x.label, x.place_holder, x.options, data_type=x.data_type, field_type=x.field)
            self.text_boxes[x.id] = field
            self.fields_layout.addWidget(field)
            self.widgets.append(field)

    def clear_layout(self, layout):
        while layout.count():
            child = layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

    def on_button_clicked(self):
        data = {}
        for field_id, custom_field in self.text_boxes.items():
            data[field_id] = self.get_widget_value(custom_field)

        table_name = self.comboBox.currentText()
        if self.info_window is None:
            self.info_window = InfoWindow({table_name: data}, parent=self)
            self.info_window.row_selected.connect(self.update_combobox_and_fields)
            
            table = self.info_window.create_table(table_name, data)
            self.info_window.layout().addWidget(table)
            self.info_window.tables[table_name] = table
        else:
            if table_name not in self.info_window.tables:
                table = self.info_window.create_table(table_name, data)
                self.info_window.layout().addWidget(table)
                self.info_window.tables[table_name] = table
            else:
                self.info_window.add_table_row(self.info_window.tables[table_name], data)

        for field_id, custom_field in self.text_boxes.items():
            if isinstance(custom_field.widget, QLineEdit):
                custom_field.widget.setText("")
            elif isinstance(custom_field.widget, QTextEdit):
                custom_field.widget.setText("")
            elif isinstance(custom_field.widget, QComboBox):
                custom_field.widget.setCurrentIndex(0)
            elif isinstance(custom_field.widget, QWidget) and custom_field.field == "radiobutton":
                custom_field.yes_radio.setChecked(False)
                custom_field.no_radio.setChecked(False)
        
        self.info_window.show()

    def get_widget_value(self, custom_field):
        widget = custom_field.widget
        if isinstance(widget, QLineEdit):
            return widget.text()
        elif isinstance(widget, QTextEdit):
            return widget.toPlainText()
        elif isinstance(widget, QComboBox):
            return widget.currentText()
        elif isinstance(widget, QWidget) and custom_field.field == "radiobutton":
            return "Sí" if custom_field.yes_radio.isChecked() else "No"

    def update_combobox_and_fields(self, table_name, data):
        self.comboBox.setCurrentText(table_name)
        
        for field_id, value in data.items():
            if field_id in self.text_boxes:
                widget = self.text_boxes[field_id].widget
                if isinstance(widget, QLineEdit):
                    widget.setText(value)
                elif isinstance(widget, QTextEdit):
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


class Form:
    def __init__(self, id, label, place_holder, field, options=None, data_type="text"):
        self.id = id
        self.label = label
        self.place_holder = place_holder
        self.field = field
        self.options = options
        self.data_type = data_type


app = QApplication([])
window = Inventario()
window.show()
app.exec()
