import emails
import re


def read_from_file(name):
   with open(name, 'r') as file:
      content = file.read()
   return content


file = read_from_file("email.txt")
file_line = file.splitlines()

print(emails.email_sender(file_line))
print(emails.email_recipient(file_line))
print(emails.email_subject(file_line))
print(emails.email_body(file_line))