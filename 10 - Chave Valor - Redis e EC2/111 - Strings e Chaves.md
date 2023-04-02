111. Strings e Chaves
A partir de agora nós vamos falar das estruturas de dados do Redis.
Aqui a gente está vendo as principais estruturas que o Redis suporta e a gente vai tratar de uma por uma.
Então a gente tem as strings (que são estruturas mais simples), e Hashes, Lists e Sets.
Então, nesta aula nós vamos falar especificamente sobre Strings.

Então, a string é um tipo de dado mais comum. A sintaxe para ler e para gravar uma string é bem simples. Então a gente usa o Set e o Get ; o Set para gravar e o Get para ler.
E aqui uma questão importante. Vejam que a gente vem falando dos bancos de dados NoSQL, que uma das modalidades são os bancos de dados chave-Valor. E o Redis é um banco de dados chave-Valor.
Então, quando você vai gravar uma informação, o que você tem que informar chave- valor. Então, aqui a chave ela pode ser qualquer valor pode ser um valor inteiro, um texto, mas é uma chave, não pode se repetir e o valor pode ser qualquer texto. Pode ser um valor real, pode ser um nome, pode ser uma fração, pode ser qualquer coisa, porém aqui você tem preenchimento livre.
A chave não. A chave não pode se repetir, então a chave ela tende a ser menor, até pela questão de busca de indexação. O valor tem de ser qualquer valor que você vai precisar lá para o banco de dados na operação do sistema.
Então, para gravar um valor, uma string, você usa o comando set, o valor da chave e o valor que você quer gravar.
Então, vejam que é bem simples a sintaxe toda do Redis. Ela é bem simples, e é bem fácil. E para você recuperar a informação, você quer ler o valor que você gravou aqui. Você usa get com a chave, então aqui a gente tem um exemplo e depois a gente vai ver esses exemplos e todos os outros codificando.

Então aqui um exemplo:
SET 1 “Engenharia de Dados”
Eu estou dizendo aqui set espaço um que aqui eu tenho a minha chave e aqui eu tenho valor, então está aqui o modelo clássico do banco de dados Chave-Valor. E para mim, recuperar esse registro eu uso get chave. Então eu passo só o get apenas com a chave e ele me recupera o valor. Ok, então é esse o tipo de dado mais simples do que o Redis suporta. E aqui, as operações mais básicas sete e Get.

Porém, eu posso às vezes querer incluir numa mesma vez numa única operação, vários conjuntos de chave valor. E aí, em vez de usar SET, eu vou usar o MSET. Então vejo que aqui a diferença é que eu tenho um m na frente.
É o que eu estou colocando aqui Chave-Valor, chave, valor, chave, valor. E assim eu poderia colocar aqui muitos pares de chave-valor e eu vou inserir todos eles simultaneamente. Quando você faz a inserção aqui, ele retorna no Shell ali (no console) OK, dizendo que a operação foi executada com sucesso.

Outra operação aqui eu quero verificar se uma chave existe para isso eu uso o comando exists. Ele verifica se uma determinada chave que eu estou passando aqui. Então aqui tem a chave, ela existe e o que ele vai fazer?
Ele vai me retornar 1 , Quer dizer que é verdadeiro quer dizer que essa chave existe. Então é o caso clássico. Você quer verificar se uma determinada chave já existe no banco de dados. Você primeiro faz a checagem. Se não, você faz a inclusão daquela chave.

E aqui eu vejo esse outro exemplo.
Eu faço a busca de uma chave que eu sei que não existe uma chave 455. E aqui vejam ele retorna 0, quer dizer, falso. Quer dizer que esta chave não existe.

Se eu quiser excluir um registro bom, aí eu vou usar o Del e o valor da chave simples. Del chave ele faz a exclusão. O 1 aqui está dizendo de novo, verdadeiro, que a operação foi executada com sucesso.
Depois eu faço uma verificação aqui com o comando Exists, que a gente acabou de ver exists 1.
Ele retorna a zero, quer dizer, falso. Quer dizer que esta chave não existe mais porque eu acabei de excluí- la.

Como quiser verificar o tipo do valor da chave, eu posso digitar type.
O comando type e a chave e aqui está me dizendo que a chave é string. Ele poderia retornar, por exemplo, inteiro ou bol. Aí vai depender do valor que você gravou dentro do valor.

A gente falou que um valor que você armazena no Redis ele pode expirar.
E como você faz isso? O comando aqui ele é parecido, mas veja aqui que a gente tem alguns parâmetros a mais: o SET que a gente já conhece, a chave que você já conhece, o valor que também a gente já conhece. E aqui eu tenho três outros parâmetros, então vejam que:
•	EX quer dizer que a expiração vai ser em segundos
•	PX Quer dizer que a expiração vai ser em milissegundos.

