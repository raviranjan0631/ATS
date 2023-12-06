from PyPDF2 import PdfReader

def get_text_from_pdf(file_name):
    ''' return text from a pdf file from all of its page'''
    reader =  PdfReader(file_name)

    text = ''
    for i in range(len(reader.pages)):
        page = reader.pages[i]
        text += page.extract_text() + '\n'

    return text

