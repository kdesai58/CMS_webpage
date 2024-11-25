import sqlite3
import pickle  # For serializing and deserializing embeddings

# Initialize SQLite database
conn = sqlite3.connect('cms.db',check_same_thread=False)
cursor = conn.cursor()

# Create table for storing files and their metadata
cursor.execute('''
CREATE TABLE IF NOT EXISTS documents (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    filename TEXT,
    categories TEXT,
    embedding_id INTEGER
)
''')
conn.commit()

# Save file metadata, including serialized embedding
def save_file_metadata(filename, categories, embedding_id):
    cursor.execute('''
    INSERT INTO documents (filename, categories, embedding_id)
    VALUES (?, ?, ?)
    ''', (filename, ",".join(categories), embedding_id))
    conn.commit()

def get_metadata_by_id(doc_id):
    cursor.execute('''
    SELECT filename, categories FROM documents WHERE id = ?
    ''', (doc_id,))
    return cursor.fetchone()