46. SQL Parte I
A linguagem SQL ou a linguagem de consulta estruturada do inglês Structured Query Language é uma importante linguagem para consultar, alterar e manter bancos de dados relacionais.

Ela é tão importante que produtos da era Big Data, ou seja, que surgiram depois do modelo relacional, muitas vezes buscam compatibilidade com essa linguagem porque ela é extremamente difundida, utilizada e conhecida. A linguagem SQL está dividida em categorias, então a gente tem:
●	DQL que é a linguagem de consulta de dados ou data query language. Esse tipo de consulta, que é o clássico select, ele não faz nenhum tipo de alteração nos dados nem na estrutura dos dados, não altera metadados nem dados, simplesmente consulta. Então você executa um comando e ele retorna um conjunto de dados de acordo com a situação que você passou.
●	DMS - Data Manipulation Language, ou Linguagem de Manipulação de dados, são as instruções que são capazes de alterar dados. Então tem a inclusão com insert, update para atualizar e delete para excluir dados. Então aqui também não mexe na estrutura dos dados, mas altera os dados em si, na forma de inclusão, de atualização e de exclusão.
●	DDL - linguagem de definição de dados data definition language, que aqui se está mexendo na estrutura dos dados. Então a gente cria tabelas e índices views ou altera essas tabelas e índices desses views.
●	DCL - linguagem de controle de dados, que é a linguagem que cuida da segurança e da privacidade dos dados, com um Grant e Revoke que vai dar permissão para usuários e para grupos sobre tabelas, sobre vírus, sobre campos, enfim, aí depende do sistema gerenciador.
●	DTL - linguagem de transmissão de dados, um banco de dados relacional ele é capaz de controlar transações. Então a gente viu lá exemplos de casos em que a transação tem que ser desfeita, que é um rollback, ou ela tem que ser confirmada com commit. Então aqui temos os comandos begin transaction, commit e rollback. Essa sintaxe é obviamente de todos os comandos SQL pode mudar de um banco de dados, de um sistema gerenciador de banco de dados para outro.

Então, aqui, um exemplo simples de uma estrutura básica, de um comando de consulta de dados. Então essa aqui é a estrutura básica, então sempre vai começar com Select, aqui você tem a cláusula opcional distinct, que vai trazer valores únicos, sem repetição. Aqui você vai informar as colunas que você quer retornar (from), se você quiser todas, você vai colocar um asterisco com o nome da tabela ou das tabelas que você vai consultar. O where é onde você vai colocar uma condição de restrição para não retornar todos os registros. Então, por exemplo, você vai querer vendas cujo valor seja maior que 6.000 R$. Você pode agrupar (group by) e você pode ordenar (order by) o resultado dessas consultas. Os principais operadores isso já deve ser conhecido: And, or, not, menor, maior, menor, igual, maior e igual ou diferente.
Então você pode, por exemplo, colocar aqui numa cláusula o Where, onde determinado campo, por exemplo, o valor seja maior que 10.000 R$. Então você está criando uma restrição com um operador maior, o Between, você consegue criar intervalos. Então, por exemplo, se você quer retornar uma consulta cujo valor seja entre 600 e 800 reais, então você pode usar o Between. O like ele retorna um texto, porém você pode usar um curinga, que é o %
(Sinal de percentual) para que ele busque antes e depois do texto.
Então, por exemplo, se você colocar aqui n a n com porcentagem antes e depois(%nan%) e você tiver o nome Fernando, ele vai retornar este valor com este nome por causa se você usar aqui o like com esses caracteres curinga aqui que é o percentual.
O in ele verifica um conjunto ou operador de conjunto, então você pode verificar, por exemplo, o status de um cliente. A gente viu lá que a loja de bicicletas tem, tem um status do cliente, que ele pode ser Silver, Platinum e Gold.
Então, por exemplo, eu posso querer pesquisar os clientes cujos status estejam no conjunto. E aí eu coloco lá, por exemplo, Platinum e Gold.
Depois a gente tem as consultas SQL de agregação Então a gente usa com o GroupBy às vezes.
Então, por exemplo, eu tenho count pra contar o número de registros. sum para somar, e AVG para média max e min para valor o max para o maior valor e min para o menor valor.

