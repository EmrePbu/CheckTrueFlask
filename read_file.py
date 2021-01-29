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


def read_margin(filename):
    mainArr = {}
    topArr = []
    rightArr = []
    bottomArr = []
    leftArr = []
    portraitArr = []
    doc = _readFile.Document(filename)
    sections = doc.sections
    for i in sections:
        if(str(i.start_type) == 'NEW_PAGE (2)'):
            # print(i.orientation)
            if(str(i.orientation) == 'PORTRAIT (0)'):
                portraitArr.append('Dikey')
            if(str(i.orientation) == 'LANDSCAPE (1)'):
                portraitArr.append('Yatay')

            topArr.append(round(Metric.emuToCm(i.top_margin), 2))
            rightArr.append(round(Metric.emuToCm(i.right_margin), 2))
            bottomArr.append(round(Metric.emuToCm(i.bottom_margin), 2))
            leftArr.append(round(Metric.emuToCm(i.left_margin), 2))
    mainArr['top'] = topArr
    mainArr['right'] = rightArr
    mainArr['bottom'] = bottomArr
    mainArr['left'] = leftArr
    mainArr['portrait'] = portraitArr

    # mainArr.append(topArr)
    # mainArr.append(rightArr)
    # mainArr.append(bottomArr)
    # mainArr.append(leftArr)
    return mainArr


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
