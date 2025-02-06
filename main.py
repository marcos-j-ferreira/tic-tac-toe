table: list = [
#    a  b  c
    [1, 2, 3], # 0
    [4, 5, 6], # 1
    [7, 8, 9]  # 2
]


def v_vertical_01(table:list) -> str:

    x:int = 0
    bolinha:int = 0 

    if table[0][0] == 1 and table[1][1] == 1 and table[2][2] == 1:
        bolinha = 3
    elif table[0][0] == 2 and table[1][1] == 2 and table[2][2] == 2:
        x = 3
    
    if bolinha == 3:
        return 'bolinha'
    elif x == 3:
        return 'x'
    else:
        return False

def v_vertical_02(table:list) -> str:

    x:int = 0
    bolinha:int = 0 

    if table[0][2] == 1 and table[1][1] == 1 and table[2][0] == 1:
        bolinha = 3
    elif table[0][2] == 2 and table[1][1] == 2 and table[2][0] == 2:
        x = 3
    
    if bolinha == 3:
        return 'bolinha'
    elif x == 3:
        return 'x'
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

            if table[i][j] == 2:
                bolinha += 1
            elif table[i][j] == 1:
                x += 1

            if bolinha == 3:
                return 'bolinha'
            elif x == 3:
                return 'x'
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

            if table[j][i] == 2:
                bolinha += 1
            elif table[j][i] == 1:
                x += 1


            if x == 3:
                return 'x'
            elif bolinha == 3:
                return 'bolinha'
    
    return False

def t_position(words) -> None:

    split = list(words)
    lette: str = split[0]
    
    number:int = int(split[1])
    letter = lette.upper()
