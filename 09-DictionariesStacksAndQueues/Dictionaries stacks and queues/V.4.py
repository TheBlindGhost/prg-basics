winter_semester = {
   "math":60,
   "programming":30,
   "history":15
}
total = 0
for key,value in winter_semester.items():
    total += int(value)
print(total)