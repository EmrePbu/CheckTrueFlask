from metric_converter import Metric
import docx as _readFile
from docx2python import docx2python

""" DOCX İLE YAZDIKLARIM"""
#sections = doc.sections
# for i in sections:
#    print(i.start_type)


def read_paragraph(filename):  # return value is an list example [EMRE ARGANA]
    doc = _readFile.Document(filename)
    return [p.text for p in doc.paragraphs]


# None left oluyor standart olan
# eğer None ve i.text i null ise enter tuşu oluyor alt satıra geçmek
#CENTER (1)
#RIGHT (2)
#JUSTIFY (3)
def read_alignment(filename):
    mainAlignmentArray = {}
    paragraphAlignmentArray = []
    paragraphTextArray = []
    doc = _readFile.Document(filename)
    paragraph = doc.paragraphs
    for i in paragraph:
        paragraphAlignmentArray.append(i.paragraph_format.alignment)
        paragraphTextArray.append(i.text)
    mainAlignmentArray['alignment'] = paragraphAlignmentArray
    mainAlignmentArray['text'] = paragraphTextArray
    return mainAlignmentArray


def read_margin(filename):
    mainMarginArray = {}
    topMarginArray = []
    rightMarginArray = []
    bottomMarginArray = []
    leftMarginArray = []
    portraitMarginArray = []
    doc = _readFile.Document(filename)
    sections = doc.sections
    for i in sections:
        if(str(i.start_type) == 'NEW_PAGE (2)'):
            if(str(i.orientation) == 'PORTRAIT (0)'):
                portraitMarginArray.append('Dikey')
            if(str(i.orientation) == 'LANDSCAPE (1)'):
                portraitMarginArray.append('Yatay')
            topMarginArray.append(round(Metric.emuToCm(i.top_margin), 2))
            rightMarginArray.append(round(Metric.emuToCm(i.right_margin), 2))
            bottomMarginArray.append(round(Metric.emuToCm(i.bottom_margin), 2))
            leftMarginArray.append(round(Metric.emuToCm(i.left_margin), 2))
    mainMarginArray['top'] = topMarginArray
    mainMarginArray['right'] = rightMarginArray
    mainMarginArray['bottom'] = bottomMarginArray
    mainMarginArray['left'] = leftMarginArray
    mainMarginArray['portrait'] = portraitMarginArray
    return mainMarginArray


def read_indent(filename):
    mainIndentArray = {}
    leftIndent = []
    rightIndent = []
    doc = _readFile.Document(filename)
    indent = doc.paragraphs
    for i in indent:
        leftIndent.append(round(Metric.emuToCm(
            i.paragraph_format.left_indent), 2))
        rightIndent.append(round(Metric.emuToCm(
            i.paragraph_format.right_indent), 2))
    mainIndentArray['left'] = leftIndent
    mainIndentArray['right'] = rightIndent
    return mainIndentArray


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
