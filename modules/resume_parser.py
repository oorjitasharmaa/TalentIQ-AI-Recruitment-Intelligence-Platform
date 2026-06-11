from pypdf import PdfReader
from docx import Document
import os


# =========================
# EXTRACT TEXT FROM PDF
# =========================

def extract_text_from_pdf(file_path):

    text = ""

    try:
        reader = PdfReader(file_path)

        for page in reader.pages:
            text += page.extract_text() + "\n"

    except Exception as e:
        print(f"Error reading PDF: {e}")

    return text


# =========================
# EXTRACT TEXT FROM DOCX
# =========================

def extract_text_from_docx(file_path):

    text = ""

    try:
        doc = Document(file_path)

        for para in doc.paragraphs:
            text += para.text + "\n"

    except Exception as e:
        print(f"Error reading DOCX: {e}")

    return text


# =========================
# MAIN RESUME PARSER
# =========================

def parse_resume(file_path):

    extension = os.path.splitext(file_path)[1]

    if extension == ".pdf":
        return extract_text_from_pdf(file_path)

    elif extension == ".docx":
        return extract_text_from_docx(file_path)

    else:
        return "Unsupported File Format"