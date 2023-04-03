115. Transações
Redis tem suporte a transações semelhante a um banco de dados relacional, inclusive com algumas características das transações que a gente encontra em bancos de dados relacionais. Então, aqui a gente tem os principais comandos para controlar transações no Redis.
•	Então, o primeiro comando aqui é o MULTI: ele marca o início das transações. Ele é o equivalente a um banco de dados relacional ao comando BEGIN ou Begin Transaction, dependendo do banco relacional, então aquele marca o início.
•	O EXEC: Ele executa todos os comandos depois do MULTI, então você vai ter MULTI vários comandos e depois o EXEC vai confirmar as operações. Um equivalente aqui no banco de dados relacional e o COMMIT que ele confirma as transações.
•	E o DISCARD descarta todos os comandos depois do MULTI, então a gente tem o equivalente ao ROLLBACK de um banco de dados relacional.
Então, vejam os comandos da transação sempre vão estar entre o MULTI e o EXEC ou entre o MULTI e um DISCARD, você pode, por exemplo, ter um controle de fluxos para definir se vai executar um ou outro.
Então o EXEC vai confirmar e o DISCARD vai descartar todas as transações criadas depois do MULTI.

O Redis tem duas características principais aqui relacionadas a transações que a gente encontra também em bancos de dados relacionais.
•	A primeira característica de isolamento, ou seja, outra transação de outro cliente, não vai ser executada durante a transação.
•	E a outra é de atromicidade que a gente estudou e que a gente falou bastante, que o conceito de tudo ou nada, ou todas as transações são confirmadas ou todas as transações são descartadas.(Obviamente, o que se está falando das transações que estão entre os blocos MULTI- EXEC ou MULTI-DISCARD)
