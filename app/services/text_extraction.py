# import fitz

# def extract_text_from_pdf(pdf_path):
#     pdf = fitz.open(pdf_path)
#     text = ""
#     for page in pdf:
#         text += page.get_text()
#     pdf.close()
#     return text

from PyPDF2 import PdfReader

def extract_text_from_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        return text
    except Exception as e:
        raise ValueError(f"Error extracting text from PDF: {e}")