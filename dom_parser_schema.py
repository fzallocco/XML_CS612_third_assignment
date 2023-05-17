#Filippo Zallocco
#CS612
#March 25, 2023
#Python code for xml parsing and xsd validation, part three of the third assignment

import xmlschema

movie = xmlschema.validate(r'C:\Users\filiz\OneDrive\Desktop\Pace\CS612\week8\xml\movie.xml', r'C:\Users\filiz\OneDrive\Desktop\Pace\CS612\week8\xml\movie.xsd')

print(f"Errors of xml and xml-schema parsing: {movie}")