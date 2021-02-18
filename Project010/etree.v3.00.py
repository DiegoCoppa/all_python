# -*- coding: utf-8 -*-

from lxml import etree
from io import StringIO, BytesIO
import dateutil.parser


dcc_software_tree_path="/dcc:digitalCalibrationCertificate/dcc:administrativeData/dcc:dccSoftware/dcc:software[@id='INTI-DCC4F']"
dcc_core_Data_tree_path="/dcc:digitalCalibrationCertificate/dcc:administrativeData/dcc:coreData"
dcc_items_tree_path="/dcc:digitalCalibrationCertificate/dcc:administrativeData/dcc:items"

def parseXML(xmlFile):
    with open(xmlFile) as fobj:
        #print("fobj type:")
        #print(type(fobj))
        xml_str = fobj.read() # devuelve string
        #print("xml_str type:")
        #print(type(xml_str))
        #root_xml_elem=etree.fromstring(xml_str) #devuelve el root
        #print("xml_elem type:")
        #print(type(root_xml_elem))
        #print(root_xml_elem)
        #bytes_xml=etree.tostring(root_xml_elem) #devuelve bytes
        #print(type(xml_bytes))
        #print(etree.tostring(store, encoding='UTF-8',xml_declaration=True, pretty_print=True))
        
        elem_tree=etree.parse(StringIO(xml_str)) # devuelve elementr tree
        #print(type(elem_tree))
        r=elem_tree.xpath(dcc_software_tree_path+'/dcc:name/dcc:content', 
                      namespaces={'dcc': 'https://ptb.de/dcc' })
        
        r=elem_tree.xpath(dcc_software_tree_path+'/dcc:release', 
                      namespaces={'dcc': 'https://ptb.de/dcc' })
        
        r=elem_tree.xpath(dcc_software_tree_path+"/dcc:description", 
                      namespaces={'dcc': 'https://ptb.de/dcc' })
        
        r=elem_tree.xpath(dcc_software_tree_path + "/dcc:description[@id='DCCbyDC']/dcc:content[@lang='es']", 
                      namespaces={'dcc': 'https://ptb.de/dcc' })
        
        r=elem_tree.xpath(dcc_core_Data_tree_path, 
                      namespaces={'dcc': 'https://ptb.de/dcc' })
                
        
        r=elem_tree.xpath(dcc_core_Data_tree_path + "/dcc:receiptDate", 
                      namespaces={'dcc': 'https://ptb.de/dcc' })
        
        r=elem_tree.xpath(dcc_core_Data_tree_path + "/dcc:uniqueIdentifier", 
                      namespaces={'dcc': 'https://ptb.de/dcc' })
        
        r=elem_tree.xpath(dcc_items_tree_path + "/dcc:description", 
                      namespaces={'dcc': 'https://ptb.de/dcc' })
        
        
        
        #print(len(r))
        data=str(r[0].tag)
        print(data[data.find("}")+1:], "-> ", r[0].text)
        """
        print(r[0].tag)
        print(r[0].text)
        """              
        
        
        """
        elem_tree=etree.parse(StringIO('<foo><bar></bar></foo>'))
        r=elem_tree.xpath('/foo/bar')
        print(len(r))
        """
        """
        f = StringIO('''<a:foo xmlns:a="http://codespeak.net/ns/test1"\
                     xmlns:b="http://codespeak.net/ns/test2">
                     <b:bar>Text</b:bar>\
                     </a:foo>''')
        doc = etree.parse(f)
        r = doc.xpath('/x:foo/b:bar', 
                      namespaces={'x': 'http://codespeak.net/ns/test1',
                                  'b': 'http://codespeak.net/ns/test2'})
        print(len(r))
        print(r[0].tag)
        print(r[0].text)
        """
        
        
        #for event, element in etree.iterwalk(store, events=('start', 'end')):
        #    print(event,element)
        
        
        
if __name__ == "__main__":
    #parseXML("calibracion.xml")
    parseXML("calibracion.xml")