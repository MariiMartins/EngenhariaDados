42. Formas Normais
Então nós vimos no estudo de caso da aula anterior que o sistema, o banco de dados, ele tem um problema sério de integridade, de redundância. E a gente falou também que o objetivo de um banco de dados relacional do sistema gerenciador de banco de dados relacional é manter a integridade e reduzir a redundância e manter a integridade ao máximo possível. Reduzir a redundância possível. Mas como que ele faz isso? 

Então existe as formas normais as mais comuns, é da primeira, a terceira forma normal, mas existe até a quinta forma, normal. Então, o processo de otimizar a estrutura dos dados, buscando redução da redundância e aumentando a sua integridade, é chamado de normalização dos dados.

Se a gente deixa os dados sem integridade, sem redundância, a gente diz que nós temos dados desnormalizados.
Em alguns casos, a gente vai ver na seção posterior na implementação de ambientes analíticos, bancos de dados exclusivamente criados exclusivamente para o propósito.Por fim, analítico, que, em alguns casos, é necessário você desnormalizar. Você tira a integridade e aumenta a redundância (os dados repetidos), mas com o benefício de você ter dados mais propícios para funções, para questões analíticas, para questões gerenciais.Mas isso é assunto da seção posterior.

Então é que a gente está de novo com os nossos dados que nós vimos na sessão anterior, que a gente viu que tem que ter um monte de problemas, a citou alguns.
A gente não sabe qual é o cliente, qual o endereço do cliente que vale se os clientes são os mesmos, se os seus produtos estão com valor errado e se existem vários problemas. Basicamente, a normalização nós vamos separar cada elemento que faz parte do negócio em uma tabela ou em uma entidade.

Então vamos voltar aqui um pouquinho a nós temos vendedor, nós temos clientes, nós temos produtos que dizem respeito a uma venda, então aqui está a venda. Então a gente identificou aqui quais entidades, o vendedor, o cliente, o endereço faz parte do cliente, nós temos aqui produtos ok, e aqui nós temos uma venda. A quantidade, o valor total fazem parte dessa venda, então identificou. E a gente identificou aqui pelo menos quatro entidades. Então, na normalização, nós separamos essa entidade, tanto do ponto de vista lógico quanto do ponto de vista físico.

Do ponto de vista físico.Isso num banco de dados relacional vai ser o que a gente chama de tabelas ou entidades.
Então, o que a gente tem aqui nós temos. Nós podemos ver o que a gente tem, o cliente, a operação de venda, o vendedor e aqui nós temos os produtos. Eles não estão mais em uma mesma tabela desnormalizado. A gente está fazendo um processo aqui que está chamando de normalização, que está separando essas entidades.
Mas o que acontece agora? A gente tem aqui, por exemplo, a venda, mas a gente não sabe aqui quem foi o cliente, quem foi o vendedor, qual foi o produto. A gente não tem nada a respeito dessa venda.

Como isso é feito? A gente atribui identificadores a essas entidades, a essas tabelas e a gente faz o que a gente chama de relacionamento. Então, vejam aqui nós temos a nossa tabela de clientes. Cada cliente vai receber um atributo, ou seja, uma característica aqui que a gente chama de chave primária, é o identificador único deste cliente.
Então cada cliente vai ter o seu identificador único. Então, por exemplo, o Antonio Carlos Amaral aqui ele é o cliente de número um. Quando fizer uma venda para esse cliente, eu vou ter uma entidade vendo uma tabela, venda e eu vou ter lá uma coluna onde eu vou colocar o identificador único deste cliente.

O que acontece agora? EAntes  de eu cadastrar o cliente de novo, eu verifico se ele já existe. Eu posso botar como chave, por exemplo, o CPF dele, se não for um identificador ou uma outra informação qualquer. Mas antes eu verifico se ele já não existe. Se ele já existe, eu apenas faço a referência. Eu não vou cadastrar o cliente de novo,vou manter uma referência àquele cliente que já existe na minha venda.
 
O que aconteceu no cadastro? Eu não tenho mais o problema da falta de integridade dos dados.Eu não tenho desperdício de uso de disco com cliente cadastrado várias vezes e eu não tenho problema de dados repetidos, eu resolvo dessa forma, todos os problemas, todos os principais problemas que a gente identificou. Vejo aqui o mesmo caso do vendedor, que tem uma tabela de vendedor que é relacionada, que a gente tem uma tabela de produtos que aqui também está relacionados através de uma chave.

Então a gente tem um processo aqui que a gente chama de normalizado. Então, vejam aqui nós aqui nós removemos os clientes repetidos, que antes a gente tinha Sete clientes, agora, na verdade, eram só três. Nós temos aqui um cadastro de produtos. Nós temos aqui um cadastro de vendedores, que são dois vendedores.

Então veja aqui PK é a sigla que quer dizer primary key que é chave primária. Então este aqui esta coluna é o identificador. Dessa entidade, deste cliente identificado por esta coluna aqui nesta outra tabela que é de vendas, o ID cliente viram FK uma chave estrangeira. Então, a referência aqui se dá por essa chave estrangeira.
Vejam que aqui você vai colocar apenas a referência. Você não vai cadastrar o cliente de novo. Se apenas uma referência, então os identificadores são as chamadas chaves primárias.
Na chave estrangeira, só pode existir códigos que existam na chave primária. Ou seja, eu não vou conseguir cadastrar aqui como cliente o cliente de número quatro. Porque? Porque o cliente número quatro não existe.
Isso se chama integridade referencial.

Da mesma forma, eu não vou conseguir excluir o cliente número um aqui, o Antonio Carlos Amaral.
Por quê? Porque existe uma venda para esse cliente. Se eu excluir o cliente, como é que eu vou saber para quem eu vendi? Então eu tenho de novo a integridade referencial. Então vejo que todos aqueles problemas que nós vimos lá no vídeo anterior por este modelo são resolvidos.

Então a chave estrangeira pode se repetir. Eu posso ter o mesmo cliente aqui várias vezes. Eu não posso repetir a chave primária. Eu não posso ter o mesmo cliente com o mesmo código. Eu não posso ter o cliente de cliente número um de novo.Este relacionamento aqui é chamado de um para ele ou um para muitos. Então a gente tinha sete clientes cadastrados, mas na verdade eram só três.

Porque esse relacionamento aqui chamado de um para muitos? Porque o único cliente ele pode aparecer n vezes em uma venda.
A mesma coisa que um mesmo produto. O produto só pode aparecer uma vez aqui, mas aqui na venda ele pode aparecer n vezes.
Existe então o relacionamento um Para ele existe um relacionamento, um para um, que não é considerado um relacionamento correto, mas pode ser criado.

E existe também o relacionamento muitos, para muitos. A gente vai ver mais adiante o orçamento, muitos para muitos que ele é resolvido através da criação de uma outra tabela que na verdade vai unir, ele vai juntar as chaves de outras duas tabelas. É o caso, por exemplo, de itens de venda, um relacionamento muitos para muitos, a gente vai estudar ele mais adiante.
