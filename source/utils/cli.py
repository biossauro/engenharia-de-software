import os


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def pause():
    input("Pressione ENTER p/ continuar...")
