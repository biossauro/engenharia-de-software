import heapq
from source.estrategia_busca import EstrategiaDeBusca


class BuscaGulosa(EstrategiaDeBusca):
    def __init__(self, problema):
        EstrategiaDeBusca.__init__(self, problema)

    def busca(self, inicio):
        '''
        Realiza a busca gulosa, armazenando os estados em uma FILA DE PRIORIDADES

        Args:
            - inicio: estado inicial do problema
            - fim: estado objetivo
        Return:
            - booleano se a solução foi encontrada, lista dos estados visitados, quantidade de estados visitados

        Obs.: A distância de Manhattan é inversamente proporcional à prioridade, quanto menor a distância, maior
        a prioridade desse estado.
        '''
        p_fila = []
        # H, ID, elemento
        id_estado = 0
        heapq.heappush(p_fila, (0, id_estado, inicio))
        solucao_encontrada = False
        estados_visitados = []
        cont_estados = 0
        while not len(p_fila) == 0:
            atual = heapq.heappop(p_fila)[2]
            estados_visitados.append(atual)
            if self.problema.verifica_objetivo(atual):
                solucao_encontrada = True
                break
            else:
                cont_estados += 1
                novos_estados = self.problema.expande_estados(atual)
                for i in novos_estados:
                    if not self.verifica_visitados(i, estados_visitados):
                        id_estado += 1
                        posicoes_sujas = self.problema.heuristica(i)
                        heapq.heappush(p_fila, (posicoes_sujas, id_estado, i))
        return solucao_encontrada, estados_visitados, cont_estados
