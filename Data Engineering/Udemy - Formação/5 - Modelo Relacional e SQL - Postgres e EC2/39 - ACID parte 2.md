39. ACID Parte II
Então, continuando com o conceito de ACID, a gente vai falar sobre consistência e isolation.
Então, as mudanças de estado do banco de dados devem seguir as regras de consistência. Então, imagine a seguinte situação você cadastra um produto, por exemplo, um veículo, um carro, você cadastra o cliente e o cliente compra o carro. Essa compra do carro gera um registro de compra, uma transação que é comentada e confirmada.
O que acontece? O usuário tenta deletar o cliente para o qual foi vendido o carro.
O banco de dados com consistência. O banco de dados relacional com consistência. Ele não permite que essa exclusão seja feita para manter a consistência das vendas. Ou se acontecesse a exclusão desse cliente, nós teríamos uma venda sem cliente e uma venda que não foi para cliente nenhum.

O outro conceito, então, isolação -isolation.
O resultado das transações executadas serão mantidos, mesmo que haja uma transação concorrente.
Então, imagine a seguinte situação voltando lá o caso das contas correntes duas transações, uma de atualização do saldo, outra de consulta. A consulta recebe um saldo de 400, mas a atualização não foi concluída e a consulta recebe o valor errado.
Então, já que no segundo caso a atualização aqui a gente está vendo, agora ela também falha, mas a consulta manteve o isolamento da transação e recebeu um valor de 500, pois a transação ainda não havia sido concluída.
Então, a questão aqui é que na primeira consulta, o cliente recebeu o saldo errado porque não se manteve o isolamento. Já na segunda, ela recebeu o saldo correto.

Nós vamos falar mais sobre isolamento em aulas posteriores e a última característica do esse de é durabilidade.
Se a transação for concluída com sucesso, seus efeitos permanecerão mesmo se ocorrerem falhas na rede de energia de hardware. 
Então, vamos imaginar aqui o caso de uma empresa aérea.
O sistema mostra a lista de assentos para o usuário, então o usuário A e o usuário B recebe do banco de dados uma lista de assentos disponíveis para que eles escolham o assento. O usuário A recebe a lista de assentos e escolhe o assento 4C . E por algum motivo essa operação não é permitida, mas ele recebeu o bilhete 4C, então ele teve a transação aqui confirmada ou o assento foi confirmado como  4C.
O usuário B também recebe a lista de assento e também escolhe o assento quatro se, pois como aqui não houve uma durabilidade dessa transação, o assento quatro sim estava disponível. Ele acabou sendo marcado duas vezes, causando um problema para a operação da empresa. Então, esse é o último conceito do esse de é o de durabilidade.
