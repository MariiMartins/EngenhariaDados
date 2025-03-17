114. Sets
Nós vamos agora estudar sets e sets ordenados. Os sets são bem semelhantes às listas que nós estudamos na aula anterior. Porém, tem algumas diferenças.

Primeiro que uma coleção não ordenada o principal é que não é repetida. Ou seja, você não pode incluir novos elementos repetidos na lista e seus elementos não são incluídos. Se os elementos estiverem repetidos, então é muito interessante e muito útil. Se você precisa criar uma lista de variáveis cujos valores têm que ser únicos, então você não precisa fazer nenhum tratamento. Se o valor estiver repetido, automaticamente a inserção não é feita.

Então vejam aqui um exemplo.
Eu estou criando um SADD não ordenado de chave 13 e estou incluindo três valores, assim como a gente fez na lista. Exatamente da mesma forma, porém, só muda aqui o comando.

Vejo aqui que ele retorna inteiro dizendo que quatro membros foram adicionados ao SADD, ao conjunto e aqui eu faço uma nova inclusão.
Vejo que aqui a chave é o mesmo e a mesma chave, então eu estou incluindo no mesmo set, no mesmo conjunto. Só que todos os valores aqui são diferentes ou vejo eu tenho FLUME, OOZIE, SOLR.
Antes eu tinha HADOOP SPARK HIVE PIG
.
Então, de novo aqui a operação ele retornou, que foi feita com sucesso.
Agora, aqui eu executo o comando pela terceira vez, a mesma chave e incluo FLUME.
O que ele acontece aqui? Zero, ele me retorna Falso.
Esse valor não foi incluído porque? Porque ele não é exclusivo, ele não é único. Então, dessa forma ele não faz a inclusão.

Se eu quiser recuperar os valores, os membros e o comando que SMEMBERS com a chave, ele me retorna todos os membros ou então vejam aqui eu passei a chave. Passei o comando SMEMBERS, a chave, e ele me retornou todos os membros. 

Se eu quiser saber o número de membros, quantos elementos tem no conjunto, eu uso SCARD e a chave, aqui está me dizendo que são sete elementos.

Se eu quiser verificar se um determinado valor é ou não membro dos SET, eu uso SISMERBERS, passo a chave e o valor. E aqui, como a gente já viu, ele retorna um para verdadeiro e se não tiver, se não for membro, ele retorna a zero, que quer dizer falso.

Para mim remover um ou mais membros. Então eu passo o comando SREM passo a chave e os membros que eu quero remover. Então eu posso remover mais de um membro simultaneamente.

Os conjuntos que nós estudamos até agora, são conjuntos não ordenados. Existe também os sets ordenados, os comandos e agora em vez de S começa com Z, então os sete ordenados eles também são uma lista de strings e também não aceitam elementos repetidos, ou seja, eles não incluem elementos repetidos. Porém, existe uma ordenação baseada num score, então você deve definir o score, esse score é a base da ordenação, então vejam que ZADD chave, Score, valor. Então eu posso executar diversos tipos de comando, considerando os scores que foram adicionados aos conjuntos.

Então vamos aqui ver algumas operações que podem ser feitas.

A primeira, que é bem simples, ela simplesmente retorna o número de elementos ZCARD

Aqui ele retorna o índice de um membro da posição de um membro.
Então ele usa ZRANK 

Aqui eu posso contar membros com score entre um intervalo, então ZCOUNT 

E o ZSCORE, ele retorna o score de um determinado membro.

ZREM remove um item da lista.
