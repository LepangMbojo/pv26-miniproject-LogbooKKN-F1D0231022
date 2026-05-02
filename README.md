# Sistem Manajemen Tugas KKN 🎓

Aplikasi desktop berbasis Python untuk mengelola, mencatat, dan memantau kegiatan Kuliah Kerja Nyata (KKN). Dibangun dengan menggunakan framework GUI **PySide6 (Qt for Python)** dan **SQLite** sebagai basis data lokal.

Aplikasi ini dirancang dengan arsitektur *Separation of Concerns* (SoC) di mana antarmuka pengguna (UI), logika basis data, dan gaya visual (Styling) dipisahkan ke dalam modul yang berbeda untuk kemudahan pemeliharaan dan pengembangan.

## 🚀 Fitur Utama

Aplikasi ini memenuhi berbagai standar pengembangan antarmuka desktop:
- **Operasi CRUD Lengkap:** Tambah, Baca, Perbarui, dan Hapus data kegiatan KKN.
- **Form Input Terstruktur:** Terdapat 6 field input yang komprehensif (Nama Kegiatan, Lokasi, Tanggal, Penanggung Jawab, Status, dan Deskripsi) dalam jendela dialog terpisah (`QDialog`).
- **Data Persistence:** Terintegrasi dengan SQLite sehingga data tidak hilang saat aplikasi ditutup.
- **Tampilan Interaktif:** Menggunakan `QTableWidget` yang rapi dan responsif.
- **Keamanan Aksi:** Dilengkapi dengan `QMessageBox` sebagai dialog konfirmasi sebelum menghapus data.
- **Menu Bar Fungsional:** Menyediakan akses cepat ke informasi aplikasi melalui Menu Bar.
- **Custom Styling:** Desain antarmuka dimodifikasi menggunakan file eksternal `style.qss`.

## 📁 Struktur Proyek (Separation of Concerns)
```text
kkn_manager/
│
├── main.py            # Entry point aplikasi & inisialisasi gaya (QSS)
├── database.py        # Modul pengelola koneksi dan query SQLite
├── ui_main.py         # Controller & UI untuk jendela utama (Main Window)
├── ui_dialog.py       # Controller & UI untuk dialog form input
├── style.qss          # File eksternal stylesheet (CSS untuk Qt)
└── README.md          # Dokumentasi proyek
