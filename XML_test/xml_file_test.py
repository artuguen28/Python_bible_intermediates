from xml.dom import minidom
import os

# We firt create a minidom document.
root = minidom.Document()

# Names the main element 'root' of the dom.
xml = root.createElement('root')
# We insert it on the file.
root.appendChild(xml)

# Creates the secondary element 'product'.
productChild = root.createElement('product')
# We add an attribute to it called 'name'.
productChild.setAttribute('name', 'Geeks for Geeks')
# We insert it on the secondary element.
xml.appendChild(productChild)


xml_str = root.toprettyxml(indent="\t")

# Name of the xml file.
save_path_file = "gfg.xml"

# Creates the actual file on the current path.
with open("XML_test\gfg.xml", "w") as f:
    f.write(xml_str)
