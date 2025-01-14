employees = ["SMITH Lucy","JONES Janet","LEE Jerry",
               "JACKSON Peter","JOHNSON Rick",
               "LEWIS Terry","CLARKE Robin"]
emp_J = list(filter(lambda e: " J" in e, employees))
# print a list …
print(emp_J)