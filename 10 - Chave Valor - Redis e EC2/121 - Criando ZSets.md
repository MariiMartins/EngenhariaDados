121. Criando ZSets
Um exemplo de transações é o ZSETS, que é um tipo especial de SET, um tipo especial de conjunto, porém ele são ordenados e são baseados em um score. Então, além da chave e do valor, você define o score.

Então, como que a gente cria?
A gente coloca o Z na frente, ZADD chave, o peso e o valor.
ZADD 35 0 NOSQL
ZADD 35 5 RELACIONAL

Agora, com ZCARD, a chave, a gente vê quantos elementos que a gente tem.

Eu posso agora também pegar o indice de um membro. Então, por exemplo, eu posso dizer ZRANK

Eu posso também verificar quantos membros existem entre o intervalo de score, para isso eu uso o ZCOUNT

Eu posso também retornar o escore de um determinado membro, então ZSCORE

A gente pode pegar os membros do ZSET pelo índice deles utilizando o ZRANGE.

Eu posso remover o elemento ZREM chave nome.
Então, no próximo tutorial a gente vai ver, então, como que a gente tem transações no Redis.
