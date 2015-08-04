__author__ = 'kzaytseva'

import os, re

import xml.dom.minidom

from xml.dom.minidom import parse, parseString
from xml.dom.minidom import Node, NodeList
from xml.dom.minidom import Text

import spotlight
import  io, json

mywd = os.chdir(r'C:\Users\kzaytseva\Documents\Repos\pyckathon\APIS-extraction\sample_data\OEBL_XML-Daten') #Return a list containing the names of the entries in the directory given by path.

#mywd = os.chdir(r'C:\Users\kzaytseva\Documents\Repos\pyckathon\APIS-extraction\sample_data\OEBL_XML-Daten')
Value = ''

for file in os.listdir(os.getcwd()):
    data_to_process = xml.dom.minidom.parse(file)
    topic = data_to_process.getElementsByTagName('Lexikonartikel')
    i = 0

    for node in topic:
        get_bytag = node.getElementsByTagName('Haupttext')

        for a in get_bytag:
            Value = Value + a.firstChild.data + '\n'
            print(Value)


annotations = spotlight.annotate('http://spotlight.dbpedia.org/rest/annotate', Value, confidence=0.2, support=20)

pi = json.dumps(annotations, sort_keys=True, indent=4, separators=(', ', ': '))
print(pi)
            #print(Value + a.firstChild.data + '\n') #Value + a.firstChild.nodeValue
        #print(get_bytag)


#needs to be written in a file (txt or html)











