from PyQt5.QtWidgets import QWidget, QVBoxLayout, QPushButton, QApplication, QLineEdit, QComboBox, QTextEdit, QRadioButton
from Form import Form
from CustomField import CustomField

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
                Form(id="descripcion", label="Descripción",
                     place_holder="Digite la descripción", field="textarea"),
                Form(id="cantidad", label="Cantidad",
                     place_holder="Digite la cantidad", field="textbox", data_type="int")
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
                     place_holder="Digite el color", field="textarea"),
                Form(id="resorte", label="Resorte",
                     place_holder="Tipo de resorte", field="combobox", options=["Solo uno", "doble", "Triple"]),
            ]
        }

        self.layout = QVBoxLayout()
        
        self.comboBox = QComboBox()
        self.comboBox.currentIndexChanged.connect(self.update_fields)
        
        self.layout.addWidget(self.comboBox)

        self.text_boxes = {}
        self.widgets = []  # Lista para almacenar los widgets creados

        self.comboBox.addItems(list(self.campos.keys()))

        self.button = QPushButton("Hola")  # Añadir el botón al layout en el constructor
        self.button.clicked.connect(self.on_button_clicked)
        self.layout.addWidget(self.button)

        self.update_fields()

        self.setLayout(self.layout)

    def update_fields(self):
        current_selection = self.comboBox.currentText()

        # Eliminar los campos antiguos del layout
        for widget in self.widgets:
            self.layout.removeWidget(widget)
            widget.setParent(None)
            print(widget)

        self.widgets.clear()  # Limpiar la lista de widgets

        # Añadir los nuevos campos según la selección
        for x in self.campos[current_selection]:
            field = CustomField(label=x.label, place_holder=x.place_holder, options=x.options,
                                data_type=x.data_type, field_type=x.field, text_boxes=self.text_boxes)
            self.text_boxes[x.id] = field
            self.layout.addWidget(field)
            self.widgets.append(field)  # Añadir el widget a la lista de widgets

    def on_button_clicked(self):
        for field_id, custom_field in self.text_boxes.items():
            value = custom_field.widget.text() if isinstance(custom_field.widget, QLineEdit) else \
                custom_field.widget.currentText() if isinstance(custom_field.widget, QComboBox) else \
                custom_field.widget.toPlainText() if isinstance(custom_field.widget, QTextEdit) else \
                custom_field.widget.text() if isinstance(
                    custom_field.widget, QRadioButton) else None

            if custom_field.data_type == "int":
                value = int(value) if value else None
            elif custom_field.data_type == "float":
                value = float(value) if value else None
            elif custom_field.data_type == "bool":
                value = bool(value) if value else None

            print(f"{field_id}: {value}")



app = QApplication([])
window = Inventario()
window.show()
app.exec()