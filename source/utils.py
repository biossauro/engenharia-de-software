import os


def cls():
    '''
    Limpa a tela.
    '''
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    '''
    Pausa a execução do programa.
    '''
    input('Pressione <ENTER> para continuar...')
