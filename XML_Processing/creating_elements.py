import xml.dom.minidom

domtree = xml.dom.minidom.parse("XML_Processing\group.xml")
group = domtree.documentElement

# Creating new elements
newperson = domtree.createElement("person")
newperson.setAttribute("id", "6")

name = domtree.createElement("name")
name.appendChild(domtree.createTextNode("Paul Smith"))

age = domtree.createElement("age")
age.appendChild(domtree.createTextNode("45"))

weight = domtree.createElement("weight")
weight.appendChild(domtree.createTextNode("78"))

height = domtree.createElement("height")
height.appendChild(domtree.createTextNode("178"))

newperson.appendChild(name)
newperson.appendChild(age)
newperson.appendChild(weight)
newperson.appendChild(height)

group.appendChild(newperson)

domtree.writexml(open("XML_Processing\group.xml", "w"))

