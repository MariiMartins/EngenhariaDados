40. Níveis de Isolamento
A gente vai falar agora sobre níveis de isolamento ou isolation levels, que é outro conceito importantíssimo quando a gente está tratando de bancos de dados relacionais.
Basicamente, os níveis de isolamento eles dizem o que vai acontecer quando ocorrer a leitura de um registro enquanto ele estiver sendo atualizado, ou seja, ele vai ser bloqueado, vai haver um lock e uma espera ou vai ocorrer uma leitura suja você vai ler um dado que não é, de fato, o dado real.
Então, aqui alguns conceitos com relação a isolation levels Dirty Read é quando se permite a leitura de um registro sem commit. O que quer dizer sem commit, quer dizer que o registro ainda não foi persistido.

Imagine o caso da transação do banco.
A transação um atualiza o saldo de 1500 para 2.000 R$.
A transação dois ela lê o saldo de 2.000 R$ a transação, aquela primeira transação ela dá o rollback Provavelmente ela não conseguiu confirmar auto atualização do saldo na outra conta.
Então, o saldo volta aqui para 1500, porque houve o que eu rollback. A transação foi desfeita.
O que aconteceu? A transação Dois Ela lê um saldo que não é real, que não existe.
Ok, então ele provavelmente ele pode ter lido lá que ele tinha um saldo de 2.000 R$, quando na verdade o saldo dele era de 1500.Porque ele fez uma leitura suja a consulta SQL. Lá ela leu uma informação sem commit.
Não foi permitida. Essa transação não foi persistido, ele leu um valor errado Então é só conceito Dirty Read de leitura suja, não repetível.

Non Repeatable read A transação lê mesmos os mesmos dados duas vezes e obtém valores diferentes. Então vamos ver que um exemplo a transação dois lê o saldo de 1.500 R$.
A transação atualiza o saldo de 1500 para 2000 e executa um commit Ela confirma essa atualização.
A transação lê novamente o saldo e O valor está de 2.000 R$.
Ok, então a transação pelos mesmos dados duas vezes e obtém valores diferentes, então é o Non Repeatable read.

E o Phanton Read na leitura fantasma.
A mesma consulta retorna registros diferentes, então imagine que a transação faz uma consulta. A transação dois insere novos registros que satisfazem a transação a consulta. A transação faz a mesma consulta, mas obtém registros diferentes. Então, por exemplo, imagine la que a transação lê a quantidade de vendas. A transação dois Ela insere novas vendas. A transação um Ela faz a mesma consulta e o número de vendas mudou, Não é mais o mesmo.
Para tratar desses problemas de leitura sujas de leitura fantasma, existe os níveis de isolamento.

Então, esse aqui são os principais quatro níveis de isolamento que são implementados pelos sistemas gerenciadores de banco de dados relacionais.
Então a gente tem: 
●	Read Uncommited
●	Read Commited
●	Repeateble read
●	Serializable.
Vamos ver o que é cada um deles.
Então Read Uncommited  você consegue ler registros sendo alterados mesmo sem commit Rollback é aquele caso.
Lá você vai ler um saldo que pode ser real. Ok, ele não gera bloqueios. Você à sua consulta não vem, não tem que está esperando a outra transação receber um commit ou um rollback, ela ser confirmada ou desfeita. Só que ela causa que a leitura suja com você. Pode ler um saldo, por exemplo, de 2.000 R$, que não é real. A transação teve um rollback e na verdade o saldo é de 2.500 R$.

Depois tem o read commited voce consegue ler apenas registros permanentes, ou seja, que sofreram commit aqui nesse caso não ocorre a leitura suja. Você só vai ler o saldo se ele for confirmado, então não vai acontecer de você ler 2.000 R$ de saldo, quando na verdade o saldo é 1500. Só que tem aqui um efeito colateral ela gera bloqueios. Esse nível de isolamento, ela gera bloqueios. O que é um bloqueio é você executar uma consulta, por exemplo, solicitando o saldo da sua conta. Mas como existe uma transação em andamento, o sistema gerenciador de banco de dados não vai retornar. Ele vai deixar você bloqueado. Ele vai deixar você esperando até ocorrer um commit ou rollback para você não ter uma leitura suja.

E depois o Repeateble read ele é mais restritivo. Ele bloqueia registros e referências até para o update e ele evita o fenômeno da leitura não repetida.

E, por último, aqui, o nível de isolamento mais alto que eu, Serializable, ele gera Locke também em Insert, não só em updates, mas também em Inserts

Então, esses são os principais níveis de bloqueios, os principais problemas de controle de transação que nós encontramos em bancos de dados relacionais. Esse quadro comparativo aqui é bem interessante porque ele nos mostra os níveis, os quatro níveis de isolamento. Ele nos diz o que pode acontecer?
Quais são os efeitos colaterais com relação a leitura sujas, leituras não repetidas e a leituras fantasmas?
Então, aqui, se você ler dados que ainda não foram confirmados, você pode ter leitura sujas.
Você pode ter leituras não repetidas e você pode ter leituras fantasmas.
Então esse quadro mostra, para cada nível de isolamento, qual tipo de efeito colateral pode ocorrer durante as transações?
As consultas, as transações em bancos de dados relacionais.