table: list = [
#    a  b  c
    [0, 0, 0], # 0
    [0, 0, 0], # 1
    [0, 8, 0]  # 2
]


def v_vertical_01(table:list) -> str:

    x:int = 0
    bolinha:int = 0 

    if table[0][0] == 'X' and table[1][1] == 'X' and table[2][2] == 'X':
        bolinha = 3
    elif table[0][0] == 'O' and table[1][1] == 'O' and table[2][2] == 'O':
        x = 3
    
    if bolinha == 3:
        return 'B'
    elif x == 3:
        return 'X'
    else:
        return False

def v_vertical_02(table:list) -> str:

    x:int = 0
    bolinha:int = 0 

    if table[0][2] == 'X' and table[1][1] == 'X' and table[2][0] == 'X':
        bolinha = 3
    elif table[0][2] == 'O' and table[1][1] == 'O' and table[2][0] == 'O':
        x = 3
    
    if bolinha == 3:
        return 'B'
    elif x == 3:
        return 'X'
    else:
        return False

#bolinha = 1
# x = 2

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
                return 'B'
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
                return 'B'
    
    return False

def t_position(words) -> None:

    split = list(words)
    lette: str = split[0]
    
    number:int = int(split[1])
    letter = lette.upper()

    return letter, number

def insert_B(table:list, words)-> bool:

    data:tuple = t_position(words)

    letter:str = data[0]
    data_int:int = data[1]
    size:int = data_int - 1

    if letter == 'A':
        table[0][size] = 'O'
        
    elif letter == 'B':
        table[0] [size] = 'O'
    else:
        table[0] [size] = 'O'

def insert_X(table:list, words)-> bool:

    data:tuple = t_position(words)

    letter:str = data[0]
    data_int:int = data[1]
    size:int = data_int - 1

    if letter == 'A':
        table[0][size] = 'X'
        
    elif letter == 'B':
        table[0] [size] = 'X'
    else:
        table[0] [size] = 'X'

    return True

def print_table(table:list) -> None:

    print("     1   2  3\n")
    print(f"A    {table[0][0]} | {table[0][1]} | {table[0][2]}")
    print("     ---------")
    print(f"B    {table[1][0]} | {table[1][1]} | {table[1][2]}")
    print("     ---------")
    print(f"C    {table[2][0]} | {table[2][1]} | {table[2][2]}")

def all_v(table):

    v1 = v_vertical_01(table)
    v2 = v_vertical_02(table)
    v3 = v_horizontal(table)
    v4 = v_lateal(table)

    if v1 == "X" or v2 == "X" or v3 == "X" or v4 == "X":
        return "X"
    elif v1 == "O" or v2 == "O" or v3 == "O" or v4 == "O":
        return "B"


def main():

    rodados:int = 0

    print("\n--- Jogo da velha ---\n")

    while rodados < 9:
        
        print("Jogador X:")
        print_table(table)

        j1 = input("\nEsclha uma posição: ") 

        insert_X(table, j1)


        print("jogador O:")

        print_table(table)

        j2 = input("\n Escolha uma posição: \n\n")

        insert_B(table, j2)

        print_table(table)

        result = all_v(table)

        if result == 'X':
            print ("X Venceu")
            break
        elif result == 'B':
            print("Bolinha venceu")
            break

main()