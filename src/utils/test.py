from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit
from PyQt5.QtCore import pyqtSignal
import sys
from typing import List


class Form:
    def __init__(self, id: str, label: str, place_holder: str, field: str):
        self.id = id
        self.label = label
        self.place_holder = place_holder
        self.field = field

    def __repr__(self):
        return f"[{self.id}, {self.label}, {self.place_holder}, {self.field}]"


class Inventario(QWidget):
    signal_text_changed = pyqtSignal(str, str)

    def __init__(self, generico: List[Form]):
        super().__init__()
        self.layout = QVBoxLayout()
        self.generico = generico
        self.text_boxes = {}

        for field in self.generico:
            label = QLabel(field.label)
            text_box = QLineEdit()
            text_box.setPlaceholderText(field.place_holder)
            text_box.textChanged.connect(self.text_changed_slot)
            
            self.text_boxes[field.id] = text_box
            
            self.layout.addWidget(label)
            self.layout.addWidget(text_box)
            print(self.text_boxes)

        self.setLayout(self.layout)

    def text_changed_slot(self, text):
        sender = self.sender()
        # print(sender)
        for field_id, text_box in self.text_boxes.items():
            if text_box == sender:
                self.signal_text_changed.emit(field_id, text)


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication(sys.argv)

    generico = [
        Form(id="nombre", label="Nombre", place_holder="Digita el nombre", field="textbox"),
        Form(id="marca", label="Marca", place_holder="Digita la marca", field="textbox"),
        Form(id="modelo", label="Modelo", place_holder="Digite el modelo", field="textbox"),
        Form(id="descripcion", label="Descripcion", place_holder="Digite la descripcion", field="textbox")
    ]

    ventana = Inventario(generico)
    ventana.signal_text_changed.connect(lambda field_id, text: print(f"{field_id}: {text}"))

    ventana.show()

    sys.exit(app.exec_())
