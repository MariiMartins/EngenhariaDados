# Explorando os dados

Para isso, consultaremos o ChatGPT. Copiamos o prompt, colamos e apertamos "Enter".

```
Os dados foram carregados e armazenados na variável "df".
Escreva o código para exploração de dados para que os resultados sejam exibidos sem a necessidade de usar a função `print()`.
Adicione um comentário em cada código para saber do que se trata.
```

Repare que, no prompt avisamos que os dados foram carregados e armazenados na variável df. Mas, se analisarmos nosso código, usamos dados ao invés de df.

Para corrigir, abrimos o Colab e fazemos essa substituição, em seguida executamos novamente o código.

```
import pandas as pd

url = 'https://github.com/alura-cursos/machine_learning_chatgpt/blob/main/Dados/emprestimo.xlsx?raw=true'

# Carregar o arquivo Excel para um dataframe
df = pd.read_excel(url)

# Exibir as primeiras linhas do dataframe para verificar se os dados foram importados corretamente
print(df.head())
```

Continuando a análise do prompt, repare que colocamos a variável entre aspas. É sempre muito importante adotar boas práticas na criação do prompt. As aspas são muito importantes para indicar data frames, classes, ou métodos, por exemplo.

Em seguida, pedimos para escrever o código para exploração de dados para que o resultado seja exibido sem a função print().

Quando executamos o código anteriormente o print foi exibido de uma forma que não é tão bacana visualmente. Por isso, pedimos para que use apenas as funções e métodos da biblioteca pandas.

Por fim, pedimos para que seja adicionado um comentário em cada código para conseguirmos entender cada trecho. Agora, podemos enviar o prompt apertando "Enter".

Assim, temos o seguinte retorno:

Claro! Aqui está o código com comentários explicando cada etapa da exploração de dados, utilizando a variável "df" para representar o DataFrame com os dados carregados:

```
import pandas as pd

# Carregar dados do arquivo Excel para o DataFrame "df" 
url = "caminho_para_o_arquivo.xlsx"
df = pd.read_excel (url)

# Exibir as primeiras 5 linhas do DataFrame
df.head()

# Exibir o número de linhas e colunas do DataFrame
df.shape

# Obter informações resumidas sobre as colunas do DataFrame
df.info()

# Exibir estatísticas descritivas para as colunas numéricas do DataFrame
df.describe()

# Contar o número de valores únicos em cada coluna do DataFrame
df.nunique()

# Exibir a contagem de valores em uma coluna especifica do DataFrame 
df['nome da coluna ].value_counts()

# Verificar se existem valores ausentes (NaN) em cada coluna do DataFrame
df.isnull().sum()

# Exibir a correlação entre as colunas numéricas do DataFrame
df.corr()
```

A IA indicou o código com comentários explicando cada etapa da exploração e utilizando a variável df para representar o dataframe.

Repare que no início do código a ferramenta novamente coloca a importação do pandas e a url, como já fizemos isso, não precisamos desse trecho.

Seguindo para o próximo, temos a função df.head(). Copiamos e colamos em uma nova célula do Colab.
```
df.head()
```
Ao executá-la, temos o seguinte dataframe:

|ID|Age|Experience|Income|ZIP Code|Family|CCAvg|Education|Mortgage|Personal Loan|Securities Account|CD Account|Online|CreditCard
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
|0|1|25|1|49|91107|4|1.6|1|0|0|1|0|0|0
|1|2|45|19|34|90089|3|1.5|1|0|0|1|0|0|0
|2|3|39|15|11|94720|1|1.0|1|0|0|0|0|0|0
|3|4|35|9|100|94112|1|2.7|2|0|0|0|0|0|0
|4|5|35|8|45|91330|4|1.0|2|0|0|0|0|0|1

Percebemos que o dataframe fica visualmente mais organizado e mais fácil de ser compreendido.

Nas colunas encontramos informações sobre os clientes dessa instituição financeira, como ID, Age, Experience, Income entre outros que vamos explorar e entender mais afundo em breve.

Agora, voltamos no ChatGPT e copiamos o pd.shape pra exibir o número de linhas e colunas o dataframe. Colamos no Colab e executamos a célula.

```
#Exibir o número de linhas e colunas do DataFrame
df.shape
```

Temos o seguinte retorno:
```
(5000, 14)
```

Isso significa que existem 5000 linhas, que provavelmente indicam a quantidade de clientes do banco, e 14 colunas com as informações.

