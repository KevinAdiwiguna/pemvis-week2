# Nama: Ida Bagus Kevin Adiwiguna
# NIM: F1D02410115
# Kelas: 6C


import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QComboBox, QPushButton, QFrame
)

class BiodataApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Form Biodata Mahasiswa")
        self.setFixedWidth(500)
        self.resize(500, 550)

        self.init_ui()
        self.set_style()
        self.show_warning() 

    def init_ui(self):
        layout = QVBoxLayout()
        layout.setSpacing(10)

        # nama
        labelNama = QLabel("Nama Lengkap:")
        self.inputNama = QLineEdit()
        self.inputNama.setPlaceholderText("Masukan Nama")

        # nim
        labelNIM = QLabel("NIM:")
        self.inputNIM = QLineEdit()
        self.inputNIM.setPlaceholderText("Masukan NIM")

        # kelas
        labelKelas = QLabel("Kelas:")
        self.inputKelas = QLineEdit()
        self.inputKelas.setPlaceholderText("TI-2A")

        # gender
        labelGender = QLabel("Jenis Kelamin:")
        self.comboGender = QComboBox()
        self.comboGender.addItems(["Pilih Gender","Laki-laki", "Perempuan"])

        # button
        buttonLayout = QHBoxLayout()

        btnSubmit = QPushButton("Sumbit")
        btnSubmit.setStyleSheet("background-color: #3498db; color: white;")
        btnSubmit.clicked.connect(self.submit)

        btnReset = QPushButton("Reset")
        btnReset.setStyleSheet("background-color: #95a5a6; color: white;")
        btnReset.clicked.connect(self.reset)

        buttonLayout.addWidget(btnSubmit)
        buttonLayout.addWidget(btnReset)

        # result
        self.resultFrame = QFrame()
        self.resultLayout = QVBoxLayout()

        self.resultTitle = QLabel("DATA BIODATA")
        self.resultText = QLabel()
        self.resultTitle.setStyleSheet("font-weight: bold; border-left: 0px solid transparent; font-size:12pt")
        self.resultText.setStyleSheet("border-left: 0px solid transparent;")
        

        self.resultLayout.addWidget(self.resultTitle)
        self.resultLayout.addWidget(self.resultText)

        self.resultFrame.setLayout(self.resultLayout)

        layout.addWidget(labelNama)
        layout.addWidget(self.inputNama)

        layout.addWidget(labelNIM)
        layout.addWidget(self.inputNIM)

        layout.addWidget(labelKelas)
        layout.addWidget(self.inputKelas)

        layout.addWidget(labelGender)
        layout.addWidget(self.comboGender)

        layout.addLayout(buttonLayout)

        layout.addWidget(self.resultFrame)
        layout.addStretch()

        self.setLayout(layout)

    def show_warning(self):
        self.resultFrame.setStyleSheet("""
        QFrame {
            background-color: #f8d7da;
            border-left: 5px solid red;
            padding: 12px;
        }
        """)

        self.resultTitle.setText("PERINGATAN")
        self.resultText.setText(
            "Masukan Nama\n"
            "Masukan NIM\n"
            "Masukan Kelas\n"
            "Pilih Gender"
        )

    def show_success(self, nama, nim, kelas, gender):
        self.resultFrame.setStyleSheet("""
        QFrame {
            background-color: #d4edda;
            border-left: 5px solid green;
            padding: 12px;
        }
        """)

        self.resultTitle.setText("DATA BIODATA")

        self.resultText.setText(
            f"Nama: {nama}\n"
            f"NIM: {nim}\n"
            f"Kelas: {kelas}\n"
            f"Jenis Kelamin: {gender}"
        )

    def submit(self):
        nama = self.inputNama.text().strip()
        nim = self.inputNIM.text().strip()
        kelas = self.inputKelas.text().strip()
        gender = self.comboGender.currentText()

        valid = True

        self.clear_input_error(self.inputNama)
        self.clear_input_error(self.inputNIM)
        self.clear_input_error(self.inputKelas)
        self.clear_input_error(self.comboGender)

        if not nama:
            self.input_error(self.inputNama)
            valid = False

        if not nim:
            self.input_error(self.inputNIM)
            valid = False

        if not kelas:
            self.input_error(self.inputKelas)
            valid = False

        if gender == "Pilih Gender":
            self.input_error(self.comboGender)
            valid = False

        if not valid:
            self.show_warning()
            return



        self.show_success(nama, nim, kelas, gender)
        
    def input_error(self, widget):
        widget.setStyleSheet("""
            border: 1px solid red;
            background-color: #ffe6e6;
            border-radius: 6px;
            padding: 6px;
        """)
    def clear_input_error(self, widget):
        widget.setStyleSheet("""
            background-color: white;
            border: 1px solid #ced4da;
            border-radius: 6px;
            padding: 6px;
        """)

    def reset(self):
        self.inputNama.clear()
        self.inputNIM.clear()
        self.inputKelas.clear()
        self.comboGender.setCurrentIndex(0)

        self.show_warning()

    def set_style(self):
        self.setStyleSheet("""
        QWidget {
            background-color: #f5f7fa;
            font-size: 10pt;
        }

        QLabel {
            color: #333;
        }

        QLineEdit, QComboBox {
            background-color: white;
            border: 1px solid #ced4da;
            border-radius: 6px;
            padding: 6px;
        }

        QLineEdit:focus, QComboBox:focus {
            border: 1px solid #4da3ff;
        }

        QPushButton {
            padding: 8px;
            border-radius: 6px;
            border: none;
        }

        QPushButton:hover {
            opacity: 0.9;
        }
        """)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BiodataApp()
    window.show()
    sys.exit(app.exec())