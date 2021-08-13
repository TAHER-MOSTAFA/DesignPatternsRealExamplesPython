'''
The same idea as electric adapter when we use it to change type of plug
suppose we use solr as search engine. It accepts data in XML format
while django serialize model objects to Json
so we want and adapter to transform that Json to xml
'''
from xml.etree import ElementTree as et
import json



class SolrDataImporter:
    def __init__(self, data) -> None:
        #only accepts json
        r = et.fromstring(data)
        print(f"{r.find('fname').text} {r.find('lname').text}")
        print(r.find('quote').text)



# old no longer used
class XmlSerializer:
    def xml_data(self):
        return """<user>
                <fname>Taher</fname>
                <lname>Mostafa</lname>
                <quote>YOU GOOD</quote>
                </user>"""
        

# new
class JsonSerializer:
    def json_data(self):
        return json.dumps({
                        "user": {
                            "fname": "Taher",
                            "lname": "Mostafa",
                            "quote": "YOU GOOD"
                        },
                        })


# Adapter class 
class Adapter(JsonSerializer, XmlSerializer):
    
    def xml_data(self):
        # handle logic
        json_data = super().json_data()
        # convert to xml
        xml_data = super().xml_data()
        return xml_data
        


if __name__ == '__main__':
    # the data importer don't know about Json data 

    # default behaviour
    # SolrDataImporter(xml data)
    
    
    # now we pass the to adapter
    SolrDataImporter(Adapter().xml_data())