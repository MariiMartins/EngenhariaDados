117. Criando Strings
Bom, estamos aqui de volta agora, então vai começar a nossa prática no Redis. É importante você ter certeza de que você está conectado no Redis, senão você vai executar os comandos no prompt do Linux e eles não vão funcionar. Então você pode observar aqui que o prompt aqui do cliente do Redis ele é diferente.

Bom, a primeira coisa que a gente vai verificar aqui é o conceito de banco de dados, então a gente viu nos nossos tutoriais que o Redis ele não tem o conceito de banco de dados como um banco de dados relacional ou como um banco de dados NoSQL, como algo que você cria um banco de dados dá o nome. Os bancos de dados no Redis funcionam como índices. Então você tem o banco de dados zero, que é o banco de dados padrão, o1, o2 e assim por diante.
E se você quer mudar de banco de dados, a gente usa o comando Select.

Outra coisa bem legal aqui no Shell, do Redis, no cliente do Redis e que ele apresenta aqui algumas dicas do que o comando espera. Então ele sabe que quando você digita Select, ele está esperando o índice do banco de dados.
É claro, você também pode usar o Tab aqui para ajudar você a completar os comandos.

O primeiro conceito que a gente vai estudar no Redis, o Redis é um banco de dados do tipo chave-valor. Então, a primeira coisa que a gente vai estudar é o tipo string, que nos traz a possibilidade de você armazenar uma chave associada a um valor. Então esse valor é um texto, então você vai criar essa chave e associado a essa chave, você vai ter um valor. E como a gente faz isso, então a gente associa com SET.

Eu posso recuperar um texto, uma string pela chave e em vez de SET, eu uso GET.

Existe a possibilidade também de incluir várias chaves simultaneamente.
Para isso, eu uso MGET (quando eu falo de Chaves, eu estou falando da chave associada ao valor)

Então a gente viu o SET que cria, o GET que recupera e o MSET que insere vários conjuntos, e a gente pode também testar a existência, para isso existe o EXISTS (ele não vai retornar o valor, só me retorna com 1, se o a chave existe ou ele retorna 0, se a chave não existe).

A gente pode verificar o tipo do dado digitando TYPE e a chave.

Outra coisa que a gente pode fazer é deletar, excluir pela chave DEL, eu posso passar mais de uma chave para excluir vários elementos de uma vez.

Uma outra coisa muito comum em B nesse tipo de banco de dados que, como eu falei, por exemplo, o utilizado para armazenar cache e o registro ou a informação ela ter um tempo de expiração, ou seja, um tempo que ela vai deixar de existir.
Quando a gente não define uma expiração, chama-se elemento persistente. Ou seja ele fica em cachê até ser excluído.

Uma outra opção aqui que tem é atualizar um valor de uma de uma string, utilizando o comando GETSET chave valor.

Bom, é uma outra funcionalidade interessante é que quando a gente fala de string e você poder recuperar valores de várias chaves para isso, a gente usa MGET.

E por fim, a gente pode ver o tamanho, o cumprimento do valor, não da chave, usando o comando STRLEN chave.
