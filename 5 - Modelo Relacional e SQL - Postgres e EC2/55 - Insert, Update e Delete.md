55. Insert, update, delete
Bom neste tutorial, então a gente vai ver um exemplo de como a gente insere dados, como a gente atualiza dados e como a gente exclui dados.

Então a gente vai incluir, atualizar, excluir o mesmo cliente.
Primeiramente, vamos fazer um select * from relacional.clientes limit 1
Para a gente ver que as colunas que nós temos ou têm o ideal cliente, o cliente que é o nome, o estado, sexo, status. Então, para mim fazer o Insert eu tenho que usar o comando Insert into, o schema e a tabela. Aí eu passo a lista das colunas que eu vou inserir, porque nem todas as colunas são obrigatórias nessa coluna.
Ela não está definida como not null. Se você não é obrigado a inserir o valor, então você passa a lista das colunas e a lista dos valores. Obviamente que tem que ter uma equivalência entre as colunas ou os registros, os atributos e os valores.

Então vamos lá.
Insert into relacional. clientes. (Aqui eu vou passar as colunas.) ID cliente, Estado, Sexo e status.

Então são essas colunas que eu vou inserir. A gente está vendo ali em cima.
ID cliente, estado, sexo, status.
E aqui vou passar o values. Então os valores que eu quero inserir.
Então eu vou passar aqui um código 251, depois o outro, o código A, o ID cliente. Depois é o nome do cliente que o cliente tem que ser da mesma ordem que estado. RS, sexo e m e status. Silver .
Lembrando que eu tenho sempre que colocar aqui um ponto e vírgula, porque daí o postgres entende que É o final do comando e ele vai executá lo.
Então ele me disse que foi inserido um registro. Vamos confirmar se o registro está no banco de dados.
Vamos fazer um select * relacional. clientes
O ID de cliente é igual a 251 ponto vírgula.
E aí está a gente ver o que se pode ver que o registro foi inserido com sucesso. Agora vamos atualizar este cliente.
Então, para mim atualizar o registro, eu vou usar o comando update.

Aí eu vou passar a tabela, meu esquema ponto, o nome da tabela.
O sete é seguido pelas colunas e valores que eu quero atualizar.
É uma condição o erro, senão eu vou atualizar o banco de dados inteiro.
Então vamos lá. Aqui a gente executando fica mais claro.
Então eu vou fazer o update no relacional Ponto Clientes.
Aí vou fazer um sete aí.
Então o Estado é igual a MS.
Eu posso autorizar qualquer campo lá que seja permitido virgula.

Posso passar vários campos aqui.
Campos e values status igual a Platinum foi o cliente foi promovido de estado, de status e aqui vou passar uma cláusula o where dizendo a onde ou qual registro vai ser atualizado, como falei, senão ele vai dar o update no banco de dados todo. Se for um banco de dados de produção, por exemplo, você pode perder o emprego, né? É uma brincadeira, uma piada que sempre se faz, que se faz um update sem o where.
Então você está fazendo um update no relacionar o ponto clientes citando o Estado pra MS e status para Platinum, aonde o ID do cliente é igual a 251 e ele me diz aqui que atualizou. Vamos recuperar o nosso select. E a gente pode ver que deu certo. O Estado passou para MS e o status passou para Platinum.

Agora, por fim, vamos excluir esse cliente. Então excluir ele é mais simples.
Eu coloco um delete.
O esquema tabela é uma condição para não escolher tudo, então delete from relacional. clientes where IDcliente = 251.
Então, assim eu garanto que eu vou escolher só o cliente cujo id é igual A25.
Eu poderia, por exemplo, excluir os clientes cujo status seja Silver. Ele exclui todos os que fossem Silver ok, e ele me disse que ele deletou. A gente pode confirmar fazendo o nosso Select você pode ver que ele retornou zero linhas no próximo tutorial. Então a gente vai ver um pouquinho de como funciona o controle de transações.