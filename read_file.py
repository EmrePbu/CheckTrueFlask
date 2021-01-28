import docx as _readFile

# read in word file


# return value is an list example [EMRE ARGANA]
def read_file(filename):
    doc = _readFile.Document(filename)
    return [p.text for p in doc.paragraphs]
