# importing required libraries
import fitz

# function to extract text from PDF 
def extract_text_from_pdf(file_path):
    try:
        doc = fitz.open(file_path)
        text = ""
        for page_num in range(len(doc)):
            page = doc.load_page(page_num)
            text += page.get_text()
        return text
    except Exception as e:  # Handle exceptions
        raise ValueError(f"Error extracting text from PDF: {e}")