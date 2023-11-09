import xml.etree.ElementTree
import datetime

#import xml.etree.ElementTree

if __name__ == "__main__":
    try:
        with open('C:\Mironchik\king_corp.xml', mode='r', encoding='UTF-8') as xml_file:
            dom: xml.etree.ElementTree.ElementTree = xml.etree.ElementTree.parse(xml_file)
            for dept in dom.findall("./departments/department"):
                print(dept.attrib['id'], dept.find("name").text, dept.find("location").text)
                for emp in dept.findall("./employees/employee"):
                    print("XYI", emp.attrib['id'], emp.find('name').text,
                          emp.find('function').text,
                          datetime.datetime.strptime(emp.find('hire_date').text, '%Y-%m-%d'),
                          emp.find('salary').text
                          )

    except Exception as e:
        raise e