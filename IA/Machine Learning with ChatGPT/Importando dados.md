Importando os dados
Para isso, utilizaremos o Google Colab. Criamos um projeto e na primeira célula, passamos a variável url que contém o endereço do arquivo com os dados no formato .xlsx, ou seja, Excel.
```
url = 'https://github.com/alura-cursos/machine_learning_chatgpt/blob/main/Dados/emprestimo.xlsx?raw=true'
```
Agora, utilizaremos o ChatGPT para nos auxiliar no desenvolvimento de todo o projeto.

Isso não significa que a IA fará nosso trabalho. Analisaremos as respostas obtidas com uma percepção crítica de uma pessoa cientista de dados e a partir disso criaremos o projeto.

Começamos abrindo o navegador e acessando o site da OpenAI. Nesse curso, utilizaremos a versão gratuita 3.5, sendo assim, basta criar uma conta e realizar o login.

Feito isso, na página inicial, clicamos em "New chat", localizado no topo esquerdo da tela. É nessa aba que enviaremos os prompts.

Recomendamos que você envie os prompts sempre no mesmo chat, assim não precisara explicar para a IA novamente o que está sendo feito.

Copiamos o primeiro prompt e colamos no chat.

```
Quero que você atue como um cientista de dados e codifique para mim. 
Estou desenvolvendo um projeto de Machine Learning sobre clientes de uma instituição financeira aceitarem um empréstimo pessoal.
Tenho o endereço do dataset no formato xlsx armazenado em uma variável chamada "url" . Escreva o código em Python para importar os dados.
```

No decorrer do curso você irá entender que existem boas práticas que devem ser seguidas nos prompts para que os resultados sejam otimizados.

Para executar o prompt apertamos "Enter" ou então clicamos no botão indicado por uma seta, no lado inferior direito da tela. Feito isso, temos o retorno abaixo.

Claro! Posso ajudá-lo com o código para importar os dados do arquivo Excel (xlsx) em Python. Vamos usar a biblioteca pandas para isso. Certifique-se de ter a biblioteca pandas Instalada em seu ambiente Python.

Aqui está o código para importar os dados do arquivo Excel:
```
import pandas as pd

url = "caminho/para/o/seu/arquivo.xlsx"
dados = pd.read_excel(url)

#Exibir as primeiras linhas do DataFrame para verificar se os dados foram importados corretamente
print(dados.head())
```
Certifique-se de substituir "caminho_para_o_arquivo.xlsx" pelo caminho real do arquivo xlsx que você possui. O código utiliza a função read_excel() da biblioteca pandas para ler o arquivo e armazenar os dados em um DataFrame chamado "dados". Em seguida, o código Imprime as primeiras linhas do DataFrame para verificar se os dados foram Importados corretamente.

Nesse caso, já temos a biblioteca Pandas instalada no Google Colab. Então, copiamos esse código gerado e colamos em uma nova célula.

Agora, apagamos o caminho da url e colamos o endereço que inserimos no início dessa aula. Dessa forma:

```
import pandas as pd

url = "https://github.com/alura-cursos/machine_learning_chatgpt/blob/main/Dados/emprestimo.xlsx?raw=true"
dados = pd.read_excel(url)

#Exibir as primeiras linhas do DataFrame para verificar se os dados foram importados corretamente
print(dados.head())
```
Apertamos "Shift + Enter" para executar. Repare que, como foi utilizado a função print(), o dataframe não fica visualmente bom.

|ID |Age|Experience|Income|ZIP Code|Family|CCAvg|Education|Mortgage|
|-|-|-|-|-|-|-|-|-|
|0|1|25|1|49|91107|4|1.6|1|0|
|1|2|45|19|34|90089|3|1.5|1|0
|2|3|39|15|11|94720|1|1.0|1|0
|3|4|35|9|100|94112|1|2.7|2|0
|4|5|35|8|45|91330|4|1.0|2|0

|Personal Loan|Securities Account|CD Account|Online|CreditCard|
|-|-|-|-|-|
|0|0|1|0|0|0|
|1|0|1|0|0|0|
|2|0|0|0|0|0|
|3|0|0|0|0|0|
|4|0|0|0|0|1|

A seguir exploraremos melhor esses dados e a formatação dataframe. Até lá!
