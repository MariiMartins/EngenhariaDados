81. Cargas de dados no DW
A gente vai começar então a carregar dados no nosso banco de dados dimensional e essa carga de dados é feita a partir do banco de dados relacional.

Como os scripts são bastante grandes, eu vou usar aqui a opção de copiar e colar.

Então vou colar que o primeiro script e eu vou explicar aqui o que ele faz:

Aqui eu estou dizendo que o With s as (Eu estou criando, aliás, para essa tabela). Ou seja, o resultado dessa consulta que de agora em diante ele vai e pode ser utilizado como S ou então como s é o resultado dessa consulta.
Aqui é vejam que eu faço um update no dimensional cliente a consulta no relacional cliente. Então o resultado dessa consulta vai ser essa tabela chamada S. Com essa tabela S ou eu faço um update no dimensional cliente que eu chamo de T e data fim de validade como a data atual de S, então da tabela S e eu faço aqui um T, que dimensão cliente igual a o s que é o select do cliente. Onde o valor final é nula?
Ok, então ele vai preencher os clientes onde a data final de validade é nula e aqui ele faz um insertion. A partir desta tabela s aqui então esse script é que faz a primeira carga dos clientes do banco de dados. Ela só dá uma mostra tabela dimensional. Vamos executar aqui e você pode ver aqui que ele fez a inserção de 251linhas. Ok, então foi a primeira carga. Então, agora a gente pode já fazer uma consulta aqui.

Select * from dimensional, dimensão, cliente.
Então, veja, nós temos a nossa dimensão cliente carregada. Vejam que é uma dimensão que a gente carregou a dimensão cliente. A gente precisa carregar as outras dimensões e depois fazer a nossa carga. A gente precisa criar a nossa tabela, fato que vai se relacionar com as dimensões que a gente criou.
Bom, eu vou então rodar o script que vai fazer a carga dos produtos, a rimeira carga dos produtos, o script, que é bem semelhante. Eu vou colar o script aqui é o mesmo princípio. A princípio, o S é um resultado de um select e ali ele vai fazer o insert da primeira carga. Então inserimos dez produtos. Ok, podemos aqui verificar a dimensão.
No esquema dimensional dimensão, produto n dimensional, dimensão, produto. Então, a gente pode ver que temos os dez produtos carregados no nosso banco de dados no nosso banco dimensional.

Vamos ficar fazendo agora a carga dos vendedores.
Então, de relacional vendedores Ele vai carregar do relacional, vendedores por dimensional para a dimensão, vendedores, ou então temos a inserção.
Podemos fazer a verificação novamente, então estamos construindo aqui o nosso DataWarehouse.

Dimensão dimensional vendedor. Então aí está os vendedores. Inclusive, o último que nós inserimos lá está aqui.
Bom agora eu posso fazer a carga da minha tabela Fato.
Então a minha tabela, fato a carga dela, ela vai relacionar as vendas com as dimensões que nós criamos.
E nessa primeira carga de forma proposital. Nós vamos carregar apenas o primeiro mês, então vejo aqui o Edit Parte Monte é igual A01. Então, apenas no primeiro mês talvez a gente vai fazer uma inserção agora na fatura da chave do vendedor chaves, cliente, produto chave, tempo, quantidade, valor unitário, valor total e desconto. E a gente vai fazer um select em todas as nossas dimensões para fazer essa inserção, mas limitando ao mesmo. 

Então esta aqui é a nossa primeira carga, nós inserimos os registros.
Agora a gente pode ver aqui o que a gente vai ter já dados na nossa dimensão.
Fato, vendas no nosso dimensional alto vendas. Então vejo que ela já está populado.
São números porque são a maioria dos valores ou são chaves estrangeiras apontando para os fatos ou são valores. São as nossas medidas como quantidade, valor unitário, valor total e desconto. Bom, agora vamos encerrar aqui.

Agora, o que é que a gente vai fazer? A gente vai atualizar o status, a gente vai verificar o status dos clientes de código 1 até 5 lá no banco de dados relacional e depois a gente vai alterar o status desses clientes para Gold.

