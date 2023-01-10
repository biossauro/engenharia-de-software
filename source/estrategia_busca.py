class EstrategiaDeBusca():
    def __init__(self, problema):
        '''
        Construtor.

        Args:
            - problema: objeto do problema a ser solucionado
        '''
        self.problema = problema

    def compara_estados(self, estado, estado_visitado):
        '''
        Compara dois estados.
        Caso haja alguma diferença, retorna False, senão retorna True.

        Args:
            - estado: estado atual
            - estado_visitado: estado para fazer a comparação com o estado atual
        Return:
            - Retorna se os estados são iguais ou não
        '''
        for i in range(self.problema.tamanho):
            for j in range(self.problema.tamanho):
                if estado[i, j] != estado_visitado[i, j]:
                    return False
        return True

    def verifica_visitados(self, estado, estados_visitados):
        '''
        Verifica se um estado está na lista de visitados.

        Args:
            - estado: estado atual
            - estados_visitados: lista com todos os estados visitados
        '''
        for estado_i in estados_visitados:
            if self.compara_estados(estado, estado_i):
                return True
        return False