Então, por exemplo, aqui, se eu coloquei EX 60, quer dizer que ela vai expirar em 60 segundos ou um minuto.
Se eu colocar PX e manter esse aviso 60, quer dizer que ela vai expirar em 60 milissegundos.
E o terceiro parâmetro aqui é o NX, é o XX um dos dois você deve usar
•	NX só funciona se a chave não existe
•	XX Só funciona se a chave já existe
Uma questão que eu não passei ainda é que você pode quando você tiver uma string que não tem espaços, você pode passá la sem aspas.

Eu posso também definir a expiração, o tempo de expiração posteriormente, o que quer dizer posteriormente? Bom, eu gravei o registro e depois eu defino a em quanto tempo ele vai expirar.
Então vejo aqui o SET 1 Engenharia de Dados.
Então, aqui eu defini um registro sem inspiração. Ele vai ficar armazenado lá na memória por tempo indeterminado. Depois eu executei um outro comando e que expire em 60. Então eu estou dizendo que o registro com a chave um sempre pela chave, vai expirar em 60 segundos. Então vejo aqui que a sintaxe é um pouquinho diferente aqui.
Anteriormente a gente tinha pra segundos, mas era dentro do próprio comando SET. Aqui a gente estava fazendo depois. Então não é um parâmetro ou um comando, o expire para a expiração em segundos e o p expire para milissegundos.
O resto aqui, é o mesmo, a chave é o intervalo, o tempo que vai levar para expirar, para o registro expirar. Eu posso verificar o tempo para respirar.
Então eu defino, por exemplo, que um determinado registro ele vai expirar e eu posso depois verificar o tempo. Então vejo que eu criei um registro.
SET 10 “engenharia de dados” EX 60 NX. Ok, aí eu posso verificar depois que o registro já está em memória, o tempo para a expiração em milissegundos e o tempo para a expiração em segundos. Vejam que, independente se eu criei o registro definindo a expiração aqui em segundos ou em milissegundos, eu posso verificar a expiração, o tempo de expiração de qualquer forma, tanto em milissegundos quanto em segundos, ok.

Então, aqui eu estou verificando o tempo para a expiração em milissegundos.
Eu uso o comando PTTL e aqui a chave para verificar o tempo da expiração em segundos Eu uso TTL com a chave.

Então a diferença é que o p para o milissegundos, então ele está me dizendo aqui faltam 34.416 milissegundos para expirar, e aqui faltam 9 segundos para o registro expirar, ou seja, ele ser removido da memória.
E eu quero, por exemplo, persistir o registro. Eu quero que ele fique em memória definitivamente ou removido. Eu posso.
Eu faço a remoção do tempo de expiração. Basta usar, o comando PERSIST e passar a chave. Eu renovo o tempo de expiração e o registro vai ficar em memória por tempo indeterminado.

O Get e Getrange
Então, aqui a gente está criando o registro que a chave é engenheiro de dados, o Get a gente já conhece que é o comando para você retornar o registro e string pela chave. Então GET 1020 ele me retorna Engenheiro de dados se eu quiser pegar apenas parte dessa string nesse texto, eu posso usar o get range.

Então o get range eu vou passar a chave novamente. O range o intervalo que esse intervalo é o índice do texto. Então eu estou dizendo que ele vai pegar o texto de zero até nove, então sempre indexado em 0 a 0, começando em zero aqui (123 456 789). Então ele me retorna uma parte do texto e de engenharia de dados eu peguei com o Get Range a posição de 0 a 9.

Quando eu quero atualizar o registro, que seria o equivalente ao update do banco de dados para atualizar, eu uso GETSET a chave é o novo valor, Quando eu uso GETSET chave, o novo valor ele vai retornar o valor antigo.
Então vejo aqui. Eu estou atualizando o registro de chave 1030, passando para ele o texto Cientistas de dados.
E ele retorna o valor que ele tinha antes que era cientista de dados. Claro que agora ele passa a persistir. Este valor é que este aqui não está mais. Ele apenas me mostrou o valor que existia antes.
O outro comando aqui que a gente está vendo é quando eu quero retornar o valor de várias chaves. Então eu em vez de ter get, eu posso ter o MGET, o MGET me retorna no console várias chaves. Então vejo aqui MGET1020, 1030, que eu poderia ter várias outras chaves e ele me retorna o valor dessas chaves de todas essas chaves que eu passei.

E o último comando aqui que a gente vai ver de string e pra ver o tamanho do valor. Ou seja, qual é o comprimento do valor, não da chave do valor que é o que é o que importa. Então eu uso a função STRLEN a chave. E ele me retorna aqui um valor inteiro com o tamanho do texto, do valor da informação, de valor do Registro.
