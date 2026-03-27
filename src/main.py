import os
from algs4.breadth_first_paths import BreadthFirstPaths
from algs4.graph import Graph
from algs4.cycle import Cycle
from algs4.cc import CC

caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "entrada.txt")

with open(caminho_arquivo, 'r') as f:
    V = int(f.readline())
    E = int(f.readline())
    graph = Graph(V)
    
    for _ in range(E):
        v, w = map(int, f.readline().split())
        graph.add_edge(v, w)

print("Lista de adjacência:")
for v in range(graph.V):
    adjacentes = " ".join(str(w) for w in graph.adj[v])
    print(f"{v}: {adjacentes}")
print()

cc = CC(graph)
print(f"Componentes conexas: {cc.count}")

componentes = [[] for _ in range(cc.count)]
for v in range(graph.V):
    componentes[cc.id[v]].append(v)

for i, comp in enumerate(componentes):
    print(f"Vértices da componente {i}:", *comp)
print()

origem = 0
destino = 8
BFS = BreadthFirstPaths(graph, origem)
path, dist = BFS.path_to(destino)

print("Caminho mínimo:", " ".join(str(v) for v in path))
print(f"Distância mínima entre o vértice {origem} e o vértice {destino}: {dist}\n")

cycle = Cycle(graph)
possui_ciclo = "Sim" if cycle.has_cycle else "Não"
print(f"O grafo possui ciclo: {possui_ciclo}")

if cycle.has_cycle and cycle.cycle:
    caminho_ciclo = " ".join(str(v) for v in cycle.cycle)
    print(f"Um ciclo encontrado: {caminho_ciclo}")

print("\nComplexidade:\nTempo: O(V + E)\nEspaço: O(V)")

bp = 1