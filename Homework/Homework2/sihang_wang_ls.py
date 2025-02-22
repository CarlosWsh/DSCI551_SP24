import sys
from lxml import etree
import time

def ls_hdfs(xml_file, path):
    """
    Simulate the 'ls' command for an HDFS-like XML structure.

    :param xml_file: Path to the XML file.
    :param path: Directory path to list.
    :return: Formatted string with file or directory information.
    :rtype: str
    :raises FileNotFoundError: If the path does not exist.
    """
    try:
        # Parse the XML file
        tree = etree.parse(xml_file)
        root = tree.getroot()

        # Handle trailing slash
        if path.endswith("/"):
            path = path[:-1]

        # Check path existence
        matched_elements = root.xpath(f"//File[Path='{path}']")

        if not matched_elements:
            return "No such file or directory."

        # Handle files and directories
        output = []
        for elem in matched_elements:
            output.append(format_output(elem))

        # List directory contents if the path is a directory
        directory_contents = root.xpath(f"//File[starts-with(Path, '{path}/')]")

        for elem in directory_contents:
            output.append(format_output(elem))

        return "\n".join(output)

    except FileNotFoundError:
        return f"Error: File {xml_file} not found."

def format_output(file_elem):
    """
    Format the file element information for display.

    :param file_elem: XML element containing file information.
    :return: Formatted string representing the file information.
    :rtype: str
    """
    # Extract and format file details
    permission = file_elem.findtext("Permission", "-")
    replication = file_elem.findtext("Replication", "-")
    user = file_elem.findtext("UserName", "")
    group = file_elem.findtext("GroupName", "")
    size = file_elem.findtext("FileSize", "0")
    mod_time = file_elem.findtext("ModificationTime", "")
    path = file_elem.findtext("Path", "")

    if not path:
        return ""

    return f"{permission}   {replication} {user} {group}   {size} {mod_time} {path}"

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python sihang_wang_ls.py <xml_file> <path>")
        sys.exit(1)

    xml_file = sys.argv[1]
    path = sys.argv[2]

    result = ls_hdfs(xml_file, path)
    print(result)
