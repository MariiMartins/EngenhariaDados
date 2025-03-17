- 93. Criando uma Tabela Desnormalizada
Então agora a gente vai criar uma tabela normalizada, que traga o nome do cliente, a data da venda, o nome do vendedor, o produto, a quantidade e o total da venda.

Eu vou então começar aqui o Select, primeiro com o nome dos campos.
Então a gente vai fazer um select  cliente, data.
Se você olhar lá no diagrama, o vendedor, o nome do vendedor está no campo nome. Só que para ficar mais fácil vamos colocar, aliás, nome, az, vendedor, produto, quantidade e total from. Aí a gente vai usar como base a tabela vendas que eu vou dar, aliás, para ver. E aí a gente tem que fazer um inner join com a tabela de clientes, com as tabelas e tem venda com a tabela de produto e com a tabela de vendedores. Para ter todas essas informações que a gente colocou ali no Select, então, primeiramente, Inner join clientes que eu vou dar.

Ponto e de vendedor é igual a ID  tabela de vendas e de vendedor. Vamos rodar aqui, ver se deu certo ou nossa consulta, se ela está. Se não tem nenhum errinho de sintaxe, nada está tudo ok. Vamos tirar o limitador que rodar de novo.
E pronto 940 registros. Esses 940 registros equivalem a todas as nossas vendas inelegíveis. Eles foram feitos a partir da perspectiva da tabela de vendas.

Se a gente fizer isso a partir da perspectiva da tabela de itens venda.A gente está olhando as vendas da perspectiva da tabela, itens, venda e não dá tabela de vendas. Então, cada venda ela vai ter um ou mais registros aqui.

Por que isso é importante? Por que eu estou fazendo a partir da Tabela de vendas e que, se por exemplo, você for carregar esses dados em uma ferramenta de dashboards, você facilmente consegue consolidar os dados por venda.
Mas se você quiser ver detalhamento de venda, o que se chama de drill down, você consegue descer até o item de venda.

É uma questão de perspectiva. A gente estudou isso lá e o nível de detalhamento que a gente está utilizando; 
A gente quer criar uma tabela que traga essas informações já normalizadas, de forma que o usuário não precise criar uma consulta, não precisa fazer interdições. Existem várias formas de fazer isso.
Eu posso criar uma via materializada, mas a forma que eu vou utilizar aqui eu vou transformar isso numa tabela.
E na maioria dos bancos relacionais, a gente consegue fazer isso de uma forma bem simples.
Com a palavra INTO, o nome da tabela Fato Vendas.
Então eu vejo quando eu vou dar essa consulta aqui o Redshift vai criar essa tabela, que vai ter exatamente as mesmas colunas e o resultado dessa consulta que vamos executar aqui para ver o que acontece. Então ele está criando a, executando a consulta e criando a tabela. Agora vamos atualizar aqui o.
Vou abrir que o nosso ed publique.E aqui está o fato vendas, Então, agora vejam que eu consigo fazer um select
* from fato vendas.
Vamos rodar. E vejam que interessante eu consigo, por exemplo, filtrar o vendedor pelo nome diretamente, sem precisar fazer join. O vendedor é igual a Armando Lago.
Só para citar aqui um exemplo.Mas essa etapa que a gente criou uma tabela que desnormalizada, chamada Fato Vendas.
