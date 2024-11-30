
from PyPDF2 import PdfReader
import fitz

import re

# from nltk.tokenize import word_tokenize

# def preprocess_text(text):
#     text  = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)  # Remove URLs
#     text = re.sub(r'<.*?>', '', text)  # Remove HTML tags
#     text = re.sub(r'[^A-Za-z0-9.,!?;:\'\"]+', ' ', text)  # Remove special characters
#     text = re.sub(r'\s+',' ', text).strip()  # Remove extra whitespaces
#     return text

def extract_text_from_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
            # print(text)
        return text
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {e}")
        # text += preprocess_text(doc[page].get_text())

# def extract_text_from_pdf(file_path):
#     try:
#         reader = PdfReader(file_path)
#         text = ""
#         for page in range(len(reader.pages)):
#             text += reader.pages[page].extract_text()
#             # text += preprocess_text(reader.pages[page].extract_text())
#         return text
#     except Exception as e:
#         raise ValueError(f"Error extracting text from PDF: {e}")