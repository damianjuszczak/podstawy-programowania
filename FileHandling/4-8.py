import re

regex = r"\.\w{4}$"

with open('files.txt', 'r') as file:
    for line in file:
        filename = line.strip()
        
        if re.search(regex, filename):
            print(filename)