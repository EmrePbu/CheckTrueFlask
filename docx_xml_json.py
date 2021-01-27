import json
import xmltodict
from docx_utils.flatten import opc_to_flat_opc


def DocToXmlToJson(docxFile):
    opc_to_flat_opc(docxFile, "./temp/temporary.xml")
    # Program to convert an xml
    # file to json file
    # import json module and xmltodict
    # module provided by python
    # open the input xml file and read
    # data in form of python dictionary
    # using xmltodict module
    with open("./temp/temporary.xml", encoding='utf-8') as xml_file:

        data_dict = xmltodict.parse(xml_file.read())
        xml_file.close()

        # generate the object using json.dumps()
        # corresponding to json data

        json_data = json.dumps(data_dict, ensure_ascii=False, indent=4)

        # Write the json data to output
        # json file
        with open('./buffer/result.json', 'w', encoding='utf-8') as json_file:
            json_file.write(json_data)
            print("done!")
