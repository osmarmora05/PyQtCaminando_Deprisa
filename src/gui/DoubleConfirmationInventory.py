from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QTableWidget, QFrame, QLabel, QVBoxLayout, QTableWidgetItem, QHeaderView, QPushButton, QHBoxLayout, QWidget
from PyQt5 import QtGui
from .Ui_DoubleConfirmationInventory import Ui_DoubleConfirmationInventory
from src.helpers.datetime_helper import getDate, getTime
from PyQt5.QtCore import pyqtSignal


class DoubleConfirmationInventory(QDialog, Ui_DoubleConfirmationInventory):
    row_selected = pyqtSignal(str, dict)


    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.setupUI(self)

    def create_table(self, table_name, initial_data):
        table = QTableWidget()
        table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        table.horizontalHeader().setMinimumSectionSize(100)
        table.setObjectName("table")
        table.setStyleSheet(
            """
            QTableWidget#table {
                color: #A1A1AA;
                gridline-color: #27272A;
            }

            QHeaderView {
                color: #A1A1AA;
            }
            """
        )
        table_title = QLabel(str(table_name))
        table_title.setObjectName("table_title")
        table_title.setStyleSheet(
            """
                QLabel#table_title {
                    color: #FAFAFA
                }
            """
        )
        table_container_frame = QFrame()
        table_container_frame.setObjectName("table_container_frame")
        table_container_frame.setMinimumHeight(200)
        table_container_frame.setStyleSheet(
            """
                QFrame#table_container_frame {
                    border-radius: 8px;
                    border: 1px solid #27272A;
                    background-color: #09090B;
                    padding: 10px 30px 10px 30px;
                }
            """
        )
        table_container_layout = QVBoxLayout()
        table_container_layout.setContentsMargins(0, 0, 0, 0)
        table_container_layout.setSpacing(10)
        table_container_layout.setAlignment(Qt.AlignTop)

        # +3 for the "Acciones", "Fecha", and "Hora" columns
        table.setColumnCount(len(initial_data) + 3)
        header_labels = list(initial_data.keys()) + \
            ["Acciones", "Fecha", "Hora"]
        table.setHorizontalHeaderLabels(header_labels)
        table.setRowCount(1)

        for col, (field_id, value) in enumerate(initial_data.items()):
            table.setItem(0, col, QTableWidgetItem(str(value)))

        # Add delete,edit button, date and time
        actions_button = self.add_buttons_actions(table_name)
        table.setCellWidget(0, len(initial_data), actions_button)

        date_item = QTableWidgetItem(getDate())
        time_item = QTableWidgetItem(getTime())

        table.setItem(0, len(initial_data) + 1, date_item)
        table.setItem(0, len(initial_data) + 2, time_item)

        table_container_layout.addWidget(table_title)
        table_container_layout.addWidget(table)
        table_container_frame.setLayout(table_container_layout)

        return table_container_frame

    def add_row(self, table_name, data):
        self.tables[table_name].layout().itemAt(1).widget().setRowCount(
            self.tables[table_name].layout().itemAt(1).widget().rowCount() + 1)

        for col, (field_id, value) in enumerate(data.items()):
            table_widget = self.tables[table_name].layout().itemAt(1).widget()
            table_widget.setItem(table_widget.rowCount() - 1,
                                 col, QTableWidgetItem(str(value)))

        actions_button = self.add_buttons_actions(table_name)
        self.tables[table_name].layout().itemAt(1).widget().setCellWidget(
            self.tables[table_name].layout().itemAt(1).widget().rowCount() - 1, len(data), actions_button)

        # Add datetime
        date_item = QTableWidgetItem(getDate())
        time_item = QTableWidgetItem(getTime())
        self.tables[table_name].layout().itemAt(1).widget().setItem(
            self.tables[table_name].layout().itemAt(1).widget().rowCount() - 1, len(data) + 1, date_item)
        self.tables[table_name].layout().itemAt(1).widget().setItem(
            self.tables[table_name].layout().itemAt(1).widget().rowCount() - 1, len(data) + 2, time_item)
        
    
    def add_buttons_actions(self,table_name):
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(
            "assets/icons/trash.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        delete_row_button = QPushButton("")
        delete_row_button.setIcon(icon)
        delete_row_button.table_name = table_name
        delete_row_button.clicked.connect(self.remove_row)
        icon.addPixmap(QtGui.QPixmap(
            "assets/icons/pencil.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        edit_row_button = QPushButton("")
        edit_row_button.table_name = table_name
        edit_row_button.clicked.connect(self.edit_row)

        edit_row_button.setIcon(icon)
        action_container_widget = QWidget()
        action_container_layout = QHBoxLayout()
        action_container_layout.setContentsMargins(5, 0, 5, 0)
        action_container_layout.setSpacing(5)
        action_container_layout.addWidget(delete_row_button)
        action_container_layout.addWidget(edit_row_button)
        action_container_widget.setLayout(action_container_layout)

        return action_container_widget

    def edit_row(self):
        btn = self.sender()  # Get the button that was clicked
        table_name = btn.table_name  # Get the table name from the button's custom attribute
        
        # Get the QTableWidget object from the QFrame
        table_widget = self.tables[table_name].layout().itemAt(1).widget()
        
        # Find the button's row by checking its position
        for row in range(table_widget.rowCount()):
            cell_widget = table_widget.cellWidget(row, table_widget.columnCount() - 3)  # Assuming the actions buttons are in the second last cell
            if cell_widget and cell_widget.layout().indexOf(btn) != -1:
                selected_row = row
                break
        else:
            selected_row = -1
        

        if selected_row >= 0:
            # Select the row
            table_widget.selectRow(selected_row)
            
            data = {}
            for col in range(table_widget.columnCount() - 3):  
                field_id = table_widget.horizontalHeaderItem(col).text()
                value_item = table_widget.item(selected_row, col)
                
                if value_item:
                    value = value_item.text()
                    data[field_id] = value

            self.row_selected.emit(table_name, data)
            
            self.hide()


    def remove_row(self):
        btn = self.sender()  # Get the button that was clicked
        table_name = btn.table_name  # Get the table name from the button's custom attribute
        
        # Get the QTableWidget object from the QFrame
        table_widget = self.tables[table_name].layout().itemAt(1).widget()
        
        # Use indexAt on the QTableWidget object to get the index of the button
        index = table_widget.indexAt(btn.pos())
        
        if index.isValid():
            table_widget.removeRow(index.row())
            
            # Check if the table is empty
            if table_widget.rowCount() == 0:
                self.layout().removeWidget(self.tables[table_name])  # Remove the table widget from the layout
                self.tables[table_name].deleteLater()  # Delete the table widget
                del self.tables[table_name]