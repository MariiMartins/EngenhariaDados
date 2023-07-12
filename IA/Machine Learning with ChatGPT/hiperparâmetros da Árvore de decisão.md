# Hiperparâmetros da Árvore de decisão

No vídeo anterior, nós ajustamos hiperparâmetros do modelo de árvore de decisão. Vamos nos aprofundar mais nesses hiperparâmetros?

O prompt abaixo nos ajuda com isso:

    Quais são os hiperparâmetros que podem ser ajustados no modelo "Decision Tree Classifier" na biblioteca sklearn? Explique cada um deles com detalhes.

A resposta foi a seguinte:

```
O modelo Decision Tree Classifier é um algoritmo de aprendizado de máquina supervisionado usado para classificação. Ele cria uma árvore de decisão que divide os dados com base em diferentes características, levando a uma série de decisões até que uma classificação seja determinada para um determinado exemplo.
```

Existem vários hiperparâmetros que podem ser ajustados no modelo Decision Tree Classifier para melhorar seu desempenho e controle sobre o processo de criação da árvore. Vou explicar alguns dos principais hiperparâmetros com detalhes:

- **Critério (criterion):** O critério é usado para medir a qualidade da divisão em cada nó da árvore. Dois critérios comuns são "gini" e "entropy". O critério de Gini mede a pureza das classes nos nós, enquanto a entropia mede a impureza. Geralmente, o critério de Gini funciona um pouco mais rápido, mas a escolha entre os dois depende do conjunto de dados e pode exigir experimentação.

- **Profundidade máxima da árvore (max_depth):** A profundidade máxima da árvore controla o número máximo de níveis ou nós da árvore. Uma árvore mais profunda pode capturar relações mais complexas nos dados, mas também pode levar ao sobreajuste (overfitting) se não for controlada. Definir um valor adequado para esse hiperparâmetro é importante para evitar overfitting.

- **Número mínimo de amostras em um nó para divisão (min_samples_split):** Esse parâmetro controla o número mínimo de amostras necessárias em um nó para que ocorra uma divisão. Se o número de amostras em um nó for menor do que esse valor, a divisão não será realizada e esse nó será considerado uma folha. Ajustar esse hiperparâmetro pode ajudar a controlar a complexidade da árvore e evitar overfitting.

- **Número mínimo de amostras necessárias em uma folha (min_samples_leaf):** Esse parâmetro especifica o número mínimo de amostras que devem estar em uma folha. Se uma divisão levar a um número menor de amostras do que esse valor em uma das folhas, a divisão não será permitida. Ajustar esse hiperparâmetro ajuda a evitar folhas com poucas amostras e pode reduzir o overfitting.

- **Número máximo de recursos considerados em cada divisão (max_features):** Esse hiperparâmetro controla o número máximo de recursos que são considerados ao procurar a melhor divisão em cada nó. O valor padrão é geralmente a raiz quadrada do número total de recursos. Ajustar esse valor pode afetar a aleatoriedade da escolha de recursos e pode ajudar a controlar o overfitting.

Esses são apenas alguns dos hiperparâmetros mais comuns no modelo Decision Tree Classifier. Existem outros, como a função de seleção de recursos (splitter), o valor mínimo para a redução de impureza em uma divisão (min_impurity_decrease), entre outros, que também podem ser ajustados para otimizar o desempenho do modelo.

Fique à vontade para criar dicionários com hiperparâmetros para serem testados! Essa exploração e experimentação permitirão uma compreensão mais aprofundada do modelo de árvore de decisão, bem como do processo de ajuste de hiperparâmetros em Machine Learning. Essa prática também ajudará a desenvolver habilidades de análise e seleção de hiperparâmetros mais eficientes, levando a modelos mais robustos e precisos.
