155. Consultas com Athena
A gente fez tudo isso para criar um data Lake.
Um data Lake corporativo não é apenas uma tabela desnormalizada, mas são diferentes áreas de dados. Você tem áreas com dados brutos. Há áreas para atender, por exemplo, à área de machine learning. A dos dados já mais limpos, tratados para a área de negócios. A áreas onde os dados estão disponíveis para consultas eventuais ad hoc.Enfim, é uma estrutura geralmente bastante complexa e o objetivo aqui é mostrar como isso funciona conceitualmente.

Mas uma vez isso criado, isso tem que servir de alguma forma.
Então, a gente criou os arquivos para o cliente, os arquivos estão adicionados ao parquet lá no S3. E de alguma forma, isso vai ser utilizado por outras ferramentas. E eu já comentei anteriormente que uma das grandes vantagens de você ter dados nesse formato é que eles são dados desacoplado de ferramentas. Então, no momento que você tem um arquivo desses, um arquivo num formato de big data em um data lake, ele pode ser consultado por diferentes ferramentas.

Eles podem ser utilizados por diferentes ferramentas, então você pode conectar uma ferramenta diretamente, uma ferramenta de business intelligence nele e construir um dashboard. Você pode construir um banco de dados, por exemplo, como o próprio redshift. Você pode criar um schema externo associado a esses dados, e uma outra forma é você utilizar o Athena que é uma outra ferramenta aqui do S3.

Então, o Athena é uma ferramenta que permite que o usuário execute consultas de forma interativa sobre dados dos quais já foram mapeados.
Então, o nosso objetivo agora é ver como é que a gente pode fazer isso com o Athena utilizando este Data Lake, que nós criamos com os arquivos Parquet. Então o processo vai ser semelhante ao que a gente já fez com os arquivos CSV.
A gente tem que criar um catálogo. A gente tem que mapear esse banco de dados, uma vez mapeado, a gente pode ir até Athena e executar, consultar esses dados, lembrando essa é apenas uma das muitas formas que a gente poderia interagir com este Data Lake, com os dados do Data Lake.
Então vamos lá, eu vou eu vou voltar aqui ao Glue.

Então vamos criar aqui um database. A gente já tem aqui, o de vendas, não precisa mexer nele. Vamos adicionar outro e eu vou chamar de vendas de Lake só para a gente diferenciar do outro que a gente criou anteriormente.
E a gente já sabe que pra criar o banco de dados é só criar aqui e pronto.
Já temos aqui o nosso Venda 30 Lake. 

Agora a gente vai criar um catálogo de dados com o crawler. Então aqui está na parte dos crawlers, o crawler que nós utilizamos anteriormente. Você está com o status que ele já executou. Vamos aqui criar crawler. Eu vou dar o nome de Crowler Data Lake.
