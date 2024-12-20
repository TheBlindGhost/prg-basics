file = input("Name a file")
try:
    with open(file) as content:

        lines=0
        words=0
        characters=0
        for line in content:
            wordslist=line.split()
            lines+=1
            words+=len(wordslist)
            characters += sum(len(word) for word in wordslist)
        print(lines)
        print(words)
        print(characters)
except FileNotFoundError:
    print(f"Hey! The file {file} does not exist.")