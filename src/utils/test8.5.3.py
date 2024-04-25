# import datetime
# from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QLabel, QWidget, QVBoxLayout, QRadioButton, QDialog
# from PyQt5.QtCore import pyqtSignal
# from PyQt5 import QtGui


# class InfoWindow(QDialog):
#     row_selected = pyqtSignal(str, dict)

#     def __init__(self, data, parent=None):
#         super().__init__(parent)

#         self.setWindowTitle("Información")

#         self.tables = {}
#         layout = QVBoxLayout()

#         self.setLayout(layout)

#     def create_table(self, table_name, initial_data):
#         table = QTableWidget()
#         table.setColumnCount(len(initial_data) + 3)
#         header_labels = list(initial_data.keys()) + \
#             ["Acciones", "Fecha", "Hora"]
#         table.setHorizontalHeaderLabels(header_labels)
#         table.setRowCount(1)

#         for col, (field_id, value) in enumerate(initial_data.items()):
#             table.setItem(0, col, QTableWidgetItem(str(value)))

#         # Add button to the "Acciones" column for editing row
#         btn_edit = QPushButton("Editar")
#         btn_edit.clicked.connect(self.edit_row)
#         btn_edit.table_name = table_name
#         table.setCellWidget(0, len(initial_data), btn_edit)

#         # Add button to the "Acciones" column for removing row
#         btn_remove = QPushButton("Eliminar")
#         btn_remove.clicked.connect(self.remove_row)
#         btn_remove.table_name = table_name
#         table.setCellWidget(0, len(initial_data) + 1, btn_remove)

#         return table

#     def edit_row(self):
#         btn = self.sender()
#         table_name = btn.table_name
#         table = self.tables[table_name]
#         selected_row = table.indexAt(btn.pos()).row()
            
#         if selected_row >= 0:
#             data = {}
#             for col in range(table.columnCount() - 3):  
#                 field_id = table.horizontalHeaderItem(col).text()
#                 value_item = table.item(selected_row, col)
                
#                 if value_item:
#                     value = value_item.text()
#                     data[field_id] = value
            
#             self.row_selected.emit(table_name, data)
            
#             self.hide()

#     def remove_row(self):
#         btn = self.sender()
#         table_name = btn.table_name
#         index = self.tables[table_name].indexAt(btn.pos())
#         if index.isValid():
#             self.tables[table_name].removeRow(index.row())
#             if self.tables[table_name].rowCount() == 0:
#                 self.layout().removeWidget(self.tables[table_name])
#                 self.tables[table_name].deleteLater()
#                 del self.tables[table_name]


# class Form:
#     def __init__(self, id, label, place_holder, field, options=None, data_type="text"):
#         self.id = id
#         self.label = label
#         self.place_holder = place_holder
#         self.field = field
#         self.options = options
#         self.data_type = data_type


# class CustomField(QWidget):
#     def __init__(self, label, place_holder, options=None, data_type="text", field_type="textbox", text_boxes=None):
#         super().__init__()

#         self.text_boxes = text_boxes
#         self.data_type = data_type
#         self.field = field_type

#         layout = QVBoxLayout()
#         label_widget = QLabel(label)
#         label_widget.setStyleSheet("color: red; font-size: 18")

#         font = QtGui.QFont()
#         font.setPointSize(14)
#         label_widget.setFont(font)

#         layout.addWidget(label_widget)

#         if field_type == "textbox":
#             self.widget = QLineEdit()
#         elif field_type == "textarea":
#             self.widget = QTextEdit()
#         elif field_type == "combobox":
#             self.widget = QComboBox()
#             self.widget.addItems(options)
#         elif field_type == "radiobutton":
#             self.widget = QWidget()
#             radio_layout = QVBoxLayout()
#             self.yes_radio = QRadioButton("Sí")
#             self.no_radio = QRadioButton("No")
#             radio_layout.addWidget(self.yes_radio)
#             radio_layout.addWidget(self.no_radio)
#             self.widget.setLayout(radio_layout)

