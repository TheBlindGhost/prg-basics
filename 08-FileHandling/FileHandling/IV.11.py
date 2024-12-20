with open("power.txt","w") as file:
    i = 1
    while i <= 100:
        file.writelines(f"{i},{i*i},{i*i*i}\n")
        i += 1
