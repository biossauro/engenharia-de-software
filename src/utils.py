import os


def cli_clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def cli_pause():
    input('\nPress Enter to continue...')
