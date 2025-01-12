translations = {
   'computer': 'komputer',
   'mouse': 'myszka',
   'keyboard': 'klawiatura',
   'printer': 'drukarka'
}
def translate(word):
    for key,value in translations.items():
        if key == word:
            return print(f"The word meanes: {value}")
    
    return print("No translation")
    
w = input("Type a word to translate:")
translate(w)