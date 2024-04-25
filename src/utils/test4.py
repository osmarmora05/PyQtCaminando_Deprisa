# from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit, QLabel, QFrame, QPushButton, QTextEdit, QComboBox, QRadioButton
# from PyQt5.QtCore import pyqtSignal


# class CustomField(QFrame):
#     signal_text_changed = pyqtSignal(str, str)

#     def __init__(self, label, place_holder, field_type, text_boxes):
#         super().__init__()
#         self.layout = QVBoxLayout()

#         self.label_widget = QLabel(label)

#         if field_type == "textbox":
#             self.widget = QLineEdit()
#             self.widget.setPlaceholderText(place_holder)
#             self.widget.textChanged.connect(self.text_changed_slot)
#         elif field_type == "textarea":
#             self.widget = QTextEdit()
#             self.widget.textChanged.connect(self.text_changed_slot)
#         elif field_type == "combobox":
#             self.widget = QComboBox()
#             self.widget.addItem(place_holder)
#             self.widget.currentTextChanged.connect(self.text_changed_slot)
#         elif field_type == "radiobutton":
#             self.widget = QRadioButton(label)
#             self.widget.toggled.connect(self.radio_button_toggled)

#         self.layout.addWidget(self.label_widget)
#         self.layout.addWidget(self.widget)
#         self.setLayout(self.layout)
        
#         self.text_boxes = text_boxes

#     def text_changed_slot(self, *args):
#         sender = self.sender()
#         for field_id, custom_field in self.text_boxes.items():
#             if custom_field.widget == sender:
#                 if isinstance(sender, QLineEdit):
#                     text = sender.text()
#                 elif isinstance(sender, QComboBox):
#                     text = sender.currentText()
#                 elif isinstance(sender, QTextEdit):
#                     text = sender.toPlainText()
#                 self.signal_text_changed.emit(field_id, text)

#     def radio_button_toggled(self, checked):
#         sender = self.sender()
#         if checked:
#             for field_id, custom_field in self.text_boxes.items():
#                 if custom_field.widget == sender:
#                     self.signal_text_changed.emit(field_id, sender.text())


# class Form:
#     def __init__(self, id: str, label: str, place_holder: str, field: str):
#         self.id = id
#         self.label = label
#         self.place_holder = place_holder
#         self.field = field

#     def __repr__(self):
#         return f"[{self.id}, {self.label}, {self.place_holder}, {self.field}]"


# class Inventario(QWidget):
#     def __init__(self):
#         super().__init__()
        
#         generico = [
#             Form(id="nombre", label="Nombre",
#                  place_holder="Digita el nombre", field="textbox"),
#             Form(id="marca", label="Marca",
#                  place_holder="Digita la marca", field="combobox"),
#             Form(id="modelo", label="Modelo",
#                  place_holder="Digite el modelo", field="radiobutton"),
#             Form(id="descripcion", label="Descripción",
#                  place_holder="Escribe la descripción", field="textarea")
#         ]

#         layout = QVBoxLayout()
#         button = QPushButton("holi")
#         button.clicked.connect(self.on_button_clicked)
#         self.text_boxes = {}

#         for x in generico:
#             field = CustomField(label=x.label, place_holder=x.place_holder, field_type=x.field, text_boxes=self.text_boxes)
#             field.signal_text_changed.connect(lambda field_id, text: print(f"{field_id}: {text}"))
#             self.text_boxes[x.id] = field

#             layout.addWidget(field)
#         layout.addWidget(button)
#         self.setLayout(layout)

#     def on_button_clicked(self):
#         for field_id, custom_field in self.text_boxes.items():
#             if isinstance(custom_field.widget, QLineEdit) or isinstance(custom_field.widget, QTextEdit) or isinstance(custom_field.widget, QComboBox):
#                 if isinstance(custom_field.widget, QComboBox):
#                     text = custom_field.widget.currentText()
#                 elif isinstance(custom_field.widget, QTextEdit):
#                     text = custom_field.widget.toPlainText()
#                 else:
#                     text = custom_field.widget.text()
#                 print(f"{field_id}: {text}")
#             elif isinstance(custom_field.widget, QRadioButton):
#                 if custom_field.widget.isChecked():
#                     print(f"{field_id}: {custom_field.widget.text()}")


