# -*- coding: utf-8 -*-
"""
Created on Fri Feb 19 09:37:44 2021

@author: Diego

#https://lxml.de/tutorial.html

"""
from lxml import etree as ET
from lxml import etree
from io import StringIO, BytesIO
from copy import deepcopy


tree = ET.parse('test.xml')
root = tree.getroot()

#root = ET.Element("root")
#print(root.tag)

#no modifica el archivo
"""
root.append( ET.Element("child1") )
child2 = ET.SubElement(root, "child2")
child3 = ET.SubElement(root, "child3")
print(ET.tostring(root, pretty_print=True))
"""


"""
print("root tag:", root.tag)
print("root att:", root.attrib)
print("root size:", len(root))
for child in root:
    print(child.tag)
child=root[0]
print("el primer child:", child[0].tag)

root[0] = root[-1] # esto no afecta el archivo

for child in root:
    print(child.tag)

# para saber quien es el padre (siempre hay uno solo)
root is root[0].getparent()
print(root.tag)
"""

"""
#creo una copia del root[1] y se lo asigno a element
element = ET.Element("neu")

element.append( deepcopy(root[1]) )
print(element[0].tag)

#no cambió nada en el root
print([ c.tag for c in root ])
"""


"""

root = ET.Element("root", interesting="totally")
print(ET.tostring(root))
print(root.get("hello"))
root.set("hello", "Huhu")
print(root.get("hello"))
print(ET.tostring(root))
print(sorted(root.keys()))
for name, value in sorted(root.items()):
    print('%s = %r' % (name, value))

##ejemplo de 
attributes = root.attrib
print(attributes["interesting"])
print(attributes.get("no-such-attribute"))
attributes["hello"] = "Guten Tag"
print(attributes["hello"])
print(root.get("hello"))

d = dict(root.attrib)
print(sorted(d.items()))
print(d)
###

"""

#sólo la palabra text
root = ET.Element("root")
root.text = "TEXT"
#print(root.text)

###ejemplo 1
ET.tostring(root)
html = ET.Element("html") #html como nombre del elemneto
body = ET.SubElement(html, "body") #body como subelement de html
body.text = "TEXT" #Text como text de body
#print(ET.tostring(html))

br = ET.SubElement(body, "br")#br como sub elemnent de body
#print(ET.tostring(html))

br.tail = "TAIL" #tail de br

#print(ET.tostring(br))
#print(ET.tostring(body))
#print(ET.tostring(html))

"""
####ejemplo 2
ET.tostring(root)
html = ET.Element("html") #html como nombre del elemneto
body = ET.SubElement(html, "body") #body como subelement de html
br = ET.SubElement(body, "br")#br como sub elemnent de body
br.text = "TEXT" #Text como text de body
#print(ET.tostring(html))
#br.tail = "TAIL" #tail de br


####ejemplo 3
ET.tostring(root)
html = ET.Element("html") #html como nombre del elemneto
body = ET.SubElement(html, "body") #body como subelement de html
br = ET.SubElement(body, "br")#br como sub elemnent de body
br.tail = "TAIL" #tail de br
br.text = "TEXT" #Text como text de body
# print(ET.tostring(html))
# br.tail = "TAIL" #tail de br
"""
#print(ET.tostring(html, with_tail=False))
#print(ET.tostring(br))
#print(ET.tostring(br, with_tail=False))

#print(ET.tostring(html, method="text"))


#print(html.xpath("string()")) # lxml.etree only!
#print(html.xpath("//text()")) # lxml.etree only!


build_text_list = ET.XPath("//text()") # lxml.etree only!
# print(build_text_list(html))

texts = build_text_list(html)
# print(texts[0])
# print(type(texts[0]))
parent = texts[0].getparent()
"""
print(parent.tag)
print(texts[1])
print(texts[1].getparent().tag)
print(type(texts[1]))
print(texts[0].is_text)
print(texts[1].is_text)
print(texts[1].is_tail)
"""


root.append(ET.Entity("#234"))
root.append(ET.Comment("some comment"))
"""
for element in root.iter():
    if isinstance(element.tag, str):  # or 'str' in Python 3
        print("%s - %s" % (element.tag, element.text))
    else:
        print("SPECIAL: %s - %s" % (element, element.text))


for element in root.iter(tag=ET.Element):
    print("%s - %s" % (element.tag, element.text))


for element in root.iter(tag=ET.Entity):
    print(element.text)
"""

"""
root = ET.XML('<root><a><b/></a></root>')
#print(ET.tostring(root))

ET.indent(root)
#print(ET.tostring(root, encoding="unicode", pretty_print=True))

ET.indent(root, space="    ")
#print(ET.tostring(root, encoding="unicode", pretty_print=True))
etree.indent(root, space="\t")
#print(ET.tostring(root, encoding="unicode", pretty_print=True))

#, encoding="unicode", pretty_print=True
#print(etree.tostring(root, encoding='iso-8859-1'))
#print(etree.tostring(root, encoding="unicode", pretty_print=True))
root = etree.XML('<root><a><b/>\n</a></root>')
#print(etree.tostring(root, encoding="unicode", pretty_print=True))
etree.indent(root)
#print(etree.tostring(root))
"""
"""
root = etree.XML('<html><head/><body><p>Hello<br/>World</p></body></html>')
etree.tostring(root) # default: method = 'xml'

print(etree.tostring(root, method='xml'))
 # same as above

print(etree.tostring(root, method='html'))

print(etree.tostring(root, method='html', pretty_print=True))
print(etree.tostring(root, method='text'))

br = next(root.iter('br'))
br.tail = u'W\xf6rld'
"""
#print(etree.tostring(root, method='text')) error no encoding

"""
print(etree.tostring(root, method='text', encoding="UTF-8"))
print(etree.tostring(root, encoding='unicode', method='text'))
"""
#root = etree.XML('''<?xml version="1.0"?><!DOCTYPE root SYSTEM "test" [ <!ENTITY tasty "parsnips"> ]><root><a>&tasty;</a></root>''')
       
#tree = ET.ElementTree(root)


""" Esto no funca
print(tree.docinfo.xml_version)
print(tree.docinfo.doctype)
tree.docinfo.public_id = '-//W3C//DTD XHTML 1.0 Transitional//EN'
etree.docinfo.system_url = 'file://local.dtd'
print(tree.docinfo.doctype)
"""

#print(etree.tostring(tree))

#Parsing from strings and files
"""
root = etree.XML("<root>data</root>")
print(root.tag)
print(etree.tostring(root))


root = etree.HTML("<p>data</p>")
print(etree.tostring(root))
"""

"""
some_file_or_file_like_object = BytesIO(b"<root>data</root>")
tree = etree.parse(some_file_or_file_like_object)
print(etree.tostring(tree))

root = tree.getroot()
print(root.tag)
print(etree.tostring(root))
"""

"""
#Parser objects
#acá falta esto.
#Incremental parsing

"""


#Event-driven parsing

"""
some_file_like = BytesIO(b"<root><a>data</a></root>")

for event, element in etree.iterparse(some_file_like):
    print("%s, %4s, %s" % (event, element.tag, element.text))
    
"""  
#some_file_like = BytesIO(b"<root><a>data</a></root>")
tree = ET.parse('test.xml')
some_file_like = BytesIO(tree)

for event, element in etree.iterparse(some_file_like, events=("start", "end")):
    print("%5s, %4s, %s" % (event, element.tag, element.text))