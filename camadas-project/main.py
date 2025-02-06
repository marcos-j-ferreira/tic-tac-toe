from board import print_table
from game_logic import all_v
from validation import insert_X, insert_B
from game_state import table

def main():
    rodadas: int = 0
    print("\n--- Jogo da velha ---\n")

    while rodadas < 9:
        print(f" Rodada {rodadas + 1}/9")
        print("\nJogador ( - X - ):")
        print_table(table)
        j1 = input("\nEscolha uma posição: ")

        if not insert_X(table, j1):
            print("\n !!! Posição já escolhida !!!\n ")
            continue

        rodadas += 1
        if (result := all_v(table)) == 'X':
            print("\n --- X Venceu --- \n")
            print_table(table)
            print("\n FIM DE JOGO \n!")
            break

        if rodadas == 9:
            print("\n\n ---- Empate!! ---- \n")
            print("\n FIM DE JOGO \n!")
            break

        print(f"\n Rodada {rodadas + 1}/9\n")
        print("\nJogador ( - O - ):")
        print_table(table)

        j2 = input("\n Escolha uma posição: \n\n")
        if not insert_B(table, j2):
            print("\n !!! Posição já escolhida !!! \n")
            continue

        rodadas += 1
        if (result := all_v(table)) == 'O':
            print("\n --- Bolinha Venceu ---\n")
            print_table(table)
            print("\n FIM DE JOGO \n!")
            break

if __name__ == "__main__":
    main()
