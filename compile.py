'''comile.py is the main script in the sociome metadata package it compiles
the defined xml data dictionary into varius formats.
'''

#imports
import argparse
import sys

#these are primitive database data types
data_type_enum = ['string', 'num', 'date', 'url']
data_documentation_enum = {1:'Database', 2:'Table', 3:''}

def depth_iter(element, tag=None):
    '''dept_iter recursively iterates through an xml tree.
    '''
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

        name = str(element.text).strip() + ' ' + data_documentation_enum[level]

        header = '#'*level + ' ' + str(element.tag) + ': ' + str(name)

        print(header)
        print(element.attrib['description'])

        if str(element.tag) == 'attribute':
            reference_file = element.attrib['compileType']

            if reference_file in data_type_enum:
                print("\nThis attribute is a "+ reference_file +" field.\n")
                continue

            print("\n This attribute is populated with the following values: ")

            ref_e = ET.parse("xml/" + reference_file + '.xml')

            for ref_element, ref_level in depth_iter(ref_e.getroot()):

                if ref_element.attrib.get('name', '') == name:
                    for child in (ref_element):

                        print('*','**'+child.text+"**:",child.attrib.get('description',""))



def parse_args():
    parser=argparse.ArgumentParser(description="Compiles the data dictionary specified in the xml file")
    parser.add_argument("target")
    args=parser.parse_args()
    return args

def main():
    inputs=parse_args()
    
    if inputs.target == 'md':
        do_md()


if __name__ == '__main__':
    main()
