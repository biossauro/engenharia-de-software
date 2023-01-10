from queue import LifoQueue
from source.estrategia_busca import EstrategiaDeBusca


class DepthFirstSearch(EstrategiaDeBusca):
    def __init__(self, problema):
        EstrategiaDeBusca.__init__(self, problema)

    def busca(self, inicio):
        '''
        Realiza a busca DFS, armazenando os estados em uma PILHA
        Args:
            - inicio: estado inicial do problema
            - fim: estado objetivo
        Return:
            - booleano se a solução foi encontrada, lista dos estados visitados, quantidade de estados visitados
        '''
        piha = LifoQueue()
        piha.put(inicio)
        solucao_encontrada = False
        estados_visitados = []
        cont_estados = 0
        while not piha.empty():
            atual = piha.get()
            estados_visitados.append(atual)
            if self.problema.verifica_objetivo(atual):
                solucao_encontrada = True
                break
            else:
                cont_estados += 1
                novos_estados = self.problema.expande_estados(atual)
                for i in novos_estados:
                    if not self.verifica_visitados(i, estados_visitados):
                        piha.put(i)
        return solucao_encontrada, estados_visitados, cont_estados
