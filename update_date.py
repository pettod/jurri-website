"""
Update dates in the footers of every html file. Run:

[bash]$ python update_date.py
"""

from datetime import datetime
import glob
import re


FIN_DATE = datetime.now().strftime("%d.%m.%Y")
EN_DATE = datetime.now().strftime("%m/%d/%Y")


def main():
    html_files = glob.glob("*.html")

    # Loop all html files
    for file_name in html_files:
        lines = []

        # Read a file and replace date
        with open(file_name) as input_file:
            for line in input_file:
                line = re.sub(r'\d{2}\.\d{2}\.\d{4}', FIN_DATE, line)
                line = re.sub(r'\d{2}/\d{2}/\d{4}', EN_DATE, line)
                lines.append(line)

        # Write updated date to a file
        with open(file_name, 'w') as output_file:
            for line in lines:
                output_file.write(line)

    print("Dates updated")


main()
