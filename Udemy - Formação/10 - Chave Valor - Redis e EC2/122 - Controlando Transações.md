122. Controlando Transações
Bom, então agora a gente vai ver transações. Lembrando que o conceito de transações é semelhante ao de um banco de dados relacional, porém que as
palavras- chave são um pouquinho diferentes.

Então o MULTI marca o início de uma transação equivalente ao Big Jim.
O EXEC executa todos os comandos que foram criados executados depois do MULTI, é o equivalente ao commit.
E o DISCARD, ele descarta todos os comandos depois do MULTI, então ele é o equivalente ao rollback.
