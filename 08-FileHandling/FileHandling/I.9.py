###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

n = 1
with open(file_name) as file:
   for line in file:
      if job_title in line:
         print (f'{n}, {line}')
         n +=1