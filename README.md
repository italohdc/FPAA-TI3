# FPAA-TI3

> **Fundamentos de Programação e Algoritmos Avançados**
> 
> Trabalho Individual 3 - Implementação do Algoritmo para
Caminho Hamiltoniano em Python


## Descrição do projeto

Este projeto tem como objetivo implementar, e explicar, o
funcionamento do algoritmo de Caminho Hamiltoniano.

### Como o algoritmo funciona

O algoritmo de Caminho Hamiltoniano é um método utilizado para
encontrar um caminho em um grafo que visita cada vértice exatamente
uma vez. O algoritmo pode ser implementado utilizando técnicas de
backtracking, onde o algoritmo tenta construir o caminho passo a
passo, verificando se o próximo vértice pode ser adicionado ao
caminho atual sem violar as condições do problema.

### Explicação do código

No código, o algoritmo de busca de caminho hamiltoniano está
implementado através de três funções principais:
`explorar_caminho`, `encontrar_caminho_hamiltoniano` e `main`.

A função `explorar_caminho` é o núcleo do algoritmo, utilizando
backtracking recursivo para encontrar um caminho que visite todos
os vértices exatamente uma vez. A função `encontrar_caminho_hamiltoniano`
prepara a estrutura de dados do grafo e coordena a busca. A função
`main` processa os argumentos da linha de comando e exibe os resultados.

Como trata-se de um código com responsabilidades bem definidas, porém
relacionadas, foi escolhido manter todo o conteúdo no arquivo main.py.
Dessa forma, fica mais fácil visualizar o fluxo completo.

Abaixo, é explicado cada passo do código. Como o código está
divido em três funções, a explicação foi organizada por função e
por ordem de chamada.

```
main() -> encontrar_caminho_hamiltoniano() -> explorar_caminho()
```

#### Função `main`

`Linha 91` | `Passo 1 (Main)`: Processamento da entrada

Converte a string de arestas fornecida via linha de comando em uma
lista de tuplas. Simultaneamente, coleta todos os vértices únicos
mencionados nas arestas.

`Linha 101` | `Passo 2 (Main)`: Contagem de vértices

Calcula o número total de vértices do grafo a partir dos vértices
únicos encontrados nas arestas.

`Linha 104` | `Passo 3 (Main)`: Execução do algoritmo

Chama a função principal que busca o caminho hamiltoniano com os
parâmetros processados.

`Linha 107` | `Passo 4 (Main)`: Exibição do resultado

Formata e exibe o resultado. Se encontrou um caminho, mostra os
vértices ordenados. Caso contrário, informa que não existe
caminho hamiltoniano.

#### Função `encontrar_caminho_hamiltoniano`

`Linha 55` | `Passo 1 (CaminhoHamiltoniano)`: Construção do grafo

Cria um dicionário representando o grafo como lista de adjacências,
onde cada vértice mapeia para uma lista de seus vizinhos.

`Linha 61` | `Passo 2 (CaminhoHamiltoniano)`: Preenchimento das arestas

Adiciona as arestas ao grafo. Se o grafo não é direcionado, adiciona
também a aresta reversa para permitir travessia bidirecional.

`Linha 65` | `Passo 3 (CaminhoHamiltoniano)`: Tentativa a partir de cada vértice

Itera por todos os vértices possíveis como ponto de partida, pois um
caminho hamiltoniano pode começar de qualquer vértice.

`Linha 70` | `Passo 4 (CaminhoHamiltoniano)`: Busca do caminho

Invoca a função de exploração recursiva para tentar encontrar um caminho
hamiltoniano a partir do vértice atual, com estado inicial preparado.

`Linha 78` | `Passo 5 (CaminhoHamiltoniano)`: Retorno da solução

Se encontrou um caminho válido, retorna imediatamente sem tentar outros
vértices iniciais.

`Linha 82` | `Passo 6 (CaminhoHamiltoniano)`: Falha na busca

Se nenhum vértice inicial levou a um caminho hamiltoniano, retorna `None`
indicando que o grafo não possui tal caminho.

#### Função `explorar_caminho`

`Linha 12` | `Passo 1 (Exploração)`: Caso base - Solução encontrada

Verifica se todos os vértices foram visitados. Se o tamanho do caminho
atual é igual ao número de vértices do grafo, significa que encontramos
um caminho hamiltoniano válido. Retorna uma cópia do caminho para
preservar o resultado.

`Linha 16` | `Passo 2 (Exploração)`: Identificação do vértice atual

Obtém o último vértice adicionado ao caminho para continuar a exploração
a partir dele. Se o caminho está vazio, inicia do vértice 0.

`Linha 19` | `Passo 3 (Exploração)`: Iteração pelos vizinhos

Percorre todos os vizinhos do vértice atual para tentar expandir o
caminho. Essa é a fase de exploração do backtracking.

`Linha 22` | `Passo 4 (Exploração)`: Verificação de visitados

Garante que apenas vértices não visitados sejam considerados,
evitando ciclos inválidos no caminho hamiltoniano.

`Linha 25` | `Passo 5 (Exploração)`: Escolha (Backtracking)

Adiciona o vizinho ao caminho atual e marca como visitado. Esta é
a fase de "fazer uma escolha" do backtracking.

`Linha 29` | `Passo 6 (Exploração)`: Chamada recursiva

Continua explorando recursivamente a partir do novo estado, tentando
construir o restante do caminho hamiltoniano.

`Linha 37` | `Passo 7 (Exploração)`: Verificação de sucesso

Se a chamada recursiva retornou um resultado válido (não None),
propaga essa solução de volta na pilha de recursão.

`Linha 41` | `Passo 8 (Exploração)`: Desfazer escolha (Backtracking)

Se a escolha não levou a uma solução, desfaz as modificações
removendo o vértice do caminho e dos visitados. Esta é a fase de
"voltar atrás" do backtracking.

`Linha 45` | `Passo 9 (Exploração)`: Retorno de falha

Se nenhum vizinho levou a uma solução válida, retorna None indicando
que não há caminho hamiltoniano a partir deste estado.


## Como executar o projeto

Este projeto utiliza Python. Para rodar o projeto, você precisa ter
o Python instalado na sua máquina. Foi utilizado, durante o
desenvolvimento, o Python 3.13. Recomendo a utilização do
[PyEnv](https://github.com/pyenv/pyenv) para instalar e gerenciar as
versões do Python.

### Configurar ambiente virtual

Para configurar um ambiente virtual, você pode usar o `venv`.
Execute os seguintes criar e rodar um novo `venv`:

```
# Criar novo venv
python -m venv venv

# Executar o venv
source venv/bin/activate  # No Linux ou macOS
venv\Scripts\activate  # No Windows
```

### Instalar Dependências

Para instalar as dependências do projeto, execute o seguinte
comando na raiz do projeto:

```
pip install -r requirements.txt
```

### Sobre as dependências

Para este projeto, foram utilizadas algumas dependências para
auxiliar no desenvolvimento. Dentre elas:

[`typer`](https://typer.tiangolo.com/): Biblioteca para a criação
de CLI (Interfaces de Linha de Comando). Utilizada para facilitar
a inserção dos números a serem multiplicados.


### Rodar o projeto

Para rodar o projeto, você pode utilizar o seguinte comando:

```
# Comando
python main.py -a "<ARESTAS>" [-d: direcionado]


# == Exemplos ==
# Grafo não direcionado
python main.py -a "0-1,1-2,2-3,3-0"

# Grafo direcionado
python main.py -a "0-1,1-2,2-3,3-4,4-0,0-2" -d
```



## Relatório Técnico

