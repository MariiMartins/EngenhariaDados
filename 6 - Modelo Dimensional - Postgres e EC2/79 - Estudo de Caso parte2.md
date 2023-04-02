79. Estudo de Caso Parte II
A parte interativa do script, que é aquela que nós vamos rodar passo a passo, etapa por etapa. Em vez de carregar e rodar o script todo, ela tem várias funções.

A primeira função que a gente está vendo aqui é fazer a carga das dimensões, então primeiro faz a carga dos clientes, então essa carga ela inicialmente carrega todos os clientes para a dimensão cliente do modelo do nosso sistema de transações.  Para o modelo dimensional, posteriormente, a carga vai ser feita.
O diferencial vão ser carregados na dimensão cliente apenas aqueles clientes que mudaram.

Mas a primeira vez que o script é rodado, todos os clientes são carregados.
Então a gente tem aqui um script. Ele faz um select no na tabela relacional clientes do banco de dados transacional, e ele faz um insert em dimensões dimensão cliente no esquema dimensional, seja no nosso banco dimensional.

E aqui ele verifica se existem alterações. Ele só vai fazer inserção se existir algum tipo de alteração, se existem diferenças entre o que já está carregado no modelo dimensional e o sistema transacional. Então a gente tem a primeira carga de clientes.

Depois a gente vai rodar a primeira carga de produtos, depois a primeira carga de vendedores e finalmente nós vamos carregar nossas vendas.
Nós vamos carregar a fato, essa carga, de fato, já faz a relação com todas as dimensões, então nós já carregamos.

Nós já fizemos a primeira carga das dimensões. Quando a gente carrega a fato, as chaves estrangeiras já vão estar ligadas com as dimensões.
Uma questão importante aqui a gente está vendo o script de forma parcial.
A gente pode ver aqui os pontos que nós estamos simulando, o ambiente de transação e no ambiente em que você tem um sistema de transação e um sistema analítico gerencial, as cargas são incrementais.

O que a gente vai fazer aqui é essa cláusula ou poeira que ela simula, que só existem lá no banco de dados transacional apenas no primeiro mês. Então ele pega o primeiro mês e carrega para o banco de dados analítico para o banco de dados dimensional. Depois nós carregamos o segundo mês, depois do terceiro mês, depois o modos os outros meses restantes.Isso para simular como se fosse um ambiente em que houvessem cargas incrementais no nosso armazém, no nosso armazém de dados.
Bom, e aí, o que acontece? Nós vamos fazer um update. Nós vamos voltar lá pro relacional que nós criamos na outra seção e nós vamos atualizar um cliente. Nós vamos alterar o seu status, que era Silver para gold, o que a gente espera que aconteça com isso? Que lá na nossa dimensão, cliente, estes clientes, que são os clientes de 1 a 5 que foram atualizados, eles terão que ser novamente carregados com códigos novos.Então, se eu tinha aqui o cliente A, B e C e esses clientes A, B e C foram novamente carregados, eles, se eles foram alterados, eles têm que ser novamente carregados. Eu vou ter de novo o cliente A e C.

A chave relacional vai ser a mesma, mas a chave substituta vai ser diferente.
Ela vai continuar incrementando. Então, quando a gente fazer a nossa nova carga de clientes. É isso que a gente espera que aconteça.

Então o script aqui é semelhante. A gente faz um select, verifica se existe atualizações dentro do banco de dados dimensional e aí a gente vai consultar a nossa dimensão. O cliente vai rodar o Select normal lá e consultar a nossa dimensão cliente, limitando aqui os clientes que nós estamos estudando. E vejam que a gente pode observar o que é exatamente o que aconteceu.

Vamos separar aqui a primeira carga de clientes do mês. Do que teoricamente ocorreu no mês um. Nós temos o que? Nós temos a chave do cliente e o ID do cliente.
Aqui, a chave do cliente é Assur Gate Key. E a PrimaryKey do banco de dados relacional. Então vejo quando eles foram carregados de novo a chave do Banco Relacional, obviamente, ela se repetiu. Já a chave substituta, ela continuou incrementando por que pula do 3 até o 251?
Porque todos os outros clientes aqui também foram carregados.
Aqui se Select três, mostrando apenas os clientes de 1 a 5, que foram aqueles que o status foi atualizado.

Vejam que está esta coluna aqui e o motivo de eu ter carregado os clientes de novo, eu ter inserido novos registros para o cliente na dimensão. Então, dessa forma, depois a gente vai rodar outras etapas que está sublinhado aqui e que a gente vai ver que a fato do primeiro mês vai se relacionar com essa proporção, com esses clientes que estão aqui.

Já a fato do segundo mês. Vai se relacionar com estes clientes aqui, vejam aqui que é esta dimensão cliente. Ela tem data de início de validade e data de validade. No momento em que os clientes foram carregados novamente, eles perderam a validade. A validade deles acabou. Então essa é uma referência do período em que aqueles dados naquela dimensão do cliente ficaram válidos.

Então, essa é são algumas das etapas que nós vamos ver no nosso caso prático, algumas convenções que nós vamos utilizar nessas aulas práticas.
Então, alguns blocos de código são grandes e repetitivos.
A gente viu que tem alguns blocos, que são uns scripts SQL bem grandes.
E se eu ficasse digitando aqui, ficaria bastante massivo, além de repetitivo.
Então, em alguns casos, eu irei colar o código e explicar e rodar, em vez de digitar todo o código.
O que você pode fazer, o que eu sugiro que você faça, é você pode pausar o vídeo e você digitar o código todo antes que eu o execute, ou você pode consultar do ambiente ou até mesmo colar que nem eu vou fazer aí uma opção sua. Você pode tranquilamente, com calma, digitar o script para pegar familiaridade com a linguagem SQL, mas aí fica a seu critério. A forma que você fizer vai estar bom, desde que você conclua as atividades até o final.