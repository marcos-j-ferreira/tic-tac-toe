def v_vertical_01(table: list) -> str:
    if table[0][0] == 'X' and table[1][1] == 'X' and table[2][2] == 'X':
        return 'X'
    if table[0][0] == 'O' and table[1][1] == 'O' and table[2][2] == 'O':
        return 'O'
    return False

def v_vertical_02(table: list) -> str:
    if table[0][2] == 'X' and table[1][1] == 'X' and table[2][0] == 'X':
        return 'X'
    if table[0][2] == 'O' and table[1][1] == 'O' and table[2][0] == 'O':
        return 'O'
    return False

def v_lateal(table: list) -> str | bool:
    for row in table:
        if row.count('X') == 3:
            return 'X'
        if row.count('O') == 3:
            return 'O'
    return False

def v_horizontal(table: list) -> str | bool:
    for col in range(3):
        x_count = sum(1 for row in table if row[col] == 'X')
        o_count = sum(1 for row in table if row[col] == 'O')
        if x_count == 3:
            return 'X'
        if o_count == 3:
            return 'O'
    return False

def all_v(table):
    if (result := v_vertical_01(table)) or (result := v_vertical_02(table)) or (result := v_horizontal(table)) or (result := v_lateal(table)):
        return result
    return False