Voltamos no ChatGPT, copiamos o código seguinte
```
 df.info() colamos no Colab e executamos.

#Verificar as informações básicas sobre o DataFrame
df.info()
COPIAR CÓDIGO
É imprimido o seguinte retorno:

<class 'pandas.core.frame.DataFrame'> RangeIndex: 5000 entries, 0 to 4999 Data columns (total 14 columns):

#|Column|Non-Null Count|Dtype
---|------|--------------|-----
0|ID|5000 non-null|int64
1|Age|5000 non-null|int64
2|Experience|5000 non-null|int64
3|Income|5000 non-null|int64
4|ZIP Code|5000 non-null|int64
5|Family|5000 non-null|int64
6|CCAvg|5000 non-null|float64
7|Education|5000 non-null|int64
8|Mortgage|5000 non-null|int64
9|Personal Loan|5000 non-null|int64
10|Securities Account|5000 non-null|int64
11|CD Account|5000 non-null|int64
12|Online|5000 non-null|int64
13|CreditCard|5000 non-null|int64

dtypes: float64(1), int64(13)|
memory usage: 547.0 KB|

```
Analisando essa tabela, notamos que não temos dados nulos. Isso é ótimo, afinal, não precisamos realizar nenhum tratamento. Além disso, o CCAvg aparece como tipo float e o restante como tipo inteiro.

O próximo código é o describe(), uma função utilizada para obter as principais estatísticas dos dados.

Colando e executando, temos alguns valores estatísticos. Primeiro temos a contagem que são 5000 linhas em cada coluna, uma média para cada valor, o desvio padrão, valor mínimo, máximo e os quartis de 25%, 50%, 75%.

|ID|Age|Experience|Income|ZIP Code|Family|CCAvg|Education|Mortgage|Personal Loan|Securities Account|CD Account|Online|CreditCard
|-|-|-|-|-|-|-|-|-|-|-|-|-|-|
count|5000.000000|5000.000000|5000.000000|5000.000000|5000.000000|5000.000000|5000.000000|5000.000000|5000.000000|5000.000000|5000.000000|5000.00000|5000.000000|5000.000000
mean|2500.500000|45.338400|20.104600|73.774200|93152.503000|2.396400|1.937913|1.881000|56.498800|0.096000|0.104400|0.06040|0.596800|0.294000
std|1443.520003|11.463166|11.467954|46.033729|2121.852197|1.147663|1.747666|0.839869|101.713802|0.294621|0.305809|0.23825|0.490589|0.455637
min|1.000000|23.000000|-3.000000|8.000000|9307.000000|1.000000|0.000000|1.000000|0.000000|0.000000|0.000000|0.00000|0.000000|0.000000
25%|1250.750000|35.000000|10.000000|39.000000|91911.000000|1.000000|0.700000|1.000000|0.000000|0.000000|0.000000|0.00000|0.000000|0.000000
50%|2500.500000|45.000000|20.000000|64.000000|93437.000000|2.000000|1.500000|2.000000|0.000000|0.000000|0.000000|0.00000|1.000000|0.000000
75%|3750.250000|55.000000|30.000000|98.000000|94608.000000|3.000000|2.500000|3.000000|101.000000|0.000000|0.000000|0.00000|1.000000|1.000000
max|5000.000000|67.000000|43.000000|224.000000|96651.000000|4.000000|10.000000|3.000000|635.000000|1.000000|1.000000|1.00000|1.000000|1.000000

É muito importante analisarmos esses dados. Na coluna Experiência, por exemplo, temos um valor de médio de 20 anos de experiência e mínimo de -3.

Acho que isso não existe, não é mesmo? Encontramos algo que precisa ser tratado.

Em sequência, temos o df.nunique() que conta quantos valores únicos temos em cada coluna.
```
#Contar o número de valores únicos em cada coluna
df.nunique()
```
Feito isso, o retorno abaixo:
campo|valor
-|-
ID|5000
Age|45
Experience|47
Income|162
ZIP Code|467
Family|4
CCAvg|108
Education|3
Mortgage|347
Personal Loan|2
Securities Account|2
CD Account|2
Online|2
CreditCard|2

dtype: int64

Temos 5000 IDs únicos, ou seja, um para cada pessoa. Também temos outra coisa interessante.

Repare que a partir do "Personal Loan" temos apenas dois valores diferentes em cada coluna. Certamente são dados binários em que temos um valor zero que representa algo que a pessoa não tenha e 1 para algo que tenha.

Para finalizar, o ChatGPT sugere a exibição da contagem de valores de uma coluna específica, muito interessante para verificar a frequência de alguma categoria.

Copiamos o código, colamos no Colab e, entre aspas simples, adicionamos o nome da coluna Personal Loan. Em seguida executamos.
```
#Calcular a contagem de valores para uma coluna específica
df['Personal Loan'].value_counts()
```

Na categoria zero temos 4520 dados e na categoria um apenas 480.
```
0 4520 1 480 Name: Personal Loan, dtype: int64
```

Também podemos descobrir qual é a porcentagem de cada categoria. Para isso, nas chaves, passamos 
```
normalize=True * 100.

#Calcular a contagem de valores para uma coluna específica
df['Personal Loan'].value_counts(normalize=True * 100)
```
Ao executar temos o retorno:
```
0 90.4 1 9.6 Name: Personal Loan, dtype: float64
```
Há uma diferença bem grande entre as variáveis.