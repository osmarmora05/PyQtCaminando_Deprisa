from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QLineEdit, QTextEdit, QRadioButton, QLabel, QHBoxLayout, QDialog, QTableWidgetItem, QTableWidget, QButtonGroup
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui

class InfoWindow(QDialog):
    def __init__(self, data, campos, parent=None):
        super().__init__(parent)
        
        self.tables = {}  # Diccionario para almacenar las tablas de cada campo
        
        layout = QVBoxLayout()
        
        max_rows = max(len(values) for values in data.values())
        
        for field_id in campos.keys():
            table = QTableWidget()
            table.setColumnCount(1)  # Una sola columna
            table.setHorizontalHeaderLabels([field_id])  # Usar el field_id como encabezado
            
            values = data.get(field_id, [])
            
            table.setRowCount(max_rows)
            
            for row, value in enumerate(values):
                table.setItem(row, 0, QTableWidgetItem(str(value)))
            
            table.itemClicked.connect(self.select_row)
            
            self.tables[field_id] = table  # Añadir la tabla al diccionario
            
            layout.addWidget(table)
        
        self.setLayout(layout)

    
    def select_row(self, item):
        table = item.tableWidget()  # Obtener la tabla a partir del QTableWidgetItem
        
        if table is None:
            return

        selected_row = item.row()
        field_id = table.horizontalHeaderItem(0).text()  # Obtener el field_id del encabezado de la tabla
        value = item.text()
        
        # Llenar el formulario principal con los datos seleccionados
        if isinstance(self.parent(), Inventario):
            if field_id in self.parent().text_boxes:
                widget = self.parent().text_boxes[field_id].widget
                if isinstance(widget, QLineEdit):
                    widget.setText(value)
                elif isinstance(widget, QTextEdit):
                    widget.setText(value)
                elif isinstance(widget, QComboBox):
                    index = widget.findText(value)
                    if index != -1:
                        widget.setCurrentIndex(index)
                elif isinstance(widget, QWidget) and self.parent().text_boxes[field_id].field == "radiobutton":
                    self.parent().radio_group.setExclusive(False)
                    if value.lower() == "sí":
                        widget.yes_radio.setChecked(True)
                        widget.no_radio.setChecked(False)
                    elif value.lower() == "no":
                        widget.yes_radio.setChecked(False)
                        widget.no_radio.setChecked(True)
                    self.parent().radio_group.setExclusive(True)


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
        self.data_type = data_type  # Definir el atributo data_type para todos los campos
        self.field = field_type  # Definir el atributo field para todos los campos

        layout = QVBoxLayout()
        label_widget = QLabel(label)
        label_widget.setStyleSheet("color: red; font-size: 18")

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
                    border: 2px solid #71717A;
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
                    border: 2px solid #71717A;
                    color: #FAFAFA;
                    padding-top: 8px;
                    padding-bottom: 8px;
                    padding-right: 12px;
                    padding-left: 12px;
                }
                """
            )
            layout.addWidget(self.widget)

        elif field_type == "combobox":
            self.widget = QComboBox()
            self.widget.setStyleSheet(
                """
                QComboBox{
                    background-color: #09090B;
                    border-radius: 8px;
                    border: 2px solid #71717A;
                    color: #FAFAFA;
                    padding-top: 8px;
                    padding-bottom: 8px;
                    padding-right: 12px;
                    padding-left: 12px;
                }
                """
            )
            self.widget.addItems(options)
            layout.addWidget(self.widget)

        elif field_type == "radiobutton":
            self.widget = QWidget()  # Widget contenedor para los botones de radio
            layout.addWidget(self.widget)

            radio_layout = QVBoxLayout()

            self.yes_radio = QRadioButton("Sí")
            self.no_radio = QRadioButton("No")

            radio_layout.addWidget(self.yes_radio)
            radio_layout.addWidget(self.no_radio)

            self.widget.setLayout(radio_layout)

        self.setLayout(layout)


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
                     place_holder="Digite el color", field="textarea")
            ]
        }

        self.layout = QVBoxLayout()

        # Crear un QVBoxLayout para los campos
        self.fields_layout = QVBoxLayout()

        # Crear un QHBoxLayout para el QComboBox y el botón
        self.control_layout = QHBoxLayout()

        self.comboBox = QComboBox()
        self.comboBox.currentIndexChanged.connect(self.update_fields)
        self.control_layout.addWidget(self.comboBox)

        self.button = QPushButton("Hola")
        self.button.clicked.connect(self.on_button_clicked)
        self.control_layout.addWidget(self.button)

        # Agregar el control_layout al fields_layout
        self.fields_layout.addLayout(self.control_layout)

        self.text_boxes = {}
        self.widgets = []

        self.comboBox.addItems(list(self.campos.keys()))

        self.update_fields()

        # Agregar fields_layout al layout principal
        self.layout.addLayout(self.fields_layout)

        self.setLayout(self.layout)

    def update_fields(self):
        current_selection = self.comboBox.currentText()

        # Limpiar el fields_layout
        while self.fields_layout.count() > 0:
            widget = self.fields_layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        # Limpiar el diccionario de text_boxes
        self.text_boxes.clear()

        # Agregar el QComboBox y el botón al inicio del fields_layout
        self.fields_layout.addLayout(self.control_layout)

        # Añadir los nuevos campos según la selección
        for x in self.campos[current_selection]:
            field = CustomField(label=x.label, place_holder=x.place_holder, options=x.options,
                                data_type=x.data_type, field_type=x.field, text_boxes=self.text_boxes)
            self.text_boxes[x.id] = field
            self.fields_layout.addWidget(field)
            self.widgets.append(field)

    def on_button_clicked(self):
        data = {}
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

            data[field_id] = value
            print(f"{field_id}: {value} {data}")

        info_window = InfoWindow(data, self.campos, self)
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
        info_window.exec_()


app = QApplication([])
window = Inventario()
window.show()
app.exec()