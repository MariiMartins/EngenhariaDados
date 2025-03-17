54. Agregação e Distinct
Então agora vamos falar de agregação. Você vai ver que algumas técnicas de agregação e também vamos falar do distinct. Vamos supor que eu queira saber quantas vendas eu tenho na minha tabela de vendas, ou seja, quantas vendas o meu sistema registrou. Eu não quero saber valor nem qual foi o vendedor, só quero saber quantas vendas eu tenho no meu banco de dados, então eu posso fazer isso com uma função count.

Então vou fazer um count asterisco e eu poderia colocar ali um nome de uma coluna. Eu ia dar o mesmo resultado relacionado ao Ponto Vendas, então ele vai simplesmente me trazer contábil. Então eu tenho 400 vendas.

Agora vamos supor que eu não quero simplesmente saber quantas vendas eu tenho. Eu quero saber quantas vendas eu tenho, cujo valor total é maior que 6000. Então você lembra lá que existe uma coluna total. Então pra isso eu posso manter que o Select count from relacional vendas.
Mas eu vou colocar aqui um where total maior igual a 6000.
Então eu quero que ele me conte quantas vendas existem com o valor, que o valor seja maior e igual a 6000. Então, o que ele está me dizendo aqui? Eu tenho 400 vendas. Dessas, 214 são de valor 6000 ou mais. Ok, é isto que é essa consulta está me respondendo.

Agora vamos supor que eu queira saber a quantidade de vendas por vendedor. Ainda não me interessa saber quanto cada vendedor vendeu, eu quero saber a quantidade de vendas por vendedor.
Antes, vamos fazer aqui um select asterisco from relacional ponto vendas limite o ano só para pra gente ver que a gente teclar aqui.

Quais são as colunas? Então você pode vir aqui que eu tenho uma coluna ID vendedor. Então essa coluna é uma chave estrangeira e a gente já estudou isso. Então é uma chave que aponta para uma tabela de vendedores, se eu quiser saber o total ou a quantidade de vendas de um vendedor pelo código dele. Olhando apenas o código, eu posso fazer essa consulta apenas nessa tabela. Agora, se eu quiser saber o nome do vendedor, eu vou ter que fazer uma junção com a tabela de vendedores.

Então, vamos supor que a pergunta agora é quantas vendas cada vendedor teve, mas o código do vendedor é suficiente? Eu sei pelo código qual o vendedor e então só pelo código eu consigo.
Então, como eu faço isso? Eu faço um select ID vendedor. Eu vou fazer um count de vendedor from relacional ponto vendas. E eu vou fazer aqui agora uma função de agregação group by ID vendedor. Então eu estou agrupando as vendas por vendedor e mostrando a contagem. Vamos ver qual é o resultado.

Então, veja, ele está me mostrando aqui que o vendedor 8 teve 30 vendas, deixando claro aqui que esta contagem aqui é o número de registros, não é o número de produto, a quantidade de produtos ou o valor das vendas.
Ele simplesmente está me mostrando quantas vendas foram registradas para o vendedor oito,  para o vendedor dez,  para o vendedor nove.
Lembrando que aqui a chave estrangeira, o nome do vendedor está na tabela de vendedores, agora vamos supor que eu não queira mais saber quantas vendas cada vendedor teve. Eu quero saber quanto cada vendedor vendeu.
Então, para mim, saber quanto cada vendedor vendeu, você lembra da gente ter coluna total. Só que eu, em vez de fazer uma contagem, em vez de usar um count na coluna total, eu vou fazer uma soma.
Eu vou usar o sum, então vamos ver como isso ficaria. Vamos fazer um select ID vendedor sum total from relacional  ponto vendas groupby ID vendedor.

Então, vejam que a consulta é semelhante à consulta anterior, porém eu não estou contando, estou somando e a coluna agora que me interessa é a coluna total.
Então vamos aqui executar. E aqui está o resultado. Então está me dizendo que o vendedor oito ele teve o total de vendas 183.000. O vendedor 2 425.000, e assim por diante.

Vamos supor agora, então, que eu queira ver apenas um determinado vendedor. Então eu posso colocar aqui antes do groupby uma cláusula no lugar é de vendedor, por exemplo ou IDvendedor igual a um.

Então eu vou contabilizar que vou somar todas as vendas, apenas o vendedor um. É claro que o resultado aqui vai ser o mesmo. A diferença que eu estou mostrando. Apenas um vendedor imagina que tivesse centenas, dezenas ou centenas de vendedores ou até milhares. Eu quero ver apenas um vendedor específico, em vez de mostrar todos e sair procurando.

Agora vamos falar do distinct. Vamos supor que, por exemplo, você sabe, você lembra que lá na tabela de clientes existe o status do cliente, que a gente sabe que é silver, platinum e gold.
Mas vamos supor que você quiser saber de forma distinta, de forma única, todos os status possíveis.
Então, eu faria, um:
 	select  distinct status from relacional.Clientes 
Vamos executar e vejam ele não me trouxe os extratos de todos os clientes.
Ele me trouxe uma linha única de cada status. Então eu sei que os únicos estados que existem, os únicos estados possíveis na minha tabela de clientes é o Silver, o Gold e o Platinum.