#         self.widget.setPlaceholderText(place_holder)
#         self.widget.setStyleSheet(
#             """
#             background-color: #09090B;
#             border-radius: 8px;
#             border: 2px solid #71717A;
#             color: #FAFAFA;
#             padding: 8px 12px;
#             """
#         )
#         layout.addWidget(self.widget)
#         self.setLayout(layout)


# class Inventario(QWidget):
#     def __init__(self):
#         super().__init__()

#         self.campos = {
#             "generico": [
#                 Form(id="nombre", label="Nombre",
#                      place_holder="Digita el nombre", field="textbox"),
#                 Form(id="modelo", label="Modelo",
#                      place_holder="Digite el modelo", field="textbox"),
#                 Form(id="marca", label="Marca",
#                      place_holder="Digite la marca", field="textbox"),
#                 Form(id="dimensiones", label="Dimensiones",
#                      place_holder="Digite la descripción", field="textbox"),
#                 Form(id="resorte", label="Resorte", place_holder="Tipo de resorte",
#                      field="combobox", options=["Solo uno", "doble", "Triple"]),
#             ],
#             "cuaderno": [
#                 Form(id="nombre", label="Nombre",
#                      place_holder="Digita el nombre", field="textbox"),
#                 Form(id="modelo", label="Modelo",
#                      place_holder="Digite el modelo", field="textbox"),
#                 Form(id="marca", label="Marca",
#                      place_holder="Digite la marca", field="textbox"),
#                 Form(id="dimensiones", label="Dimensiones",
#                      place_holder="Digite la descripción", field="textbox"),
#                 Form(id="descripcion", label="Descripción",
#                      place_holder="Digite la descripción", field="textarea"),
#                 Form(id="formato", label="Formato",
#                      place_holder="Digite el formato: cuadriculado, rayado ...", field="textarea"),
#                 Form(id="color", label="Color",
#                      place_holder="Digite el color", field="textarea"),
#                 Form(id="tipo_papel", label="Tipo de papel",
#                      place_holder="Digite el tipo de papel", field="textarea")
#             ]
#         }

#         self.layout = QVBoxLayout()
#         self.fields_layout = QVBoxLayout()
#         self.control_layout = QHBoxLayout()
#         self.comboBox = QComboBox()
#         self.comboBox.currentIndexChanged.connect(self.update_fields)
#         self.control_layout.addWidget(self.comboBox)
#         self.button = QPushButton("Agregar")
#         self.button.clicked.connect(self.on_button_clicked)
#         self.control_layout.addWidget(self.button)
#         self.fields_layout.addLayout(self.control_layout)
#         self.text_boxes = {}
#         self.widgets = []
#         self.info_window = None

#         self.comboBox.addItems(list(self.campos.keys()))

#         self.update_fields()

#         self.layout.addLayout(self.fields_layout)

#         self.setLayout(self.layout)

#     def update_fields(self):
#         current_selection = self.comboBox.currentText()

#         while self.fields_layout.count() > 0:
#             widget = self.fields_layout.takeAt(0).widget()
#             if widget:
#                 widget.deleteLater()

#         self.text_boxes.clear()

#         self.fields_layout.addLayout(self.control_layout)

#         for x in self.campos[current_selection]:
#             field = CustomField(label=x.label, place_holder=x.place_holder, options=x.options,
#                                 data_type=x.data_type, field_type=x.field, text_boxes=self.text_boxes)
#             self.text_boxes[x.id] = field
#             self.fields_layout.addWidget(field)
#             self.widgets.append(field)

#     def on_button_clicked(self):
#         data = {}
        
