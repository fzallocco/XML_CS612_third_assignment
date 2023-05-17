# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 15:55:58 2023

@author: filiz
"""

from lxml import etree

def validate(xml_path: str, xsd_path: str) -> bool:

    xmlschema_doc = etree.parse(xsd_path)
    xmlschema = etree.XMLSchema(xmlschema_doc)

    xml_doc = etree.parse(xml_path)
    result = xmlschema.validate(xml_doc)

    return result