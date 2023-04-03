43. Formas Normais: chaves e outros aspectos
Então vamos entender um pouquinho melhor, que são as chaves primárias.
Então, o objetivo de uma chave primária é minimizar a redundância. Então, ela é um identificador exclusivo daquele registro na tabela no banco de dados. Então, como a gente viu lá um cliente, ele vai ter uma chave primária que não pode ser repetida. O sistema gerenciador de banco de dados, ou seja, o Oracle PostGree, o SQL Server, é que vai garantir que, uma vez cadastrado, o cliente com uma chave primária não vai ser possível cadastrar outro com a mesma chave. Primeiro, isso é função do sistema gerenciador de banco de dados. Se alguém tentar inserir, ele vai emitir um erro alerta e não vai permitir que esse registro seja inserido.
Uma chave primária, ela pode ser criada artificialmente pelo sistema gerenciador de banco de dados. É o que a gente chama de incremental. No nosso caso prático, a gente vai usar esse tipo de chave primária ou pode ser o que a gente chama de um valor natural, o CPF. Então eu posso ter lá um cadastro de clientes que eu decida cadastrar o cliente com CPF e criar esse campo como chave primária. É uma decisão exclusivamente de quem vai fazer a modelagem do banco de dados. Não existe uma regra se a chave primária ela tem que ser produzida pelo sistema gerenciador de banco de dados ou se ela vai ser natural, a gente diz aqui que ela é incremental porque o gerenciador de banco de dados, automaticamente ele vai atribuindo valores de forma incremental.

Então o primeiro cliente vai ser um, o segundo vai ser dois, o terceiro três e assim sucessivamente.
Outra característica que o banco de dados que tabela de um banco de dados podem ter são com relação a chaves primárias compostas e as chaves primárias simples.
Não existem tabelas com mais de uma chave primária.A tabela do banco de dados tem apenas uma chave primária.
O que acontece é que, às vezes, a chave primária pode ser composta por mais de uma informação, por mais de um registro.

Então, veja aqui essa chave primária, que é simples é o ID do cliente. Então a integridade é mantida só sobre este campo. Então, se eu colocar aqui um cliente número um e eu tentar colocar o cliente de número um de novo, eu vou ter um erro. O sistema gerenciador de banco de dados não vai permitir.
Na chave primária composta, eu tenho mais de uma coluna, mas de um atributo que compõe a chave primária.
E a integridade referencial se dá pelas três colunas, pelos três atributos.
Então, o que acontece? Eu posso ter um ID de funcionário número um no mês de competência dois e no mês e no ano de competência 2019. Então, ele é a chave primária. Está composta por esses três registros.

O que acontece? Um funcionário não pode receber um abono duas vezes no mesmo funcionário no mesmo mês, no mesmo ano, não pode receber outro abono. Então, o que acontece se você tentar inserir de novo lá no banco de dados o funcionário um no mês de competência dois de 2019. O que vai acontecer aqui? Um erro. O sistema gerenciador de banco de dados não vai permitir. Você está violando a integridade da chave primária, que aqui no caso, é composta pelas três colunas.

Agora, o que acontece? no outro mês o funcionário um no mês três, no ano de 2019 ele vai receber um abono e este registro aqui ele vai ser incluído com sucesso, porque a violação da chave primária que não acontece, vejam ela, é composta apenas pela repetição das três colunas, não apenas de uma, já que em cima não. Se eu tentar incluir um cliente com o mesmo número, como em uma chave primária simples, ha violação da integridade.
Então, só reforçando o conceito não existe mais de uma chave primária, uma tabela e um banco de dados pode ter apenas uma chave primária. O que existe são chaves primárias compostas.

A gente viu já no nosso modelo os relacionamentos, no relacionamento. Eu tenho uma chave primária que é colocada em outra tabela como chave estrangeira. Então, aqui a gente tem a chave de vendedor, e vendas é uma chave estrangeira pela sigla FK e de vendedor. Então este aqui a gente diz que um relacionamento, um para muitos.
Então um único vendedor. Aqui só posso ter um. Ele pode constar em muitas vendas. Um vendedor pode fazer muitas vendas e um relacionamento, um para muitos. Então aqui a chave primária ela é exclusiva.
Quando ela vem para cá, não.Aqui ela pode ocorrer n vezes. Quanto mais vezes o vendedor vender, mais ele vai aparecer na minha tabela de vendas. 

