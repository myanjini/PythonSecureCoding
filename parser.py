import xml.etree.ElementTree as etree

# Open the file and read into memory with etree
with open('entity_example.xml') as fh:
    tree = etree.parse(fh)

# Iterate through the XML nodes, printing the tag name and text values
for node in tree.iter():
    print(node.tag, node.text)
