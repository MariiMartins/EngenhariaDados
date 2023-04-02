- 96. Introdução
NoSQL se refere um conjunto de produtos que implementam novas técnicas de armazenamento e gestão de dados, e essas novas técnicas têm as características diferentes, não têm as mesmas restrições que a gente encontra nos modelos relacionais elas são flexibilizadas. Então esses produtos NoSQL, essas técnicas de armazenamento de dados são desnormalizadas, sem restrições de integridade, e o modelo de transação é mais flexível.

Então, a gente pode ver que são bem diferentes do que a gente estudou até agora dos modelos transacionais e dimensionais. É importante salientar, mais uma vez, que os produtos NoSQL eles atendem problemas de aplicações orientadas a dados específicos, eles não são substitutos ao modelo transacional nem ao modelo dimensional, porque eles são um complemento, eles vieram para propor soluções a problemas diferentes de dados.

Então, os produtos, as ferramentas NoSQL, elas buscam resolver problemas específicos de certos tipos de aplicações que até de certa forma, poderiam ser resolvidas ou implementadas no modelo relacional, mas com muita dificuldade.

Então, o que esses produtos trazem? Processamento mais eficiente, paralelismo, escalabilidade e menor custo.

Esses conjuntos de ferramentas estão divididos em quatro principais tipos.
Então, veja o que a gente está falando de ferramentas comerciais a gente vai falar disso a partir do próximo slide. A gente está falando de tipos de técnicas, de armazenamento de dados. A gente vai falar um pouco mais de que de cada uma dessas técnicas em vídeos posteriores e depois nós vamos implementar (Nós vamos conhecer na prática uma delas)

Então, quais são essas técnicas?
•	São os bancos de dados que armazenam um conjunto chave valor Key-Value Database (KVP) 
•	Colunas ordenadas, que é uma técnica diferenciada de armazenamento para registros, com muitas quantidades de dados com grande quantidade de dados. 
•	Banco de dados de documentos que armazenam. Em vez de armazenar registros, eles armazenam documentos. São estruturas de documentos que o que a gente vai estudar em formato de JSON. 
•	E os bancos de dados de grafos.

Implementações comerciais ou opensource. Então, que produtos a gente encontra de cada um desses produtos no modelo KVP nós temos, por exemplo, o Amazon Dynamo e o Coach DB. E estão aqui alguns exemplos de produtos que implementam a forma modelo de armazenamento de chave valor.
O Couchbase DB anteriormente era o MBase, existe ainda o KyotCabinet, o Redis que está aqui e o DynamoDB é um produto do Amazon.

Colunas ordenadas, então são dados orientados a coluna. Cada linha tem um ponteiro armazenado de maneira contínua. Ele é tolerante à falha através de um sistema de arquivos distribuído e é baseado no modelo BigTable, que é o modelo proposto pelo Google.
Então, aqui a gente tem algumas implementações: A primeira que dá a Fundação Apache HBase, pois a gente tem o HiperTable, são alguns dos produtos que implementam esse modelo.

Depois a gente tem os bancos de dados de documentos.
É importante a gente lembrar que um banco de dados de documento não se refere a ele, como um documento, por exemplo, um documento texto, um documento do Word, o que na verdade é um documento estruturado, geralmente com formato JSON, e depois a gente vai entender um pouquinho melhor o que é esse formato como implementações.
A gente tem o MongoDB, que é um dos bancos de dados mais utilizados no mundo ele tem a sua implementação, sua utilização próxima aos bancos de dados relacionais, e o CouchDB.

Bancos de dados de graficos que são aplicações de redes sociais, medicina, genética, recursos humanos. Os grafos são formados por uma vez por vértices e arestas, então, por exemplo, os vértices podem ser pessoas de uma rede social e aresta quer dizer, por exemplo, um vínculo de um vínculo de amizade entre essas pessoas.
Exemplos de aplicações que tipos de aplicações são implementadas por bancos de dados NoSQL.
•	Então, sessões de usuários em aplicações web.
•	Conteúdos como ebooks, artigos e documentos em geral.
•	Agregação e repositório central de dados.
•	Plataforma de anúncios direcionados.
•	Registros eletrônicos de pacientes (EHR – Eletronic Healthcare Records)
•	Análise de séries temporais.
•	Dados de crachá sóciométrico.
Aqui, por curiosidade, a gente vê quais são os bancos de dados de cada modelo mais utilizados.
•	Então, do modelo relacional, o mais utilizado é o Oracle, 
•	Do modelo chave valor: Redis, 
•	Do modelo orientado a documento: Mongo DB 
•	Do modelo de grafo: Neo4j 
•	De colunas ordenadas: o Cassandra.
