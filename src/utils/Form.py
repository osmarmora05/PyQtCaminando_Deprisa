# class Form:
#     def __init__(self, id: str, label: str, place_holder: str, field: str, options=None, data_type="str"):
#         self.id = id
#         self.label = label
#         self.place_holder = place_holder
#         self.field = field
#         self.options = options if options is not None else []
#         self.data_type = data_type

#     def __repr__(self):
#         return f"[{self.id}, {self.label}, {self.place_holder}, {self.field}, {self.options}, {self.data_type}]"


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
