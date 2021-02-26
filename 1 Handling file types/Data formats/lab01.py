#!/usr/bin/env python3
# Import modules
import sys
from helper import *

import xml.etree.ElementTree as ET

import xml.dom.minidom as MD


print('YAML file handling')

# Open the user.yaml file as read only

# Load the stream using safe_load

# Print the object type
print("Type of user_yaml variable:")

print('----------------------')

# Iterate over the keys of the user_yaml and print them
print('Keys in user_yaml:')

print('----------------------')

# Create a new instance of class User

# Assign values form the user_yaml to the object user

# Print the user object
print('User object:')


#########################################
#              Procedure 3              #
#########################################
print('##################')
print('###### JSON ######')
print('##################')

# Create JSON structure from the user object

# Print the created JSON structure
print('Print user_json:')

print('----------------------')

# Create JSON structre with indents and soreted keys
print('JSON with indents and sorted keys')


#########################################
#              Procedure 4              #
#########################################
print('######################')
print('# XML - Element Tree #')
print('######################')

# Parse the user.xml file
tree = ET.parse('user.xml')

# Get the root element
root = tree.getroot()

# Print the tags
print('Tags in the XML:')
for element in root:
    print(element.tag)
print('----------------------')

# Print the value of id tag
print('id tag value:')
elementId = root.find('id').text
print(elementId)
print('----------------------')

# Find all elements with the tag address in root
addresses = root.findall('address')

# Print the adresses in the xml
print('Addresses:')

for address in addresses:
    for i in address:
        print(i.tag, ":", i.text)
print('----------------------')

# Print the elements in root with their tags and values
print('Print the structure')
for value in root.iter():
    print(value.tag + ": "+ value.text)


# Parsing XML files with MiniDOM
print('######################')
print('### XML - MiniDOM ####')
print('######################')

# Parse the user.xml file
dom = MD.parse('user.xml').documentElement
# Print the tags
print('----------------------')
print('Tags in the XML')
for node in dom.childNodes:
    printTags(node.childNodes)
# Accessing element value
print('Accessing element value')
idElements = dom.getElementsByTagName('id')
print(idElements)
elementId = idElements[0]
print(elementId.childNodes)
idValue = elementId.firstChild.data
print(idValue)
print('----------------------')

# Print elements from the DOM with tag name 'address'
print('Addresses:')
for element in dom.getElementsByTagName('address'):
    printNodes(element.childNodes)

print('----------------------')

# Print the entire structure with printNodes
print('The structure:')
for value in dom.childNodes:
    printNodes(value.childNodes)

#########################################
#              Procedure 5              #
#########################################
print('######################')
print('#   Use Namespaces   #')
print('######################')

# Parse the user.xml file
itemTree = ET.parse('item.xml')
# Get the root element
root = itemTree.getroot()

# Define namespaces
namespaces = {'a':"https://www.example.com/network",'b':"https://www.example.com/furniture"}
# Set table as the root element
elementInNSa = root.findall('a:table', namespaces)
elementInNSb = root.findall('b:table', namespaces)
# Elements in NS a
print('Elements in NS a:')
for e in elementInNSa:
    for i in e.iter():
        print(i.tag + ": " + i.text)

print('----------------------')

# Elements in NS b
print('Elements in NS b:')
for i in list(elementInNSb[0]):
    print(i.tag + ": " + i.text)