# app = QApplication([])
# window = Inventario()
# window.show()
# app.exec()


# from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit, QLabel, QFrame, QPushButton, QTextEdit, QComboBox, QRadioButton
# from PyQt5.QtCore import pyqtSignal


# class CustomField(QFrame):
#     signal_text_changed = pyqtSignal(str, str)

#     def __init__(self, label, place_holder, options, field_type, text_boxes):
#         super().__init__()
#         self.layout = QVBoxLayout()

#         self.label_widget = QLabel(label)

#         if field_type == "textbox":
#             self.widget = QLineEdit()
#             self.widget.setPlaceholderText(place_holder)
#             self.widget.textChanged.connect(self.text_changed_slot)
#         elif field_type == "textarea":
#             self.widget = QTextEdit()
#             self.widget.textChanged.connect(self.text_changed_slot)
#         elif field_type == "combobox":
#             self.widget = QComboBox()
#             self.widget.addItems(options)
#             self.widget.currentTextChanged.connect(self.text_changed_slot)
#         elif field_type == "radiobutton":
#             self.widget = QRadioButton(label)
#             self.widget.toggled.connect(self.radio_button_toggled)

#         self.layout.addWidget(self.label_widget)
#         self.layout.addWidget(self.widget)
#         self.setLayout(self.layout)
        
#         self.text_boxes = text_boxes

#     def text_changed_slot(self, *args):
#         sender = self.sender()
#         for field_id, custom_field in self.text_boxes.items():
#             if custom_field.widget == sender:
#                 if isinstance(sender, QLineEdit):
#                     text = sender.text()
#                 elif isinstance(sender, QComboBox):
#                     text = sender.currentText()
#                 elif isinstance(sender, QTextEdit):
#                     text = sender.toPlainText()
#                 self.signal_text_changed.emit(field_id, text)

#     def radio_button_toggled(self, checked):
#         sender = self.sender()
#         if checked:
#             for field_id, custom_field in self.text_boxes.items():
#                 if custom_field.widget == sender:
#                     self.signal_text_changed.emit(field_id, sender.text())


# class Form:
#     def __init__(self, id: str, label: str, place_holder: str, field: str, options=None):
#         self.id = id
#         self.label = label
#         self.place_holder = place_holder
#         self.field = field
#         self.options = options if options is not None else []

#     def __repr__(self):
#         return f"[{self.id}, {self.label}, {self.place_holder}, {self.field}, {self.options}]"


# class Inventario(QWidget):
#     def __init__(self):
#         super().__init__()
        
#         generico = [
#             Form(id="nombre", label="Nombre",
#                  place_holder="Digita el nombre", field="textbox"),
#             Form(id="marca", label="Marca",
#                  place_holder="Digita la marca", field="combobox", options=["Opción 1", "Opción 2", "Opción 3"]),
#             Form(id="modelo", label="Modelo",
#                  place_holder="Digite el modelo", field="radiobutton"),
#             Form(id="descripcion", label="Descripción",
#                  place_holder="Escribe la descripción", field="textarea")
#         ]

#         layout = QVBoxLayout()
#         button = QPushButton("holi")
#         button.clicked.connect(self.on_button_clicked)
#         self.text_boxes = {}

#         for x in generico:
#             field = CustomField(label=x.label, place_holder=x.place_holder, options=x.options, field_type=x.field, text_boxes=self.text_boxes)
#             field.signal_text_changed.connect(lambda field_id, text: print(f"{field_id}: {text}"))
#             self.text_boxes[x.id] = field

#             layout.addWidget(field)

#         layout.addWidget(button)
#         self.setLayout(layout)

#     def on_button_clicked(self):
#         for field_id, custom_field in self.text_boxes.items():
#             if isinstance(custom_field.widget, QLineEdit) or isinstance(custom_field.widget, QTextEdit) or isinstance(custom_field.widget, QComboBox):
#                 if isinstance(custom_field.widget, QComboBox):
#                     text = custom_field.widget.currentText()
#                 elif isinstance(custom_field.widget, QTextEdit):
#                     text = custom_field.widget.toPlainText()
#                 else:
#                     text = custom_field.widget.text()
#                 print(f"{field_id}: {text}")
#             elif isinstance(custom_field.widget, QRadioButton):
#                 if custom_field.widget.isChecked():
#                     print(f"{field_id}: {custom_field.widget.text()}")


