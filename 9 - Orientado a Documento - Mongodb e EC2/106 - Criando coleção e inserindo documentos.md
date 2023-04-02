106. Criando coleção e inserindo documentos
Agora que nós já vimos que o mundo também está instalado, a gente pode interagir com ele. É claro que a gente pode interagir com o Mongo DB de várias formas. Por exemplo, através de um aplicativo como nós vamos interagir com ele agora, nós vamos utilizar um shell, um aplicativo de linha comando, que é o Mongosh. Então eu vou digitar aqui e mongosh, esse aplicativo ele já é de linha de comando. Ele já é instalado por padrão quando você instala o Mongo.

Então aqui ele traz algumas informações Importantes, (mas se aqui você não precisa se preocupar que para o nosso curso) eu vou limpar aqui a tela e a primeira coisa que a gente vai ver aqui. Eu vou mostrar os bancos de dados existentes ou então eu vou digitar aqui db.
Você pode ver que existe esse mostro banco de dados atual (Então é o banco de dados que a gente está conectado), E para mim ver todos os bancos de dados que existe, vou digitar show dbs, então, ele mostra o admin, config e o local. A gente pode ver que ele não mostra o teste, que era o banco de dados, que a gente estava conectado.

Bom, como que eu vou criar um banco de dados?
Eu posso utilizar o comando e use o nome do banco de dados. Se este banco de dados existir, ele vai passar a utilizar ele. Então ele vai sair do teste e vai passar a utilizar ele. Se ele não existir, ele vai criar ele ok e vai passar também a utilizar ele.
Então vou chamar aqui de dbvendas e (use dbvendas). Vou dar o Enter.
Então, veja só, ele fez um switch para o dbVendas. A gente viu que este banco de dados, ele não existia, mas ele fez um switch. Então, se a gente digitar aqui de novo o show dbs. Ele não foi criado ainda. Ele só vai ser criado quando eu persistir algum documento nele. Enquanto não criar um documento neste DB Vendas, ele não vai existir fisicamente no banco de dados.

Então, pra mim, criar um documento como um banco de dados NoSQL, como o Mongo DB, ele é flexível com relação ao schema, eu não preciso fazer uma declaração de schema, como no banco de dados relacional. Eu não preciso fazer um create table para depois poder inserir dados.

Com o schema flexível como Mongo DB. À medida que você vai inserindo informações, o schema vai sendo criado e, obviamente, se você faz a inserção de dados em um documento que uma propriedade já existe com campo, já existe ele não vai criar. Mas se ele não existe, ele vai fazer a criação.

Então vamos ver que um comando para gente inserir um único cliente.
Então vamos lá, dB.Clientes.insertOne({nome: “José”, sobrenome: ”da Silva”, idade =38}) então veja a coleção de clientes também não existe. Nem o banco de dados existia.
Então recordando um pouco os conceitos que nós estudamos:
Então aqui eu tenho um banco de dados. Eu criei o banco de dados de vendas.
Esta linha aqui, esse clientes aqui é uma coleção que seria equivalente ao banco de dados relacional, uma tabela. Esta linha é toda aqui que a gente criou, que seria uma linha no banco de dados. É um documento, então, que seria inserir um documento e na coluna dessas a gente pode chamar de campo, ok, então a gente seria um documento na coleção Clientes, que está no banco de dados de vendas. Vamos pedir para listar aqui show dB.
E como a gente havia previsto, o DB Vendas agora está aparecendo aqui e agora ele é um banco de dados que existe fisicamente no meu, no meu banco de dados do meu MongoDB. 

Bom, então a gente inserir um único cliente. Vamos ver como a gente encontra esse cliente. Vamos usar primeiro a forma mais simples de ver dB.clientes.find()
Ele vai ali buscar todos os registros e eu tenho apenas um cliente.
Se lembra lá que a gente criou o campo, o nome do campo, sobrenome e o campo idade, ele já está lá.
Agora, pra gente inserir mais de um cliente, eu posso usar o InsertMany().
A diferença agora é que eu vou passar para ele cada documento como um item de uma lista. Então, cada documento é a coleção de documentos que eu vou passar no Insert. Ele vai estar dentro de colchetes delimitados por chaves e separados por vírgulas. 