import sqlite3
import pickle  # For serializing and deserializing embeddings

# Initialize SQLite database
conn = sqlite3.connect('cms.db',check_same_thread=False)
cursor = conn.cursor()

# Create table for storing files and their metadata
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

# Save file metadata, including serialized embedding
def save_file_metadata(filename, text, embedding, categories):
    # Serialize the embedding list into a bytes object
    serialized_embedding = pickle.dumps(embedding)
    cursor.execute('''
    INSERT INTO files (filename, text, embedding, categories)
    VALUES (?, ?, ?, ?)
    ''', (filename, text, serialized_embedding, ",".join(categories)))
    conn.commit()

# Retrieve file metadata by index
def get_file_by_index(index):
    cursor.execute('''
    SELECT filename, text, embedding, categories FROM files WHERE id = ?
    ''', (index + 1,))
    result = cursor.fetchone()
    if result:
        filename, text, serialized_embedding, categories = result
        # Deserialize the embedding back into a list
        embedding = pickle.loads(serialized_embedding)
        return filename, text, embedding, categories.split(",")
    return None
