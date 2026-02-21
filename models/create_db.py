import sqlite3
import os

os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/db.sqlite3")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tipos_combustivel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT UNIQUE
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS pessoas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    categoria TEXT,
    equipe TEXT,
    tipo_combustivel INTEGER,
    cota_mensal REAL
)
""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS entregas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    pessoa_id INTEGER,
    data TEXT,
    quantidade REAL,
    observacao TEXT
)
""")

cursor.execute("INSERT OR IGNORE INTO tipos_combustivel VALUES (1,'Gasolina')")
cursor.execute("INSERT OR IGNORE INTO tipos_combustivel VALUES (2,'Diesel')")

conn.commit()
conn.close()

print("Banco criado com sucesso.")