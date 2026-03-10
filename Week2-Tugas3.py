# Nama: Ida Bagus Kevin Adiwiguna
# NIM: F1D02410115
# Kelas: 6C

import sys
from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QCheckBox
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
import os

base_dir = os.path.dirname(__file__)
image_path = os.path.join(base_dir, "login.jpg")


class LoginForm(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login")
        self.init_ui()
        self.set_style()
        self.showFullScreen()

    def init_ui(self):
        mainLayout = QHBoxLayout()

        containerInputLayout = QVBoxLayout()
        containerInputLayout.setSpacing(10)
        containerInputLayout.setAlignment(Qt.AlignCenter)

        labelTitle = QLabel("Login Page")
        labelTitle.setObjectName("title")

        labelDescription = QLabel("Selamat datang\nSilahkan login terlebih dahulu")
        labelDescription.setObjectName("desc")

        labelUsername = QLabel("Username")
        self.inputUsername = QLineEdit()
        self.inputUsername.setPlaceholderText("admin")

        labelPassword = QLabel("Password")
        self.inputPassword = QLineEdit()
        self.inputPassword.setPlaceholderText("******")
        self.inputPassword.setEchoMode(QLineEdit.Password)

        self.checkboxShow = QCheckBox("Tampilkan Password")
        self.checkboxShow.stateChanged.connect(self.toggle_password)

        self.labelStatus = QLabel("")
        self.labelStatus.setMinimumHeight(20)

        containerButton = QHBoxLayout()

        btnLogin = QPushButton("Submit")
        btnLogin.setStyleSheet("""
            background-color: #f0f0f0;
            color: black;
            padding: 8px 0px;
            border-radius: 6px;""")
        btnLogin.clicked.connect(self.submit)

        btnReset = QPushButton("Reset")
        btnReset.setStyleSheet("""
            background-color: #212121;
            color: white;
            padding: 8px 0px;
            border-radius: 6px;""")
        btnReset.clicked.connect(self.reset)

        containerButton.addWidget(btnLogin)
        containerButton.addWidget(btnReset)

        containerInputLayout.addWidget(labelTitle)
        containerInputLayout.addWidget(labelDescription)
        containerInputLayout.addWidget(labelUsername)
        containerInputLayout.addWidget(self.inputUsername)
        containerInputLayout.addWidget(labelPassword)
        containerInputLayout.addWidget(self.inputPassword)
        containerInputLayout.addWidget(self.checkboxShow)
        containerInputLayout.addWidget(self.labelStatus)
        containerInputLayout.addLayout(containerButton)

        imageLabel = QLabel()
        imageLabel.setAlignment(Qt.AlignCenter)

        pixmap = QPixmap(image_path)

        if not pixmap.isNull():
            imageLabel.setPixmap(
                pixmap.scaled(
                    700,
                    700,
                    Qt.KeepAspectRatio,
                    Qt.SmoothTransformation
                )
            )

        mainLayout.addLayout(containerInputLayout, 1)
        mainLayout.addWidget(imageLabel, 1)

        self.setLayout(mainLayout)

    def toggle_password(self):
        if self.checkboxShow.isChecked():
            self.inputPassword.setEchoMode(QLineEdit.Normal)
        else:
            self.inputPassword.setEchoMode(QLineEdit.Password)

    def submit(self):
        username = self.inputUsername.text()
        password = self.inputPassword.text()

        if username == "admin" and password == "12345":
            self.labelStatus.setText("Berhasil login")
            self.labelStatus.setStyleSheet("color: #00ff7f;")
        else:
            self.labelStatus.setText("Username atau password salah")
            self.labelStatus.setStyleSheet("color: red;")

    def reset(self):
        self.inputUsername.clear()
        self.inputPassword.clear()
        self.labelStatus.setText("")

    def set_style(self):
        self.setStyleSheet("""
            QWidget {
                background-color: black;
                color: white;
                font-size: 14px;
            }

            QLineEdit {
                background-color: #1e1e1e;
                border: 1px solid #333;
                padding: 8px;
                border-radius: 6px;
            }

            QLineEdit:focus {
                border: 1px solid #4da3ff;
            }

            QLabel#title {
                font-size: 28px;
                font-weight: bold;
            }

            QLabel#desc {
                color: #aaaaaa;
            }
        """)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = LoginForm()
    window.show()
    sys.exit(app.exec())