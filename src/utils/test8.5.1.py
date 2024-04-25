import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QLabel, QWidget, QVBoxLayout, QRadioButton, QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui

# Edita correctamente las filas

class InfoWindow(QDialog):
    row_selected = pyqtSignal(str, dict)
    
    def __init__(self, data, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Información")
        
        self.tables = {}
        layout = QVBoxLayout()

        # for table_name, table_data in data.items():
        #     table = self.create_table(table_name, table_data)
        #     layout.addWidget(table)
        #     self.tables[table_name] = table  

        self.button = QPushButton("Seleccionar")
        self.button.clicked.connect(self.select_row)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
    
    def create_table(self, table_name, initial_data):
        table = QTableWidget()
        table.setColumnCount(len(initial_data) + 3)  # +3 for the "Acciones", "Fecha", and "Hora" columns
        header_labels = list(initial_data.keys()) + ["Acciones", "Fecha", "Hora"]
        table.setHorizontalHeaderLabels(header_labels)
        table.setRowCount(1)
        
        for col, (field_id, value) in enumerate(initial_data.items()):
            table.setItem(0, col, QTableWidgetItem(str(value)))
        
        # Add button to the "Acciones" column
        btn = QPushButton("Eliminar")
        btn.clicked.connect(self.remove_row)
        btn.table_name = table_name  # Establecer un atributo personalizado para el botón
        table.setCellWidget(0, len(initial_data), btn)
        
        return table
    
    def select_row(self):
        for table_name, table in self.tables.items():
            selected_row = table.currentRow()
            
            if selected_row >= 0:
                data = {}
                for col in range(table.columnCount() - 3):  # -3 to exclude "Acciones", "Fecha", and "Hora" columns
                    field_id = table.horizontalHeaderItem(col).text()
                    value_item = table.item(selected_row, col)
                    
                    if value_item:
                        value = value_item.text()
                        data[field_id] = value
                
                self.row_selected.emit(table_name, data)
                
        self.hide()
    

    def remove_row(self):
        btn = self.sender()  # Get the button that was clicked
        table_name = btn.table_name  # Get the table name from the button's custom attribute
        index = self.tables[table_name].indexAt(btn.pos())  # Get the index of the button
        if index.isValid():
            self.tables[table_name].removeRow(index.row())
            # Check if the table is empty
            if self.tables[table_name].rowCount() == 0:
                self.layout().removeWidget(self.tables[table_name])  # Remove the table widget from the layout
                self.tables[table_name].deleteLater()  # Delete the table widget
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

        layout = QVBoxLayout()
        label_widget = QLabel(label)
        label_widget.setStyleSheet("color: red; font-size: 18")

        font = QtGui.QFont()
        font.setPointSize(14)
        label_widget.setFont(font)

        layout.addWidget(label_widget)

        if field_type == "textbox":
            self.widget = QLineEdit()
        elif field_type == "textarea":
            self.widget = QTextEdit()
        elif field_type == "combobox":
            self.widget = QComboBox()
            self.widget.addItems(options)
        elif field_type == "radiobutton":
            self.widget = QWidget()  
            radio_layout = QVBoxLayout()
            self.yes_radio = QRadioButton("Sí")
            self.no_radio = QRadioButton("No")
            radio_layout.addWidget(self.yes_radio)
            radio_layout.addWidget(self.no_radio)
            self.widget.setLayout(radio_layout)

        self.widget.setPlaceholderText(place_holder)
        self.widget.setStyleSheet(
            """
            background-color: #09090B;
            border-radius: 8px;
            border: 2px solid #71717A;
            color: #FAFAFA;
            padding: 8px 12px;
            """
        )
        layout.addWidget(self.widget)
        self.setLayout(layout)


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

        while self.fields_layout.count() > 0:
            widget = self.fields_layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        self.text_boxes.clear()

        self.fields_layout.addLayout(self.control_layout)

        for x in self.campos[current_selection]:
            field = CustomField(label=x.label, place_holder=x.place_holder, options=x.options,
                                data_type=x.data_type, field_type=x.field, text_boxes=self.text_boxes)
            self.text_boxes[x.id] = field
            self.fields_layout.addWidget(field)
            self.widgets.append(field)

    def on_button_clicked(self):
        data = {}
        
        for field_id, custom_field in self.text_boxes.items():
            value = custom_field.widget.text() if isinstance(custom_field.widget, QLineEdit) else \
                custom_field.widget.currentText() if isinstance(custom_field.widget, QComboBox) else \
                custom_field.widget.toPlainText() if isinstance(custom_field.widget, QTextEdit) else \
                "Sí" if custom_field.yes_radio.isChecked() else "No" if custom_field.no_radio.isChecked() else None

            if custom_field.data_type == "int":
                value = int(value) if value else None
            elif custom_field.data_type == "float":
                value = float(value) if value else None
            elif custom_field.data_type == "bool":
                value = bool(value) if value is not None else None

            data[field_id] = value

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
                selected_row = self.info_window.tables[table_name].currentRow()
                
                if selected_row >= 0:
                    print("estamos aqui sobreescribiendo")
                    for col, (field_id, value) in enumerate(data.items()):
                        self.info_window.tables[table_name].setItem(selected_row, col, QTableWidgetItem(str(value)))
                        
                    # Update the timestamp for the selected row
                    current_date = QTableWidgetItem(datetime.datetime.now().strftime("%Y-%m-%d"))
                    current_time = QTableWidgetItem(datetime.datetime.now().strftime("%H:%M:%S"))
                    self.info_window.tables[table_name].setItem(selected_row, len(data) + 1, current_date)
                    self.info_window.tables[table_name].setItem(selected_row, len(data) + 2, current_time)
                    
                    # Reset selected_row to -1
                    self.info_window.tables[table_name].setCurrentCell(-1, -1)
                    
                else:
                    self.info_window.tables[table_name].setRowCount(self.info_window.tables[table_name].rowCount() + 1)
                    
                    for col, (field_id, value) in enumerate(data.items()):
                        self.info_window.tables[table_name].setItem(self.info_window.tables[table_name].rowCount() - 1, col, QTableWidgetItem(str(value)))
                        
                    # Add the new row to the table
                    btn = QPushButton("Eliminar")
                    btn.clicked.connect(self.info_window.remove_row)
                    btn.table_name = table_name  # Store the table name in the button
                    self.info_window.tables[table_name].setCellWidget(self.info_window.tables[table_name].rowCount() - 1, len(data), btn)  # Add button to the "Acciones" column
                    
                    # Update the timestamp for the new row
                    current_date = QTableWidgetItem(datetime.datetime.now().strftime("%Y-%m-%d"))
                    current_time = QTableWidgetItem(datetime.datetime.now().strftime("%H:%M:%S"))
                    self.info_window.tables[table_name].setItem(self.info_window.tables[table_name].rowCount() - 1, len(data) + 1, current_date)
                    self.info_window.tables[table_name].setItem(self.info_window.tables[table_name].rowCount() - 1, len(data) + 2, current_time)

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

app = QApplication([])
window = Inventario()
window.show()
app.exec()
