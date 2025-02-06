def t_position(words) -> tuple:
    split = list(words)
    letter = split[0].upper()
    number = int(split[1])
    return letter, number

def insert_B(table: list, words) -> bool:
    letter, number = t_position(words)
    column = ord(letter) - ord('A')
    if table[column][number - 1] in ['X', 'O']:
        return False
    table[column][number - 1] = 'O'
    return True

def insert_X(table: list, words) -> bool:
    letter, number = t_position(words)
    column = ord(letter) - ord('A')
    if table[column][number - 1] in ['X', 'O']:
        return False
    table[column][number - 1] = 'X'
    return True
