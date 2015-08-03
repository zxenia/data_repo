__author__ = 'Ksenia'

import spotlight
import os, re

#import pickle

import xml.dom.minidom
from xml.dom.minidom import Node
from xml.dom.minidom import parse, parseString

import io, json

data_to_process = xml.dom.minidom.parse(r'C:\Users\kzaytseva\Documents\Repos\pyckathon\APIS-extraction\sample_data\OEBL_XML-Daten\Aberle_Karl_1818_1892.xml')
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


pi = json.dumps(annotations, sort_keys=True, indent=4, separators=(', ', ': '))
#print(annotations)


print(pi)

pi = open('test_haupttext.html', 'w') #writing output in html file

#out_string = str(annotations) #convering annotations value to string

#myfile. write(out_string + '\n')

#out = json.dump(annotations, myfile, sort_keys = True, indent = 4, )

#myfile.write(out + '\n')

pi.close()


#for item in annotations:
    #myfile.write(str(item) + '\n')
#myfile.close()







