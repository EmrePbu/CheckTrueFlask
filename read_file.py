import docx as _readFile


# return value is an list example [EMRE ARGANA]
def read_paragraph(filename):
    doc = _readFile.Document(filename)
    return [p.text for p in doc.paragraphs]
