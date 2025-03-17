Na nossa implementação prática do MongoDB, nós vamos voltar JJBike e o objetivo é criar um banco de dados onde vão ser armazenados comentários de usuários que foram coletados de redes sociais, então comentários a respeito da empresa.

Então, o objetivo é que no futuro, esse banco de dados seja utilizado pelo cientista de dados para minerar sentimentos. E o gestor da empresa quer saber qual a percepção atual dos clientes a respeito da empresa e quer acompanhar mudanças nessa percepção. Então, o MongoDB foi escolhido pelo suporte natural a documentos. Então um post uma rede social. Ele tem uma estrutura natural no formato JSON, no formato de um documento. 

Então, a gente vai começar a ver que os principais comandos, as principais funções do mundo e depois, obviamente, você não precisa se preocupar que a gente vai ver isso. Na prática, a gente vai praticar, mas primeiro a gente vai conhecer como o Mongo funciona.

Então, primeiro você precisa criar um banco de dados. A criação do banco de dados do Mongo é feita de forma implícita. Você usa o comando e use o nome do banco de dados. E mesmo que o banco de dados não exista, vejo aqui que ele informa que ele alterou o prompt para uso nesse banco de dados.
Só que o que acontece você precisa inserir dados nesse banco de dados, senão ele não é persistido. Então, você passa a usar o banco de dados e insere a primeira relação com o primeiro documento e automaticamente o banco é criado fisicamente.

Como é que a gente insere um documento bom, mas antes de inserir um documento, não preciso criar uma relação. Sim, você até você até pode criar a coleção explicitamente você declarar. Só que também você pode fazer isso de forma explícita, ou seja, você insere diretamente um documento, não existindo ainda a coleção, o Mongo vai criar então veja só que o DB faz parte sempre da sintaxe dos comandos, Post Aqui eu tenho o nome da minha coleção. Então, lembra a coleção é o equivalente a tabela do banco de dados de documentos onde os documentos vão ser armazenados. Então eu estou criando a coleção que vai chamar posts aqui, o nome que eu estou dando e estou usando o comando Insert de Inserção. Então vejam aqui eu tenho o início do documento usando a estrutura do JSON então eu tenho aqui o nome do campo, o valor do campo, nome José. Aqui vírgula. Tenho outro campo, o valor do campo, aqui o comentário, então um comentário do José. Ele disse que a empresa tem bons produtos e o terceiro campo aqui é uma data que eu sei ou então provavelmente a data da postagem. Então eu vejo que o formato aqui a partir do abre e fecha parênteses é JSON.

Você tem uma abertura de chave, um fechamento de chave campo, o valor vírgula campo valor separados por dois pontos. Aqui embaixo nós temos a saída do Mongo, ele está dizendo que o resultado da escrita, um documento foi criado, ele foi inserido. Eu posso usar o mesmo comando para inserir mais de um documento simultaneamente. Então, vejam aqui eu estou usando a mesma função e tenho três documentos separados por chaves. Então vejo que a mesma estrutura, cada um deles, o nome, o nome do campo, dois pontos, o valor do campo, o nome do campo, dois pontos, o valor do campo e assim segue os campos.
Aqui, como eu tenho mais de um documento, os documentos aqui são separados por vírgulas, aqui o último não tem um vírgula, porque ele é o último, eu não tenho nenhum para separar.

E a diferença que eu tenho aqui do comando anterior e que, como eu tenho um conjunto, eu estou usando colchetes. Então colchetes é usado para determinar o início e o fim do conjunto. E as chaves, abertura e fechamento das chaves para determinar o início e o fim do documento. O parênteses é o parentes da função, então eu estou executando a função insert abre e fecha parêntese dentro da função insert.

Eu tenho um conjunto de dados, um conjunto de documentos, então eu tenho colchetes e cada documento delimitado pela Chaves. Então o comando vai até aqui, a função vai até aqui e esta aqui é saída. Então ele está me dizendo que foram inseridos três documentos. 

Bom como a gente faz para recuperar documentos que já se encontram no banco de dados que já foram inseridos.Então, aqui eles têm os principais métodos.
•	O DB Find, com o nome da coleção no meio.
•	DB Clientes FindOne, aqui ele vai retornar, apenas um.

Aqui o nome da coleção é clientes que a gente estava vendo lá, por exemplo, outro exemplo a coleção era posts, então, aqui ele vai retornar todos os documentos, porque eu não estou passando nenhum parâmetro para o Find.

