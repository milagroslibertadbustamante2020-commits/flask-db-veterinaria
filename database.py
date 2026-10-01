import sqlite3

def conectar():
    conn = sqlite3.connect("veterinaria.db")
    conn.row_factory = sqlite3.Row
    return conn

def crear_tablas():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS mascotas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            especie TEXT NOT NULL,
            fecha_nacimiento TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS veterinarios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            especialidad TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS consultas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha TEXT NOT NULL,
            mascota_id INTEGER,
            veterinario_id INTEGER,
            FOREIGN KEY (mascota_id) REFERENCES mascotas(id),
            FOREIGN KEY (veterinario_id) REFERENCES veterinarios(id)
        )
    """)
    conn.commit()
    conn.close()