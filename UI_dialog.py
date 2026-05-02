from PySide6.QtWidgets import (QDialog, QVBoxLayout, QFormLayout, QLineEdit, 
                               QDateEdit, QComboBox, QTextEdit, QPushButton, QHBoxLayout)
from PySide6.QtCore import QDate

class TaskDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Tambah Kegiatan KKN")
        self.setMinimumWidth(400)

        # Layout
        self.main_layout = QVBoxLayout(self)
        self.form_layout = QFormLayout()

        # Inputdata
        self.input_nama = QLineEdit()
        self.input_lokasi = QLineEdit()
        
        self.input_tanggal = QDateEdit()
        self.input_tanggal.setCalendarPopup(True)
        self.input_tanggal.setDate(QDate.currentDate())
        
        self.input_pj = QLineEdit()
        
        self.input_status = QComboBox()
        self.input_status.addItems(["Belum Mulai", "Sedang Berjalan", "Selesai"])
        
        self.input_deskripsi = QTextEdit()

        #layoutAwalForm
        self.form_layout.addRow("Nama Kegiatan:", self.input_nama)
        self.form_layout.addRow("Lokasi:", self.input_lokasi)
        self.form_layout.addRow("Tanggal:", self.input_tanggal)
        self.form_layout.addRow("Penanggung Jawab:", self.input_pj)
        self.form_layout.addRow("Status:", self.input_status)
        self.form_layout.addRow("Deskripsi:", self.input_deskripsi)

        # Tombol 
        self.btn_layout = QHBoxLayout()
        self.btn_simpan = QPushButton("Simpan")
        self.btn_batal = QPushButton("Batal")
        
        self.btn_layout.addWidget(self.btn_simpan)
        self.btn_layout.addWidget(self.btn_batal)

        self.main_layout.addLayout(self.form_layout)
        self.main_layout.addLayout(self.btn_layout)

        # signalSlot
        self.btn_simpan.clicked.connect(self.accept)
        self.btn_batal.clicked.connect(self.reject)

    def get_data(self):
        return (
            self.input_nama.text(),
            self.input_lokasi.text(),
            self.input_tanggal.date().toString("yyyy-MM-dd"),
            self.input_pj.text(),
            self.input_status.currentText(),
            self.input_deskripsi.toPlainText()
        )
    def set_data(self, data):
        self.input_nama.setText(data[0])
        self.input_lokasi.setText(data[1])
        self.input_tanggal.setDate(QDate.fromString(data[2], "yyyy-MM-dd"))
        self.input_pj.setText(data[3])
        self.input_status.setCurrentText(data[4])
        self.input_deskripsi.setPlainText(data[5])