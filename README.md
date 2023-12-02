# AG002

## Grupo

<a href="https://github.com/joaodutra88">
<img src="https://img.shields.io/static/v1?label=Github&message=Profile&color=blue&?style=social&logo=GitHub">
</a>

**João Vítor Carvalho de Paula Dutra 351 GES**

![Repo Size](https://img.shields.io/github/repo-size/joaodutra88/AG002)
![Linguagens usadas](https://img.shields.io/github/languages/count/joaodutra88/AG002)
![Linguagem mais usada](https://img.shields.io/github/languages/top/joaodutra88/AG002)
![Última atualização](https://img.shields.io/github/last-commit/joaodutra88/AG002)

# Instituto Nacional de Telecomunicações - Inatel

## AG002 – Engenharias de Computação e Software

[Prof. Me. Marcelo Vinícius Cysneiros Aragão](mailto:marcelovca90@inatel.br)  
[Prof. Me. Renzo Mesquita Paranaíba](mailto:renzo@inatel.br)

### 1. Introdução

Neste semestre, a AG002 acontecerá na forma de um trabalho prático. Você deverá utilizar seus conhecimentos para, a partir do conjunto de dados proposto, treinar, avaliar e disponibilizar um modelo de aprendizado de máquina para apontar o desfecho de uma partida de jogo da velha.

![Ilustração de jogo da velha](./img.jpeg)

### 2. Conjunto de Dados

Jogo da velha é um jogo para duas pessoas que requer apenas lápis e papel. O tabuleiro é uma matriz de três linhas por três colunas. Cada jogador se reveza desenhando uma cruz ou um círculo em uma posição desta matriz. O vencedor é aquele que conseguir colocar três peças iguais em uma fileira, na vertical, na horizontal ou na diagonal (conforme ilustrado na figura).

Neste sentido, o conjunto de dados apresenta 958 amostras, que representam todas as possibilidades de se preencher o tabuleiro do jogo da velha. Cada amostra do conjunto é dada por:

- Nove atributos (enumerados de 1 a 9) que representam o estado de cada posição do tabuleiro; os possíveis valores são x (cruz), o (círculo) ou b (vazio).
- Um rótulo de classe, que representa o desfecho daquela configuração em particular; os possíveis valores são “positivo” (que indica a vitória do x) ou “negativo” (que indica empate ou derrota do x).

Neste trabalho será utilizada uma versão traduzida do conjunto originalmente concebido por Aha [[1]](#referencias) em 1991. Os dados originais foram obtidos do [UCI Machine Learning Repository](https://archive.ics.uci.edu/dataset/101/tic+tac+toe+endgame).

### 3. Etapas para Realização

1. Baixar o [conjunto de dados em formato CSV](https://raw.githubusercontent.com/marcelovca90-inatel/AG002/main/tic-tac-toe.csv).
2. Fazer a leitura dos dados utilizando a biblioteca [Pandas](https://www.machinelearningplus.com/pandas/pandas-read_csv-completed/).
3. Converter os valores presentes no conjunto de dados para números inteiros, de acordo com este mapeamento: o → −1, b → 0, x → +1, negativo → −1 e positivo → +1. Dica: método [replace](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.replace.html) presente na classe DataFrame do Pandas.
4. Escolher um dos modelos de classificação a seguir:
   - Decision Tree: [Wikipedia](https://en.wikipedia.org/wiki/Decision_tree), [KDnuggets](https://www.kdnuggets.com/2020/01/decision-tree-algorithm-explained.html) e [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.tree.DecisionTreeClassifier.html).
   - k-Nearest Neighbors: [Wikipedia](https://en.wikipedia.org/wiki/K-nearest_neighbors_algorithm), [Towards Data Science](https://towardsdatascience.com/machine-learning-basics-with-the-k-nearest-neighbors-algorithm-6a6e71d01761) e [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html).
   - Multilayer Perceptron: [Wikipedia](https://en.wikipedia.org/wiki/Multilayer_perceptron), [KDnuggets](https://www.kdnuggets.com/2016/11/quick-introduction-neural-networks.html) e [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.neural_network.MLPClassifier.html).
   - Naïve Bayes: [Wikipedia](https://en.wikipedia.org/wiki/Naive_Bayes_classifier), [Towards Data Science](https://towardsdatascience.com/naive-bayes-classifier-explained-50f9723571ed) e [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.GaussianNB.html).
   - Perceptron: [Wikipedia](https://en.wikipedia.org/wiki/Perceptron), [Towards Data Science](https://towardsdatascience.com/perceptron-learning-algorithm-d5db0deab975) e [scikit-learn](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html).
5. [Separar o conjunto de dados](https://scikit-learn.org/stable/modules/generated/sklearn.model_selection.train_test_split.html) em duas partes: 80% para treinamento e 20% para testes.
   - Treinar o modelo escolhido usando 80% dos dados.
   - Avaliar o modelo escolhido usando os 20% restantes.
6. Exibir [métricas de avaliação](https://scikit-learn.org/stable/modules/model_evaluation.html#classification-metrics) para verificar a acurácia do modelo.
7. Criar uma opção que permita ao usuário inserir dados arbitrários que devem ser classificados pelo modelo. O modelo deverá imprimir se, com base no conhecimento adquirido com os dados do conjunto, os dados inseridos constituem vitória de x (“sim” ou “não”). Dica: método [predict](https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.Perceptron.html#sklearn.linear_model.Perceptron.predict) presente em todos os classificadores.

### 4. Orientações Adicionais

- O trabalho deverá ser feito em dupla.
- Qualquer linguagem de programação pode ser utilizada.
- A entrega deverá ser feita por meio de um arquivo zip com todo o conteúdo do projeto ou um link de um repositório privado do GitHub.
- Para apresentação, o aluno deverá gravar um vídeo de no máximo 7 minutos, explicando em detalhes as etapas do projeto desenvolvido.
- O vídeo poderá ser feito gravando a própria tela do computador enquanto o aluno explica ou até mesmo usando o smartphone, desde que as explicações das etapas estejam nítidas.
- A entrega deve ser feita até o dia 03/12/2023. Disponibilize o vídeo e arquivo zip (se for usar) no OneDrive ou Google Drive, com permissão de acesso para renzo@inatel.br. Se usar GitHub (em vez de arquivo zip), disponibilize o link também com permissão de acesso.
