118. Criando Hashs
Ele permite que você armazene um conjunto de campos no formato do campo valor, então você pode ter um conjunto de campos, só que todos eles associados a uma única chave. Ele é um pouco semelhante a um dicionário de uma linguagem de programação.

Vamos ver que como que funciona.

HMSET CADASTRO NOME JOSÉ PROFISSAO ENGENHEIRO CIDADE “SANTA MARIA”

Eu tenho uma chave cadastro e as associadas acharem eu tenho três campos nome, profissão e cidade. 
Para nome o valor é José, Profissão o valor engenheiro e cidade o valor Santa Maria.

E aí eu posso recuperar todo o conjunto de chave valor com HGETALL e eu vou passar obviamente a chave. Que neste caso é cadastro.

Bom, eu posso excluir um campo. Obviamente que quando excluir um campo, o valor também vai ser excluído junto. Ele não pode ficar órfão.

Então, por exemplo, vamos supor que eu queira excluir o campo cidade.
Eu posso utilizar HDEL (eu preciso passar a chave e o campo) a chave que é cadastro e o campo cidade.


Outra coisa que eu posso fazer é retornar o valor pelo nome do campo, por exemplo, eu posso passar nomes de Campos, e ele vai me retornar o valor desse campo.
HMGET Cadastro NOME PROFISSAO

Eu posso também pegar todos os valores. Eu não quero saber dos campos, eu quero só os valores. Então eu posso ter HVALS a chave que é cadastro.

Eu posso também verificar a existência pelo campo. Se um campo existe ou não para isso, o uso HEXISTS a chave cadastro e o campo.

Para mim saber o número de campos eu uso HLEN

Eu posso retornar uma lista de todos os campos, HKEYS.

Então vejo a lista de campos e nome e profissão.
Então, antes a gente tinha visto ali para ele retornar todos os valores.
Que o HValls, o h que retornam todos os campos.
Ok, então são nome e profissão.
Por último aqui, a gente vai utilizar o TYPE que nos mostra o tipo do objeto em que o Redis está armazenando.