O findOne()  vai retornar apenas o primeiro documento do resultado da consulta. Eu posso passar num critério de restrição que a gente vai ver depois.
Se eu não passar critério nenhum, ele vai retornar apenas um documento.

•	E o, dB.clientes.find().pretty(),  ele vai retornar o documento de forma formatada, de forma estruturada.
O DB find, o DB findOne eles vão trazer o documento apenas no formato de uma linha.

Então, aqui a gente tem o find sem nenhum parâmetro. Ele retorna simplesmente a relação de documentos sem estrutura, Ele traz eles linha a linha, este identificador, aqui ele é criado automaticamente pelo Mongo.
Quando você faz a inserção do documento, você pode, opcionalmente, inserir esse identificador. Essa chave não é um campo único.

A única questão que se você for inserir, se você vai fazer isso ao invés de deixar o Mongo criar a chave é que o valor tem que ser único, tem que ser uma chave primária, senão você vai violar a integridade referencial do Mongo.

Aqui usando a função Pretty.
Então, veja, eu estou buscando os documentos na coleção Post, porém, depois do find  eu tenho o .pretty, então esse pretty ele formata o documento, ele traz o documento, mas formatado cada campo em uma linha, aqui o comando ele continuaria, trouxe apenas um documento.
Então, essa diferença de usar, por exemplo, DB. find, e usar o pretty junto.

E aqui o DB.FindOne, Então o findOne sempre vai trazer apenas um documento, um registro apenas, Mesmo que você tenha lá 500 documentos, ele vai trazer apenas o primeiro.

E se eu quiser ler um documento específico?
Bom, existem várias formas, então a gente está vendo aqui a primeira forma.
Eu estou passando aqui dentro um filtro para busca do documento.

Como é que funciona? Então eu estou simplesmente dizendo o que o campo, o nome deve ser José. Então ele vai me retornar apenas os documentos que obedeçam esse critério. Então vejam o retorno do documento onde o campo nome é igual a José. Obviamente que se tivesse mais de um documento com esse critério, ele iria retornar mais de um documento.

Vamos observar aqui este outro exemplo, com AND, com o operador lógico E, então incluir mais um registro que tem José, porém, a postagem dele aqui ele reclama que a loja é suja. Quando eu faço aqui o AND, eu coloco que o critério de busca é José e postagem bons produtos. Então ele retorna a postagem do outro José, que fez um elogio, esta postagem aqui de loja suja não aparece porque não atender os critérios do filtro estabelecido aqui, que o nome teria que ser José e a postagem teria que ser bons produtos.

Eu posso estabelecer também operadores, condições de buscas usando operadores, um operador no Mongo, ele vai ser sempre precedido pelo sinal de cifrão ($).
| Operador | Descrição |
| --- | --- |
| $eq | igual |
| $gt | maior que |
| $gte | maior ou igual que |
| $lt | menor que |
| $lte | menor ou igual que |
| $ne | diferente de |
| $in | contém |
| $nin| não contém |


Então vejo aqui o exemplo da condição AND com o operador lógico menor ou igual que.
Então o que a gente vai fazer depois na hora da aula prática, a gente faz a inserção de dois novos registros. Vejam que interessante aqui eu estou inserindo documentos da mesma coleção, na mesma coleção posts, mas eu estou criando um novo campo, veja só para vocês ver que a gente pode alterar. A gente pode mudar a qualquer momento o schema, a estrutura do documento. Não existe, uma estrutura definida, uma estrutura rígida. Então esses dois documentos aqui adicionaram um novo campo.

O que meu DB.posts.find() faz. Vejam que ele está buscando ou a gente tem o operador menor ou igual a 12. Então, como eu tenho dois registros, um com idade 25, outro com 21 O que ele faz?
Ele busca aonde a postagem, o texto de postagem e produtos caros.
Dois Os dois atendem, mas operador lógico menor igual é 12. Então, por isso ele retorna apenas este registro como uma condição em que tem que atender os dois critérios.

Então, eu posso também usar uma condição que atenda um critério ou o outro. Então, vejam eu estou dizer eu estou usando o operador, estou passando aqui entre colchetes. O critério ele está indo colchetes porque é um conjunto. E eu estou dizendo que pode ser ou José ou Antonio pode ser qualquer um dos dois nomes que eu queira retornar na minha busca e ele me retorna que três registros ao porquê?
Porque eu tenho o nome José, Eu tenho o nome Antônio e eu tenho novamente o nome José. Então e aqui é um exemplo do uso do operador ou lembrando que a implementação dele está aqui?
