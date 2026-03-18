import os
import numpy as np
from algs4.graph import Graph
from algs4.depth_first_paths import DepthFirstPaths
from algs4.breadth_first_paths import BreadthFirstPaths

caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "nordeste.txt")

with open(caminho_arquivo, 'r') as f:
        V = int(f.readline())
        E = int(f.readline())
        
        g = Graph(V)
        for _ in range(E):
            linha = f.readline().split()
            if linha:
                v = int(linha[0])
                w = int(linha[1])
                g.add_edge(v, w)
                
"""
Perguntas que o programa deve responder

Dado o estado de origem X e o estado de destino Y, é possível sair de X e chegar a Y atravessando apenas fronteiras terrestres?

Qual caminho foi encontrado pela DFS do estado de origem X até o estado de destino Y?

Qual caminho foi encontrado pela BFS do estado de origem X até o estado de destino Y?

Qual foi a ordem de visita dos estados na execução da DFS a partir de X?

Qual foi a ordem de visita dos estados na execução da BFS a partir de X?

R: Sim
"""

print(g)

X = int(input("\ndigite um estado de origem\n0 (AL) 1 (BA)  2 (CE)  3 (MA)  4 (PB)  5 (PE) 6 (PI)  7 (RN) 8 (SE)"))

dfs = DepthFirstPaths(g, X)

Y = int(input("\ndigite um estado de destino\n0 (AL) 1 (BA)  2 (CE)  3 (MA)  4 (PB)  5 (PE) 6 (PI)  7 (RN) 8 (SE)\n"))
print(dfs.has_path_to(Y))
print(dfs.path_to(Y))

"""
BFS
"""

x = int(input("\ndigite um estado de origem\n0 (AL) 1 (BA)  2 (CE)  3 (MA)  4 (PB)  5 (PE) 6 (PI)  7 (RN) 8 (SE)"))

bfs = BreadthFirstPaths(g, x)

y = int(input("\ndigite um estado de destino\n0 (AL) 1 (BA)  2 (CE)  3 (MA)  4 (PB)  5 (PE) 6 (PI)  7 (RN) 8 (SE)\n"))
print(bfs.has_path_to(y))
print(bfs.path_to(y))

bp = 1


"""
Quantos estados são alcançáveis a partir do estado de origem X?
"""

count_dfs = 0
count_bfs = 0
for i in range(0, V):
    if dfs.has_path_to(i):
        count_dfs+=1
    if bfs.has_path_to(i):
        count_bfs+=1
        
print(count_dfs)
print(count_bfs)

bp = 1