Ok, então os clientes de 1 a 5, a gente vai alterar o status dele deles para Gold. Aí a gente vai rodar um script para atualizar a nossa dimensão cliente. E a gente vai consultar a dimensão cliente.
Vê se o histórico do status do cliente foi mantido porque esse é o objetivo de um banco de dados dimensional.

Eu vou fazer o Select no status do relacional Clientes o ID do cliente ele vai estar between 1 e 5, então vamos ver qual é o status desse cliente. Então são todos clientes com o status silver, clientes de 1 a 5.

Agora vamos supor que lá no banco de dados transacional esses clientes compraram mais, fizeram mais compras, o status dele deles passou para Gold.
Então vamos fazer aqui um update relacional.clientes set status = Gold where IDcliente between 1 and 5
Ok, então vamos fazer a atualização desses clientes, vamos selecionar aqui de novo. E a gente viu que esses clientes estão agora com o status gold. Bom, agora então a gente vai e vai rodar novamente o script de carga da dimensão cliente.
E esse script ele tem que detectar automaticamente. Ele tem que ser esperto para detectar que os clientes de 1 a 5 tiveram o status alterado e ele deve inserir novos registros na dimensão do cliente com esse novo status, porque o conceito desse banco no banco de dados dimensional ele não vai atualizar os dados. Ele vai inserir novas informações a fim de manter o histórico.
Então eu vou.
Simplesmente aqui colar, o script de atualização. Vejo aqui da dimensão cliente eu vou executar o script. Ele está dizendo que ele fez inserção de umas cinco, de cinco registros, então isso já é um bom sinal.
Agora, então vamos consultar a dimensão do cliente.
Select * dimensional dimensão cliente where idcliente Between 1 and 5.
 Vamos executar, e vejo aqui que interessante esta aqui é a chave substituta à chave cliente, ou seja, esta é a chave que o cliente tem no banco de dados dimensional.
Esta aqui é a chave do cliente no banco de dados ou operacional ou relacional. Então a gente pode ver aqui, por exemplo, ao que o cliente Adelina Buenaventura, ele foi inserido a primeira vez com o status silver. Porém, quando houve uma nova carga dos dados, o script de carga, ele verificou que o Adelina Ventura teve uma mudança e um registro era silver, passou para Gold, então ele inseriu um novo registro.

Vejo que a chave do banco de dados operacional é a mesma, mas a chave substituta não.
As transações na fato vendas que já eram desses clientes, elas têm que estar relacionadas com essas chaves que as novas vendas eventualmente. O que acontecer para esses clientes a partir de agora têm que estar relacionadas com essas chaves substitutas aqui.

Então você consegue, por exemplo, saber em um determinado período exatamente quantos clientes você tinha Silver e quanto você tinha como status de Gold. Se eu simplesmente atualizasse aqui, eu ia perder esta informação histórica, então esse é o principal conceito de um banco de dados dimensional.
Agora vamos verificar se na carga da fatura referente ao primeiro mês que a gente carregou. Se elas estão apontando para essas chaves de cliente aqui de 1 a 5, que a gente tem que verificar, isso sim. 
Então veja, eu estou verificando na dimensão da fato vendas fazendo higiene com a dimensão cliente. Os clientes de um do I-D de 1 a 5 e você pode ver que todas as vendas na fatto a chave cliente aqui. Então eu vejo que a chave cliente vem da tabela cliente pra gente ver o nome.

