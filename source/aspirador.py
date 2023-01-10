import numpy as np


class Aspirador():
    def __init__(self, tamanho):
        '''
        Construtor.

        Args:
            - tamanho: quantidade de linhas e colunas
        '''
        self.tamanho = tamanho

    def encontra_posicao(self, estado, elemento):
        '''
        Varre todo o tabuleiro (estado) e verifica em qual posição 'elemento' está.

        Args:
            - estado: matriz contendo o estado do tabuleiro
            - elemento: elemento a ser buscado na matriz
        Return:
            - Retorna a linha e coluna onde o elemento se encontra
        '''
        for i in range(self.tamanho):
            for j in range(self.tamanho):
                if estado[i, j] == elemento:
                    return i, j
        return None, None

    def verifica_objetivo(self, estado):
        '''
        Verifica se o estado atual é o objetivo.

        Objetivo:
            - Não haver sujeira ("i") -> Todos blocos, exceto onde o aspirador está devem ser "o".
        Args:
            - estado: estado atual do tabuleiro
        Return:
            - booleano dizendo se o estado atual é ou não o objetivo
        '''
        item, cont = np.unique(estado, return_counts=True)
        mapa = dict()
        for i in range(len(item)):
            mapa[item[i]] = cont[i]
        # Todos elementos exceto onde o aspirador está
        if mapa['o'] == (self.tamanho**2 - 1):
            return True
        return False

    def expande_estados(self, atual):
        '''
        Dado o estado atual, realiza a expansão de estados.

        Args:
            - atual: matriz que descreve o estado atual
        Return:
            - lista com os novos estados após a expansão
        '''
        novos_estados = []
        linha, coluna = self.encontra_posicao(atual, 'x')
        # Cima
        if linha > 0:
            novo_estado = np.copy(atual)
            nova_linha = linha - 1
            novo_estado[nova_linha, coluna] = 'x'
            novo_estado[linha, coluna] = 'o'
            novos_estados.append(novo_estado)
        # Baixo
        if linha < self.tamanho - 1:
            novo_estado = np.copy(atual)
            nova_linha = linha + 1
            novo_estado[nova_linha, coluna] = 'x'
            novo_estado[linha, coluna] = 'o'

            novos_estados.append(novo_estado)
        # Esquerda
        if coluna > 0:
            novo_estado = np.copy(atual)
            nova_coluna = coluna - 1
            novo_estado[linha, nova_coluna] = 'x'
            novo_estado[linha, coluna] = 'o'
            novos_estados.append(novo_estado)
        # Direita
        if coluna < self.tamanho - 1:
            novo_estado = np.copy(atual)
            nova_coluna = coluna + 1
            novo_estado[linha, nova_coluna] = 'x'
            novo_estado[linha, coluna] = 'o'
            novos_estados.append(novo_estado)
        return novos_estados

    def heuristica(self, estado):
        '''
        Dado o estado atual, retorna o número de elementos sujos 'i'.

        Args:
            - estado: matriz contendo o estado do tabuleiro
        Return:
            - número de elementos sujos 'i'
        '''
        return np.count_nonzero(estado == 'i')