# app = QApplication([])
# window = Inventario()
# window.show()
# app.exec()


from PyQt5.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit, QLabel, QFrame, QPushButton, QTextEdit, QComboBox, QRadioButton
from PyQt5.QtCore import pyqtSignal


class CustomField(QFrame):
    signal_text_changed = pyqtSignal(str, str)

    def __init__(self, label, place_holder, options, field_type, text_boxes):
        super().__init__()
        self.layout = QVBoxLayout()

        self.label_widget = QLabel(label)

        if field_type == "textbox":
            self.widget = QLineEdit()
            self.widget.setPlaceholderText(place_holder)
            self.widget.textChanged.connect(self.text_changed_slot)
        elif field_type == "textarea":
            self.widget = QTextEdit()
            self.widget.textChanged.connect(self.text_changed_slot)
        elif field_type == "combobox":
            self.widget = QComboBox()
            self.widget.addItems(options)
            self.widget.currentTextChanged.connect(self.text_changed_slot)
        elif field_type == "radiobutton":
            self.widget = QRadioButton(label)
            self.widget.toggled.connect(self.radio_button_toggled)

        self.layout.addWidget(self.label_widget)
        self.layout.addWidget(self.widget)
        self.setLayout(self.layout)
        
        self.text_boxes = text_boxes

    def text_changed_slot(self, *args):
        sender = self.sender()
        for field_id, custom_field in self.text_boxes.items():
            if custom_field.widget == sender:
                if isinstance(sender, QLineEdit):
                    text = sender.text()
                elif isinstance(sender, QComboBox):
                    text = sender.currentText()
                elif isinstance(sender, QTextEdit):
                    text = sender.toPlainText()
                self.signal_text_changed.emit(field_id, text)

    def radio_button_toggled(self, checked):
        sender = self.sender()
        if checked:
            for field_id, custom_field in self.text_boxes.items():
                if custom_field.widget == sender:
                    self.signal_text_changed.emit(field_id, sender.text())


class Form:
    def __init__(self, id: str, label: str, place_holder: str, field: str, options=None):
        self.id = id
        self.label = label
        self.place_holder = place_holder
        self.field = field
        self.options = options if options is not None else []

    def __repr__(self):
        return f"[{self.id}, {self.label}, {self.place_holder}, {self.field}, {self.options}]"


class Inventario(QWidget):
    def __init__(self):
        super().__init__()
        
        generico = [
            Form(id="nombre", label="Nombre",
                 place_holder="Digita el nombre", field="textbox"),
            Form(id="marca", label="Marca",
                 place_holder="Digita la marca", field="combobox", options=["Opción 1", "Opción 2", "Opción 3"]),
            Form(id="modelo", label="Modelo",
                 place_holder="Digite el modelo", field="radiobutton"),
            Form(id="descripcion", label="Descripción",
                 place_holder="Escribe la descripción", field="textarea")
        ]

        layout = QVBoxLayout()
        button = QPushButton("holi")
        button.clicked.connect(self.on_button_clicked)
        self.text_boxes = {}

        for x in generico:
            field = CustomField(label=x.label, place_holder=x.place_holder, options=x.options, field_type=x.field, text_boxes=self.text_boxes)
            field.signal_text_changed.connect(lambda field_id, text: print(f"{field_id}: {text}"))
            self.text_boxes[x.id] = field

            layout.addWidget(field)

        layout.addWidget(button)
        self.setLayout(layout)

    def on_button_clicked(self):
        for field_id, custom_field in self.text_boxes.items():
            if isinstance(custom_field.widget, QLineEdit) or isinstance(custom_field.widget, QTextEdit) or isinstance(custom_field.widget, QComboBox):
                if isinstance(custom_field.widget, QComboBox):
                    text = custom_field.widget.currentText()
                elif isinstance(custom_field.widget, QTextEdit):
                    text = custom_field.widget.toPlainText()
                else:
                    text = custom_field.widget.text()
                print(f"{field_id}: {text}")
            elif isinstance(custom_field.widget, QRadioButton):
                if custom_field.widget.isChecked():
                    print(f"{field_id}: {custom_field.widget.text()}")


app = QApplication([])
window = Inventario()
window.show()
app.exec()