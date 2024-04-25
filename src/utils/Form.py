class Form:
    def __init__(self, id, label, place_holder, field, options=None, data_type="text"):
        self.id = id
        self.label = label
        self.place_holder = place_holder
        self.field = field
        self.options = options
        self.data_type = data_type

    def __repr__(self) -> str:
        return f"[{self.id}, {self.label}, {self.place_holder}, {self.field}, {self.options}, {self.data_type}]"