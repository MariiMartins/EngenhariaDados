59. Atividades
Estou aqui como encerramento dessa sessão. Eu trago algumas propostas de atividade que você deve desenvolver.
Diferente da sessão em que vai ser apresentado proposta de um projeto maior que eu vou apresentar, a solução aqui fica apenas por sua responsabilidade desenvolver o que não existe, o modelo de comparação e também não há correção, são apenas atividades para estimular o seu a suas atividades práticas do seu conhecimento.
Então, aqui são propostas de você desenvolver algumas consultas utilizando o modelo de dados que você já tem.
Pronto lá no post que o modelo de dados relacional que você já criou, então, assim você vai conseguir ter uma prática maior, uma fluência maior com a linguagem SQL.

Então são quatro consultas.
A primeira, que o objetivo é ver as compras de um cliente específico. Então, o que essa consulta deve trazer?
Ela deve trazer o nome do cliente, o produto, a quantidade, o valor total e a data da venda. E deve ter um filtro de código do cliente. Então, o usuário, quando rodar a consulta, ele vai botar qual o código do cliente. Ele quer ver e ele vai ter todas as compras daquele cliente.  Você, opcionalmente, ainda pode botar uma cláusula ordem e para ordenar, por exemplo, por data ok. A data é um campo que vem ali, mas você ainda pode ordenar por data, a outra consulta, que, na verdade, aqui são duas consultas. Porém, elas são semelhantes e a lista dos cinco melhores e dos cinco piores vendedores. Então, a consulta tem que trazer apenas os cinco melhores vendedores e apenas os cinco piores duas consultas diferentes.
Na verdade, a única coisa que você vai mudar lá é o derby, né? Que vai vai ser crescente e outra vai ser decrescente.
O que ela vai trazer aqui? O nome do vendedor, o total de vendas do vendedor agrupado por vendedor ou de lado pelo total de vendas. Para ter uma ordem bairro dos cinco melhores, você ordena pela venda crescente e decrescente. Opcionalmente, você ainda pode colocar outras informações, por exemplo, se você quiser botar o período para, por exemplo, o mesmo ano. Mas, em princípio, a consulta aqui o objetivo não é trazer por período, é apenas o total apenas de toda de todas as vendas. Quais foram os melhores e os piores vendedores?

A outra consulta é o total de vendas em determinado período. Então, por ser um determinado período, tem um filtro de mês e ano. Você deve informar lá qual o mês e qual ano você quer que retorne o total de vendas do período, o que você, o que a consulta deve retornar, o produto e o total de vendas do produto agrupado por produto. Então, você vai ter lá, por exemplo, o produto a vendeu, por exemplo, sem o produto, por exemplo, produto B vendeu 500.  O produto que aquilo vendeu, o produto B vendeu 500, o produto você vendeu 300.
Esse é o resultado que a consulta deve trazer e deve trazer um filtro por mês e ano.

Então você quer ver o total de vendas por período.
Você quer ver só um mês e um ano. Você muda lá na cláusula SQL. Qual o mês de qual ano você quer vir e a última consulta aqui?
Se vocês lembram o nosso modelo, ele tem um campo no item vendas, tem um campo de desconto e às vezes os vendedores começam a dar mais desconto do que deveriam.
Existem sistemas que controlam e existem outros que não.
Então qual é a ideia?O que a pessoa que estiver rodando a consulta ela consiga visualizar os produtos que tem maiores descontos e que apareça também o nome do vendedor que está dando o desconto, então é agrupado por produto.

Então existe uma semelhança aqui com o campo de cima.
Só que, em vez de trazer aqui o total de vendas, você vai trazer o total de descontos que foi dado para cada produto.
Você pode, por exemplo, aqui, se você quiser ter uma informação mais detalhada do vendedor e não do produto, você, em vez de agrupar por produto, você não agrupa.
Você vê produto ou produto por vendedor? Qual foi o desconto que foi dado?
Então fica aí algumas sugestões de consultas para você desenvolver.