from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QComboBox, QPushButton, QLineEdit, QTextEdit, QRadioButton, QLabel, QHBoxLayout, QTableWidget, QTableWidgetItem, QHeaderView, QDialog, QAbstractItemView
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui

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
            self.widget = QWidget()  
            layout.addWidget(self.widget)

            radio_layout = QVBoxLayout()

            self.yes_radio = QRadioButton("Sí")
            self.no_radio = QRadioButton("No")

            radio_layout.addWidget(self.yes_radio)
            radio_layout.addWidget(self.no_radio)

            self.widget.setLayout(radio_layout)

        self.setLayout(layout)

class InfoWindow(QDialog):
    row_selected = pyqtSignal(int)

    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.data = data

        self.table = QTableWidget()
        self.table.setColumnCount(len(data[0]))
        self.table.setHorizontalHeaderLabels(data[0].keys())

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.horizontalHeader().setStretchLastSection(True)
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)

        self.setLayout(self.layout)

        self.table.itemSelectionChanged.connect(self.on_item_selected)

    def setup_table(self):
        self.table.setRowCount(len(self.data))
        for row, row_data in enumerate(self.data):
            for column, (key, value) in enumerate(row_data.items()):
                item = QTableWidgetItem(str(value))
                self.table.setItem(row, column, item)

    def on_item_selected(self):
        selected_row = self.table.currentRow()
        self.row_selected.emit(selected_row)

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

        self.fields_layout = QVBoxLayout()
        self.control_layout = QHBoxLayout()

        self.comboBox = QComboBox()
        self.comboBox.currentIndexChanged.connect(self.update_fields)
        self.control_layout.addWidget(self.comboBox)

        self.button = QPushButton("Hola")
        self.button.clicked.connect(self.on_button_clicked)
        self.control_layout.addWidget(self.button)

        self.fields_layout.addLayout(self.control_layout)

        self.text_boxes = {}

        self.comboBox.addItems(list(self.campos.keys()))


        self.layout.addLayout(self.fields_layout)

        self.setLayout(self.layout)

        self.info_window = InfoWindow(data={}, parent=self)
        self.update_fields()

        self.info_window.row_selected.connect(self.update_fields)

    def update_fields(self, row=None):
        current_selection = self.comboBox.currentText()

        while self.fields_layout.count() > 0:
            widget = self.fields_layout.takeAt(0).widget()
            if widget:
                widget.deleteLater()

        self.text_boxes.clear()

        self.fields_layout.addLayout(self.control_layout)

        if row is None:
            for x in self.campos[current_selection]:
                field = CustomField(label=x.label, place_holder=x.place_holder, options=x.options,
                                    data_type=x.data_type, field_type=x.field, text_boxes=self.text_boxes)
                self.text_boxes[x.id] = field
                self.fields_layout.addWidget(field)
        else:
            data_dict = self.info_window.data[row]
            for x in self.campos[current_selection]:
                field = CustomField(label=x.label, place_holder=x.place_holder, options=x.options,
                                    data_type=x.data_type, field_type=x.field, text_boxes=self.text_boxes)
                value = data_dict.get(x.id, "")
                if isinstance(field.widget, QLineEdit):
                    field.widget.setText(str(value))
                elif isinstance(field.widget, QTextEdit):
                    field.widget.setText(str(value))
                elif isinstance(field.widget, QComboBox):
                    index = field.widget.findText(str(value))
                    if index != -1:
                        field.widget.setCurrentIndex(index)
                elif isinstance(field.widget, QWidget) and field.field == "radiobutton":
                    field.yes_radio.setChecked(value == "Sí")
                    field.no_radio.setChecked(value == "No")
                self.text_boxes[x.id] = field
                self.fields_layout.addWidget(field)

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
            print(f"{field_id}: {value}")

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

        self.info_window.setup_table()
        self.info_window.exec()

app = QApplication([])
window = Inventario()
window.show()
app.exec()
