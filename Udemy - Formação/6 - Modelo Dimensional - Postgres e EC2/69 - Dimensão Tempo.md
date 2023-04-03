- 69. Dimensão Tempo
Vamos então detalhar um pouquinho, falar um pouco mais sobre a dimensão, tempo.
Como a gente já disse, a dimensão tempo é uma dimensão obrigatória em todos os modelos. Uma dimensão tempo também pode ter atributos para indicar se a data é um dia útil ou feriado, a estação do ano, trimestre, semestre. Se você tem já essa informação armazenada, registrada na dimensão tempo, o seu sistema gerencial não vai precisar calcular porque essa informação já está registrada. Ela vai estar registrada, vai estar vinculada a fato e, por exemplo, já se sabe se aquela venda, por exemplo, ocorreu em um dia útil ou se foi num feriado, se foi no inverno ou se foi no verão ou qual o trimestre pertence, por exemplo.

Então, você pode colocar informação do ponto de vista hierárquico, dentro da dimensão tempo. Normalmente se carrega toda a dimensão tempo de acordo com o grão da data escolhido. Não se carrega nem mais nem menos que o necessário para o grão escolhido. Para o nível de detalhe escolhido na carga se relaciona a chave da data com a fato.

Então, o mesmo registro pode ser relacionado com o fato mais de uma vez, a gente vai ver em seguida. Então, por exemplo, se você tem uma dimensão, um produto e dois produtos foram vendidos no mesmo dia, você vai relacionar a dimensão duas vezes com a fato, uma com cada produto.

Então, aqui a gente tem esse exemplo: 
Se você tem mais de uma data, você tem a data da venda, a data do pagamento e a data da entrega. A dimensão tempo é uma só. Eu vou relacionar cada uma das datas com o meu fato vendas, a dimensão sempre é a mesma.
Porquê uma dimensão tempo? Porque simplesmente não se inclui a data na fato.
Em vez de ter uma chave estrangeira aqui apontando para uma outra tabela que é uma dimensão tempo, porque eu simplesmente não crio uma coluna, data aqui. O principal motivo é que se você for produzir relatórios ou consultas e você quiser inserir as datas sem ocorrência do fato, você resolve isso com o Left join na dimensão tempo.
Se a dimensão tempo não existir, você vai ter que usar algumas consultas bem complexas ou mesmo programação para obter o resultado.

Então, esse é o principal motivo que se utiliza obrigatoriamente sempre uma dimensão tempo, em vez de você simplesmente incluir a data do fato no fato, vendo a data da ocorrência do fato na tabela de fato Vendas.