import fitz  # PyMuPDF
import docx2txt

def extract_text(file_path):
    if file_path.endswith('.pdf'):
        text = ""
        doc = fitz.open(file_path)
        for page in doc:
            text += page.get_text()
        return text
    elif file_path.endswith('.docx'):
        return docx2txt.process(file_path)
    else:
        return ""
