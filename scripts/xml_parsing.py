import xml.etree.ElementTree as ET


def print_xml():

    names = []
    paid=[]
    due=[]

    # Opening the file
    tree = ET.parse('C:/Users/Sreyan/Desktop/test-git/DevNetTrainingAssignments/data/db.xml')
    root = tree.getroot()

    # Parsing
    count = 0
    for child in root:
        print ("Account name is:" + child.tag)
        print("Paid ammount is:"+ str(root[count][0].text))
        print("Due ammount is:"+ str(root[count][1].text))
        print("------------------------------------------------------------------------")
    
        names.append(child.tag)
        paid.append(str(root[count][0].text))
        due.append(str(root[count][1].text))

        count += 1

    return [names,paid,due]

if __name__ == "__main__":

    print_xml()
