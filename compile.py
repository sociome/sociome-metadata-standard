'''comile.py is the main script in the sociome metadata package it compiles
the defined xml data dictionary into varius formats.
'''
import argparse
import sys


def parse_args():
    parser=argparse.ArgumentParser(description="Compiles the data dictionary specified in the xml file")
    parser.add_argument("target")
    args=parser.parse_args()
    return args


def depth_iter(element, tag=None):
    stack = []
    stack.append(iter([element]))
    while stack:
        e = next(stack[-1], None)
        if e == None:
            stack.pop()
        else:
            stack.append(iter(e))
            if tag == None or e.tag == tag:
                yield (e, len(stack) - 1)


def do_md():
    import xml.etree.ElementTree as ET

    e = ET.parse("xml/core.xml")
    for element, level in depth_iter(e.getroot()):

        name = str(element.text).strip()

        if level == 1:
            name = "Database"

        if len(name) == 0:
            name = 'Table'

        header = '#'*level + ' ' + str(element.tag) + ': ' + str(name)

        print(header)
        print(element.attrib['description'])

        if str(element.tag) == 'attribute':
            reference_file = element.attrib['compileType']

            if reference_file == 'string':
                print("\nThis attribute is a text field.\n")
                continue

            if reference_file == 'url':
                print("\nThis attribute is a url.\n")
                continue

            print("This attribute is populated with the following values: ")

            ref_e = ET.parse("xml/" + reference_file + '.xml')
            for ref_element, ref_level in depth_iter(ref_e.getroot()):

                if ref_element.attrib.get('name', '') == name:
                    for child in (ref_element):

                        print('*','**'+child.text+"**:",child.attrib.get('description',""))



def main():
    inputs=parse_args()
    
    if inputs.target == 'md':
        do_md()



if __name__ == '__main__':
    main()
