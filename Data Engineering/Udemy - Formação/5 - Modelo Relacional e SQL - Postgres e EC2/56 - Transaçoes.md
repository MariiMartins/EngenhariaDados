56. Transações
Então a gente já estudou que uma das características de um banco de dados relacional é o controle de transação.
Então, o controle de transações garante a integridade dos dados no banco de dados.
Então, a gente vai ver um exemplo aqui que a gente vai iniciar um controle de transação com begin.
A gente vai fazer uma inserção de um cliente. A gente vai fazer um select. A gente vai ver que esse cliente foi inserido e a gente vai fazer um rollback e depois a gente vai ver que esse cliente não está mais disponível.

Aí a gente vai executar o mesmo processo, uma outra transação só que em vez de dar o rollback, a gente vai dar um comitê. E o commit ele deve confirmar a transação. Então, quando a gente buscar este cliente, ele deve estar persistindo no banco de dados. Então vamos lá.

Primeiro eu vou começar aqui com o Begin então isso me diz que eu estou iniciando aqui o controle de transação.
Eu vou fazer um insert de um cliente, eu vou buscar que o registro. Onde nós inserimos o cliente para não precisar digitar tudo de novo. Então, veja, eu estou inserindo de novo o cliente 251, Fernando Amaral Não tem problema nenhum que nós excluímos. Ele não existe mais.

Então vamos fazer a inserção. Veja que eu estou no controle de transação ainda. Agora vamos buscar esse cliente.
Vamos recuperar o comando select asterisco forma relacional. Vejam que é o mesmo código do cliente que eu acabei de inserir. Veja então vou dar o enter aqui. Vejo que este cliente existiu. Eu inseri. Ele existe, mas eu ainda estou dentro do controle de transação. Agora, o que vou fazer?
Vou fazer um rollback no momento que eu faço rollback todas as transações, operações que eu tinha, que entre o Begin e o rollback, vão ser desfeitas.

Então imagine o caso aquele que você tirou dinheiro de uma conta e você não conseguiu atualizar da outra. Se isso tiver dentro de um controle de transação, você dá o rollback e tudo volta como estava antes do begin. Então eu vou dar que o rollback. E vamos buscar de novo este cliente de ID 251. Ele não existe mais porque eu dei o rollback. Eu disse fiz tudo o que estava entre o Begin e o rollback.

Agora vamos repetir tudo.
Eu vou fazer um Begin  novo, vou buscar aqui o comando de inserção ou vou inserir mais uma vez este cliente. Vou buscar esse cliente. Olha, está aqui.
Agora, em vez de eu fazer o o rollback, vou fazer um commit. E quando fizer um commit, o controle de transação encerra e as transações são confirmadas. Então vamos lá. Fiz o commit, vamos fazer um Select e aí está o registro. Ele está confirmado, ok, porque o controle de transação confirmou ele no meu banco de dados.