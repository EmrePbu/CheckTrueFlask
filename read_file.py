from metric_converter import Metric
import docx as _readFile
from docx2python import docx2python

""" DOCX İLE YAZDIKLARIM"""
# sections = doc.sections
# for i in sections:
#    print(i.start_type)


def read_paragraph(filename):
    """
    ENGLISH:
        Returns each paragraph in the file as a sequence.
    TÜRKÇE:
        Dosyadaki her bir paragrafı bir dizi olarak geri döndürür.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns each line in the given file as a string.
        TÜRKÇE:
            Verilen dosyadaki her bir satırı dizi şeklinde geri döndürür.
    """
    doc = _readFile.Document(filename)
    return [p.text for p in doc.paragraphs]


# None left oluyor standart olan
# eğer None ve i.text i null ise enter tuşu oluyor alt satıra geçmek
# CENTER (1)
# RIGHT (2)
# JUSTIFY (3)
def read_alignment(filename):
    """
    ENGLISH:
        It is used to find the alignment values of each paragraph in the file.
    TÜRKÇE:
        Dosyadaki her bir paragrafın hizalama değerlerini bulmaya yarar.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns the alignment values as a dictionary data structure.
        TÜRKÇE:
            Hizalama değerlerini sözlük veri yapısı şeklinde geri döndürür.
        `mainAlignmentArray['alignment']`
        `mainAlignmentArray['text']`
    """
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


def read_page_structure(filename):
    """
    ENGLISH:
        It is used to find the margin values of each paragraph in the file.
    TÜRKÇE:
        Dosyadaki her bir paragrafın kenar boşluk değerlerini bulmaya yarar.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns the margin values as a dictionary data structure.
        TÜRKÇE:
            Kenar boşluk değerlerini sözlük veri yapısı şeklinde geri döndürür.
        `mainMarginArray['top']`
        `mainMarginArray['right']`
        `mainMarginArray['bottom']`
        `mainMarginArray['left']`
        `mainMarginArray['portrait']`
    """
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


def read_alignment_and_indent(filename):
    """
    ENGLISH:
        It is used to find the indent values of each paragraph in the file.
    TÜRKÇE:
        Dosyadaki her bir paragrafın girinti değerlerini bulmaya yarar.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns the indent values as a dictionary data structure.
        TÜRKÇE:
            Girinti değerlerini sözlük veri yapısı şeklinde geri döndürür.
        `read_alignment_and_indent['left']`
        `read_alignment_and_indent['right']`
    """
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
    """
    ENGLISH:
        It is a method that provides access to file properties.
    TÜRKÇE:
        Dosya özelliklerine ulaşmayı sağlayan metoddur.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns a dictionary data structure containing file properties.
        TÜRKÇE:
            Dosya özelliklerini içeren bir sözlük veri yapısı döndürür.
    """
    doc = docx2python(filename)
    return doc.properties


def file_header(filename):
    """
    ENGLISH:
        It is the method that provides access to the header of the file.
    TÜRKÇE:
        Dosyanın üst başlığını ulaşmayı sağlayan metoddur.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns a TablesList containing file properties.
        TÜRKÇE:
            Dosya özelliklerini içeren bir TablesList döndürür.
    """
    doc = docx2python(filename)
    return doc.header


def file_footer(filename):
    """
    ENGLISH:
        It is the method that provides access to the footer of the file.
    TÜRKÇE:
        Dosyanın alt başlığını ulaşmayı sağlayan metoddur.
    \nArgs:
        filename (str):
            ENGLISH:
                File path.
            TÜRKÇE:
                Dosya yolu.
    \nReturns:
        str:
        ENGLISH:
            Returns a TablesList containing file properties.
        TÜRKÇE:
            Dosya özelliklerini içeren bir TablesList döndürür.
    """
    doc = docx2python(filename)
    return doc.footer


# Dönüş türü [] list
# genelde bütün data bu kısımda oluyor
def file_body(filename):
    doc = docx2python(filename)
    return doc.body
    # print('body', doc.body[0][0][0][1])
