import os

# Constants
EMPTY = 0
PLAYER_X = 'X'
PLAYER_O = 'O'
BOARD_SIZE = 3

# Function to clear the terminal
def clear_terminal():
    # Clear command for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear command for macOS and Linux
    else:
        os.system('clear')

# Initialize the board
table: list = [[EMPTY for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def check_winner(table: list) -> str | bool:
    # Check rows, columns, and diagonals
    for i in range(BOARD_SIZE):
        # Check rows
        if table[i][0] == table[i][1] == table[i][2] != EMPTY:
            return table[i][0]
        # Check columns
        if table[0][i] == table[1][i] == table[2][i] != EMPTY:
            return table[0][i]
    # Check diagonals
    if table[0][0] == table[1][1] == table[2][2] != EMPTY:
        return table[0][0]
    if table[0][2] == table[1][1] == table[2][0] != EMPTY:
        return table[0][2]
    return False

def t_position(words) -> tuple:
    split = list(words)
    letter = split[0].upper()
    number = int(split[1])
    return letter, number

def insert_move(table: list, words: str, player: str) -> bool:
    letter, number = t_position(words)
    column = ord(letter) - ord('A')
    if table[column][number - 1] in [PLAYER_X, PLAYER_O]:
        return False
    table[column][number - 1] = player
    return True

def print_table(table: list) -> None:
    print("     1   2   3\n")
    for i in range(BOARD_SIZE):
        print(f"{chr(ord('A') + i)}    {table[i][0]} | {table[i][1]} | {table[i][2]}")
        if i < BOARD_SIZE - 1:
            print("    -----------")

def main():
    rodadas = 0
    print("\n--- Jogo da velha ---\n")

    while rodadas < 9:
        clear_terminal()  # Clear the terminal before printing the table
        print(f" Rodada {rodadas + 1}/9")
        print("\nJogador ( - X - ):")
        print_table(table)
        j1 = input("\nEscolha uma posição (ex: A1): ")

        if not insert_move(table, j1, PLAYER_X):
            print("\n !!! Posição já escolhida ou inválida !!!\n")
            input("Pressione Enter para continuar...")  # Wait for user input before continuing
            continue

        rodadas += 1
        result = check_winner(table)
        if result == PLAYER_X:
            clear_terminal()
            print("\n --- X Venceu --- \n")
            print_table(table)
            print("\n FIM DE JOGO \n!")
            break

        if rodadas == 9:
            clear_terminal()
            print("\n\n ---- Empate!! ---- \n")
            print("\n FIM DE JOGO \n!")
            break

        clear_terminal()  # Clear the terminal before printing the table
        print(f"\n Rodada {rodadas + 1}/9\n")
        print("\nJogador ( - O - ):")
        print_table(table)

        j2 = input("\nEscolha uma posição (ex: A1): \n\n")
        if not insert_move(table, j2, PLAYER_O):
            print("\n !!! Posição já escolhida ou inválida !!! \n")
            input("Pressione Enter para continuar...")  # Wait for user input before continuing
            continue

        rodadas += 1
        result = check_winner(table)
        if result == PLAYER_O:
            clear_terminal()
            print("\n --- O Venceu ---\n")
            print_table(table)
            print("\n FIM DE JOGO \n!")
            break

if __name__ == "__main__":
    main()