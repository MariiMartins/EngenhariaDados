# Para saber mais: o que a classe MinMaxScaler faz?

Fizemos a normalização dos dados numéricos das variáveis 'Age', 'Income', 'Family', 'CCAvg' e 'Mortgage' para que todas fiquem na mesma escala de valores, variando de 0 a 1.
Essa normalização é importante para evitar que alguma variável tenha um peso desproporcional sobre o modelo. Mas como essa normalização é feita? Podemos pedir uma explicação detalhada para o ChatGPT:
```
Explique com detalhes como a classe "MinMaxScaler" da biblioteca sklearn faz a normalização das variáveis numéricas.
```
A resposta foi a seguinte:
```
A classe "MinMaxScaler" da biblioteca scikit-learn (sklearn) é usada para realizar a normalização das variáveis numéricas. Essa normalização transforma as variáveis para que elas estejam em uma faixa específica, geralmente entre 0 e 1. Isso é útil quando as variáveis têm escalas diferentes e é desejável colocá-las em uma escala comparável.

A normalização realizada pelo MinMaxScaler segue a seguinte fórmula para cada valor da variável:

X_scaled = (X - X_min) / (X_max - X_min)
```
Onde:

X é o valor original da variável.
X_scaled é o valor normalizado da variável.
X_min é o valor mínimo da variável.
X_max é o valor máximo da variável. Para aplicar o MinMaxScaler, primeiro você precisa criar uma instância dessa classe. Em seguida, você pode ajustar e transformar os dados usando os métodos "fit" e "transform", respectivamente.
Aqui está um exemplo de como usar o MinMaxScaler:
```
from sklearn.preprocessing import MinMaxScaler

# Dados de exemplo
data = [[2, 4], [1, 3], [3, 6], [4, 8]]

# Criação do MinMaxScaler
scaler = MinMaxScaler()

# Ajuste do scaler aos dados
scaler.fit(data)

# Transformação dos dados
scaled_data = scaler.transform(data)

print(scaled_data)
```
A saída será:
```
[[0.33333333 0.33333333]
 [0.         0.        ]
 [0.66666667 0.66666667]
 [1.         1.        ]]
```

Observe que o MinMaxScaler calcula os valores mínimos e máximos para cada variável durante o ajuste, armazenando-os internamente. Em seguida, ele aplica a fórmula de normalização a cada valor da variável durante a transformação.

Além disso, se você tiver novos dados após ajustar o scaler, poderá usar o método "transform" diretamente nos novos dados sem a necessidade de ajuste adicional. Isso é útil quando você deseja aplicar a mesma transformação aos dados de teste ou novos dados que não foram usados durante o ajuste inicial.

Maravilha! Agora que já aprendemos a normalizar dados numéricos, que tal dedicarmos um tempo aos dados categóricos?