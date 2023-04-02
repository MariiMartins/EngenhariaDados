47. SQL Parte II
Então agora você vai começar vendo comandos de manipulação de dados Insert para incluir, o PD para atualizar e delete, delete para excluir então qualquer sintaxe básica de um comando insert.
Então você vai colocar aqui insert into, O nome do schema (o nome da tabela).
Você vai colocar a lista de colunas que você vai inserir dados de registro, de atributos, de colunas onde você vai inserir dados. Você não precisa colocar todas as colunas se você não vai colocar algum valor em alguma coluna. Por exemplo, se é um cliente cujo endereço ou cujo status vai ser incluído depois, você pode iniciar inserir a primeira vez só, por exemplo, com o identificador ou com o nome dele. Então, você não precisa colocar todos, desde que no banco de dados não tenha uma restrição de que determinada coluna seja de preenchimento obrigatório.
Aí o comando Insert vai falhar se não existir o valor.
E depois você tem que inserir os valores usando a cláusula Values que têm que ser equivalentes na mesma ordem das colunas que você colocou no INTO.
Você tem que ter uma equivalência entre o nome das colunas e os valores.
Quando você tem colunas auto incremento, onde a chave é definida pelo sistema gerenciador de banco de dados, você não inclui esta chave, o próprio banco de dados vai incluir o registro.

E aqui o comando de atualização comando básico de atualização, então você vai usar o update.
Você vai começar com UPDATE schema no nome da tabela e depois você vai usar o SET para definir todas as colunas que vão ser atualizadas, então você tem que colocar coluna, valor, coluna, valor, coluna, valor separado, separados por virgula e depois é importantíssimo e cláusula WHERE o que acontece você não colocar uma cláusula WHERE. O update vai afetar todos os seus clientes.
Então, por exemplo, se você não tivesse aqui essa cláusula WHERE e você desse um update relacional clientes, todos os clientes passariam a constar com o Estado MS e com o status Platinum ia ficar a maior bagunça no banco de dados, então sempre tem que ter uma cláusula WHERE.

E por fim o delete.
O delete é mais simples eu vou usar delete FROM schema, tabela e também aqui a condição. Da mesma forma, aquilo que o update tem que criar uma condição, senão ele vai escolher todos os registros do banco de dados.

E agora aqui há um comando de criação de estrutura data definition language.
Então a gente tem de ter e aos comandos CREATE TABLE, INDEX, VIEW, ALTER TABLE, INDEX e VIEW.

E ele está dizendo aqui que o próximo valor dele é um alto incremento.
Ele vai receber o Relacional ID, cliente Reckless e a sintaxe das consultas dos comandos SQL são parecidas, bastante parecidas entre todos os gerenciadores de banco de dados, mas sempre existem algumas características especiais.
Essa aqui é uma característica especial, diferente do post, aqui então a gente tem cliente que é do tipo caractere de tamanho 50, estado caractere de tamanho dois ou sexo caractere de tamanho 1. Um status caractere do tamanho 50 é aqui uma restrição, uma restrição do banco de dados, que aqui, no caso, é a restrição da chave primária, que não pode ser repetida, que a gente tem ali ou é de cliente. É uma das características do banco de um banco de dados relacional.

E aqui por fim, para encerrar essa aula, o Data Transaction Language usa os comandos que controlam as transações do banco de dados.
Então a tem o Begin Transaction, Commit e o rollback no postgrees é isso que a gente vai ver.
O exemplo prático é simplesmente Begin, commit e rollback.
Então eu vejo aqui um exemplo eu inicio a transação, eu insiro um registro cliente, veja aqui que eu estou criando, estou inserindo o cliente se chama Fernando Amaral, aqui eu vou fazer um select. Eu vou consultar esse cliente que acabou de ser inserido.
Eu vou conseguir enxergar ele porque? Porque eu tenho uma transação aberta,  a transação está pendente. O commit aqui está comentado, então ele não é executado. Então o que acontece? Eu comecei a transação inserir o cliente e fiz uma seleção. Fiz um select no cliente e eu consigo ver ele no banco de dados.
O que acontece depois? Eu dou um rollback.
O cliente desistiu da compra? Eu dou um rollback.
Se eu fizer um select agora, esta consulta novamente de retornar o registro, porque como não confirmei a transação, vejo que a confirmação aqui está comentada.
Dei um rollback, a transação não foi permitida. Todos os comandos que faziam parte daquela transação desde lá do begin foram desfeitos. Ok, a gente vai ver esse exemplo na prática, lá na nossa aula prática no Postgres.