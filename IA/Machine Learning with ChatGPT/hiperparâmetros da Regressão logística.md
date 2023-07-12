# Hiperparâmetros da Regressão logística

No vídeo anterior, tentamos melhorar o desempenho do modelo de regressão logística. Ao treiná-lo com os dados balanceados, observamos uma melhoria no recall da classe 1, porém, houve uma significativa redução na precisão dessa mesma classe. O ChatGPT recomendou testar algumas abordagens, e uma delas foi a modificação do peso das classes por meio do hiperparâmetro class_weight.

Ao utilizar o hiperparâmetro class_weight, é possível atribuir pesos diferentes às classes durante o treinamento do modelo. Esses pesos indicam a importância relativa de cada classe na função de custo do algoritmo de otimização. A ideia é dar mais peso à classe minoritária, de forma a equilibrar a influência das classes durante o ajuste dos coeficientes. Nesse caso, isso não fazia tanto sentido, pois os dados já tinham passado pelo balanceamento com SMOTE. Porém, após realizar alguns testes criando um dicionário personalizado com diferentes valores de pesos, nós conseguimos contornar a situação da queda da precisão da classe 1.

Além de testar essa alteração desse parâmetro, seria possível tentar ajustar outras coisas. Vamos perguntar ao ChatGPT com o prompt a seguir:

``` 
Quais são os hiperparâmetros do modelo "Logistic regression" na biblioteca sklearn? Explique cada um deles com detalhes.
```

A resposta foi a seguinte:

O modelo de regressão logística possui vários hiperparâmetros que podem ser ajustados para otimizar o desempenho do modelo. Aqui estão alguns dos hiperparâmetros mais comuns da classe LogisticRegression do scikit-learn e uma breve explicação de cada um:

**C (parâmetro de regularização):** O hiperparâmetro C controla a força da regularização no modelo de regressão logística. Valores menores de C aumentam a força da regularização, o que pode ajudar a evitar overfitting. Por outro lado, valores maiores de C diminuem a regularização, permitindo que o modelo se ajuste mais aos dados de treinamento. Em outras palavras, C é o inverso do termo de regularização, portanto, quanto menor o valor de C, mais forte é a regularização.

**solver (algoritmo de otimização):** O hiperparâmetro solver define o algoritmo de otimização a ser usado no modelo de regressão logística. O solver é responsável por encontrar os valores ótimos dos coeficientes do modelo. Alguns dos solvers disponíveis no scikit-learn incluem:

- *'lbfgs':* é um solver otimizado para problemas de pequena escala e é uma boa opção para conjuntos de dados menores.
- *'liblinear':* é um solver eficiente para problemas de penalização L1 e L2 e é uma boa escolha quando se lida com conjuntos de dados grandes.
- *'newton-cg', 'newton-cholesky', 'sag', 'saga':* são solvers baseados em métodos de otimização diferentes, cada um com vantagens e desvantagens em termos de eficiência e escalabilidade.

**penalty (tipo de penalidade):** O hiperparâmetro penalty especifica o tipo de penalidade a ser aplicada na função de perda durante o treinamento. Existem duas opções comuns:

-*'l1':* aplica uma penalidade L1 (valor absoluto) aos coeficientes do modelo, o que favorece a criação de modelos com menos coeficientes não nulos. Isso pode ajudar na seleção de recursos e tornar o modelo mais interpretável.
-*'l2':* aplica uma penalidade L2 (valor quadrado) aos coeficientes do modelo, o que incentiva o modelo a ter coeficientes menores em magnitude. Isso pode ajudar a evitar overfitting e melhorar a generalização do modelo.

Esses são apenas alguns dos hiperparâmetros disponíveis na classe LogisticRegression. Além desses, existem outros parâmetros que podem ser ajustados, como max_iter (número máximo de iterações permitidas para a convergência do algoritmo) e class_weight (pesos atribuídos às classes para lidar com desbalanceamento de classes).

É importante ajustar esses hiperparâmetros com cuidado, pois eles afetam o desempenho e a capacidade de generalização do modelo de regressão logística. A seleção adequada dos hiperparâmetros pode ajudar a evitar o overfitting, melhorar a capacidade de generalização e otimizar o desempenho do modelo nos dados de teste.

Você pode testar alguns desses hiperparâmetros e utilizar técnicas de validação cruzada para avaliar o desempenho do modelo após os ajustes, verificando o valor de AUC nos dados de treino e teste.

Explorar e experimentar hiperparâmetros são ações que podem te ajudar a desenvolver uma compreensão mais profunda dos modelos.
