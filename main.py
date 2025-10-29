import typer
from typing import Optional


def explorar_caminho(
  grafo: dict[int, list[int]],
  num_vertices: int,
  caminho_atual: list[int],
  visitados: set[int]
) -> Optional[list[int]]:

  # Passo 1 (Exploração): Caso base - Se visitamos todos os vértices, encontramos o caminho
  if len(caminho_atual) == num_vertices:
    return caminho_atual.copy()

  # Passo 2 (Exploração): Obter o último vértice adicionado ao caminho
  ultimo_vertice = caminho_atual[-1] if caminho_atual else 0

  # Passo 3 (Exploração): Tentar adicionar cada vizinho não visitado ao caminho
  for vizinho in grafo.get(ultimo_vertice, []):

    # Passo 4 (Exploração): Verificar se o vértice ainda não foi visitado
    if vizinho not in visitados:

      # Passo 5 (Exploração): Adicionar o vértice ao caminho (backtracking - escolha)
      caminho_atual.append(vizinho)
      visitados.add(vizinho)

      # Passo 6 (Exploração): Chamada recursiva para continuar construindo o caminho
      resultado = explorar_caminho(
        grafo,
        num_vertices,
        caminho_atual,
        visitados
      )

      # Passo 7 (Exploração): Se encontrou solução, retornar
      if resultado is not None:
        return resultado

      # Passo 8 (Exploração): Backtracking - desfazer escolha se não levou a solução
      caminho_atual.pop()
      visitados.remove(vizinho)

  # Passo 9 (Exploração): Nenhum caminho encontrado a partir deste estado
  return None


def encontrar_caminho_hamiltoniano(
  num_vertices: int,
  arestas: list[tuple[int, int]],
  direcionado: bool = False
) -> Optional[list[int]]:

  # Passo 1 (CaminhoHamiltoniano): Construir o grafo como lista de adjacências
  grafo: dict[int, list[int]] = {i: [] for i in range(num_vertices)}

  for origem, destino in arestas:
    grafo[origem].append(destino)

    # Passo 2 (CaminhoHamiltoniano): Se o grafo não é direcionado, adicionar aresta reversa
    if not direcionado:
      grafo[destino].append(origem)

  # Passo 3 (CaminhoHamiltoniano): Tentar iniciar o caminho a partir de cada vértice
  for vertice_inicial in range(num_vertices):
    caminho = [vertice_inicial]
    visitados = {vertice_inicial}

    # Passo 4 (CaminhoHamiltoniano): Buscar caminho hamiltoniano começando deste vértice
    resultado = explorar_caminho(
      grafo,
      num_vertices,
      caminho,
      visitados
    )

    # Passo 5 (CaminhoHamiltoniano): Se encontrou, retornar o caminho
    if resultado is not None:
      return resultado

  # Passo 6 (CaminhoHamiltoniano): Nenhum caminho hamiltoniano existe
  return None


def main(
  arestas: str = typer.Option(..., "--arestas", "-a", help="Arestas (ex '0-1,1-2,2-3')"),
  direcionado: bool = typer.Option(False, "--direcionado", "-d", help="Define que o grafo é direcionado")
):

  # Passo 1 (Main): Processar a string de arestas
  lista_arestas = []
  vertices_unicos = set()

  for aresta in arestas.split(","):
    origem, destino = map(int, aresta.strip().split("-"))
    lista_arestas.append((origem, destino))
    vertices_unicos.add(origem)
    vertices_unicos.add(destino)

  # Passo 2 (Main): Calcular o número de vértices a partir das arestas
  num_vertices = len(vertices_unicos)

  # Passo 3 (Main): Buscar o caminho hamiltoniano
  caminho = encontrar_caminho_hamiltoniano(num_vertices, lista_arestas, direcionado)

  # Passo 4 (Main): Exibir resultado
  if caminho:
    print(f"Caminho encontrado: {' > '.join(map(str, caminho))}")
  else:
    print("Nenhum caminho hamiltoniano encontrado")


if __name__ == "__main__":
  typer.run(main)
