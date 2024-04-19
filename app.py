import json
from flask import Flask, jsonify, render_template, request

# Função para ler o grafo do arquivo JSON
def ler_grafo(arquivo):
    with open(arquivo, 'r') as file:
        grafo_romenia = json.load(file)
    return grafo_romenia

# Carregar o grafo do arquivo
grafo_romenia = ler_grafo('grafo_romenia.json')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', cities=list(grafo_romenia.keys()))

# Implementação do algoritmo de Dijkstra para encontrar o caminho mais curto
@app.route('/get_waypoints', methods=['POST'])
def dijkstra():

    origem = request.json['origin']
    destino = request.json['destination']

    # Inicializa as distâncias com infinito e a distância para a origem como 0
    distancias = {vertice: float('infinity') for vertice in grafo_romenia}
    distancias[origem] = 0
    anteriores = {vertice: None for vertice in grafo_romenia}
    vertices = grafo_romenia.copy()

    # Loop para visitar cada vértice (cidade) no grafo_romenia
    while vertices:

        # Percorre todas as Cidades
        # Seleciona o vértice com a menor distância ainda não visitado
        vertice_atual = min(vertices, key=lambda vertice: distancias[vertice])

        # Interrompe o loop se o vértice mais próximo estiver inacessível
        if distancias[vertice_atual] == float('infinity'):
            break

        # Filtro
        # Atualiza as distâncias para os vizinhos do vértice atual
        for vizinho, custo in grafo_romenia[vertice_atual].items():
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

    print(caminho)

    # Retorna o caminho se possível
    if caminho[0] == origem:
        if len(caminho) > 2:
            caminho.pop(0)
            caminho.pop(-1)
        return jsonify(['Romania, ' + cidade for cidade in caminho])
    else:
        return "Não é possível chegar ao destino."

if __name__ == '__main__':
    app.run(debug=True)