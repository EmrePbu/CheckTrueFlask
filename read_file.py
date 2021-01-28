import docx as _readFile
from docx2python import docx2python
import os

# return value is an list example [EMRE ARGANA]


def read_paragraph(filename):
    doc = _readFile.Document(filename)
    return [p.text for p in doc.paragraphs]


def file_properties(filename):
    doc = docx2python(filename)
    return doc.properties
