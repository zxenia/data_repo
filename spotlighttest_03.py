__author__ = 'Ksenia'

import spotlight
import os, re

import xml.dom.minidom
from xml.dom.minidom import Node
from xml.dom.minidom import parse, parseString

data_to_process = xml.dom.minidom.parse(r'C:\Users\Ksenia\Desktop\OEBL_XML-Daten\Aberle_Karl_1818_1892.xml')
#variable to process xml file

topic = data_to_process.getElementsByTagName('Lexikonartikel')
i = 0
Value = ''
for node in topic:
    get_tag = node.getElementsByTagName('Haupttext')
    for a in get_tag:
        Value = Value + a.firstChild.data
        print(Value)

annotations = spotlight.annotate('http://spotlight.dbpedia.org/rest/annotate', Value, confidence=0.2, support=20)

myfile = open('haupttext_spot.html', 'w')
for item in annotations:
    myfile.write(str(item) + '\n')
myfile.close()







