import xml.etree.ElementTree

if __name__ == "xml":
    try:
        with open('C:\code\contextMenu.xml', mode='r', encoding="UTF-8") as xml_in_file:
            #xml.etree.ElementTree.ElementTree.parse(xml_in_file)
            dom:xml.etree.ElementTree.ElementTree = xml.etree.ElementTree.ElementTree.parse('xml_in_file')
            print('ok')
    except Exception as e:
        raise e