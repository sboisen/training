import xlrd

DATAFILE = 'I:/LRSInfo/Everyone/Ben Amundgaard/Anglican/L6 Portfolio/compcharttext.xlsx'

def sheet_matrix(file=DATAFILE):
    """Return the data from DATAFILE as a list of lists. Doesn't include the headers. 
    """
    sheet = xlrd.open_workbook(DATAFILE).sheet_by_index(0)
    rows = []
    for index in range(0, sheet.nrows):
        rows.append(sheet.row_values(index))
    return rows

import xml.etree.cElementTree as ET

#f = open('myfile.xml','w')

def indent(elem, level=0):
    """formats machine-readable XML to make it human friendly"""
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
        for elem in elem:
            indent(elem, level+1)
        if not elem.tail or not elem.tail.strip():
            elem.tail = i
    else:
        if level and (not elem.tail or not elem.tail.strip()):
            elem.tail = i

x = sheet_matrix()


def create_xml(filename):
    """takes xlsx file and converts it to .xml where each row is a tagged line. Filename = output file"""
    element = ET.Element("productcomparison")
    #section = ET.SubElement(section)
    for i in x:
        if i[0]:
            ET.SubElement(element, "/rows")
            ET.SubElement(element, "section", label=i[0], id=str(int(i[1]))).text = ' '
            ET.SubElement(element, "rows")
        else:
            ET.SubElement(element, "row", kind="Resource", id=i[1], newForVersion=i[2], footnoteCode=i[3], label=i[4], productId=str(int(i[5]))).text = ' '
    indent(element)
    tree = ET.ElementTree(element)
    tree.write(filename)

create_xml("myfile.xml")