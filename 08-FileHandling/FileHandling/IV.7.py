import re

email_file = 'voles.txt'

with open(email_file,'r') as file:
    text = file.read()


pattern = '[a,e,u,o,i,y,A,E,U,O,I,Y]'
count = 0

amounts = re.findall(pattern, text)
for char in text:
    if re.match(pattern,char):
        count += 1


print(count)