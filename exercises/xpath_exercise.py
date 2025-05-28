# XML/XPath Exercise
#
# Instructions:
# 1. Implement a function named `modify_xml` that:
#    - Parses the XML file `input_form.xml` (provided in this directory).
#    - Locates the `<field name="author"/>` element and moves it to be the first child of the root `<form>` element.
#    - Adds a new `<section>` element with the text "Details" after the fields.
#    - Adds a `<button>` element with the attribute `name="toggle_availability"` after the section.
#    - Outputs the modified XML as `output_form.xml`.
#
# Write your solution in this file.

# Your code here

import os
import xml.etree.ElementTree as ET

def modifyXML(input_file, output_file):
    
    #verify if path exist
    if not os.path.exists(input_file):
        base_dir = os.path.dirname(os.path.abspath(__file__)) #we can obtain absolut path
        input_file = os.path.join(base_dir, input_file) #combine absolut path and input_file

    tree = ET.parse(input_file) #Parse xlm file
    root = tree.getroot()

    author_field = root.find(".//field[@name='author']") #find and locate author field

    #verify if author_field is valid or None
    if author_field is not None:
        root.remove(author_field)
        root.insert(0, author_field)

    #new type "section" element creation
    section = ET.Element("section")
    section.text = "Details" #set text
    root.append(section) #add section as child
    
    #new type "button" element creation
    button = ET.Element("button")
    button.set("name", "toggle_availability") #set name attribute
    root.append(button) #add section as child

    tree.write(output_file, encoding="utf-8", xml_declaration=True) #asign name

if __name__ == "__main__":
    input_file = "input_form.xml"    
    output_file = "output_form.xml"
    modifyXML(input_file, output_file)