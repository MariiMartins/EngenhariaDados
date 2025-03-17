120. Criando Sets
Agora vamos ver sets, que é uma pela definição, e uma coleção não ordenada, não repetida, é semelhante a uma lista, porém ela não tem uma ordenação.
Então e também você não consegue inserir valores repetidos. Ela simplesmente vai ignorar se o valor tiver repetido.

SADD – adiciona elementos

Para mim, recuperar os valores, então SMEMBERS e veja que estão todos os elementos.

Para mim saber o número de membros SCARD

Eu posso saber se um elemento é membro ou não, passando a chave e o elemento, então para isso eu uso SISMEMBER.

Para mim, remover um ou mais elementos eu posso usar o SREM, passo a chave e os elementos.

Com SETS eu posso, por exemplo, verificar a diferença entre dois conjuntos, para isso, eu uso SDIFF, a chave de um elemento, e a chave do outro elemento que eu quero buscar a diferença.

Outra funcionalidade que a gente pode testar aqui é a intersecção, a intersecção ela mostra os elementos em comum, onde há uma intersecção entre os conjuntos usando SINTER.