#         for field_id, custom_field in self.text_boxes.items():
#             value = custom_field.widget.text() if isinstance(custom_field.widget, QLineEdit) else \
#                 custom_field.widget.currentText() if isinstance(custom_field.widget, QComboBox) else \
#                 custom_field.widget.toPlainText() if isinstance(custom_field.widget, QTextEdit) else \
#                 "Sí" if custom_field.yes_radio.isChecked() else "No" if custom_field.no_radio.isChecked() else None

#             if custom_field.data_type == "int":
#                 value = int(value) if value else None
#             elif custom_field.data_type == "float":
#                 value = float(value) if value else None
#             elif custom_field.data_type == "bool":
#                 value = bool(value) if value is not None else None

#             data[field_id] = value

#         table_name = self.comboBox.currentText()
        
#         if self.info_window is None:
#             self.info_window = InfoWindow({table_name: data}, parent=self)
#             self.info_window.row_selected.connect(self.update_combobox_and_fields)
            
#             table = self.info_window.create_table(table_name, data)
#             self.info_window.layout().addWidget(table)
#             self.info_window.tables[table_name] = table
            
#         else:
#             if table_name not in self.info_window.tables:
#                 table = self.info_window.create_table(table_name, data)
#                 self.info_window.layout().addWidget(table)
#                 self.info_window.tables[table_name] = table
                    
#             else:
#                 if self.info_window.isHidden():
#                     self.info_window.show()

#                 if self.info_window.tables[table_name].rowCount() > 1:
#                     selected_row = self.info_window.tables[table_name].currentRow()
                    
#                     if selected_row >= 0:
#                         for col, (field_id, value) in enumerate(data.items()):
#                             self.info_window.tables[table_name].setItem(selected_row, col, QTableWidgetItem(str(value)))
                            
#                         current_date = QTableWidgetItem(datetime.datetime.now().strftime("%Y-%m-%d"))
#                         current_time = QTableWidgetItem(datetime.datetime.now().strftime("%H:%M:%S"))
#                         self.info_window.tables[table_name].setItem(selected_row, len(data) + 1, current_date)
#                         self.info_window.tables[table_name].setItem(selected_row, len(data) + 2, current_time)
                        
#                         self.info_window.tables[table_name].setCurrentCell(-1, -1)
                        
#                     else:
#                         row_count = self.info_window.tables[table_name].rowCount()
#                         self.info_window.tables[table_name].setRowCount(row_count + 1)
                        
#                         for col, (field_id, value) in enumerate(data.items()):
#                             self.info_window.tables[table_name].setItem(row_count, col, QTableWidgetItem(str(value)))
                            
#                         btn_edit = QPushButton("Editar")
#                         btn_edit.clicked.connect(self.edit_row)
#                         btn_edit.table_name = table_name
#                         self.info_window.tables[table_name].setCellWidget(row_count, len(data), btn_edit)
                        
#                         btn_remove = QPushButton("Eliminar")
#                         btn_remove.clicked.connect(self.remove_row)
#                         btn_remove.table_name = table_name
#                         self.info_window.tables[table_name].setCellWidget(row_count, len(data) + 1, btn_remove)
                        
#                         current_date = QTableWidgetItem(datetime.datetime.now().strftime("%Y-%m-%d"))
#                         current_time = QTableWidgetItem(datetime.datetime.now().strftime("%H:%M:%S"))
#                         self.info_window.tables[table_name].setItem(row_count, len(data) + 2, current_date)
#                         self.info_window.tables[table_name].setItem(row_count, len(data) + 3, current_time)

#                 else:
#                     row_count = self.info_window.tables[table_name].rowCount()
#                     self.info_window.tables[table_name].setRowCount(row_count + 1)
                    
#                     for col, (field_id, value) in enumerate(data.items()):
#                         self.info_window.tables[table_name].setItem(row_count, col, QTableWidgetItem(str(value)))
                        
#                     btn_edit = QPushButton("Editar")
#                     btn_edit.clicked.connect(self.edit_row)
#                     btn_edit.table_name = table_name
#                     self.info_window.tables[table_name].setCellWidget(row_count, len(data), btn_edit)
                    
