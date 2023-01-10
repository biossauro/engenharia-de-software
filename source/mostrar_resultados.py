import numpy as np


def mostrar_resultados(resultados, tempo):
    solucao, _, num_visitados = resultados
    print(f'- Finalizado em {np.format_float_scientific(tempo)} segundos.\n')
    print(f'- Foram visitados {num_visitados} estados.\n')
    if solucao:
        print('- A solução foi encontrada! =)\n')
    else:
        print('- A solução não foi encontrada! =(\n')
