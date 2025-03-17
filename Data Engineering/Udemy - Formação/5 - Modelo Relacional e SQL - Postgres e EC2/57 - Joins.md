
57. Joins
Bom, agora a gente vai ver algumas das funcionalidades de joins, de junções.
Por isso eu estou colocando aí no cantinho do vídeo o diagrama do banco de dados para ajudar você a entender o que está, o que está acontecendo.
Então primeiro vamos ver aqui os nossos vendedores, ou então você vai ver que nós temos dez vendedores.
Então é select count * from relacional.Vendedores;
Temos dez vendedores e a gente tem  400 vendas e você pode ver pelo diagrama, a relação que existe entre vendas e vendedores. Então, uma venda tem uma chave estrangeira, para uma chave primária de um vendedor.
Então vamos primeiro aqui fazer um inner join entre relacional vendas e relacional vendedores.

Então esse inner join ele tem que ter um match de onde isso vai ser feito e a gente vai fazer esse match, obviamente, pela chave primária e chave estrangeira.
E a gente vai fazer o inner join  entre essas duas tabelas. É o que a gente espera é que a gente vai fazer utilizando o count. A gente espera que o resultado deste join nos traga uma contagem de 400. Porque? Porque toda a venda tem um vendedor então não existe uma venda sem um vendedor. A gente vai ver depois que a gente vai fazer um right join e a gente vai ter um resultado diferente, porque a gente vai ter um vendedor sem vendas. Mas agora isso ainda não acontece. Então vamos confirmar isso.

Então a gente vai fazer aqui um Select Count * From Relacional.vendas as vendas
Vai fazer o inner join relacional.vendedores  as vendedores on (vendas.id vendedor = vendedores.idvendedor);
ou criando o alias, ou é aqui que eu vou dizer aonde deve ter um match, qual coluna ele vai fazer, a junção com que vai que ele vai usar para fazer a junção, senão ele vai cruzar todas com todas as vendas, que é o alias que a gente criou.

O resultado nos dá 400.
Por quê? Porque toda venda tem um vendedor. E se a gente fizer um left join, eu vou só mudar aqui para left join e a gente vai ter o mesmo resultado.
Então a Left join porque mesmo assim vai haver um match perfeito nos dois lados. Não vai existir um registro, uma venda sem um vendedor, como também não existe nenhum vendedor que não está em alguma venda.
Agora a gente vai inserir  um novo vendedor, este novo vendedor obviamente que como ele acabou de ser inserido, ele não vai ter nenhuma venda. Aí a gente vai repetir o right Join e vamos ver o que acontece. Então vamos lá.
Insert into relacional.vendedores (nome) values (‘Fernando Amaral’)
O nome vai inserir o nome Fernando Amaral. Na tabela de vendedores, ele confirma que inseriu o registro.
Agora vamos voltar aqui. Para o nosso inner join. E ele nos mostra 400 porque o inner join, ele nos traz apenas os matches. Agora, se a gente mudar para um risght join o que ele vai mostrar. Ele vai trazer os matchs do lado direito.

Então, o que a gente espera agora que a gente tenha 401 registros? Porque a gente tem um vendedor que não tem venda, ok, então está fazendo o join pela tabela da direita, que é a tabela de vendedores. A gente tem um vendedor que não está em nenhuma venda, então ele nos traz aqui 401, ok.
Então, assim a gente tem uma noção básica dos fundamentos de como os as funções, as funções de joins funcionam.
Ok, a gente vai, então, no próximo tutorial, ver mais alguns Joins e também na próxima sessão, quando a gente estudar. A gente vai construir um DataWarehouse com essa mesma tabela e  vai ter ainda uma compreensão ainda melhor.