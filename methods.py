import json
import docx_xml_json as myMethods


myMethods.DocToXmlToJson(
    "./documents/5150rnek_Tez_O_Orhan_YL_Parametresiz.docx")


# Opening JSON file
with open("./buffer/result.json", encoding='utf-8-sig') as data_file:
    data = json.load(data_file)
    data_file.close()

arrSize = len(data["pkg:package"]["pkg:part"])-1


# Developer tools
def DataSave(data, fileName):
    """Summary
    Saves any given string, array, list, dict data as json.
    Args:
        data (dict): Data type can be json, dict, array, list.
        fileName (string): The name to save the data given
    """
    with open('./buffer/%s.json' % fileName, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def GetAllImages():
    """
    It enables all images in the docx file to be saved to the ./word/media folder.
    """
    arrLength = data["pkg:package"]["pkg:part"]
    for i in range(len(arrLength)):
        if (str(arrLength[i]["@pkg:contentType"]) == "image/png"):
            DataSave(arrLength[i], arrLength[i]["@pkg:name"])
    print("pictures were saved in the ./buffer/word/media file location.")


def GetAllFonts():
    """
    It ensures that all fonts used in the docx file are saved in the ./word folder.
    """
    arrLength = data["pkg:package"]["pkg:part"]
    for i in range(len(arrLength)):
        if ("word/fontTable.xml" == str(arrLength[i]["@pkg:name"])):
            DataSave(arrLength[i]["pkg:xmlData"]["w:fonts"]
                     ["w:font"], arrLength[i]["@pkg:name"])
    print("fonts were saved in the ./word/fontTable.xml.json file location.")


def GetBody():
    """
    Include the contents of the docx file saves in the ./word folder.
    """
    arrLength = data["pkg:package"]["pkg:part"]
    for i in range(len(arrLength)):
        if ("word/document.xml" == arrLength[i]["@pkg:name"]):
            DataSave(arrLength[i]["pkg:xmlData"]
                     ["w:document"]["w:body"], arrLength[i]["@pkg:name"])
    print("body were saved in the ./word/document.xml.json file location.")


def GetPageNumber():
    """Prints the number of pages of the docx file on the screen.

    Returns:
        int: Number of pages
    """
    arrLength = data["pkg:package"]["pkg:part"]
    for i in range(len(arrLength)):
        if ("word/document.xml" == str(arrLength[i]["@pkg:name"])):
            pageNumbers = arrLength[i]["pkg:xmlData"]["w:document"]["w:body"]["w:p"]
            return len(pageNumbers)
    print("Done!")


def GetPagesMargin():
    """
    Checks the margins of each page in the docx file. Returns a value as True or False.
    """
    defaultMarginDict = {'@w:top': '567',
                         '@w:right': '567',
                         '@w:bottom': '567',
                         '@w:left': '567',
                         '@w:header': '0',
                         '@w:footer': '0',
                         '@w:gutter': '0'
                         }
    arrLength = data["pkg:package"]["pkg:part"]
    try:
        for i in range(len(arrLength)):
            if ("word/document.xml" == str(arrLength[i]["@pkg:name"])):
                pages = arrLength[i]["pkg:xmlData"]["w:document"]["w:body"]["w:p"]
                for j in range(len(pages)):  # her bir sayfa
                    if(defaultMarginDict == pages[j]["w:pPr"]["w:sectPr"]["w:pgMar"]):
                        print(j+1, ". Page", True)
                    else:
                        print(j+1, ". Page", False)
    except KeyError as e:
        print("KeyError : ", e)
