45. Modelo Relacional da JJBike
Aqui que você está vendo na tela o modelo relacional de JJBike, esse modelo é importante para o nosso curso, porque ele vai ser utilizado bastante durante o curso. Tem vários exemplos, então é interessante que você conheça esse modelo.

É um modelo simples, mas ele implementa as principais características de um modelo relacional. Então, para fins didáticos, ele é muito bom. Então, era interessante que você conhecesse bem esse modelo até, se possível, você fizesse um print ou imprimisse. E você se familiarizar com ele, que a gente vai rodar consultas, a gente vai importar dados.
Depois, na próxima sessão, nós vamos criar um armazém de dados baseado neste modelo.
Então, como falei repetindo, é bom você que você tenha um conhecimento bem legal desse modelo.
Então, a JJBike é uma loja fictícia de produtos relacionadas a bicicletas a ciclismo.
Então, o que a gente tem aqui? Tem um cadastro, uma tabela de vendedores. Você tem o identificador do vendedor, o nome, você tem uma tabela de clientes, tem o identificador do cliente. Aí você tem o cliente qual é o nome dele, o estado, o sexo, o status, o status do cliente. É como se fosse um status de uma empresa aérea, aquelas questões de fidelidade. Então, ele pode ser silver gold ou platinum, quanto mais ele compra produtos da loja, melhor é o status dele. 
Então a gente vai ver algumas questões lá com relação a atualização do status. A gente tem um cadastro de produto, tem o identificador do produto, aí o produto, o atributo produto e uma descrição do produto e o preço é o preço de tabela do produto.
Bom, aqui então a tabela de vendas, toda a venda efetivada, ela é registrada aqui, ela tem o identificador único da venda.
Ela recebe o ID do vendedor, ou seja, quem fez a venda. Ela tem um identificador do cliente, a data que a venda foi realizada e o total da venda. Então, o total de todos os itens que foram vendidos e calculado aqui. E, por fim, aqui a gente tem um relacionamento, muitos para muitos que diz quais produtos foram vendidos em uma determinada venda.Então, uma relação n para n, a chave primária é composta, ela vem do identificador do produto identificador da venda.

Então, o que acontece?
Eu posso repetir o ID da venda e eu posso repetir ID do produto, mas os dois ao mesmo tempo não.
Em uma única venda, só posso ter registrado o mesmo produto uma vez. Se eu vendi o produto mais de uma vez, eu vou aumentar aqui a quantidade. Então, a quantidade de produtos daquela venda, daquele produto, o valor unitário, o valor total, porque eu posso ter vendido mais de um, é considerando aqui o desconto que foi dado certo. Então este é o modelo que a gente vai usar bastante durante o curso.