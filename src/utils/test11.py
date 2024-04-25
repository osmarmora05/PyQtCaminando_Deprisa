from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QLineEdit, QTextEdit, QRadioButton, QLabel, QHBoxLayout, QDialog, QTableWidget, QTableWidgetItem
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui

class InfoWindow(QDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Información")
        
        self.table = QTableWidget()
        self.table.setColumnCount(len(data))
        
        header_labels = list(data.keys())
        self.table.setHorizontalHeaderLabels(header_labels)
        
        self.table.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for column, (key, value) in enumerate(row_data.items()):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row, column, item)
        
        for col, (field_id, value) in enumerate(data.items()):
            self.table.setItem(0, col, QTableWidgetItem(str(value)))
        
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        
        self.button = QPushButton("Seleccionar")
        self.button.clicked.connect(self.select_row)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
    
    def select_row(self):
        selected_row = self.table.currentRow()
        
        if selected_row >= 0:
            data = {}
            for col in range(self.table.columnCount()):
                field_id = self.table.horizontalHeaderItem(col).text()
                value_item = self.table.item(selected_row, col)
                
                if value_item:
                    value = value_item.text()
                    data[field_id] = value
                
            if isinstance(self.parent(), Inventario):
                for field_id, value in data.items():
                    if field_id in self.parent().text_boxes:
                        widget = self.parent().text_boxes[field_id].widget
                        if isinstance(widget, QLineEdit) or isinstance(widget, QTextEdit):
                            widget.setText(value)
                        elif isinstance(widget, QComboBox):
                            index = widget.findText(value)
                            if index != -1:
                                widget.setCurrentIndex(index)
                        elif isinstance(widget, QWidget) and self.parent().text_boxes[field_id].field == "radiobutton":
                            self.parent().radio_group.setExclusive(False)
                            widget.yes_radio.setChecked(value.lower() == "sí")
                            widget.no_radio.setChecked(value.lower() == "no")
                            self.parent().radio_group.setExclusive(True)
            
        self.close()

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

        self.widget = self.create_widget(field_type, place_holder, options)
        layout.addWidget(self.widget)
        
        self.setLayout(layout)
    
    def create_widget(self, field_type, place_holder, options):
        widget = None
        if field_type == "textbox":
            widget = QLineEdit()
        elif field_type == "textarea":
            widget = QTextEdit()
        elif field_type == "combobox":
            widget = QComboBox()
            widget.addItems(options)
        elif field_type == "radiobutton":
            widget = QWidget()
            radio_layout = QVBoxLayout()
            self.yes_radio = QRadioButton("Sí")
            self.no_radio = QRadioButton("No")
            radio_layout.addWidget(self.yes_radio)
            radio_layout.addWidget(self.no_radio)
            widget.setLayout(radio_layout)
        if widget:
            widget.setPlaceholderText(place_holder)
            widget.setStyleSheet("""
                background-color: #09090B;
                border-radius: 8px;
                border: 2px solid #71717A;
                color: #FAFAFA;
                padding: 8px 12px;
            """)
        return widget

class Inventario(QWidget):
    def __init__(self):
        super().__init__()

        self.campos = {
            "generico": [
                Form(id="nombre", label="Nombre",
                     place_holder="Digita el nombre", field="textbox"),
                Form(id="modelo", label="Modelo",
                     place_holder="Digite el modelo", field="textbox"),
                Form(id="marca", label="Marca",
                     place_holder="Digite la marca", field="textbox"),
                Form(id="dimensiones", label="Dimensiones",
                     place_holder="Digite la descripción", field="textbox"),
                Form(id="resorte", label="Resorte",
                     place_holder="Tipo de resorte", field="combobox", options=["Solo uno", "doble", "Triple"]),
            ],
            "cuaderno": [
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
                     place_holder="Digite el tipo de papel", field="textarea")
            ]
        }

        self.layout = QVBoxLayout()
        self.fields_layout = QVBoxLayout()
        self.control_layout = QHBoxLayout()

        self.comboBox = QComboBox()
        self.comboBox.currentIndexChanged.connect(self.update_fields)
        self.control_layout.addWidget(self.comboBox)

        self.button = QPushButton("Seleccionar")
        self.button.clicked.connect(self.on_button_clicked)
        self.control_layout.addWidget(self.button)

        self.fields_layout.addLayout(self.control_layout)

        self.text_boxes = {}
        self.widgets = []

        self.comboBox.addItems(list(self.campos.keys()))

        self.update_fields()

        self.layout.addLayout(self.fields_layout)
        self.setLayout(self.layout)

    def update_fields(self):
        current_selection = self.comboBox.currentText()

        while self.fields_layout.count() > 1:
            widget = self.fields_layout.takeAt(1).widget()
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
            value = None
            if isinstance(custom_field.widget, QLineEdit) or isinstance(custom_field.widget, QTextEdit):
                value = custom_field.widget.text()
            elif isinstance(custom_field.widget, QComboBox):
                value = custom_field.widget.currentText()
            elif isinstance(custom_field.widget, QWidget) and custom_field.field == "radiobutton":
                value = "Sí" if custom_field.yes_radio.isChecked() else "No"
            
            if custom_field.data_type == "int" and value:
                value = int(value)
            elif custom_field.data_type == "float" and value:
                value = float(value)
            elif custom_field.data_type == "bool" and value:
                value = value.lower() == "sí"
            
            data[field_id] = value

        info_window = InfoWindow(data, parent=self)
        for field_id, custom_field in self.text_boxes.items():
            if isinstance(custom_field.widget, QLineEdit) or isinstance(custom_field.widget, QTextEdit):
                custom_field.widget.setText("")
            elif isinstance(custom_field.widget, QComboBox):
                custom_field.widget.setCurrentIndex(0)
            elif isinstance(custom_field.widget, QWidget) and custom_field.field == "radiobutton":
                custom_field.yes_radio.setChecked(False)
                custom_field.no_radio.setChecked(False)
        info_window.exec()

app = QApplication([])
window = Inventario()
window.show()
app.exec()
