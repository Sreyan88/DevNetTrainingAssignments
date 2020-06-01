import xml.etree.ElementTree as ET

tree = ET.parse('db.xml')
root = tree.getroot()

count = 0
for child in root:
    print ("Account name is:" + child.tag)
    print("Paid ammount is:"+ str(root[count][0].text))
    print("Due ammount is:"+ str(root[count][1].text))
        
    count += 1