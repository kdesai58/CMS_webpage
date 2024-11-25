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
    text TEXT
)
''')
conn.commit()

# Save file metadata, including serialized embedding
def save_file_metadata(filename, text):
    cursor.execute('''
    INSERT INTO documents (filename, text)
    VALUES (?, ?)
    ''', (filename, text))
    conn.commit()
    return cursor.lastrowid

def get_metadata_by_id(doc_id):
    # Assuming doc_id is the FAISS index (1-based indexing for the database)
    cursor.execute("SELECT * FROM documents WHERE id = ?", (doc_id,))
    metadata = cursor.fetchone()
    # print(f"Fetched metadata for doc_id {doc_id}: {metadata}")
    return metadata

def get_all_files():
    """Retrieve all file metadata."""
    cursor.execute('SELECT id, filename, text FROM documents')
    return cursor.fetchall()