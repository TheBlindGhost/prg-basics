import statistics
grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

valid_gardes = list(filter(lambda x: x>2, grades))

mean = statistics.mean(valid_gardes)
print(round(mean,2))
