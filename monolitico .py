import os

table: list = [
    [0,0,0], 
    [0,0,0], 
    [0,0,0] 
]

def clear_terminal():

    if os.name=='nt':
        os.system('cls')

def v_vertical_01(table:list) -> str:
    x:int = 0
    bolinha:int = 0 
    if table[0][0] == 'X' and table[1][1] == 'X' and table[2][2] == 'X':
        x = 3
    elif table[0][0] == 'O' and table[1][1] == 'O' and table[2][2] == 'O':
        bolinha = 3
    if bolinha == 3:
        return 'O'
    elif x == 3:
        return 'X'
    else:
        return False

def v_vertical_02(table:list) -> str:
    x:int = 0
    bolinha:int = 0 
    if table[0][2] == 'X' and table[1][1] == 'X' and table[2][0] == 'X':
        x = 3
    elif table[0][2] == 'O' and table[1][1] == 'O' and table[2][0] == 'O':
        bolinha = 3
    if bolinha == 3:
        return 'O'
    elif x == 3:
        return 'X'
    else:
        return False
    
def v_lateal(table:list) -> str | bool:
    bolinha:int = 0
    x:int = 0
    size:int = len(table)
    for i in range(size):
        x = 0
        bolinha = 0
        for j in range(size):
            if table[i][j] == 'O':
                bolinha += 1
            elif table[i][j] == 'X':
                x += 1
            if bolinha == 3:
                return 'O'
            elif x == 3:
                return 'X'
    return False
        
def v_horizontal(table:list) -> str | bool:
    x:int = 0
    bolinha:int = 0
    count:int = 0
    size:int = len(table)
    for i in range(size):
        x = 0
        bolinha = 0
        for j in range(size):
            if table[j][i] == 'O':
                bolinha += 1
            elif table[j][i] == 'X':
                x += 1
            if x == 3:
                return 'X'
            elif bolinha == 3:
                return 'O'
    return False

def t_position(words) -> None:
    split = list(words)
    lette: str = split[0]
    number:int = int(split[1])
    letter = lette.upper()
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

def print_table(table:list) -> None:
    print("     1   2  3\n")
    print(f"A    {table[0][0]} | {table[0][1]} | {table[0][2]}")
    print("     ---------")
    print(f"B    {table[1][0]} | {table[1][1]} | {table[1][2]}")
    print("     ---------")
    print(f"C    {table[2][0]} | {table[2][1]} | {table[2][2]}")

def all_v(table):
    if (result := v_vertical_01(table)) or (result := v_vertical_02(table)) or (result := v_horizontal(table)) or (result := v_lateal(table)):
        return result
    return False
    
def main():
    rodadas:int = 0
    print("\n--- Jogo da velha ---\n")
    x, b = 0, 0

    while rodadas < 10:

        # play_x(table, rodadas)
        # play_b(table, rodadas)

        print(f" Rodada {rodadas}/9")
        print("\nJogador ( - X - ):")
        print_table(table)
        j1 = input("\nEsclha uma posição: ") 

        clear_terminal()
        v_x = insert_X(table, j1)
        if v_x == False:
            print("\n !!!  Posição já escolhida !!!\n ")
            continue
        clear_terminal()

        rodadas += 1
        result = all_v(table)
        if result == 'X':
            print ("\n --- X Venceu --- \n")
            print_table(table)

            print("\n FIM DE JOGO \n!")
            break
        clear_terminal()
        print(f"\n Rodada {rodadas}/9\n")
        print("\njogador ( - O - ):")
        print_table(table)

        j2 = input("\n Escolha uma posição: \n\n")
        clear_terminal()
        v_b = insert_B(table, j2)


        if v_b == False:
            print("\n !!! Posição já escolhida !!! \n")
            continue

 
        print_table(table)
        rodadas += 1
        result = all_v(table)
        if result == 'O':
            print ("\n --- Bolinha Venceu ---\n")
            print_table(table)
            print("\n FIM DE JOGO \n!")
            break
            
        if rodadas == 9:
            print("\n\n ---- Empate!! ---- \n")

            print("\n FIM DE JOGO \n!")
            break
     
main()
