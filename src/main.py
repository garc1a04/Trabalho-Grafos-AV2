import os
from algs4.graph import Graph
from algs4.depth_first_paths import DepthFirstPaths
from algs4.breadth_first_paths import BreadthFirstPaths

# Mapeamento para facilitar a leitura
ESTADOS = {
    0: "AL", 1: "BA", 2: "CE", 3: "MA", 4: "PB", 
    5: "PE", 6: "PI", 7: "RN", 8: "SE"
}

def carregar_grafo():
    caminho_arquivo = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "data", "nordeste.txt")
    try:
        with open(caminho_arquivo, 'r') as f:
            V = int(f.readline().strip())
            E = int(f.readline().strip())
            g = Graph(V)
            for _ in range(E):
                linha = f.readline().split()
                if linha:
                    g.add_edge(int(linha[0]), int(linha[1]))
            return g, V
    except FileNotFoundError:
        print("Erro: Arquivo 'nordeste.txt' não encontrado.")
        return None, 0

def exibir_caminho(path_iter):
    if path_iter is None: return "Nenhum caminho encontrado"
    return " -> ".join([ESTADOS[v] for v in path_iter])


def main():
    g, V = carregar_grafo()
    if not g: return

    print("--- Analisador de Fronteiras do Nordeste ---")
    origem = int(input("Digite o ID do estado de ORIGEM (0-8): "))
    destino = int(input("Digite o ID do estado de DESTINO (0-8): "))

    # Execução dos Algoritmos
    dfs = DepthFirstPaths(g, origem)
    bfs = BreadthFirstPaths(g, origem)

    print(f"\nResultados de {ESTADOS[origem]} para {ESTADOS[destino]}:")
    print("-" * 40)
    
    # 1. Possibilidade de chegar
    possivel = dfs.has_path_to(destino)
    print(f"É possível chegar por terra? {'Sim' if possivel else 'Não'}")
    
    print(f"Caminho encontrado pela DFS: {exibir_caminho(dfs.path_to(destino))}")

    print(f"Caminho encontrado pela BFS: {exibir_caminho(bfs.path_to(destino))}")

    # 4. Estados alcançáveis
    alcansaveis = sum(1 for i in range(V) if dfs.has_path_to(i))
    print(f"Total de estados alcançáveis a partir de {ESTADOS[origem]}: {alcansaveis}")

if __name__ == "__main__":
    main()