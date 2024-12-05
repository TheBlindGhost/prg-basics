def is_binary(number):
    for num in number:
        if num != '1' and num != '0' and num != None:
            return False
    return True

print(is_binary('10010010011'))

        