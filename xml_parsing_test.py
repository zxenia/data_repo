__author__ = 'Ksenia'

import xml.dom.minidom
from xml.dom.minidom import Node
dom = xml.dom.minidom.parse("Emil_Zuckerkandl.xml")
Topic = dom.getElementsByTagName('swivt:Subject')
i = 0
for node in Topic:
    alist=node.getElementsByTagName('property:Jubil-C3-A4um')
    for a in alist:
        Value = a.firstChild.data
        print(Value)