Aí a gente vai ver alguns exemplos de consultas. Você não precisa se preocupar agora, porque a gente vai executar isso na prática. Então, mas ao final dessa sessão, a gente vai construir esse ambiente relacional e essas mesmas consultas que a gente está vendo aqui. Você vai executá las na prática, mas quando você chegar lá, você já deve conhecer a consulta e o resultado que ela deve retornar.
Então a gente vai vir aqui essas consultas.Depois a gente vai executá la na prática.

A gente sempre foi ver esse ed igual a cifrão aqui. (ed=#) Mas só que você pode ignorar que isso aqui é o prompt do shell do PSQL, que é a ferramenta de pra você rodar a consulta do posgree, então esse conjunto de caracteres que você pode ignorar. Ele vai aparecer aqui nos prints, então a gente tem uma consulta bem básica select asterisco.
Então o asterisco aqui está dizendo para retornar todas as colunas from e aqui eu tenho o nome da tabela.
O que é esse relacional aqui? Então esse relacional aqui é o schema.
O que é um schema? O schema é uma forma de você separar, logicamente, dentro de um mesmo banco de dados, tabelas diferentes.
Então, nessa sessão a gente está trabalhando com um schema relacional. Na próxima sessão a gente vai falar sobre modelagem dimensional e a gente vai ter o schema dimensional. Eles vão estar dentro de um mesmo banco de dados. Mas o que interessa aqui, neste caso, pra nós mesmo é o cliente.
Porém, a consulta precisa saber que o cliente está dentro do schema relacional. Então o schema é apenas uma forma de você organizar as suas tabelas dentro do banco de dados.
Então eu pedi para ele me retornar todas as tabelas e vejo que não tem nenhuma cláusula, eu não tenho uma condição de restrição.

O que ele faz, então? Ele me traz todos os registros. Claro que aqui é um print, não tem todos, mas a consulta vai retornar todos os registros da tabela que existem no banco de dados.
Agora, mais exemplos aqui de consultas de Data Query Legend.
Vejam que aqui eu tenho uma definição das colunas que vão fazer parte que vão ser retornadas pela minha consulta.
Eu não tenho mais um asterisco. Eu estou me dizendo para retornar apenas clientes, sexo, status de relacional, clientes. E tem outra característica que eu estou colocando uma condição que faz uma restrição para o retorno.
Eu estou me dizendo pra ele me trazer apenas os clientes cujo status e silver, então a gente não está vendo aqui no meio nenhum gold e nenhum platinum por causa dessa restrição aqui, nessa consulta do lado, eu tenho uma restrição com or, vejam então é Silver. O status é silver, ora, o status é platinum. Então vejo que a diferença que apareceu um Platinum aqui no meio que antes não tinham. Então eu estou dizendo que pode ser tanto um quanto o outro. Não é uma condição end, ele não tem que ser dos dois e tem que ser ou um ou outro.
Se eu tivesse aqui uma condição end, status, silver and status platinum, ele não ia retornar nenhum registro, porque ele não pode ser Silver e Platinum ao mesmo tempo. O end iria funcionar se, por exemplo, aqui o outro atributo fosse uma outra coluna, por exemplo, se eu quisesse o sexo fosse apenas masculino, aí os registros femininos aqui não seriam exibidos.
Continuando então aqui, com as nossas consultas, novas instruções de retorno de dados. Aqui a gente está usando operadora IN e aqui, nesse caso, ele vai ter o mesmo resultado prático ou neste caso específico, aqui só consigo fazer a consulta de forma mais simplificada.

Eu estou me dizendo que eu quero os clientes cujo status estejam dentro do conjunto e aquilo em forma de conjunto. Se houver, é platinum. Então aqui não aparece clientes com o status gold e aqui eu faço o contrário, eu coloco um not eu estou negando aqui a condição. Eu quero que me traga os clientes, que o status não esteja dentro do conjunto Silver Platinum e aí ele me retorna só Gold são só nove registros aqui.
O Print pegou todos os dados aqui, então eu estou usando o operador like, que a gente falou já lá um pouquinho.
Então o like ele vai procurar em um campo do tipo texto, usando aqui o caractere curinga, que é o percentual.
Ele vai me trazer qualquer resultado que atenda aquela demanda, mesmo que o texto esteja no meio.
Então a gente vê aqui onde botou o cifrão, alb, cifrão. (%alb%)Então ele trouxe Alberto aqui e vejo aqui. Ele trouxe também a Janaína Albuquerque. Se eu não tivesse colocado o percentual do lado esquerdo, a Janaína não viria.
Ok, como eu coloquei do lado esquerdo, ele busca o A L B. Que esteja entre texto tanto à esquerda quanto à direita.
Se eu tivesse colocado só direita, ele ia trazer apenas os 3/1 registros. No retorno da consulta aqui eu tenho uma outra condição, que é numérica. Então eu estou usando operadora aqui maior. Vejam aqui. Então eu peço para ele me trazer todos os registros agora da tabela vendas, onde o total de vendas seja maior que 6000.
Então, qualquer venda que seja menor que ou menor ou igual que 6000 não vai aparecer aqui no meu resultado, só se for maior que 6000. Aqui a consulta é semelhante, só que em vez de maior, eu estou usando um intervalo.
Então eu estou dizendo pra ele me trazer as vendas, cujo total esteja entre 6000 e 8000.
Então, ele vai me trazer as vendas que ao mesmo tempo seja maior que 6000, mas que não sejam maiores do que 8000. Veja esse primeiro registro aqui da outra consulta 8053.
Ele já não vem aqui porque? Porque ele é maior do que 8000 e eu quero apenas entre 6000 e 8000. Agora aqui eu estou usando um operador de agregação. Estou contando os registros.
Então eu estou usando Select Count Asterisco (select count *) contar todos os registros de relacionar o vendas.
Então ele está me dizendo aqui que o sistema tem registrada 400 vendas. Aqui, nesse outro exemplo, eu tenho a mesma consulta, porém eu estou criando uma restrição.
Eu quero apenas saber as vendas cujo valor seja maior que 6.000 R$.
Então, vejo aqui que o total de vendas caiu quase pela metade.

Aqui, neste ou desta outra consulta, eu estou usando operador distinct. Então eu lembro que a gente falou que o distinct ele traz apenas registros únicos. Então eu quero, por exemplo, só quero saber quais são os status existentes.
Eu não preciso fazer um select status from relacionamento, que ele vai trazer todos os clientes, registro. Eu quero saber quais são os status existentes. Então eu escrevo distinct status, promo, relacional, clientes.
Eu estou restringindo aqui apenas a coluna status. E ele vai me trazer apenas registros únicos. Ele não vai repetir.

E aqui, finalizando esse vídeo, essa aula, eu estou agregando informações.
Então, por exemplo, eu quero saber quantas vendas, não o total, apenas a quantidade de vendas por cada vendedor.
Como esse é um banco de dados relacional. Eu não tenho o nome do vendedor aqui nessa tabela. Vendas eu vou ter o nome do vendedor apenas na tabela de vendedores. Pra mim, trazer o nome do vendedor eu tenho que fazer o n join que a gente vai ver depois.

Então, por enquanto, a gente vai ficar apenas com ID do vendedor. Então, eu vou contar quantas vendas cada vendedor tem, de acordo com o ID. Como que eu faço isso?
Eu coloco ali o campo que eu quero contar, o id do vendedor. Vou contar, usar a função de Operação Count, de relacionar o vendas. É aqui que está o grupo e eu vou agrupar pelo id do vendedor.
Então, o que ele está me dizendo aqui? Que o vendedor Oito. Ele teve 30 registros na tabela de vendas, ou seja, ele teve 30 vendas. Quem teve mais vendas aqui, o vendedor de número dois teve 50 vendas. Isso não quer dizer que ele vendeu mais. A gente não está fazendo uma soma do valor.
Ele está apenas contando a quantidade de ocorrências do ID vendedor.
Você poderia facilmente adaptar essa consulta para saber o total de vendas de cada vendedor, segundo a tabela de vendas.