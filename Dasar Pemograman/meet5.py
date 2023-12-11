from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QMessageBox
from PyQt6.QtCore import Qt

class StudentPaymentForm(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Pembelian Formulir Mahasiswa UBSI")
        self.setGeometry(100, 100, 400, 200)

        self.init_ui()

    def init_ui(self):
        self.label_name = QLabel('Nama:')
        self.edit_name = QLineEdit()

        self.label_purchase_date = QLabel('Tanggal Pembelian Formulir:')
        self.edit_purchase_date = QLineEdit()

        self.button_submit = QPushButton('Submit')
        self.button_submit.clicked.connect(self.show_billing)

        layout = QVBoxLayout()
        layout.addWidget(self.label_name)
        layout.addWidget(self.edit_name)
        layout.addWidget(self.label_purchase_date)
        layout.addWidget(self.edit_purchase_date)
        layout.addWidget(self.button_submit)

        self.setLayout(layout)

    def show_billing(self):
        student_name = self.edit_name.text()
        purchase_date = self.edit_purchase_date.text()
        registration_fee = 350000
        nim = '2023' + str(hash(student_name) % 1000000)

        billing_message = (
            f"Nama Mahasiswa: {student_name}\n"
            f"Tanggal Pembelian Formulir: {purchase_date}\n"
            f"Biaya Pendaftaran Ulang: Rp. {registration_fee}\n"
            f"NIM Mahasiswa: {nim}\n\n"
            "Terima kasih! Cetak print out hasilnya ya guysss tencuu >_<"
        )

        QMessageBox.information(self, "Student Billing", billing_message, QMessageBox.StandardButton.Ok)

if __name__ == '__main__':
    app = QApplication([])
    window = StudentPaymentForm()
    window.show()
    app.exec()
