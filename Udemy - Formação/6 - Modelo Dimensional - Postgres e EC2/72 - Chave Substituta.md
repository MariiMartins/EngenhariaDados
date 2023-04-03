- 72. Chave Substituta
A chave substituta. É um conceito importantíssimo em modelagem dimensional e muitas pessoas erram esse conceito na modelagem de modelos dimensional.

Eles esquecem de criar a chave substituta e colocar ainda a chave primária.
Então, eu vou explicar com calma aqui, bem detalhado, o que é a chave substituta e por que ela é importante.

Então, a gente viu que no modelo relacional um cliente possui uma chave primária. Ela pode ser simples ou composta, mas ela sempre vai ter que ter uma chave primária que identifica de forma única aquele registro do banco de dados. Então a chave primária não pode ser repetida, ela tem que ser única.

E a gente viu também que um cliente ou qualquer outro dado que vai para uma dimensão do modelo dimensional pode ser carregado várias vezes.
Então, vamos repetir aqui o exemplo que a gente viu.

Um cliente é cadastrado no sistema da empresa de bicicletas e ele recebe aqui um código de status. Então, o status pode ser Silver, Gold ou Platinum.
A primeira vez que ele é carregado aqui é o modelo relacional e aqui o modelo dimensional. A primeira vez que ele é carregado, ele recebe lá um código do cliente e o status. O status vem obviamente desnormalizado.
Quando há uma nova carga, por exemplo, esse cliente, aquele mudou de status ou ele passou para o status gold. O que acontece de novo aqui é o relacional, aqui, o dimensional.
O que acontece? O registro dele não é atualizado, se inclui um novo registro para não se perder o histórico. Então, o que a gente tem aqui tem um outro registro do mesmo cliente, com o status novo.

Só que observem aqui o código do cliente identifica o cliente de forma única no modelo relacional, então, eu tenho que colocar o código do cliente aqui repetido. Então, é óbvio que o código do cliente aqui no modelo dimensional não pode ser uma chave certo, porque ele vai se repetir, só que eu tenho outro problema. Eu vou ter que relacionar esta dimensão com a minha fato.

Toda vez que ocorrer uma venda pra esse cliente, eu vou ter que passar o código do cliente para cá. Agora, como que eu vou saber a qual registro que se refere esse fato? Se era ao cliente Pedro Silva quando ele ainda era um status silver, ou já quando ela já quando ele era do status gold, eu perco essa referência.

Então fica óbvio que a chave do modelo relacional não pode ser utilizada como chave no modelo dimensional.

Então aí entra o conceito de chave substituta e a solução para esse problema.
Como que funciona? Você vai carregar o cliente do modelo relacional para o modelo dimensional, mantendo a chave original? 

Então, a chave original do modelo relacional ela se mantém. Por quê? Porque eu preciso saber a que cliente se refere a minha operação lá no dia a dia da empresa. Então eu não posso deixar essa informação de lado. Eu tenho que carregar. Ela tem que manter essa referência.

E eu carrego aqui essa esse código do cliente, essa chave do modelo relacional, quantas vezes for necessária.
Então está este atributo no meu modelo dimensional. Não vai ser a chave primária. É o que eu faço. Eu crio a Sangatte, que é a chave substituta. Então, aqui eu crio uma outra coluna que eu vou chamar de chave substituta para identificar de forma única aquela informação na dimensão.

Então, vejam a chave substituta. Ela não se repete no meu modelo dimensional. Agora o problema está resolvido.
Eu vou ter aqui a minha fato que quando o cliente comprar a primeira vez, vai se relacionar com o cliente Pedro Silva, que era do status silver.

Quando ele tiver outra transação que o status dele passou para Gold, eu vou relacionar esta outra chave aqui na mesma coluna.
Observe que enquanto o status do cliente aqui não mudar ou nenhuma da informação do cliente mudar aqui, eu não preciso carregar ele de novo.
Eu só vou carregar ele de novo na dimensão cliente quando houver mudanças na informação, nos dados, quando tiver novidades nos dados, quando tiver atualização dos dados, enquanto não tiver atualização, eu posso continuar mantendo a relação da dimensão cliente com o fato pelo.
O registro mais antigo.
Quando eu atualizo, eu faço esta referência com o registro mais atual.
E assim eu consigo manter o histórico do cliente.
Eu sei quando ele era Silva, eu sei quando ele era gold e eu não perco a referência com o sistema de operação, que é importantíssimo você manter referência com o sistema de transação.
Senão vai chegar um ponto que você não sabe mais à qual o cliente se refere.
Você pode ter lá, às vezes, vários dezenas de clientes com o mesmo nome, só pra citar o exemplo do cliente.
Então é importantíssimo o conceito da chave substituta num banco de dados dimensional. 
E não é apenas importante você modelar o seu modelo dimensional com a chave substituta. Você precisa incluir uma coluna para a chave primária do modelo transacional, a chave primária do modelo transacional.

Ela vai se repetir um processo natural, então por isso ela não é a chave primária. Então, esse é um conceito importantíssimo.
