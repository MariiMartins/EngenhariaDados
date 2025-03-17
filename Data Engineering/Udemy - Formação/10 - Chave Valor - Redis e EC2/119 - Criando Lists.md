119. Criando Lists
Estão listas é um outro tipo de objeto, que é uma sequência de strings.
Porém, elas estão associadas a uma chave única e também você pode inserir ou remover elementos nesta lista.

Para criar nossa primeira lista utilizamos o comando LPUSH.
Para recuperar elementos individuais ou um intervalo, eu posso utilizar LRANGE.

Você pode inserir novos elementos no fim da lista, então vou para isso usar RPUSH

Então vamos supor que eu queira inserir um outro dado no meio da lista, para isso uso LINSERT chave  ai eu defino se eu quero BEFORE ou AFTER, o valor anterior e o valor que quero inserir.

Com essas operações, eu posso atualizar o valor da minha lista.

Então, por exemplo, eu quero remover o primeiro elemento eu vou usar LPOP.

Eu posso também remover pelo fim,  para isso eu uso RPOP.
