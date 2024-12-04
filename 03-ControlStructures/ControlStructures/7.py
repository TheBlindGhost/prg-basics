
age = int(input("How old are you?"))

if age < 13:
    print("You are a child")
elif age >= 13 and age <= 19:
    print("You are a Teen")
elif age >= 20 and age <= 64:
    print("You are an Adult")
elif age > 65:
    print("You are a senior")