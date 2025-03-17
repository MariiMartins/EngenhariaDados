101. Mongodb Parte I
Por ser o banco NoSQL mais popular, mais utilizado no mundo. O nosso caso prático e a nossa implementação prática nesta seção vai ser utilizando este banco de dados na nossa máquina virtual que nós já viemos utilizando nas seções anteriores até aqui, algumas características para a gente conhecer melhor o MongoDB.
•	Ele é uma ferramenta opensource.
•	Multiplataforma.
•	Extremamente escalável.
•	Orientado a documentos, ou seja, ele armazena documentos.
•	Permite documentos aninhados, ou seja, ele pode ter dentro dele outro documento.
•	Ele é indexado, ou seja, você pode buscar conteúdo dos documentos de forma indexada, ou seja, ele consegue indexar campos dentro do próprio documento.
•	Não tem schema fixo. Isso quer dizer o que uma mesma relação você pode ter documentos com estruturas diferentes. Você pode mudar a estrutura. Cada novo documento você pode mudar o schema a cada novo documento.
•	Não tem nenhum tipo de integridade referencial no sentido que a gente conhece lá nos bancos de dados relacionais, até porque não faz sentido que ele é orientado a documentos.

Aqui, alguns conceitos importantíssimos.
Então a gente faz uma comparação do relacional com o MongoDB, um banco de dados orientado ao documento, para a gente ter através de uma analogia, conseguir entender melhor os conceitos do Mongo. 

Então, aqui, no sentido de banco de dados, o conceito é o mesmo. Então, o banco de dados é uma estrutura que armazena várias coleções de documentos, porém o Mongo não tem tabelas. O equivalente a uma tabela é uma coleção, uma coleção que vai armazenar documentos.
Então dentro da coleção não vão existir linhas, estruturas de linhas e colunas.
Vão existir documentos, ok, um ou mais documentos.

No banco de dados relacional você tem a linha dentro da tabela. Dentro da coleção, como a gente falou, a gente tem documentos. Cada documento pode ter uma estrutura diferente, um schema diferente, e eles são sempre armazenados no formato JSON.

O banco de dados relacional tem coluna o MongoDB.
Ele tem campos, então, por exemplo, um documento ele pode ter um campo nome, pode ter um campo, idade, pode ter, por exemplo, um campo, profissão e assim sucessivamente.

|Relacional | MongoDB|
|---| ----|
| Banco de Dados | Banco de Dados |
|Tabela | Coleção|
|Linha | Documento|
|Coluna | Campo|


Principais tipos de dados do modelo.
•	String
•	inteiro 
•	booleano 
•	double 
•	array, que é um vetor.
•	Timestamp (é usado principalmente para o registro em alterações em documentos)
•	Object, ele pode também armazenar um objeto Um objeto pode ser um documento embutido no Mongo, uma característica que você não precisa declarar os tipos, isso é feito implicitamente ele faz o reconhecimento do tipo de acordo com o dado que está sendo inserido.
