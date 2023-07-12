Para saber mais: Prompts com resultados otimizados
PRÓXIMA ATIVIDADE

Durante o curso, vamos utilizar prompts específicos, que estão disponíveis nos notebooks das aulas, para que o ChatGPT seja utilizado como um assistente no desenvolvimento do projeto de Machine Learning.

Ao executar esses prompts no ChatGPT em seu próprio computador, é possível que você obtenha respostas um pouco diferentes das que são mostradas nas aulas, pois o modelo tem como uma de suas características a aleatoriedade. Inclusive, se você executar o mesmo prompt várias vezes, as respostas podem sofrer variações. No entanto, não se preocupe, pois o objetivo é analisar as respostas geradas pelo ChatGPT e adaptá-las às nossas necessidades.

No decorrer das aulas, você vai notar que algumas boas práticas devem ser seguidas na escrita dos prompts. Vamos dar uma olhada em um exemplo de boa prática?

Nós vamos desenvolver um projeto de Machine Learning para auxiliar uma instituição financeira a reduzir custos de uma campanha de marketing definindo quais clientes têm mais chances de aceitar um empréstimo pessoal. Para isso, nós temos um arquivo no formato xlsx disponibilizado em um repositório do GitHub e queremos importá-lo no Google Colab, para começar a analisar os dados. Como poderíamos pedir isso para o ChatGPT?

Abaixo temos um prompt com essa finalidade:

Tenho o endereço de um dataset. Escreva o código para importar os dados.

A resposta neste caso foi a seguinte:

Certamente! Para importar um dataset, você precisará usar uma biblioteca apropriada para a linguagem de programação que está utilizando. Como você não especificou a linguagem, vou fornecer exemplos em duas linguagens populares: Python e R.

```
Python:
import pandas as pd

# Substitua 'caminho/do/dataset.csv' pelo caminho real do arquivo CSV

df = pd.read_csv('caminho/do/dataset.csv')

# Agora você pode usar o DataFrame 'df' para trabalhar com os dados

R:

# Substitua 'caminho/do/dataset.csv' pelo caminho real do arquivo CSV

df <- read.csv('caminho/do/dataset.csv')

# Agora você pode usar o objeto 'df' para trabalhar com os dados
```

Esses são exemplos básicos para importar um arquivo CSV, que é um formato comum para datasets. Se o seu dataset estiver em um formato diferente, você precisará usar uma função apropriada para importá-lo. Além disso, certifique-se de ter a biblioteca necessária instalada em sua máquina antes de executar o código.

Lembre-se de substituir 'caminho/do/dataset.csv' pelo caminho real do arquivo contendo o dataset que você deseja importar.

Observe que, com esse prompt extremamente direto e simples, o ChatGPT não foi capaz de determinar qual linguagem de programação usar no código, resultando em exemplos em Python e R. Além disso, como o formato do arquivo não foi especificado, o modelo presumiu que fosse um arquivo CSV. Outro ponto importante é que não fornecemos nenhum contexto, então o modelo nem sequer tem conhecimento do tema do projeto. Ao iniciar uma conversa, é importante fornecer um contexto adequado ao modelo sobre o trabalho em questão. Vamos tentar fazer isso agora e trazer um prompt mais detalhado?

Abaixo temos o primeiro prompt que será utilizado na primeira aula do curso:

Quero que você atue como um cientista de dados e codifique para mim. Estou desenvolvendo um projeto de Machine Learning sobre clientes de uma instituição financeira aceitarem um empréstimo pessoal. Tenho o endereço do dataset no formato xlsx armazenado em uma variável chamada "url". Escreva o código em Python para importar os dados.

O resultado dessa vez é o seguinte:

Claro! Posso ajudá-lo com o código Python para importar os dados do arquivo xlsx e começar o projeto de Machine Learning. Vou assumir que você já possui a biblioteca pandas instalada, pois ela é amplamente usada para trabalhar com conjuntos de dados estruturados.

Aqui está o código para importar os dados do arquivo xlsx usando a biblioteca pandas:

```
import pandas as pd
# URL do arquivo xlsx
url = "caminho/para/o/seu/arquivo.xlsx"

# Importar os dados
df = pd.read_excel(url)

# Exibir as primeiras linhas do DataFrame para verificar se os dados foram importados corretamente
print(df.head())
```

Certifique-se de substituir "caminho/para/o/seu/arquivo.xlsx" pelo caminho real do arquivo xlsx que você possui.

Ao executar o código acima, os dados serão importados do arquivo xlsx e armazenados em um DataFrame chamado df. A função read_excel() é usada para ler o arquivo xlsx e a função head() exibe as primeiras linhas do DataFrame para verificar se os dados foram importados corretamente.

Depois de importar os dados, você pode prosseguir com a análise exploratória dos dados, pré-processamento e treinamento de modelos de Machine Learning, de acordo com os objetivos do seu projeto.

O resultado foi bem melhor, né? Quando fornecemos um contexto claro ao prompt, especificando o tipo de arquivo e a linguagem desejada, o ChatGPT terá uma compreensão melhor das nossas necessidades e será capaz de gerar respostas mais relevantes e precisas. Ao estabelecer um contexto adequado, informamos ao modelo as informações essenciais para que ele possa direcionar suas respostas de maneira mais adequada e útil para o nosso projeto. Isso resultará em interações mais produtivas e eficientes com o ChatGPT.

Agora que você já compreende a importância de todos esses aspectos, vamos iniciar o projeto?
