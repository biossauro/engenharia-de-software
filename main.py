from os import system, name as system_name
from src.questao_1 import calculate_shortest_path
from src.questao_2 import calculate_maximum_flow


def calcula_valor_arcos(num_matricula: int) -> dict:
    a = (num_matricula % 5) + 1
    b = sum([int(digit) for digit in str(num_matricula)])
    valor_arcos = {
        "A": a + b,
        "B": a,
        "C": b,
        "D": a + 5,
        "E": b - 2,
        "F": a + 3,
        "G": b - 3,
        "H": a + 4,
        "I": b - 4,
        "J": a,
        "K": a + b,
        "L": b - 2,
        "M": a + 4,
        "N": b - 4,
        "O": b,
        "P": a + 5,
        "Q": b - 3,
        "R": a + 1,
        "S": a + 3,
        "T": b - 2,
        "U": b - 4
    }
    return valor_arcos


def clear_console():
    system("cls" if system_name == "nt" else "clear")


def pause():
    input()


if __name__ == "__main__":
    clear_console()
    # ----------------- Matrícula -----------------
    matricula = int(input("Matrícula: "))
    valor_arcos = calcula_valor_arcos(matricula)
    pause()
    clear_console()
    # ----------------- Questão 1 -----------------
    # print("Questão 01 - Shortest Path\n")
    calculate_shortest_path(valor_arcos)
    pause()
    clear_console()
    # ----------------- Questão 2 -----------------
    # print("Questão 02 - Maximum Flow\n")
    calculate_maximum_flow(valor_arcos)
    pause()
    clear_console()
