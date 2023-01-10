import numpy as np
import time
from source.aspirador import Aspirador
from source.busca_bfs import BreadthFirstSearch
from source.busca_dfs import DepthFirstSearch
from source.busca_gulosa import BuscaGulosa
from source.mostrar_resultados import *
from source.utils import *


start = np.array([['x', 'i', 'o'],
                  ['i', 'i', 'i'],
                  ['o', 'o', 'i']])

problema = Aspirador(3)

cls()

# BFS
print('BFS\n')
tempo = time.time()
bfs = BreadthFirstSearch(problema)
bfs_resultados = bfs.busca(start)
tempo_f = time.time() - tempo
mostrar_resultados(bfs_resultados, tempo_f)
pause()
cls()

# DFS
print('DFS\n')
tempo = time.time()
dfs = DepthFirstSearch(problema)
dfs_resultados = dfs.busca(start)
tempo = time.time() - tempo
mostrar_resultados(dfs_resultados, tempo)
pause()
cls()

# Busca Gulosa
print('Busca Gulosa\n')
tempo = time.time()
bg = BuscaGulosa(problema)
bg_resultados = bg.busca(start)
tempo = time.time() - tempo
mostrar_resultados(bg_resultados, tempo)
pause()
cls()
