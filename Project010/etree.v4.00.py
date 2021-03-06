# -*- coding: utf-8 -*-


#https://lxml.de/api/lxml.etree._Element-class.html

from lxml import etree
from io import StringIO, BytesIO
import dateutil.parser

def parseXML(xmlFile):
        tree = etree.parse(xmlFile)
        
        for tag in tree.iter():
            if not len(tag):
                #print (tag.tag, tag.text)
                #print(type(tag))
                #print (tag.tag, tag.text, tag.get)
                #print (tag.items)
                #print (tag.tag)
                data=str(tag.tag)
                print(data[data.find("}")+1:], "-> ", tag.text)
                
        
if __name__ == "__main__":
    #parseXML("calibracion.xml")
    parseXML("calibracion.xml")
    
    
    