#                     btn_remove = QPushButton("Eliminar")
#                     btn_remove.clicked.connect(self.remove_row)
#                     btn_remove.table_name = table_name
#                     self.info_window.tables[table_name].setCellWidget(row_count, len(data) + 1, btn_remove)
                    
#                     current_date = QTableWidgetItem(datetime.datetime.now().strftime("%Y-%m-%d"))
#                     current_time = QTableWidgetItem(datetime.datetime.now().strftime("%H:%M:%S"))
#                     self.info_window.tables[table_name].setItem(row_count, len(data) + 2, current_date)
#                     self.info_window.tables[table_name].setItem(row_count, len(data) + 3, current_time)

#         for field_id, custom_field in self.text_boxes.items():
#             if isinstance(custom_field.widget, QLineEdit):
#                 custom_field.widget.setText("")
#             elif isinstance(custom_field.widget, QTextEdit):
#                 custom_field.widget.setText("")
#             elif isinstance(custom_field.widget, QComboBox):
#                 custom_field.widget.setCurrentIndex(0)
#             elif isinstance(custom_field.widget, QWidget) and custom_field.field == "radiobutton":
#                 custom_field.yes_radio.setChecked(False)
#                 custom_field.no_radio.setChecked(False)
        
#         if self.info_window.isHidden():
#             self.info_window.show()

#     def update_combobox_and_fields(self, table_name, data):
#         self.comboBox.setCurrentText(table_name)
        
#         for field_id, value in data.items():
#             if field_id in self.text_boxes:
#                 widget = self.text_boxes[field_id].widget
#                 if isinstance(widget, QLineEdit):
#                     widget.setText(value)
#                 elif isinstance(widget, QTextEdit):
#                     widget.setText(value)
#                 elif isinstance(widget, QComboBox):
#                     index = widget.findText(value)
#                     if index != -1:
#                         widget.setCurrentIndex(index)
#                 elif isinstance(widget, QWidget) and self.text_boxes[field_id].field == "radiobutton":
#                     if value.lower() == "sí":
#                         widget.yes_radio.setChecked(True)
#                         widget.no_radio.setChecked(False)
#                     elif value.lower() == "no":
#                         widget.yes_radio.setChecked(False)
#                         widget.no_radio.setChecked(True)

#     def edit_row(self):
#         btn = self.sender()
#         table_name = btn.table_name
#         table = self.info_window.tables[table_name]
#         selected_row = table.indexAt(btn.pos()).row()
            
#         if selected_row >= 0:
#             data = {}
#             for col in range(table.columnCount() - 3):  
#                 field_id = table.horizontalHeaderItem(col).text()
#                 value_item = table.item(selected_row, col)
                
#                 if value_item:
#                     value = value_item.text()
#                     data[field_id] = value

#             self.info_window.row_selected.emit(table_name, data)
            
#             self.info_window.hide()

#     def remove_row(self):
#         btn = self.sender()
#         table_name = btn.table_name
#         index = self.info_window.tables[table_name].indexAt(btn.pos())
#         if index.isValid():
#             self.info_window.tables[table_name].removeRow(index.row())
#             if self.info_window.tables[table_name].rowCount() == 0:
#                 self.info_window.layout().removeWidget(self.info_window.tables[table_name])
#                 self.info_window.tables[table_name].deleteLater()
#                 del self.info_window.tables[table_name]


# app = QApplication([])
# window = Inventario()
# window.show()
# app.exec()


import datetime
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QComboBox, QPushButton, QLineEdit, QTextEdit, QTableWidget, QTableWidgetItem, QLabel, QWidget, QVBoxLayout, QRadioButton, QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5 import QtGui


