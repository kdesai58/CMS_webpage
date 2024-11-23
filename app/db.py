import sqlite3

conn = sqlite3.connect('cms.db')
cursor = conn.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    text TEXT,
    embedding BLOB,
    categories TEXT
)
''')
conn.commit()

def save_file_metadata(filename, text, embedding, categories):
    cursor.execute('''
    INSERT INTO files (filename, text, embedding, categories)
    VALUES (?, ?, ?, ?)
    ''', (filename, text, sqlite3.Binary(embedding), ",".join(categories)))
    conn.commit()

def get_file_by_index(index):
    cursor.execute('''
    SELECT filename, text, categories FROM files WHERE id = ?
    ''', (index+1,))
    return cursor.fetchone()