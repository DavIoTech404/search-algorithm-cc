import json


# Função para ler o grafo do arquivo JSON
def ler_grafo(arquivo):
    with open(arquivo, 'r') as file:
        grafo = json.load(file)
    return grafo


# Implementação do algoritmo de Dijkstra para encontrar o caminho mais curto
def dijkstra(grafo, origem, destino):

    # Inicializa as distâncias com infinito e a distância para a origem como 0
    distancias = {vertice: float('infinity') for vertice in grafo}
    distancias[origem] = 0
    anteriores = {vertice: None for vertice in grafo}
    vertices = grafo.copy()

    # Loop para visitar cada vértice (cidade) no grafo
    while vertices:

        # Percorre todas as Cidades
        # Seleciona o vértice com a menor distância ainda não visitado
        vertice_atual = min(vertices, key=lambda vertice: distancias[vertice])

        # Interrompe o loop se o vértice mais próximo estiver inacessível
        if distancias[vertice_atual] == float('infinity'):
            break

        # Filtro
        # Atualiza as distâncias para os vizinhos do vértice atual
        for vizinho, custo in grafo[vertice_atual].items():
            caminho_alternativo = distancias[vertice_atual] + custo
            if caminho_alternativo < distancias[vizinho]:
                distancias[vizinho] = caminho_alternativo
                # anteriores: para cada cidade, armazena o vértice anterior que
                # faz parte do caminho mais curto encontrado até aquele ponto
                anteriores[vizinho] = vertice_atual

        # Remove o vértice atual do conjunto de vértices ainda a visitar
        vertices.pop(vertice_atual)

    # Tratamento do Resultado
    # Constrói o caminho percorrendo de trás para frente a partir do destino
    caminho, vertice_atual = [], destino
    while vertice_atual is not None:
        caminho.append(vertice_atual)
        vertice_atual = anteriores[vertice_atual]
    caminho = caminho[::-1]

    # Retorna o caminho se possível
    if caminho[0] == origem:
        return caminho
    else:
        return "Não é possível chegar ao destino."


# Carregar o grafo do arquivo
grafo_romenia = ler_grafo('grafo_romenia.json')

# Encontrar o caminho mais curto de Arad a Bucharest
caminho = dijkstra(grafo_romenia, 'Arad', 'Bucharest')
print(caminho)
