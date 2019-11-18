import  sys
import sqlite3
from PyQt5 import QtWidgets


class Pencere(QtWidgets.QWidget):

    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):

        self.lblad = QtWidgets.QLabel("Adı")
        self.kullanici_adi = QtWidgets.QLineEdit()

        self.lblsoyad = QtWidgets.QLabel("Soyadı")
        self.soyad = QtWidgets.QLineEdit()

        self.lblparola = QtWidgets.QLabel("Parola")
        self.parola = QtWidgets.QLineEdit()

        self.parola.setEchoMode(QtWidgets.QLineEdit.Password)
        self.giris = QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani = QtWidgets.QLabel("deneme")

        v_box = QtWidgets.QVBoxLayout()
        v_box.addWidget(self.lblad)
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.lblsoyad)
        v_box.addWidget(self.soyad)
        v_box.addWidget(self.lblparola)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        h_box = QtWidgets.QHBoxLayout()
        h_box.addStretch()
        h_box.addLayout(v_box)
        h_box.addStretch()
        self.setLayout(h_box)
        self.setWindowTitle("Kullanıcı Girişi")
        self.giris.clicked.connect(self.login)
        self.show()

    def login(self):

        adi = self.kullanici_adi.text()
        par = self.parola.text()

        self.yazi_alani.setText("butona tıklandı"+adi)


app = QtWidgets.QApplication(sys.argv)

pencere = Pencere()

sys.exit(app.exec_())