Então a gente pode ver que de fato estão apontando para a primeira versão dos clientes quando eles não eram gold, quando ainda eram do tipo Silver, ok?
Bom, agora vamos carregar mais um mês na foto vendas. A gente carregou só janeiro. A gente agora vai carregar o mês de fevereiro. Ok, então o script é o mesmo, eu vou colar aqui. A única alteração que vai ter no script é aqui o final.
Vou mostrar o que eu estou carregando da operação do banco de dados relacional apenas o mês dois, vamos carregar então, essas vendas.
Agora, supondo que essas vendas tenham ocorrido agora, essas foram carregadas agora. Então existe uma nova versão dos clientes de 1 a 5.
O que será que vai acontecer na tabela Fato? Será que vai apontar para a versão nova ou antiga da fato Clientes? Então a gente vai rodar um script aqui que vai fazer essa consulta. Então a gente vai consultar na Fatto Vendas um winner join. Com a dimensão cliente, este script já conhece e já conhece onde os clientes estão entre os cinco. Então vamos executar. E vejam que interessante: Todas as vendas que estavam lá a gente já tinha visto para os clientes de 1 a 5 continua apontando esta que a chave substituta continua apontando para a primeira versão. Porém, com a venda como a venda em fevereiro, vejo que tem apenas o cliente de cinco e como existe uma nova versão deste cliente ou ele já está apontando? A gente tem que ver que a chave substituta dois, cinco, seis para essa nova versão.

O ID do cliente aqui é o mesmo ID do cliente que vem da doca nacional.
Então o cliente cinco aparece aqui na sua primeira versão, quando o status dele era Silver e aqui na sua segunda versão, quando o status dele é Gold.
Seguindo aqui, vamos então carregar o mês de março. Você pode ver aqui que ele está filtrando o mês de março. Vamos consultar aqui os clientes de 1 a 5 novamente no mês de março. Vamos executar e tabela vazia. Quer dizer, não teve compras desses clientes no mês de março.

Agora vamos novamente alterar um dos clientes. Vamos alterar que eu vou rodar um script para a gente alterar o cliente 3.
Então o cliente 3 era Silver, depois passou para Gold.
Agora a gente passou e vai passar ele lá no Relacional, ele para Platinum. Obviamente que a gente tem que rodar novamente o script que vai fazer a carga desses, dessas atualizações, desses clientes.
Vamos rodar aqui para fazer a atualização da dimensão cliente.
O script já é conhecido e agora a gente vai consultar novamente o histórico dos clientes de 1 a 5, vai consultar a dimensão.

E vejam que agora existe uma nova versão do Adélio Lisboa. Então o Adélio Lisboa aparece aqui com a chave substituta 3, depois ele aparece aqui com a chave substituta 254 e agora uma terceira versão dele 257. Então vejo que todo o histórico dele está aqui. Ele era Silver, ele passou para Gold e agora ele passou para Platinum.

Vamos carregar o restante dos meses, todo o resto das vendas. Então é o mesmo script, porém, a única alteração aqui que vai pegar o maior que 3 aqui.
Para não carregar de novo os dados que nós já tínhamos carregado, você pode ver aqui inserir os 694 registros.

E por fim, então a gente vai verificar as compras de todos os clientes que a gente está acompanhando, que são os clientes de 1 a 5.
E aqui vejam o Adélio Lisboa, a gente tem versão aqui de compra dele, do Adélio Lisboa, com a chave substituta, Aqui acharam o substituto A3.
O Adélio Lisboa com a chave substituta 257, quando ele já tinha aqui o novo, o novo status. Então a gente tem três gerações e diria sim, de carga de clientes aqui, de versões do cliente.
Então, essa aula serviu para a gente entender como que funciona um banco de dados dimensional e como é importante manter o histórico. É claro que no mundo real existem ferramentas que vão fazer essa carga automaticamente.
Não vai ter ninguém lá rodando script. Isso acontece de forma automática, uma vez ao dia, normalmente em algum horário de dia de menor tráfico.
Mas aí depende de cada, de cada situação, de cada necessidade aqui.
Mas as ferramentas fazem a atualização desse banco de dados dimensional de forma automática.
A gente mostrou que passo a passo para a gente entender os conceitos e o que você precisa gravar disso que você precisa ter, o que precisa ficar.
Importante disso é o conceito, o conceito em que você abre mão.
De propriedades que utilizam o banco de dados relacional tinha que era não redundância e integridade. Você abre mão disso em troca de informação analítica.
Então, aqui você mantém a informação com mais redundância, com maior volume. Mas você tem informação analítica, de qualidade e com dados históricos, você não tem integridade, você tem redundância.
Mas você ter informação histórica, então, é um propósito diferente. Um DataWarehouse, ele tem uma funcionalidade, um propósito, um objetivo diferente.