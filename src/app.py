from .gui.MainWindow import MainWindow

class CaminandoDeprisaSystem():
    def __init__(self):
        super().__init__()
        self.app = MainWindow()
        self.app.show()