import pandas as pd
from lxml import etree
import sys


def convert(fsimage_csv, output_xml):
    """
    Convert a CSV file to an XML file.

    :param fsimage_csv: Path to the input CSV file.
    :param output_xml: Path to the output XML file.
    :return: None
    :raises FileNotFoundError: If the CSV file is not found.
    """

    #Convert a CSV to XML by reading data
    
    #Create elements from rows
    
    #Save with pretty printing

if __name__=="__main__":
    # Input and output file paths

    if len(sys.argv) != 3:
        print("Usage: python firstname_lastname_convert.py <csv_path> <xml_file>")
        sys.exit(1)

    fsimage_csv = sys.argv[1]
    output_xml = sys.argv[2]

    convert(fsimage_csv, output_xml)