# Matriz de Confusão

Para obter uma avaliação mais completa do desempenho dos nossos modelos, estamos explorando métricas além da simples acurácia.
No vídeo anterior, discutimos a importância de utilizar uma matriz de confusão para analisar de forma mais detalhada como o nosso modelo está se saindo em termos de acertos e erros.

A matriz de confusão nos fornece informações valiosas sobre as previsões do modelo em relação às classes positivas e negativas. Ela nos permite visualizar e quantificar os verdadeiros positivos (casos em que o modelo previu corretamente a classe positiva), os falsos positivos (casos em que o modelo previu erroneamente a classe positiva), os verdadeiros negativos (casos em que o modelo previu corretamente a classe negativa) e os falsos negativos (casos em que o modelo previu erroneamente a classe negativa).

Portanto, utilizando o prompt abaixo, vamos aprofundar ainda mais o nosso conhecimento sobre essa métrica.

```
Explique com detalhes o que é uma matriz de confusão em Machine Learning.
```

O resultado foi o seguinte:

```
Uma matriz de confusão, também conhecida como tabela de contingência, é uma ferramenta comumente usada em machine learning para avaliar o desempenho de um modelo de classificação. 
Ela fornece uma representação visual da qualidade das previsões feitas pelo modelo, comparando os resultados esperados com os resultados obtidos.
```

A matriz de confusão é construída com base nos quatro possíveis resultados de uma classificação binária:

- Verdadeiro Positivo (True Positive - TP): Refere-se aos casos em que o modelo previu corretamente a classe positiva (verdadeira) de uma amostra. Por exemplo, se um modelo de detecção de spam classificar corretamente um e-mail como spam, será considerado um verdadeiro positivo.

- Falso Positivo (False Positive - FP): Ocorre quando o modelo prevê incorretamente a classe positiva (verdadeira) para uma amostra que pertence à classe negativa (falsa). Nesse caso, o modelo de detecção de spam rotula um e-mail legítimo como spam.

- Verdadeiro Negativo (True Negative - TN): Indica os casos em que o modelo prevê corretamente a classe negativa (falsa) para uma amostra. Seria quando o e-mail não é spam e o modelo o identifica corretamente como tal.

- Falso Negativo (False Negative - FN): Refere-se aos casos em que o modelo prevê incorretamente a classe negativa (falsa) para uma amostra que pertence à classe positiva (verdadeira). Um falso negativo ocorre quando o modelo falha em identificar corretamente um e-mail como spam, quando, na verdade, ele é um spam. Por exemplo, se um spam chega à caixa de entrada e o modelo não o marca como spam.

A matriz de confusão é uma tabela 2x2 que organiza esses resultados da seguinte maneira:

Classe Positiva |Classe Negativa
-|-
Positivo (Previsto)|TP
Negativo (Previsto) |FN

Cada célula da matriz representa uma contagem do número de instâncias que caem em uma determinada categoria. A diagonal principal da matriz (da esquerda superior para a direita inferior) contém os verdadeiros positivos e verdadeiros negativos, enquanto as células fora da diagonal principal contém os falsos positivos e falsos negativos.

A matriz de confusão fornece uma visão geral do desempenho do modelo em termos de sua capacidade de fazer previsões corretas e identificar corretamente as classes positivas e negativas. Com base nessa matriz, várias métricas de avaliação podem ser calculadas, incluindo a acurácia, precisão, recall e F1-score, que fornecem uma compreensão mais aprofundada do desempenho do modelo.

Tendo em mente essas considerações que o ChatGPT trouxe, temos a seguir uma figura que ilustra os resultados obtidos em uma matriz de confusão. Na figura, os acertos do modelo para a classe negativa (0) e a classe positiva (1) são destacados em verde, enquanto os erros do modelo, ou seja, os falsos negativos e falsos positivos, são representados em vermelho.

Alt text: Representação de uma matriz de confusão. Eixo x, Valor predito, tem dois quadrantes, 0 e 1. Eixo y, Valor verdadeiro, também tem dois quadrantes, 1 e 0. Em valor verdadeiro 0, valor predito 0, temos VN em verde, representando verdadeiro negativo. Em valor verdadeiro 0, valor predito 1, temos FP em vermelho, representando falso positivo. Em valor verdadeiro 1, valor predito 0, temos FN em vermelho, representando falso negativo. Em valor verdadeiro 1, valor predito 1, temos VP em verde, representando verdadeiro positivo.

Nessa imagem, também temos siglas importantes na matriz de confusão, que no caso do nosso modelo, para prever se a pessoa aceitou ou não o empréstimo pessoal, indicam o seguinte:

- VP: verdadeiro positivo (classe=1 e predição=1). Indica que a pessoa aceita o empréstimo pessoal.
- VN: verdadeiro negativo (classe=0 e predição=0). Indica que a pessoa não aceita o empréstimo pessoal.
- FP: falso positivo (classe=0 e predição=1). Indica que a pessoa não aceita o empréstimo pessoal, mas a predição diz que aceita.
- FN: falso negativo (classe=1 e predição=0). Indica que a pessoa aceita o empréstimo pessoal, mas a predição diz que não aceita.

Ao analisar essas informações, podemos ter uma compreensão mais precisa das capacidades e limitações do nosso modelo. Além disso, como o ChatGPT mencionou, a matriz de confusão nos permite calcular outras métricas de avaliação importantes, como precisão, recall (revocação) e F1-score, que fornecem uma visão mais abrangente do desempenho do modelo em diferentes aspectos.
