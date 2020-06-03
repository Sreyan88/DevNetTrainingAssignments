from json_parsing import JSON
from xml_parsing import XML
from yaml_parsing import YAML
from parsing_dnac_devices import DNAC

def main():

    J = JSON()
    X = XML()
    Y = YAML()
    D = DNAC()

    J.print_json()
    X.print_xml()
    Y.print_yaml()
    D.print_dnac_devices()

main()