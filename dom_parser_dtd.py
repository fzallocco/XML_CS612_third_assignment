#Filippo Zallocco
#CS612
#March 25, 2023
#Python code for xml parsing and dtd validation, part three of the third assignment

from lxml import etree

parser = etree.XMLParser(dtd_validation=True)
parser_result = etree.parse(r"C:\Users\filiz\OneDrive\Desktop\Pace\CS612\week8\xml\movie.xml", parser)

#To write the code to parse xml files and validate them against the dtd files, I resorted to import the xml and lxml libraries and their objects minidom and etree following the resources below:
#https://www.geeksforgeeks.org/parsing-xml-with-dom-apis-in-python/
#https://stackoverflow.com/questions/31769514/how-do-i-validate-xml-against-dtd-using-python
