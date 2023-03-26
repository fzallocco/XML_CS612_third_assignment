#Filippo Zallocco
#CS612
#March 25, 2023
#Python code for xml parses and dtd validation, part three of the third assignment
from xml.dom import minidom
from lxml import etree

doc = minidom.parse("movie.xml")

movies = doc.getElementsByTagName("movie")

for movie in movies:
        Movie_id = movie.getAttribute("id")
        Title = movie.getElementsByTagName("title")[0]
        Format = movie.getElementsByTagName("format")[0]
        Genre = movie.getElementsByTagName("genre")[0]
        Director = movie.getElementsByTagName("director")[0]
        print(f"id: {Movie_id} title: {Title.firstChild.data} format: {Format.firstChild.data} genre: {Genre.firstChild.data} director: {Director.firstChild.data} \n")

parser = etree.XMLParser(dtd_validation=True)
tree = etree.parse("movie.xml", parser)

#To write the code to parse xml files and validate them against the dtd files, I resorted to import the xml and lxml libraries and their objects minidom and etree following the resources below:
#https://www.geeksforgeeks.org/parsing-xml-with-dom-apis-in-python/
#https://stackoverflow.com/questions/31769514/how-do-i-validate-xml-against-dtd-using-python
