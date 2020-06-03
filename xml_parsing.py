import xml.etree.ElementTree as ET

class XML:

    def __init__(self):
        tree = ET.parse('./data/db.xml')
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
            print("<h3>Printing Device Details</h3>")
            print ("<h3>Account name is</h3><br><br>{}".format(child.tag))
            print("<h3>Paid ammount is</h3><br><br>{}".format(str(root[count][0].text)))
            print("<h3>Due ammount is</h3><br><br>{}".format(str(root[count][1].text)))
            print("------------------------------------------------------------------------")
            count += 1
            print("<h3>Device Details Printed</h3>")
    

if __name__ == "__main__":

    X= XML()
    X.print_xml()

