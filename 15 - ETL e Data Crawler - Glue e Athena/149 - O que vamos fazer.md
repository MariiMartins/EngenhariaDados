149. O que vamos  fazer
Então vamos entender o que nós vamos fazer nas nossas atividades práticas de ETL.
Então, nosso objetivo vai ser criar um DataLake com dados de vendas, para que esse data lei que seja esteja disponível para consultas adhoc, para que consultores, usuários, gerentes, enfim, possam consultar esses dados.
A fonte desses dados vai ser um arquivo CSV.

Então o que a gente vai fazer?
Vão ser vários arquivos CSV, a gente vai ter um bucket no S3, dentro desse bucket S3 a gente vai criar uma pasta e a gente vai colocar esses arquivos de vendas em formato CSV lá dentro.

E o nosso objetivo é dentro desse mesmo bucket I-Motion em uma outra pasta, criar esse DataLake.
Claro que o conceito aqui de DataLake é uma coisa maior, você vai ter dados de várias organizações, de vários setores da empresa, como diversos tipos de consolidação ou formatos. Isso vai ser uma fonte central de consulta, mas claro que aqui a nossa atividade é simplificada. Então a gente vai criar apenas uma tag, uma tabela de consulta sobre vendas. 

Então a gente vai ter dentro do bucket uma pasta com os arquivos de origem e uma outra pasta que vai ter o resultado final, que seria que é o Lake. E a gente vai utilizar o formato de big data.
Só que para fazer isso, para que a gente possa transformar esses arquivos CSV que vão estar desnormalizados porque cada um, cada ponto de negócio tem a sua própria tabela.

A gente tem um arquivo de vendas, a gente tem um arquivo de vendedores, de um arquivo de clientes.  É um formato que você conhece já de atividades anteriores, para que a gente transforme isso numa tabela desnormalizada, num formato de big data.

A gente tem que fazer algumas coisas.
A gente vai precisar criar uma IAMRole, essa role é uma permissão para o Glue a acessar o S3.
A gente vai criar uma role com mais privilégios. A gente vai criar uma Role administrativa para o Glue, para que ele possa, por exemplo, ir até o S3 e ler esses arquivos.

Depois a gente vai começar a trabalhar com o Glue. Então, a primeira coisa que a gente vai precisar é criar um banco de dados no Glue por quê? Porque posteriormente a gente vai ter tabelas e essas tabelas precisam ser agrupadas. Logicamente, isso vai ser feito através desse banco de dados que a gente vai criar.

Bom, aí a gente precisa descobrir que tabelas, que dados a gente tem. Então a gente vai criar e executar o crawler, esse crawler a gente vai apontar ele para o banco e o diretório do S3, onde estão os nossos dados CSV.

Ele vai ir lá e ele vai descobrir o schema. E vai descobrir quantas tabelas existem lá, quais são as colunas, quais são os tipos..
O crawler vai fazer isso para nós e vai associar ao banco de dados que nós criamos.

Bom, isso feito. A gente está pronto, então, para criar um job no Glu.
Só um detalhe o Glue depois que o cloud ele executar, ele vai colocar essas tabelas no catálogo do Glue.

Depois a gente vai criar um job no Glue. Esse job o objetivo dele é pegar esses dados que estão em formato CSV lá em uma tabela. Ele vai fazer uma transformação nesses dados. Ele vai fazer um tratamento de nomes de campos. Ele vai juntar tudo. Então são cinco tabelas e vai ter uma única tabela desnormalizada. E ele vai salvar isso no bucket numa outra pasta no formato parquet, com uma partição.
Então, esses dados, além de ser consolidados no formato parquet eles vão produzir uma partição através do status do cliente.

Então esse job, uma vez executado, ele vai lá no S3 através do catálogo que nós criamos. Ele vai fazer um processo de transformação desses dados, vai criar isso e ele vai consolidar isso através dos joins, e vai salvar no formato parquet no S3 que isso vai ser o nosso DataLake.

Então a gente cria um DataLake e por fim vai usar uma outra ferramenta do AWS que é o Athena e atende a gente.

Então o Athena ele vai acessar este DataLake através do catálogo que o Glue cria. Então, depois que a gente criou o DataLake, a gente vai rodar um outro crawler. Porém, agora, em vez de olhar os arquivos CSV, a gente vai olhar os dados parquet que foram criados.
É uma única referência lógica, mas fisicamente é mais de uma, porque ele foi particionado. Então, automaticamente, havendo um catálogo que vai ser criado pelo crawler, o Athena consegue acessar isso quase que automaticamente.

E aí eu vou mostrar que você pode realizar imediatamente qualquer consulta com esses dados nesse DataLake que a gente criou, então você pode criar consultas.Você pode salvar as consultas, você pode exportar os dados.
Tudo isso permite que seja feito.