#Filippo Zallocco
#CS612
#March 25, 2023
#Python code for xml parses and xsd validation, part three of the third assignment

#Install xmlschema package through pip install xmlschema

from xml.dom import minidom
import xmlschema

doc = minidom.parse("movie.xml")

#movie = doc.getElementsByTagName()

movies = doc.getElementsByTagName("movie")

for movie in movies:
        Movie_id = movie.getAttribute("id")
        Title = movie.getElementsByTagName("title")[0]
        Format = movie.getElementsByTagName("format")[0]
        Genre = movie.getElementsByTagName("genre")[0]
        Director = movie.getElementsByTagName("director")[0]
        print(f"id: {Movie_id} title: {Title.firstChild.data} format: {Format.firstChild.data} genre: {Genre.firstChild.data} director: {Director.firstChild.data} \n")


xmlschema.validate('movie.xml', 'movie.xsd')

#To write the code to parse xml files and validate them against xml schemas, I resorted to import the xml and xmlschema libraries following the resources below:
#https://www.geeksforgeeks.org/parsing-xml-with-dom-apis-in-python/
#https://stackoverflow.com/questions/299588/validating-with-an-xml-schema-in-python
#https://pypi.org/project/xmlschema/

    