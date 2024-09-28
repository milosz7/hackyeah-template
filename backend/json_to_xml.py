import json
from dicttoxml import dicttoxml
from xml.dom.minidom import parseString

def json_to_xml(json_data, root_name):
    data = json.loads(json_data)
    # Convert to XML
    xml_bytes = dicttoxml(data, custom_root=root_name, attr_type=False)
    xml_str = xml_bytes.decode()

    # Pretty-print XML
    dom = parseString(xml_str)
    pretty_xml = dom.toprettyxml()


    return pretty_xml
    