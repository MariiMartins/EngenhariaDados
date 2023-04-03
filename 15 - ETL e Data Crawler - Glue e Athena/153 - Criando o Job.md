153. Criando o Job
Bom agora, então a gente pode ir para nossa parte de transformação.
Então a gente vai aqui pra essa área do Glue, que é o Data Integration and ETL, integração de dados e ETL.
E você pode clicar aqui em Glue, Em Jobs. Então eu cliquei no AWS, com um de Jobs e aqui ele abre essa interface que você pode escolher a forma como você vai criar o job.
Então, você pode criar de uma forma visual que você vai informar apenas a origem, o destino de uma forma visual com canvas em blanco em branco que você tem mais flexibilidade.

Aqui você tem um editor de código do Spark, aqui, um editor de código do Python e aqui um notebook do Jupiter. Lembrando que você é claro que todas as opções aqui você tem praticamente as mesmas funcionalidades, mas com as opções de código você tem mais flexibilidade.

Agora você pode começar, por exemplo, com o visual, por o item black canvas e você pode construir parte do pipeline. Em determinado momento, você pode ir lá e editar o código. Só que quando você fizer isso, você não tem mais o editor visual com canvas em branco. Então você quando você utiliza a parte visual para você construir o workflow nos bastidores, ele vai construir o código para você. Mas se você resolver você mexer no código, aí você tem que continuar apenas com o código.

Nós vamos optar aqui pelo visual with a Blank Canvas, porque a gente tem mais flexibilidade aqui.

Então, vejam aqui primeiro vamos dar o nome aqui para nosso job. Vamos chamar de job vendas.Eu vou aqui salvar o nosso job.
Ele está informando que alguns detalhes precisam ser informados e depois a gente vai até ali. Bom, vejam aqui eu tenho as origens.
Então, de onde posso extrair meus dados? Então ele pode vir do catálogo do Glue, diretamente do S3, do Kineses, do Kafka, de um banco de dados relacional, do Red Shift. Enfim, são muitas as fontes aqui de onde o banco ou os dados podem ter sua origem.

E aqui as opções de transformação. Então você pode aplicar o método em que você pode renomear os tipos e os nomes dos dados. Você pode selecionar Excluir alguns campos, tirar títulos, remover duplicados, renomear, fazer junções, enfim, tem muitas opções aqui, filtrar ou fazer união. Você pode aqui detectar informação sensível. Você pode digitar aqui um código SQL diretamente. Então, essas são as opções de transformação e aqui o objetivo ou alvo para onde os dados vão. Então, normalmente você tem um source, algumas etapas de transformação e um target.

O nosso objetivo é pegar e base cinco tabelas, criar uma tabela única. Então a gente pode criar e a gente pode querer colocar elementos de origem para as nossas tabelas. E a gente pode fazendo transformações do tipo join e depois como destino, a gente coloca lá a pasta de quando escolhe essas três e coloca pasta lá que a gente selecionou como, como nosso Data Lake que é selecionada e que o formato vai ser parquet. Só que na transformação, o join tem que ser feito de duas em duas tabelas. Eu não posso fazer um join de tudo ao mesmo tempo. E uma outra observação é que eu posso ter problemas com os joins quando eu tiver campos repetidos.

E se você olhar o nosso schema de dados, a gente vai ter nomes repetidos quando a gente tem chave estrangeira. E a gente vai ter chave estrangeira em duas tabelas, em vendas, em itens-vendas.
Então, em vendas a gente tem o ID do vendedor e o ID do cliente, e em itens-vendas, ID produto e ID venda.

Então, quando ocorreu um drop, isso pode ter um problema que o nome dos campos vai ser o mesmo. Então, primeiramente, a gente vai alterar o nome dessas, dessas colunas ou desses campos nas tabelas onde eles são chaves estrangeiras.
