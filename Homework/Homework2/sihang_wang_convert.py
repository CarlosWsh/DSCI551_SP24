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
    try:
        #Convert a CSV to XML by reading data
        df = pd.read_csv(fsimage_csv)
        #Create elements from rows
        root = etree.Element("FileSystemMetadata")
        for _, row in df.iterrows():
            file_element = etree.SubElement(root, "File")

            etree.SubElement(file_element, "Path").text = row["Path"]
            etree.SubElement(file_element, "Replication").text = str(row["Replication"])
            etree.SubElement(file_element, "ModificationTime").text = row["ModificationTime"]
            etree.SubElement(file_element, "AccessTime").text = row["AccessTime"]
            # Only add block information if there are blocks
            if row["BlocksCount"] > 0:
                etree.SubElement(file_element, "PreferredBlockSize").text = str(row["PreferredBlockSize"])
                etree.SubElement(file_element, "BlocksCount").text = str(row["BlocksCount"])
                etree.SubElement(file_element, "FileSize").text = str(row["FileSize"])
            etree.SubElement(file_element, "Permission").text = row["Permission"]
            etree.SubElement(file_element, "UserName").text = row["UserName"]
            etree.SubElement(file_element, "GroupName").text = row["GroupName"]

        #Save with pretty printing
        tree = etree.ElementTree(root)
        with open(output_xml, "wb") as f:
            tree.write(f, pretty_print=True, xml_declaration=True, encoding="UTF-8")
        print(f"Converted {fsimage_csv} to {output_xml}")

    except FileNotFoundError:
        print(f"Error: File {fsimage_csv} not found.")
        sys.exit(1)

if __name__=="__main__":
    # Input and output file paths

    if len(sys.argv) != 3:
        print("Usage: python sihang_wang_convert.py <csv_path> <xml_file>")
        sys.exit(1)

    fsimage_csv = sys.argv[1]
    output_xml = sys.argv[2]

    convert(fsimage_csv, output_xml)