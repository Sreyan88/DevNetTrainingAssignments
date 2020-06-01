import xml.etree.ElementTree as ET

class XML:

    def __init__(self):
        tree = ET.parse('C:/Users/Sreyan/Desktop/test-git/DevNetTrainingAssignments/data/db.xml')
        root = tree.getroot()
        self.object = root

    def testing(self):
        root = self.object

        names = []
        paid=[]
        due=[]

        count = 0

        for child in self.object:
            names.append(child.tag)
            paid.append(str(root[count][0].text))
            due.append(str(root[count][1].text))
            count += 1

        return [names,paid,due]



    def print_xml(self):
        root = self.object

        count = 0

        for child in self.object:
            print ("Account name is:" + child.tag)
            print("Paid ammount is:"+ str(root[count][0].text))
            print("Due ammount is:"+ str(root[count][1].text))
            print("------------------------------------------------------------------------")
            count += 1
    

if __name__ == "__main__":

    X= XML()
    X.print_xml()

