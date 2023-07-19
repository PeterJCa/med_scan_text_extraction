from pdf2image import convert_from_path
import pytesseract
import util

from parser_prescription import PrescriptionParser
from parser_patient_details import PatientDetailsParser


pytesseract.pytesseract.tesseract_cmd=r'G:\Program Files\Tesseract-OCR\tesseract.exe'
POPPLER_PATH = r'G:\poppler-23.07.0\Library\bin'

def extract(file_path, file_format):
    # extract text from pdf file
    pages = convert_from_path(file_path, poppler_path=POPPLER_PATH)
    document_text = ''

    for page in pages:
        processed_imaage = util.preprocess_image(page)
        text = pytesseract.image_to_string(processed_imaage, lang='eng')
        document_text += '\n' + text

    # extract fields from text
    if file_format == 'prescription':
        extracted_data = PrescriptionParser(document_text).parse()
    elif file_format == 'patient_details':
        extracted_data = PatientDetailsParser(document_text).parse()
    else:
        raise Exception(f"Invalid document format: {file_format}")
    return extracted_data

if __name__ == "__main__":
    data = extract(r'backend\resources\prescription\pre_1.pdf', 'prescription')
    print(data)