Agora, observe esse caso aqui eu tenho vendas e eu tenho produtos. Eu preciso, de alguma forma, informar quais produtos fizeram parte de uma venda. Então, imagine o seguinte você chega numa loja para fazer uma compra.
Você não compra um produto, só você pode comprar vários produtos. Por exemplo, se você vai numa loja de peças, você pode ir lá comprar uma pastilha de freio, uma lâmpada, uma borracha. Você comprou três produtos lá no seu banco de dados o que você tem? Você tem a tabela de produtos e você tem a tabela de vendas. Aqui você tem o cadastro de produtos e aqui você tem dados de vendas.
O que acontece se eu vendi três itens, o que eu teria que fazer?
Eu teria que, por exemplo, colocar aqui um ID do produto e eu iria inserir três registros aqui nessa tabela. Só o que acontece. Eu vou inserir a data de venda de novo, o ID  do vendedor de novo o ID  cliente de novo, o total e o desconto.Ou seja, eu ia repetir informações e eu ia estar incorrendo aqui num problema de redundância de dados e de integridade. Então, como a gente tem o X aqui. Quer dizer que este modelo aqui ele não está correto. Esse tipo de relacionamento não está correto.

É aí que a gente tem um conhecido relacionamento. Muitos para muitos, ele para n.
Então, antes a gente tinha um para n. O vendedor podia estar em várias vendas. Agora, quando a gente tem vendas e produtos, a gente tem um lançamento muitos.
Para muitos eu posso ter vários produtos em uma venda e eu posso ter uma mesma venda, que tem vários produtos.
Como que eu resolvo isso criando uma tabela de integridade Muitos, para muitos. Eu vou resolver esse conflito fisicamente no banco de dados, esse conflito não esse problema no banco de dados, através da implementação de uma tabela.

Normalmente, a chave primária desta tabela é composta pelo que pelo identificador único da venda e o identificador único do produto. Vejam se eu vendi mais de um produto na mesma venda se a quantidade de um produto aqui de um mesmo produto é mais de um, eu vou simplesmente aumentar a quantidade eu não vou cadastrar o item de venda de novo.
Então, por isso que a chave primária que funciona, eu nunca vou repetir ID de  produto para ID  de venda na mesma venda. Não vou vender o produto mais de uma vez. Se eu vender ele mais de uma vez, eu vou simplesmente adicionar quantidade. Eu não vou adicionar um outro registro. Então, essa é uma chave primária que se cria naturalmente em itens de venda, fazendo a relação entre vendas e produto.

Claro que isso aqui é um caso clássico de um relacionamento, n  para n  de vendas. Mas o relacionamento n pra n acontece de forma espontânea diversas vezes em vários tipos de modelagem de negócio, em bancos de dados.

Então, aqui um exemplo físico com dados do relacionamento n para n. Então, vejam aqui a gente tem o identificador da venda, que tem um vendedor que tem um cliente que tem uma data e que tem o total da venda.
Por que o total da venda fica aqui?  Porque, como a gente vendeu três produtos, faz mais sentido colocar o total aqui do que nos itens a venda que está consolidando o valor total dos produtos vendidos, certo?
Então, o ID vendedor e ID cliente aqui eles apontam para outras tabelas.Então, aqui eu tenho a venda, aqui eu tenho o produto e aqui eu tenho o meu relacionamento, n para n.
Então eu vendi o produto dois, 09h10.
Aqui eu tenho o ID da venda, que foi a primeira venda, a quantidade foi um de cada quilo. Tem o valor unitário, o valor total e o desconto. Então é outra coisa que eu posso colocar aqui, fazer um novo relacionamento, muitos para muitos lá no cadastro do produto eu tenho preço.Se eu apliquei um desconto, eu vou registrar aqui no meu item de venda, que também tem que ser na tabela de relacionamento, muitos para a multidão lá na venda, porque o desconto normalmente é individual para o produto.
Se a modelagem do negócio diz que muda sobre o total da venda. Aí sim, aí o desconto poderia passar para esta tabela de vendas.