58. Mais Joins
Agora vamos ver mais algumas operações interessantes que a gente pode fazer utilizando junções utilizando Joins. Mais uma vez eu peço que você utilize e visualize o diagrama do banco de dados. Fica mais fácil de entender o que a gente está fazendo.

Na nossa primeira consulta. Você lembra lá que quando a gente fazia um select nas vendas, eu tinha apenas o ID do vendedor. 
Por quê? Porque o ID do vendedor é uma chave estrangeira para tabela de vendedores. Só que o nome do vendedor está lá na tabela de vendedores.
Então, se eu quiser ver a tabela de vendas com o nome do vendedor, eu tenho que fazer uma junção da tabela de vendas com a tabela de vendedores. Então eu faço um inner join.

Então, como é que eu vou fazer isso? Vamos supor que eu queira o nome, a data e o total.
Veja o seguinte eu posso não qualificar que esse nome de colunas, desde que não haja ambiguidade que o que eu quero dizer com isso eu vou fazer
um join entre vendas, a tabela de vendas e a tabela vendedores.
Se o nome existir apenas na tabela de vendedores, não tem problema. Agora, se eu tivesse essa coluna em mais de uma tabela, eu teria que qualificar. Eu teria que colocar, por exemplo, vendedores. nome. Como não é o caso aqui eu posso deixar apenas nome, data e total.
Então select nome,data, total  from relacional.vendas as vendas
Eu vou dar um alias aqui para ver as vendas, vou chamar simplesmente de vendas mesmo. Vou fazer um inner  join relacional.vendedores as vendedores.

Então, assim eu não preciso novamente colocar, relacionar o ponto Vendedores eu posso só falar vendedores.
É que quando eu faço inner join, tenho que dizer o campo onde vai haver o match então ou então agora eu uso alias vendas ponto e ID vendedor é igual a vendedores, ponto e de vendedor. Vamos ver que está tudo certo na nossa digitação e pronto.
Então, agora a gente tem uma tabela de vendas. Que nos mostram o nome do vendedor, não apenas o código, isso graças ao inner join. Então fez aqui a junção.

Agora imagine que, além de fazer um join com o vendedor, você também quer mostrar o nome do cliente. Então, você pode ver que na tabela de vendas existe o id cliente. Então, isso seria mais um campo para adicionar que vou fazer aqui. Vamos fazer aqui umas alterações. Mais uma coluna para fazer um join

Primeiro vou mudar o nome. Vou colocar vendedor então, o nome da coluna, em vez de nome, vai aparecer vendedor para ficar claro que é o nome do vendedor. Então, o nome do vendedor, a data, o total. E eu quero também o cliente, que é o que a gente vai adicionar. Vamos botar o cliente aqui depois do vendedor, então eu vou ter o vendedor, o cliente, a data e o total. Então eu tenho já o relacional vendas. Eu tenho já o Inner Join com os vendedores. Agora eu vou tirar este ponto e vírgula aqui e vou adicionar que um outro é inner join, relacionar o ponto clientes. Vou criar aqui uma linha de clientes ou vendas. id Cliente e a minha chave estrangeira igual a clientes que é o Alias, é a minha chave primária, que é o mesmo nome cliente. 
Vamos ver que se deu tudo certo e pronto.
Então aqui a gente tem o vendedor, o cliente, a data e o valor de cada venda, que é assim claro. A gente pode fazer Joins entre múltiplas tabelas.