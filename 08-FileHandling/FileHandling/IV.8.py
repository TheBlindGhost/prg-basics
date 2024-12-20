import re


with open ("files.txt") as file:
    file_content = file.read()
    file_line = file_content.splitlines()


    for line in file_line:
        if re.match(r'.{0,}\..{4}',line):
            print(line)
