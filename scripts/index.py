from json_parsing import JSON
from xml_parsing import XML
from yaml_parsing import YAML
from parsing_dnac_devices import DNAC

J = JSON()
X = XML()
Y = YAML()

J.print_json()
X.print_xml()
Y.print_yaml()