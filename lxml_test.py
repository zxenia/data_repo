__author__ = 'kzaytseva'

from lxml import etree


root = etree.Element('mytest') #create element
print(root.tag) #access tag name of element via tag method
root.append(etree.Element('child1')) #create child element of root via append

child2 = etree.SubElement(root, 'child2') #or via SubElement method
child3 = etree.SubElement(root, 'child3')
print(etree.tostring(root, pretty_print=True)) #serialise the tree you've created

child = root[2] #to access child element in root by its index
print(child.tag)


print(len(root)) #lenght of root element (how many child elements it has)


print(etree.iselement(root)) #chekc if it is some kind of element

if len(root): #to check if element has children
    print('it has children')


root.insert(0, etree.Element('child0')) #to insert one more child
start = root[:1]
end = root [-1:]

print(start[0].tag)
print(end[0].tag)

children = list(root)
for child in children: #or for child in root   is it the same
    print(child.tag)


root =etree.Element('root', interesting ='totally') #to add attributes to the element
print(etree.tostring(root))

root.set('hello', 'huhu')
print(root.get('hello'))
po = etree.tostring(root)
print(po)












