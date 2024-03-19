import csv
import subprocess
import urllib.parse
import os

# Replace with your CSV file path
csv_file_path = 'search_terms.csv'

# Documents to search
docs = ["Narrative", "Project Description", "Letter of Support", "Budget", "Benefits", "Map", "Project Map", "Action Plan", "Safety Action Plan"]

with open(csv_file_path, 'r') as csv_file:
    reader = csv.reader(csv_file)
    next(reader)  # Skip the header
    for row in reader:
        # Merge the last three columns to form the base search term
        base_term = ' '.join(row[1:])
        for doc in docs:
            # Add the document type to the base search term
            term = base_term + ' ' + doc
            # Generate the URL
            base_url = "https://www.google.com/search"
            query = {
                # 'q': term + " pdf",
                # 'oq': term + " pdf",
                'q': term + " filetype:pdf",
                'oq': term + " file",
                'aqs': "chrome.1.69i57j69i59j0l2j69i60l2.4361j1j7",
                'sourceid': "chrome",
                'ie': "UTF-8"
            }
            url = base_url + '?' + urllib.parse.urlencode(query)

            # Call the greysearch command with the --output option to specify the download directory
            command = ["greysearch", "--url", url, "--program", ' '.join(row[1:3]), "--project", row[3], "--doc", doc, "--results", "5"]
            subprocess.run(command)
