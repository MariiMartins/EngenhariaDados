38. ACID Parte I
Com o banco de dados relacional ele deve ter as características que são conhecidas aqui pelo acrônimo Exceed, que é de tonicidade, consistência e isolamento e durabilidade.
Então a gente vai ver cada uma dessas características, dessas quatro características que formam esse acrônimo, então a tonicidade, então o banco de dados relacional ele deve ter a tonicidade.
O que quer dizer isso é o conceito de tudo ou nada. Ou as transações acontecem de forma integral ou não acontece.

Então, imagine o seguinte caso imagine uma conta bancária transferência de valores entre contas bancárias?
Você tem a conta A e A conta B e você quer fazer uma transferência de um valor aqui, no caso, 100R$ entre as contas.
Então, o que o sistema faz?
Ele faz uma transação de débito de uma conta, atualiza o saldo. Meu saldo era 500, debitou 100, passou para 400.
É o que ele faz lá na outra conta. Ele faz um crédito de 100. Então, o saldo era 200. Ele acreditou 100. O saldo passa a ser 300.
Então, aqui tudo certo.

Com as transações, não houve nenhuma violação de integridade. Está tudo correto.
Agora, vamos supor o seguinte caso a mesma transação o sistema, ele fez o débito de 100 R$, ele atualizou o saldo na conta do cliente. Quando ele foi fazer o crédito no cliente B, houve um problema qualquer de infraestrutura.
Esse problema pode ser problema de rede de banco de dados, falha de hardware, de comunicação. Enfim, houve um problema qualquer, de forma que ele não conseguiu atualizar o crédito na conta B O que aconteceu?
Bom, o valor de 100 R$. Ele foi debitado da conta, mas não foi creditado na conta dele. O que aconteceu com esses 100 R$? Eles simplesmente desapareceram.

Qual é a forma correta?
No momento que é feito o débito no valor da conta da conta, o que acontece?
Inicia um processo de transação e essa transação aqui ela fica pendente, certo? Então ele faz lá uma anotação que foi debitado 100 R$, mas isso fica pendente caso ocorra uma falha no restante da transação, ou seja, no crédito no valor da conta. Na conta B, ocorre um processo chamado como rollback.
Ou seja, ele desfaz essa transação inicial. Tudo volta como era. 
Os 100 R$ não desaparecem. Não há o crédito do valor na conta B, mas também não há o débito do valor na conta. As transações não são concluídas, não são computadas? Ok, então é um processo chamado de rollback.