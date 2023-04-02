- 82. Desnormalização
Um conceito importante quando a gente fala de armazéns de dados ou de informação analítica, é a desnormalização.

A desnormalização é um processo em que você entrega para um usuário final ou para uma ferramenta, todas as funções necessárias já prontas.

Então você abstrai o fato de que você tem, por exemplo, um banco de dados normalizado, em que as informações se relacionam por chaves primárias e chaves estrangeiras. Você abstrai isso através de um script, criando uma nova tabela ou dentro de um conceito de view.

Então, o script de desnormalização que você tem junto do material do curso que eu vou colar aqui e executar, eu vou mostrar ele aqui, colei aqui. Então ele é um grande script que faz a desnormalização dos dados. Então você pode ver que ele é uma junção da fato vendas com todas as dimensões e ele cria com isso uma tabela dentro do dimensional chamado des_Vendas. Então você a partir dessa des_Vendas, você consegue consultar o seu o seu DataWarehouse sem precisar criar junções. Sem precisar fazer N joins, conhecer conceitos de chaves, junções de chaves, entre outras.

Então eu vou aqui executar o script. E agora aqui a gente pode uma vez essa desorganização feita. 
Eu posso consultar a tabela onde eu vou ter todas essas informações importantes, sem que eu precise fazer joins ou então des_Vendas aqui ela fica Desorganizada.

Eu vou encerrar aqui a consulta, vamos colocar aqui alguns campos, ID cliente, estado, valor total, o valor total não dá certo. Então, veja, eu tenho as informações normalizadas.

Então veja que eu tenho cliente pelo nome e eu posso filtrar o cliente pelo próprio nome. Eu não preciso mais aqui, necessariamente saber o código dele. Quando eu usar assim uma tabela normalizada, então, por exemplo, eu posso dizer que você cliente é igual.

O nome que eu copiei dele é Ventura, ponto de vírgula.
Eu tenho só as vendas do cliente Adelina Buenaventura.
Então é um conceito interessante, importante, Você tem o script junto com o material do curso. Não existe nada de muito diferente do que qualificar os campos, as colunas que você vai utilizar e fazer os interiores. Você precisa fazer os originais, senão você vai ter uma função exponencial. Você vai cruzar tudo com tudo, então os idiomas você precisa fazer.
O único grande diferencial do script que você tem, o INTO é uma palavra para você colocar o resultado da consulta dentro de uma outra tabela. Funcionaria da mesma forma se nós criássemos, por exemplo, uma vila de uma forma bem semelhante.