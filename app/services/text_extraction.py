
from PyPDF2 import PdfReader

import re
# from nltk.tokenize import word_tokenize

def preprocess_text(text):
    text  = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # Remove URLs
    text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
    text = re.sub(r'[^A-Za-z0-9.,!?;:\'\"]+', ' ', text)  # Remove special characters
    text = re.sub(r'\s+',' ', text).strip()  # Remove extra whitespaces
    return text

def extract_text_from_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in range(len(reader.pages)):
            text += preprocess_text(reader.pages[page].extract_text())
        return text
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {e}")