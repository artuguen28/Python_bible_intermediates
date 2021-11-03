import xml.dom.minidom

domtree = xml.dom.minidom.parse("XML_Processing\group.xml")
group = domtree.documentElement

# Manipulating files
persons = group.getElementsByTagName("person")
# We adress the index zero persons[0] for the first element.
persons[0].getElementsByTagName("name")[0].childNodes[0].nodeValue = "New Name"

# We can also change the attributes by using the function setAttribute.
persons[0].setAttribute("id", "1")

domtree.writexml(open("XML_Processing\group.xml", "w"))
