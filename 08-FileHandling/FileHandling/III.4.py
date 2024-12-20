###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file,'r') as file:
    email = file.read()

# regular expression pattern
# for amounts
pattern = '[0-9]{1,10}'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email)

# calculate the total purchases
cost = 0
for amount in amounts:
   cost += int(amount)

# print result
print(cost)