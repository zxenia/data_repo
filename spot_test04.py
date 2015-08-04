__author__ = 'kzaytseva'

import os, re

import xml.dom.minidom

from xml.dom.minidom import parse, parseString
from xml.dom.minidom import Node, NodeList
from xml.dom.minidom import Text

import spotlight
import io, json

os.chdir(r'C:\Users\Ksenia\Desktop\OEBL_XML-Daten')  #Return a list containing the names of the entries in the directory given by path.

for file in os.listdir(os.getcwd()): #iterate over files in the current directory
    Value = '' #initialize value with an empty string
    outputFilePath = 'C:\Users\Ksenia\Desktop\OEBL_Annotations_files' + '\\' + file.split('.')[0] + '_annotations.txt'
    #creating dynamically a name for each new file
    output = open(outputFilePath, 'w') #open this new file
    data_to_process = xml.dom.minidom.parse(file) #parsing each file
    topic = data_to_process.getElementsByTagName('Lexikonartikel') #variable to hold root node
    print(file)
    for node in topic:
        text_content = node.getElementsByTagName('Haupttext') #access the content of haupttext tag
        if text_content != None: #check if content of haupttext tag exists then loop
            for a in text_content:
                if a.firstChild != None: #check if content of haupttext has child then
                    Value = Value + a.firstChild.data + '\n'
                    #output.write(Value)
                    #print(Value)
        if Value != '': #check if content is not an empty string and if not then annotate
            try: #handling exceptions
                annotations = spotlight.annotate('http://spotlight.dbpedia.org/rest/annotate', Value, confidence=0.2, support=20)
                json_annotations = json.dumps(annotations, sort_keys=True, indent=4,separators=(', ', ': '))
                print(json_annotations)
                output.write(str(json_annotations)) #writing annotations into new file
            except spotlight.SpotlightException: #handling exception which was internally declared in spotlight module
                print('got problems with annotations')
                output.write(str('got problems with annotations'))#writing problems message

    output.close()













