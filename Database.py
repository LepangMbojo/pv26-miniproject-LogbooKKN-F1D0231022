import sqlite3

class Database:
    def __init__(self, db_name="kkn_tasks.db"):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nama_kegiatan TEXT,
                lokasi TEXT,
                tanggal TEXT,
                penanggung_jawab TEXT,
                status TEXT,
                deskripsi TEXT
            )
        """)
        self.conn.commit()

    def insert_task(self, data):
        self.cursor.execute("""
            INSERT INTO tasks (nama_kegiatan, lokasi, tanggal, penanggung_jawab, status, deskripsi)
            VALUES (?, ?, ?, ?, ?, ?)
        """, data)
        self.conn.commit()

    def get_all_tasks(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()

    def delete_task(self, task_id):
        self.cursor.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
        self.conn.commit()
    
    def update_task(self, task_id, data):
        query = """
            UPDATE tasks
            SET nama_kegiatan = ?, lokasi = ?, tanggal = ?, penanggung_jawab = ?, status = ?, deskripsi = ?
            WHERE id = ?
        """

        parameters = (*data, task_id)
        self.cursor.execute(query, parameters)
        self.conn.commit()