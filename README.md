# Apresentação do Algoritmo de Busca 

## Caminho Mais Curto em Romênia

Este repositório contém a implementação do algoritmo de Dijkstra para encontrar o caminho mais curto entre cidades na Romênia, especificamente de Arad a Bucharest. Utilizamos um grafo onde os nós representam cidades e as arestas representam as distâncias em quilômetros entre essas cidades.

## Estrutura do Grafo

O grafo é definido em um dicionário de Python, onde cada chave é uma cidade e o valor correspondente é outro dicionário. Os dicionários internos têm cidades vizinhas como chaves e distâncias como valores. O grafo foi atualizado para incluir várias cidades importantes como Deva, Alba Iulia, Petroșani, Ploiești, Brașov, Slatina e Alexandria. Aqui está um exemplo do grafo:

```python
grafo_romenia = {
    'Arad': {'Timisoara': 118, 'Sibiu': 140, 'Zerind': 75},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90},
    'Deva': {'Alba Iulia': 70, 'Petrosani': 95},
    ...
}
```

## Algoritmo de Dijkstra

O algoritmo de Dijkstra é usado para encontrar o caminho mais curto de um ponto de origem a um ponto de destino em um grafo. A função Dijkstra recebe o grafo, a cidade de origem e a cidade de destino como argumentos e retorna o caminho mais curto entre eles. A implementação considera todas as conexões e distâncias para calcular a rota mais eficiente.

### Como Usar

Para utilizar este código:

1. Clone o repositório em seu ambiente local.
2. Certifique-se de ter Python instalado em sua máquina.
3. Execute o arquivo Python que contém o código do algoritmo de Dijkstra.
4. Você pode modificar as cidades de origem e destino no código para explorar diferentes caminhos.