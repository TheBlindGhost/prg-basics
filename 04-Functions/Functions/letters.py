def letter_cal(letter, text):
    letter_count = 0
    for num in range(0,len(text)):
        if text[num] == letter:
            letter_count += 1
    return letter_count