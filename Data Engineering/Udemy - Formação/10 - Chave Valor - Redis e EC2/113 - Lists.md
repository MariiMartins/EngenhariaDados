113. Lists
Lista é outra estrutura de dados do Redis. Então a lista nada mais é do que um conjunto de strings associados a uma mesma chave. E o detalhe é que elas podem ser inseridas separadamente. Ou seja, você tem uma chave, por exemplo, x. Você insere uma string, um texto, um valor. Depois, para essa mesma chave, você vai e insere, por exemplo, uma outra string e depois outra.
Então você inclui todas. Simultaneamente, você vai ter uma lista, várias textos, uma lista de textos associadas a uma mesma chave. Os comandos associado à lista começam com a letra R ou L.

Eu posso retornar o intervalo da lista, então vejam a lista que eu havia criado no slide anterior. Eu uso raiz LRANGE 4545 0 3 Ele me retorna os três registros aqui.

Eu posso inserir antes ou depois de um determinado valor que já existe na lista. Então veja o uso LINSERT.

Eu posso retornar um valor pelo índice. Então eu uso LINDEX, a chave e o índice. Ele me retorna o valor que está naquele índice.

E finalmente, aqui eu posso ver o cumprimento da lista.
Então, vejam LLEN e a chave, está me dizendo que existem sete strings na lista.

E para remover valores da lista, eu posso remover do início da lista ou do fim da lista. Então, o LPOP ele remove do início da lista e ele sempre exibe o valor que foi removido.
E o RPOP remove do fim da lista e também exibe o valor que foi removido.
Então, esses foram os principais comandos, as principais operações sobre listas.