from src.app import CaminandoDeprisaSystem
from PyQt5.QtWidgets import QApplication

import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CaminandoDeprisaSystem()
    app.exec()