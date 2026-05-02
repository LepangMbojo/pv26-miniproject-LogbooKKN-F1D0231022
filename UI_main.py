from PySide6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, 
                               QPushButton, QTableWidget, QTableWidgetItem, 
                               QLabel, QMessageBox, QHeaderView)
from PySide6.QtGui import QAction
from Database import Database
from UI_dialog import TaskDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Sistem Manajemen Tugas KKN")
        self.resize(800, 500)
        
        self.db = Database()

        menu_bar = self.menuBar()
        menu_bar.setNativeMenuBar(False) 
        tentang_action = QAction("Tentang Aplikasi", self)
        tentang_action.triggered.connect(self.show_about)
        menu_bar.addAction(tentang_action)

        # layoutUtama
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        self.main_layout = QVBoxLayout(central_widget)

        # LabelIdentitas
        self.identitas_label = QLabel("Nama: M. Khalid Al Rejeki | NIM: F1D02310122")
        self.identitas_label.setObjectName("identitasLabel")
        self.main_layout.addWidget(self.identitas_label)

        # TabelData
        self.table = QTableWidget()
        self.table.setColumnCount(7)
        self.table.setHorizontalHeaderLabels(["ID", "Nama Kegiatan", "Lokasi", "Tanggal", "PJ", "Status", "Deskripsi"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.main_layout.addWidget(self.table)

        # TombolAction
        self.btn_layout = QHBoxLayout()
        self.btn_tambah = QPushButton("Tambah Kegiatan")
        self.btn_hapus = QPushButton("Hapus Kegiatan Terpilih")
        self.btn_edit = QPushButton("Edit Kegiatan Terpilih")
        
        self.btn_layout.addWidget(self.btn_tambah)
        self.btn_layout.addWidget(self.btn_hapus)
        self.btn_layout.addWidget(self.btn_edit)
        self.main_layout.addLayout(self.btn_layout)

        # signalSlot
        self.btn_tambah.clicked.connect(self.open_add_dialog)
        self.btn_hapus.clicked.connect(self.delete_task)
        self.btn_edit.clicked.connect(self.open_edit_dialog)

        # LoadData
        self.load_data()

    def load_data(self):
        self.table.setRowCount(0)
        tasks = self.db.get_all_tasks()
        for row_idx, task in enumerate(tasks):
            self.table.insertRow(row_idx)
            for col_idx, data in enumerate(task):
                self.table.setItem(row_idx, col_idx, QTableWidgetItem(str(data)))

    def open_add_dialog(self):
        dialog = TaskDialog(self)
        if dialog.exec(): 
            data = dialog.get_data()
            if data[0]:  
                self.db.insert_task(data)
                self.load_data()
            else:
                QMessageBox.warning(self, "Peringatan", "Nama Kegiatan tidak boleh kosong!")

    def delete_task(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih kegiatan yang ingin dihapus terlebih dahulu!")
            return

        task_id = self.table.item(current_row, 0).text()
        
        reply = QMessageBox.question(self, 'Konfirmasi Hapus', 
                                     "Apakah Anda yakin ingin menghapus kegiatan ini?",
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            self.db.delete_task(task_id)
            self.load_data()


    def open_edit_dialog(self):
        current_row = self.table.currentRow()
        if current_row < 0:
            QMessageBox.warning(self, "Peringatan", "Pilih kegiatan yang ingin diedit terlebih dahulu!")
            return

        task_id = self.table.item(current_row, 0).text()
        
        current_data = (
            self.table.item(current_row, 1).text(),
            self.table.item(current_row, 2).text(),
            self.table.item(current_row, 3).text(), 
            self.table.item(current_row, 4).text(),
            self.table.item(current_row, 5).text(), 
            self.table.item(current_row, 6).text()  
        )

        dialog = TaskDialog(self)
        dialog.setWindowTitle("Edit Kegiatan KKN")
        dialog.set_data(current_data)

        if dialog.exec():
            new_data = dialog.get_data()
            if new_data[0]:  
                self.db.update_task(task_id, new_data) 
                self.load_data() 
                QMessageBox.information(self, "Sukses", "Data berhasil diperbarui!")
            else:
                QMessageBox.warning(self, "Peringatan", "Nama Kegiatan tidak boleh kosong!")
    def show_about(self):
        QMessageBox.information(self, "Tentang Aplikasi", 
                                "Sistem Manajemen Tugas KKN\n\n"
                                "Dibuat oleh M. Khalid Al Rejeki (F1D02310122)\n"
                                "Aplikasi ini digunakan untuk mengelola kegiatan KKN, termasuk menambah, mengedit, dan menghapus tugas.")