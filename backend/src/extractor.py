from pdf2image import convert_from_path
import pytesseract
import util
import os

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
    return document_text

    # if file_format == 'prescription':
    #     pass # extract data from prescription
    # elif file_format == 'patient_details':
    #     pass  # extract data from patien details

if __name__ == "__main__":
    data = extract(r'backend\resources\patient_details\pd_1.pdf', 'prescription')
    print(data)
    print(os.getcwd())