import docx as _readFile
from docx2python import docx2python
from docx2python.iterators import get_text

""" DOCX İLE YAZDIKLARIM"""


def read_paragraph(filename):  # return value is an list example [EMRE ARGANA]
    doc = _readFile.Document(filename)
    return [p.text for p in doc.paragraphs]


"""DOCX2PYTHON İLE YAZDIKLARIM"""


def file_save_image(filename, image_folder):
    doc = docx2python(filename, image_folder)
    return doc.properties


def file_properties(filename):
    doc = docx2python(filename)
    return doc.properties


# includes/file_header.html de kontrolu yapıldı
def file_header(filename):
    doc = docx2python(filename)
    return doc.header


# Dönüş türü [] list
def file_footer(filename):
    doc = docx2python(filename)
    return doc.footer


# Dönüş türü [] list
# genelde bütün data bu kısımda oluyor
# html ile parde ederek yapıyorum
def file_body(filename):
    doc = docx2python(filename)
    return doc.body
    # print('body', doc.body[0][0][0][1])
