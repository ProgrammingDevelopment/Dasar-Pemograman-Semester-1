import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QFormLayout, QMessageBox
from flask import Flask, render_template, request, jsonify
from PyQt6.QtCore import Qt
from PyQt6.QtCore import requests, QDialog, QTableWidget
class ChickenOrderApp(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Warung Ayam Geprek 1945")
        self.setGeometry(100, 100, 600, 400)

        self.init_ui()

    def init_ui(self):
        self.label_intro = QLabel('WARUNG AYAM GEPREK 1945')
        self.label_intro.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_instruction = QLabel('Beli Ayam Geprek Online')
        self.label_instruction.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label_jenis_potong = QLabel('Jenis Potong:')
        self.edit_jenis_potong = QLineEdit()

        self.label_banyak_potong = QLabel('Banyak Potong:')
        self.edit_banyak_potong = QLineEdit()

        self.button_add_order = QPushButton('Add Order')
        self.button_view_orders = QPushButton('View Orders')

        layout_form = QFormLayout()
        layout_form.addRow(self.label_jenis_potong, self.edit_jenis_potong)
        layout_form.addRow(self.label_banyak_potong, self.edit_banyak_potong)

        layout_buttons = QHBoxLayout()
        layout_buttons.addWidget(self.button_add_order)
        layout_buttons.addWidget(self.button_view_orders)

        layout = QVBoxLayout()
        layout.addWidget(self.label_intro)
        layout.addWidget(self.label_instruction)
        layout.addLayout(layout_form)
        layout.addLayout(layout_buttons)

        self.setLayout(layout)

        # Connect buttons to functions
        self.button_add_order.clicked.connect(self.place_order)
        self.button_view_orders.clicked.connect(self.view_orders)

    def place_order(self):
        jenis_potong = self.edit_jenis_potong.text()
        banyak_potong = int(self.edit_banyak_potong.text())

        response = requests.post('http://127.0.0.1:5000/place_order', json={"jenis_potong": jenis_potong, "banyak_potong": banyak_potong})

        if response.status_code == 200:
            billing_message = response.json()["billing_message"]
            QMessageBox.information(self, "Order Result", billing_message, QMessageBox.StandardButton.Ok)
        else:
            QMessageBox.warning(self, "Order Failed", "Failed to place the order. Please try again later.",
                                QMessageBox.StandardButton.Ok)

    def view_orders(self):
        view_orders_dialog = ViewOrdersDialog()
        view_orders_dialog.exec_()

class ViewOrdersDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("View Chicken Orders")

        self.table_orders = QTableWidget()
        self.table_orders.setColumnCount(3)
        self.table_orders.setHorizontalHeaderLabels(["Jenis Potong", "Harga", "Jumlah"])

        self.button_close = QPushButton('Close')

        layout = QVBoxLayout()
        layout.addWidget(self.table_orders)
        layout.addWidget(self.button_close)

        self.setLayout(layout)

        # Connect buttons to functions
        self.button_close.clicked.connect(self.accept)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChickenOrderApp()
    window.show()
    sys.exit(app.exec())
