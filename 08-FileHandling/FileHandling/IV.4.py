def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content

content = read_from_file("it_company.csv")
file_line = content.splitlines()
i = 0
for line in file_line:
   if i < 5:
      print(line)
      i+=1 
   else:
      input("Press Enter to continue...")
      i = 0
