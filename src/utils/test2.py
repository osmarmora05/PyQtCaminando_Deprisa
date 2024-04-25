from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel
from typing import List
from PyQt5.QtCore import pyqtSignal

from PyQt5.QtWidgets import QLabel, QLineEdit, QFrame, QHBoxLayout, QWidget

class CustomQLineEdit(QFrame):
    def __init__(self, label, place_holder):
        super().__init__()

        layout = QHBoxLayout()
        self.label = QLabel(label)
        self.text_box = QLineEdit()
        
        self.text_box.setPlaceholderText(place_holder)

        layout.addWidget(self.label)
        layout.addWidget(self.text_box)

        self.setLayout(layout)

class Form:
    def __init__(self, id: str, label: str, place_holder: str):
        self.id = id
        self.label = label
        self.place_holder = place_holder

    def __repr__(self):
        return f"[{self.id}, {self.label}, {self.place_holder}]"


class GenericForm(QWidget):
    signal_text_changed = pyqtSignal(str, str)

    def __init__(self, generico: List[Form]):
        super().__init__()
        self.layout = QVBoxLayout()
        self.generico = generico
        self.text_boxes = {}

        for field in self.generico:
            custom_line_edit = CustomQLineEdit(label=field.label, place_holder=field.place_holder)
            custom_line_edit.text_box.textChanged.connect(self.text_changed_slot)
            
            self.text_boxes[field.id] = custom_line_edit
            
            self.layout.addWidget(custom_line_edit)

        self.setLayout(self.layout)

    def text_changed_slot(self, text):
        sender = self.sender()
        for field_id, custom_line_edit in self.text_boxes.items():
            if custom_line_edit.text_box == sender:
                self.signal_text_changed.emit(field_id, text)


# Ejemplo de uso
if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication
    import sys

    app = QApplication(sys.argv)

    generico = [
        Form(id="nombre", label="Nombre", place_holder="Digita el nombre"),
        Form(id="marca", label="Marca", place_holder="Digita la marca"),
        Form(id="modelo", label="Modelo", place_holder="Digite el modelo")
    ]

    ventana = GenericForm(generico)
    ventana.signal_text_changed.connect(lambda field_id, text: print(f"{field_id}: {text}"))

    ventana.show()

    sys.exit(app.exec_())
