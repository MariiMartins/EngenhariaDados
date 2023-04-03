53. Consultas Básicas
Bom, então agora com o banco de dados populado, a gente pode começar aqui a praticar a linguagem SQL e através da linguagem SQL a gente vai também descobrindo aqui os dados que a gente tem. Eu vou começar aqui fazendo uma consulta básica, que é o:
 	select * from relacional.clientes;

Então aqui eu estou dizendo aqui eu vou selecionar todos os campos do esquema relacional, o ponto clientes. Uma observação importante aqui sobre o schema que é esse prefixo aqui da tabela. Quando você utiliza a maioria dos bancos de dados relacionais, ele possui esse conceito de schema, que é uma forma de você poder separar logicamente diferentes assuntos ou unidades dentro de um mesmo banco de dados.
Existe sempre o schema public, que é o esquema padrão. Se você criar suas tabelas sem citar um schema, sem definir o schema, eles vão ser criados no esquema público. E se você criar no schema público, você poderia consultar simplesmente assim, sem o schema.

Então, se você fizer um select * from clientes.
Você está subentendido que você está consultando a tabela de clientes que está no banco de dados e de um schema público. Porém, como nós criamos um schema próprio aqui ou relacional, a gente tem que qualificar dizendo no banco de dados ed, que a nossa tabela de clientes está dentro do schema relacional, então vamos executar aqui.
Você pode ver aqui que ele trouxe o resultado, aqui, a lista dos clientes, então eu tenho o identificador, o nome do cliente, o estado, o sexo e o status dele, se ele é silver platinum ou gold.
Aqui eu posso dar um q aqui para ele voltar.

Então a gente fez a nossa primeira consulta básica aqui. Vamos supor agora que eu queira, eu não quero todos os atributos, eu não quero todas as colunas. Então, em vez de um asterisco aqui eu vou botar que eu quero clientes, Sexo, status from relacional clientes e eu vou colocar aqui um filtro ou uma cláusula where status igual a Silver.
Então, veja, eu estou dizendo aqui que eu quero que ele me traga a coluna, cliente, sexo e status apenas do esquema relacional Tabela clientes no banco de dados ed, mas somente aonde a coluna Status for igual a Silver.
Então vamos executar, e aqui está. Então você pode vir agora que você não vai encontrar aqui um gold ou Platinum, apenas silver, porque nós definimos isso como um filtro.

Ok, então ele está trazendo apenas o Silver, agora vamos mais ou menos repetir aqui a consulta. Então eu vou querer as mesmas colunas. Porém, o status ele deve ser silver ou Igual a Platinum.
Então, vejam agora ele deve me trazer, como resultado da consulta às colunas Cliente Sexo, status, do schema relacional da tabela clientes do schema relacional onde o status seja Silver ou Platinum. Ou seja, qualquer um dos dois ele deve me retornar aqui como resultado da consulta.
Então, vejo como o Platinum é mais raro e aparece apenas uma vez aqui. Mas a gente pode ver aqui que o Gold não aparece porque? Porque a gente limitou a Silver e Platinum.
Vamos aqui fazer isso de uma outra forma. Eu posso ter o mesmo resultado usando o in, então eu posso dizer que o status ele deve ser o in , o operador de conjunto Silver ou Platinum. Eu posso passar quantas informações eu quiser aqui. Então, aqui eu devo ter o mesmo efeito da consulta anterior. Eu tenho todos os clientes que status é silver ou Platinum.

Ok, então gente mudou aqui. A forma como a gente faz, fez a consulta.
Agora, se eu quiser somente os clientes Gold, por exemplo. Eu posso colocar o in gold ou eu posso fazer um not in e então eu vou ter todos os clientes que não são, que não estejam no conjunto Silver Platinum porque o status dele não estejam no conjunto Silver Platinum. Então eu vejo que ele retorna apenas os clientes Gold.
Ok, porque esses são os clientes que o status não está no conjunto Silver e Platinum.
Uma outra operação interessante aqui vamos dar uma limpada na tela. Aqui é o uso do like,  o like ele procura um texto que vai ter um match com a característica que eu passar. Então: 
from relacional clientes where cliente like %Alb%
Então cliente e uma coluna, onde o cliente ligue, eu vou colocar aqui o percentual, o percentual alb, então eu estou dizendo aqui que a coluna cliente ela é lá e que alb. Então esse operador aqui ele quer dizer que pode ter qualquer coisa antes e depois, ou seja, a coluna é cliente, ela tem que ter no meio dela ALB se tiver isso, ele deve retornar aqui.

Então vejam o Alb aqui ele retorna porque? Porque o asterisco está depois aqui, então pode ter qualquer coisa depois, Isso se aplica aqui aos três casos. Agora vamos dizer que o ALB está no meio, como tem o asterisco percentual aqui à direita. Ele também retorna este esta informação aqui, ok.
Uma coisa que você deve ter notado ou que eu vou usar que o comando limit que é para limitar o número de linhas, o resultado. Então vou botar o limite aqui só pra gente ver o que vai acontecer. Então, veja só, eu coloquei aqui no Select em vez de cliente, que é o nome de uma coluna, coloquei clientes.

Quando eu faço isso, ele me traz todas as colunas. Como uma tupla, todos os valores. Se eu quiser apenas a coluna cliente, eu vou tirar os clientes que o clientes é o nome da tabela, o cliente e o nome da relação.
Então eu tenho apenas a coluna cliente, sexo e status, ok. Quando eu coloco clientes, ele traz todas as colunas em uma mesma tupla. Ok, vamos continuar aqui. Eu vou mostrar agora um operador de comparação.Então vamos fazer que primeiro para a gente só conhecer melhor aqui a tabela:
 select * from relacional.vendas limit 1
Vamos limitar que limite um só pra gente ver como que é essa tabela?
Vamos supor que eu queira ver as vendas, cujo total apenas das vendas, cujo total seja maior, de 6000.

Então, como é que eu faria isso? Então eu vou tirar aqui o limit E eu vou colocar o where total maior que 6000. Então, veja, eu estou dizendo pra ele me trazer às vendas maior que 6000.
Isso não incluiria alguma venda que tenha o valor de 6000, porque eu estou pedindo maior 6001 ou 6.000,01 já valeria mais 6000, não. Se eu quisesse incluir os 6000, eu iria colocar maior igual.
Então vamos executar aqui. Então, e essas são todas as vendas.
Eu vou dando enter que ele vai me trazendo mais que o total que eu, que a coluna total é maior que 6000.
Então eu vejo que são bastantes vendas, vendas.
Eu vou digitar o q aqui para interromper.

Agora, vamos supor que eu queira o intervalo, então eu quero onde o total de vendas seja maior, que esteja entre 6000 e 8000, ou seja, maior que 6000 é menor que 8000.
Bom, eu posso colocar aqui total maior que 6000 e vende total menor do que 8000. Então vamos lá, vende total menor que 8000. Vamos executar. E aqui está você não vai encontrar nenhum valor que não esteja entre o intervalo de maior que 6000 é menor que 8000, agora existe uma outra forma, mais elegante, de eu fazer isso que eu colocar o Between, então o where total.
Então eu vou colocar aqui o Between, que em inglês entre 6000 and 8000.
Aliás, tem uma diferença que aqui no Between ele equivale não ao maior e menor, mas o maior igual e menor igual. Ou seja, ele inclui o 6000 e o 8000.

Então vamos executar. E aqui também. A gente tem o resultado de que os valores que estão entre 6000 e 8000. Então, no próximo tutorial a gente continua. A gente vai começar a falar de agregação, a sumarizar valores.