class InfoWindow(QDialog):
    row_selected = pyqtSignal(str, dict)

    def __init__(self, data, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Información")

        self.tables = {}
        layout = QVBoxLayout()

        self.setLayout(layout)

    def create_table(self, table_name, initial_data):
        table = QTableWidget()
        table.setColumnCount(len(initial_data) + 3)
        header_labels = list(initial_data.keys()) + \
            ["Acciones", "Fecha", "Hora"]
        table.setHorizontalHeaderLabels(header_labels)
        table.setRowCount(1)

        for col, (field_id, value) in enumerate(initial_data.items()):
            table.setItem(0, col, QTableWidgetItem(str(value)))

        return table

    def add_row(self, table_name, data):
        table = self.tables[table_name]
        row_count = table.rowCount()
        table.setRowCount(row_count + 1)

        for col, (field_id, value) in enumerate(data.items()):
            table.setItem(row_count, col, QTableWidgetItem(str(value)))

        btn_edit = QPushButton("Editar")
        btn_edit.clicked.connect(self.edit_row)
        btn_edit.table_name = table_name
        table.setCellWidget(row_count, len(data), btn_edit)

        btn_remove = QPushButton("Eliminar")
        btn_remove.clicked.connect(self.remove_row)
        btn_remove.table_name = table_name
        table.setCellWidget(row_count, len(data) + 1, btn_remove)

        current_date = QTableWidgetItem(datetime.datetime.now().strftime("%Y-%m-%d"))
        current_time = QTableWidgetItem(datetime.datetime.now().strftime("%H:%M:%S"))
        table.setItem(row_count, len(data) + 2, current_date)
        table.setItem(row_count, len(data) + 3, current_time)

    def edit_row(self):
        btn = self.sender()
        table_name = btn.table_name
        table = self.tables[table_name]
        selected_row = table.indexAt(btn.pos()).row()
        print(selected_row)
            
        if selected_row >= 0:
            data = {}
            for col in range(table.columnCount() - 3):  
                field_id = table.horizontalHeaderItem(col).text()
                value_item = table.item(selected_row, col)
                
                if value_item:
                    value = value_item.text()
                    data[field_id] = value

            self.row_selected.emit(table_name, data)
            
            self.hide()

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
                Form(id="nombre", label="Nombre",
                     place_holder="Digita el nombre", field="textbox"),
                Form(id="modelo", label="Modelo",
                     place_holder="Digite el modelo", field="textbox"),
                Form(id="marca", label="Marca",
                     place_holder="Digite la marca", field="textbox"),
                Form(id="dimensiones", label="Dimensiones",
                     place_holder="Digite la descripción", field="textbox"),
                Form(id="resorte", label="Resorte", place_holder="Tipo de resorte",
                     field="combobox", options=["Solo uno", "doble", "Triple"]),
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
                if self.info_window.isHidden():
                    self.info_window.show()

                if self.info_window.tables[table_name].rowCount() > 1:
                    selected_row = self.info_window.tables[table_name].currentRow()
                    
                    if selected_row >= 0:
                        for col, (field_id, value) in enumerate(data.items()):
                            self.info_window.tables[table_name].setItem(selected_row, col, QTableWidgetItem(str(value)))
                            
                        current_date = QTableWidgetItem(datetime.datetime.now().strftime("%Y-%m-%d"))
                        current_time = QTableWidgetItem(datetime.datetime.now().strftime("%H:%M:%S"))
                        self.info_window.tables[table_name].setItem(selected_row, len(data) + 1, current_date)
                        self.info_window.tables[table_name].setItem(selected_row, len(data) + 2, current_time)
                        
                        self.info_window.tables[table_name].setCurrentCell(-1, -1)
                        
                    else:
                        self.info_window.add_row(table_name, data)

                else:
                    self.info_window.add_row(table_name, data)

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
        
        if self.info_window.isHidden():
            self.info_window.show()

        # Restablecer la fila seleccionada
        self.info_window.tables[table_name].setCurrentCell(-1, -1)


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
